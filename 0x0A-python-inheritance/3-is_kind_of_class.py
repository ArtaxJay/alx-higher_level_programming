#!/usr/bin/python3
"""Lorem dolor sit amet."""


def is_kind_of_class(obj, a_class):
    """No stories, just facts.

    Args:
        obj (class object): check this object.
        a_class (instance): instance of object.
    Returns:
        True if a_class is an instance or inherited from obj.
        False in case the above cond is nit fulfilled.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
