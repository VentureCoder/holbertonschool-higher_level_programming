#!/usr/bin/python3
def safe_function(fct, *args):
    sys = __import__("sys")
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
