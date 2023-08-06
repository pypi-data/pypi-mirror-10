import re
from collections import defaultdict
import subprocess
from datetime import datetime

from watcher import Watcher
from easy_alert.entity import Alert, Level
from easy_alert.util import CaseClass, get_server_id
from easy_alert.i18n import *


class ProcessReader(object):
    """
    Read process information from operating system
    """

    def read(self):
        """
        Get the running processes information
        :return: dict of process id -> tuple(parent process id, args string)
        """

        def f(line):
            tokens = line.split(None, 2)
            return int(tokens[0]), (int(tokens[1]), tokens[2])

        # trim header line then parse
        return dict(map(f, self._read_raw().splitlines()[1:]))

    def _read_raw(self):
        cmd = ['/bin/ps', 'ax', '-o', 'pid,ppid,args']
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]


class ProcessCounter(CaseClass):
    """
    Count the number of the processes
    """

    def __init__(self, process_dict):
        super(ProcessCounter, self).__init__(['process_dict', 'cache_distinct', 'cache_aggregated'])
        self.process_dict = process_dict
        self.cache_distinct = None
        self.cache_aggregated = None

    def count(self, regexp, aggregate=True):
        pattern = re.compile(regexp)
        d = self._aggregate() if aggregate else self._distinct()
        return sum(x * bool(pattern.search(s)) for s, x in d.items())

    def _distinct(self):
        """
        :return: dict of args string -> count with default value (0)
        """
        if self.cache_distinct is None:
            d = defaultdict(int)
            for ppid, args in self.process_dict.values():
                d[args] += 1
            self.cache_distinct = d
        return self.cache_distinct

    def _aggregate(self):
        """
        Aggregate forked processes.
        That is, if the 'args' strings of one process is same as the parent process, it is not counted.

        :return: dict of args string -> count with default value (0)
        """
        if self.cache_aggregated is None:
            d = defaultdict(int)
            for ppid, args in self.process_dict.values():
                parent = self.process_dict.get(ppid)
                if parent is None or parent[1] != args:
                    d[args] += 1
            self.cache_aggregated = d

        return self.cache_aggregated


class ProcessWatcher(Watcher):
    """
    Watch the number of the running processes
    """

    def __init__(self, alert_settings, process_reader=ProcessReader()):
        super(ProcessWatcher, self).__init__(alert_settings=alert_settings, process_reader=process_reader)

    def watch(self):
        """
        :return: list of Alert instances
        """
        start_time = datetime.now()
        pc = ProcessCounter(self.process_reader.read())

        result = []
        for s in self.alert_settings:
            st = self.ProcessStatus(
                s['name'], pc.count(s['regexp'], s.get('aggregate', True)), self._make_conditions(s))
            if st.level:
                result.append(st)

        if result:
            max_level = max(r.level for r in result)
            message = MSG_PROC_ALERT % {'server_id': get_server_id(), 'result': '\n'.join('%s' % s for s in result)}
            return [Alert(start_time, max_level, MSG_PROC_ALERT_TITLE, message)]
        else:
            return []

    @staticmethod
    def _make_conditions(alert_setting):
        """
        :return: list of tuple(Level, condition string)
        """
        ret = [(l, alert_setting.get(l.get_keyword())) for l in Level.seq if l.get_keyword() in alert_setting]
        return ret

    class ProcessStatus(CaseClass):
        def __init__(self, name, count, conditions):
            super(ProcessWatcher.ProcessStatus, self).__init__(['name', 'count', 'level', 'condition'])
            self.name = name
            self.count = count
            self.level, self.condition = self._check_conditions(count, conditions)

        def __str__(self):
            count_msg = MSG_PROC_NOT_RUNNING if self.count == 0 else MSG_PROC_RUNNING % {'count': self.count}
            return MSG_PROC_STATUS_FORMAT % {
                'level': self.level.get_text(),
                'name': self.name,
                'count': count_msg,
                'condition': self.condition
            }

        @classmethod
        def _check_conditions(cls, count, conditions):
            for level, condition in conditions:
                # find the first False from the severest level
                if not cls._parse_condition(condition)(count):
                    return level, condition
            return None, None

        @staticmethod
        def _parse_condition(condition):
            op, threshold = re.match("""([=!<>]+)\s*(\d+)""", condition).groups()
            return {
                "=": lambda x: x == int(threshold),
                "==": lambda x: x == int(threshold),
                "!=": lambda x: x != int(threshold),
                "<": lambda x: x < int(threshold),
                "<=": lambda x: x <= int(threshold),
                ">": lambda x: x > int(threshold),
                ">=": lambda x: x >= int(threshold),
            }[op]
