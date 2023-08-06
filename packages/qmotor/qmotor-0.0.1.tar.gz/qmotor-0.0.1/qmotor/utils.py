from typing import List, Union
from datetime import date, datetime
from time import mktime


def is_str_blank(s: str):
    if not s.strip():
        return True
    else:
        return False


def str_contains(s: str, t: List[str]):
    return any(w in s for w in t)


def unixtimestamp(t: Union[datetime, date, None]):
    return t and mktime(t.timetuple())
