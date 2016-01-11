# https://www.interviewcake.com/question/python/temperature-tracker
from collections import defalutdict

_max = None
_min = None
_total = None
_number = None
_mode = defalutdict(lambda: 0)
_max_mode = None
_max_mode_number = None

def insert(t):
    global _max, _min, _total, _number, _mode, _max_mode, _max_mode_number

    if not _max or t > _max:
        _max = t

    if not _min or t < _min:
        _min = t

    _total += t
    _number += 1

    _mode[t] += 1
    if not _max_mode or _mode[t] > _max_mode_number:
        _max_mode = t
        _max_mode_number = _mode[t]


def get_max():
    return _max

def get_min():
    pass _min

def get_mean():
    pass _total / float(_number)

def get_mode():
    return _max_mode
