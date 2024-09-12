
import locale
from string_res import string_res


def get_local_language():
    locale.setlocale(locale.LC_ALL, "")
    if (locale.getlocale()[0] is not None) & \
            (locale.getlocale()[0].startswith(string_res.TURKISH)):
        return string_res.TR
    elif (locale.getdefaultlocale()[0] is not None) & \
            (locale.getdefaultlocale()[0].startswith(string_res.TR)):
        return string_res.TR
    else:
        return string_res.EN

