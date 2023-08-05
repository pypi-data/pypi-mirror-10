#!/usr/bin/env python
# encoding: utf-8

import sys
import datetime
import re
from itertools import chain
from .exception import UnexpectedTypeError, CanNotFormatError


py = sys.version_info
py3k = py >= (3, 0, 0)
py2k = (2, 6, 0) < py < (3, 0, 0)
py25 = py < (2, 6, 0)

str_tuple = (str,) if py3k else (str, unicode)

_current = str(datetime.datetime.today().date())


def _exchange_y_d(string, y_l):
    d_l = 2 if len(string.split('-')[2]) > 1 else 1
    _st_l = list(string)
    _st_l[:d_l], _st_l[-y_l:] = _st_l[-y_l:], _st_l[:d_l]
    return ''.join(_st_l)


# with letter `M` for minutes, `m` for month
UNIT_DICT = {'years': ['years', 'year', 'yea', 'ye', 'y', 'Y'],
             'months': ['months', 'month', 'mont', 'mon', 'mo', 'm'],
             'weeks': ['weeks', 'week', 'wee', 'we', 'w', 'W'],
             'days': ['days', 'day', 'dy', 'da', 'd', 'D'],
             'hours': ['hours', 'hour', 'hou', 'hr', 'ho', 'h', 'H'],
             'minutes': ['minutes', 'minute', 'minut', 'minu', 'min', 'mi', 'M'],
             'seconds': ['seconds', 'second', 'sec', 'se', 's', 'S']}


def filter_unit(arg):
    if len(arg) > 1:
        arg = arg.lower()
    result = [key for key in UNIT_DICT.keys() if arg in UNIT_DICT[key]]
    if result:
        return result[0]
    else:
        raise CanNotFormatError


class BaseParser(object):
    """Parse string to regular datetime/date type

    1990-10-28 23:23:23  - 19
    90-10-28 23:23:23    - 17

    1990-10-28           - 10
    28-10-1990           - 10
    1990/10/28           - 10
    28/10/1990           - 10
    1990.10.28           - 10
    28.10.1990           - 10

    10-28-90  USA        - 8
    28-10-90  on hold    - 8
    10/28/90  USA        - 8
    28/10/90  on hold    - 8

    19901028             - 8
    90-10-28             - 8
    90/10/28             - 8

    23:23:23             - 8

    23:23                - 5
    23:2                 - 4
    5:14                 - 4
    5:2                  - 3
    """

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def _str_parser(string):
        """
        return method by the length of string
        :param string:
        :return:
        """
        if not any(c.isalpha() for c in string):
            _string = string[:19]
            _length = len(_string)
            if _length > 10:
                return BaseParser.parse_datetime
            elif 6 <= _length <= 10:
                if ':' in _string:
                    return BaseParser.parse_time
                else:
                    return BaseParser.parse_date
            elif _length < 6:
                return BaseParser.parse_time
            else:
                return BaseParser.parse_special
        else:
            return BaseParser.parse_diff

    @staticmethod
    def _datetime_parser(value):
        return value

    @staticmethod
    def _special_parser(value):
        return value

    def _main_parser(func):
        def wrapper(cls, *args, **kwargs):
            value = args[0]
            if isinstance(value, str_tuple):
                method = BaseParser._str_parser(value)
            elif isinstance(value, (datetime.date, datetime.time, datetime.datetime)):
                method = BaseParser._datetime_parser
            else:
                method = BaseParser._special_parser

            if hasattr(method, '__call__'):
                return method(value)
            else:
                raise UnexpectedTypeError(
                    'can not generate method for {value} type:{type}'.format(value=value, type=type(value)))

        return wrapper

    @classmethod
    @_main_parser
    def main(cls, value):
        """parse all type value"""

    @staticmethod
    def parse_datetime(string, formation=None):
        if formation:
            _stamp = datetime.datetime.strptime(string, formation)
        elif len(string) >= 18:
            _stamp = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        elif len(string) < 18:
            if '-' in string:
                _stamp = datetime.datetime.strptime(string, '%y-%m-%d %H:%M:%S')
            else:
                try:
                    _stamp = datetime.datetime.strptime(string, '%Y%m%d %H:%M:%S')
                except ValueError:
                    _stamp = datetime.datetime.strptime(string, '%y%m%d %H:%M:%S')
        else:
            raise CanNotFormatError('Need %Y-%m-%d %H:%M:%S or %y-%m-%d %H:%M:%S')
        return _stamp

    @staticmethod
    def parse_date(string, formation=None):
        """
        string to date stamp
        :param string: date string
        :param formation: format string
        :return: datetime.date
        """
        if formation:
            _stamp = datetime.datetime.strptime(string, formation).date()
            return _stamp

        _string = string.replace('.', '-').replace('/', '-')
        if '-' in _string:
            if len(_string.split('-')[0]) > 3 or len(_string.split('-')[2]) > 3:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%Y-%m-%d').date()
                except ValueError:
                    try:
                        _stamp = datetime.datetime.strptime(_string, '%m-%d-%Y').date()
                    except ValueError:
                        _stamp = datetime.datetime.strptime(_string, '%d-%m-%Y').date()
            else:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%y-%m-%d').date()
                except ValueError:
                    try:
                        _stamp = datetime.datetime.strptime(_string, '%m-%d-%y').date()
                    except ValueError:
                        _stamp = datetime.datetime.strptime(_string, '%d-%m-%y').date()
        else:
            if len(_string) > 6:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%Y%m%d').date()
                except ValueError:
                    _stamp = datetime.datetime.strptime(_string, '%m%d%Y').date()
            elif len(_string) <= 6:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%y%m%d').date()
                except ValueError:
                    _stamp = datetime.datetime.strptime(_string, '%m%d%y').date()
            else:
                raise CanNotFormatError
        return _stamp

    @staticmethod
    def parse_time(string):
        pass

    @staticmethod
    def parse_special(string):
        pass

    @staticmethod
    def parse_diff(base_str):
        """
        parse string to regular timedelta
        :param base_str: str
        :return: dict
        """
        temp_dict = {'years': 0,
                     'months': 0,
                     'days': 0,
                     'hours': 0,
                     'minutes': 0,
                     'seconds': 0}

        _pure_str = re.findall("[a-zA-Z]+", base_str)
        pure_num = [int(_) for _ in re.findall(r'\d+', base_str)]
        pure_str = [filter_unit(_) for _ in _pure_str]
        result_dict = dict(chain(temp_dict.items(), dict(zip(pure_str, pure_num)).items()))
        if result_dict['months'] >= 12:
            advance = result_dict['months'] // 12
            remain = result_dict['months'] % 12
            result_dict['years'] += advance
            result_dict['months'] = remain
        return result_dict


if __name__ == "__main__":
    BaseParser.main(_current)
