"""NanamiLang Shortcuts"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

import functools
import random
import string
from typing import Any, Generator


def get(coll: tuple or list, idx: int, _def):
    """Safely get value from tuple or list"""

    try:
        return coll[idx]
    except IndexError:
        return None or _def


def plain2partitioned(coll: tuple or list,
                      n: int = 2) -> Generator:
    """Allows to iterate partitioned (by n) collection"""

    return (coll[i:i + n] for i in range(0, len(coll), n))


def truncated(source: str, n: int) -> str:
    """
    Return possibly truncated strings
    :param source: maybe \n joined strings
    :param n: a maximum string length allowed
    :return: truncated string like foobar...baz
    """

    def handle(_: str) -> str:
        """Actual handling is implemented here"""

        length = len(_)
        if length <= n:
            return _
        mid = int(n / 2)
        left = _[:mid]
        right = _[length-mid+2:]

        return left + '...' + right

    if '\n' not in source:
        return handle(source)
    return '\n'.join(tuple(map(handle, source.split('\n'))))


def partitioned2plain(coll: tuple or list,
                      default: ()) -> tuple:
    """De-partitionate previously partitioned collection"""

    return functools.reduce(lambda e, n: e + n, coll or default)


def randstr(length: int = 10) -> str:
    """Return randomly generated string using predefined alphabet"""

    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def aligned(start: str,
            source: str,
            n: int) -> str:
    """
    Return aligned right string
    :param start: to add at the start
    :param source: source to align right
    :param n: maximum length of the string
    :return: returns aligned to right string
    """

    start_len = len(start)
    maybe_truncated = truncated(source, n - 3)

    return start + ' ' * (n - start_len - len(maybe_truncated)) + maybe_truncated


########################################################################################################################


def ASSERT_COLL_LENGTH_IS(coll: list or tuple or set, length: int, message: str = '') -> None:
    """ASSERT_COLL_LENGTH_IS: whether collection length equals to or not?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_COLL_LENGTH_IS: not a list, set or tuple'
    assert len(coll) == length, message or f'collection length does not equal to {length}'


def ASSERT_COLL_LENGTH_IS_EVEN(coll: list or tuple or set, message: str = '') -> None:
    """ASSERT_COLL_LENGTH_IS_EVEN: whether collection length is even or not?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_COLL_LENGTH_IS_EVEN: not a list, set or tuple'
    assert len(coll) % 2 == 0, message or 'collection length must be even'


########################################################################################################################


def ASSERT_COLLECTION_IS_NOT_EMPTY(collection: Any, message: str = '') -> None:
    """ASSERT_COLLECTION_IS_NOT_EMPTY: whether collection (or string) empty or not?"""
    assert hasattr(collection, '__len__'), 'ASSERT_COLLECTION_IS_NOT_EMPTY: has no __len__'
    assert len(collection) > 0, message or 'collection (or string) could not be empty'


########################################################################################################################


def ASSERT_NO_DUPLICATES(coll: list or tuple or set, message: str = '') -> None:
    """ASSERT_NO_DUPLICATES: does the list contain duplicates?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_NO_DUPLICATES: not a list, set or tuple'
    assert len(coll) == len(set(coll)), message or 'collection could not contain duplicates'


########################################################################################################################


def ASSERT_DICT_CONTAINS_KEY(key: Any, dct: dict, message: str = '') -> None:
    """ASSERT_DICT_CONTAINS_KEY: does the dict keys contain key?"""
    assert isinstance(dct, dict), 'ASSERT_DICT_CONTAINS_KEY: not a dict'
    assert key in dct.keys(), message or f'dictionary does not contain "{key}" key'


def ASSERT_COLL_CONTAINS_ELEMENT(elem: Any, coll: list or tuple or set, message: str = '') -> None:
    """ASSERT_COLL_CONTAINS_ELEMENT: does the coll contain element?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_COLL_CONTAINS_ELEMENT: not a list, set or tuple'
    assert elem in coll, message or f'collection does not contain "{elem}", valid values are: "{coll}"'


########################################################################################################################


def ASSERT_IS_INSTANCE_OF(inst: Any, of: Any, message: str = '') -> None:
    """ASSERT_IS_INSTANCE_OF: whether given instance is actually instance of ...?"""
    assert isinstance(inst, of), message or f'must be an instance of {of.__name__}"'


def ASSERT_IS_CHILD_OF(inst: Any, of: Any, message: str = '') -> None:
    """ASSERT_IS_CHILD_OF: whether given instance is actually child of ...?"""
    assert issubclass(inst.__class__, (of,)), message or f'must be an child of {of.__name__}"'


########################################################################################################################


def ASSERT_EVERY_COLLECTION_ITEM_EQUALS_TO(coll: list or tuple or set, to: Any, message: str = '') -> None:
    """ASSERT_EVERY_COLLECTION_ITEM_EQUALS_TO: does every collection item equal to ...?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_EVERY_COLLECTION_ITEM_EQUALS_TO: not a list, set or tuple'
    assert len(list(filter(lambda x: x == to, coll))) == len(coll), message or (
        f'every collection item must be equal to {to.__name__}'
    )


def ASSERT_EVERY_COLLECTION_ITEM_IS_CHILD_OF(coll: list or tuple or set, of: Any, message: str = '') -> None:
    """ASSERT_EVERY_COLLECTION_ITEM_IS_CHILD_OF: does every collection item is a child of ...?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_EVERY_COLLECTION_ITEM_IS_CHILD_OF: not a list, set or tuple'
    assert len(list(filter(lambda x: issubclass(x.__class__, (of,)), coll))) == len(coll), message or (
        f'every collection item must be an instance of {of.__name__}'
    )


def ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF(coll: list or tuple or set, of: Any, message: str = '') -> None:
    """ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF: does every collection item is an instance of ...?"""
    assert isinstance(coll, (list, tuple, set)), 'ASSERT_EVERY_COLLECTION_ITEM_IS_INSTANCE_OF: not a list. set or tuple'
    assert len(list(filter(lambda x: isinstance(x, of), coll))) == len(coll), message or (
        f'every collection item must be an instance of {of.__name__}'
    )


########################################################################################################################


def UNTERMINATED_STR():
    """UNTERMINATED_STR()"""
    return 'Encountered an unterminated string literal'


def UNTERMINATED_SYMBOL(sym: str, m: str = ''):
    """UNTERMINATED_SYMBOL(sym) -> message"""
    return m or f'Encountered an unterminated \'{sym}\' symbol'


def UNTERMINATED_SYMBOL_AT_EOF(sym: str, m: str = ''):
    """UNTERMINATED_SYMBOL_AT_EOF(sym) -> message"""
    return m or f'Encountered an unterminated \'{sym}\' symbol at the end of file'

########################################################################################################################


def NML_M_ASSERT_COLL_FORM_ITEMS_COUNT_IS(form: list, n: int, message: str) -> None:
    """Should be used only in builtin macros, contains desired items count"""
    ASSERT_COLL_LENGTH_IS(form[1:], n, message or 'collection items count is wrong')


def NML_M_ASSERT_COLL_FORM_ITEMS_COUNT_IS_EVEN(form: list, message: str) -> None:
    """Should be used only in builtin macros, contains even items count"""
    ASSERT_COLL_LENGTH_IS_EVEN(form[1:], message or 'collection items count ! even')


def NML_M_FORM_IS_A_VECTOR(form: list) -> bool:
    """Whether given form is a Vector coll"""
    return form[0].dt().origin() == 'make-vector'


def NML_M_FORM_IS_A_HASHMAP(form: list) -> bool:
    """Whether given form is a HashMap coll"""
    return form[0].dt().origin() == 'make-hashmap'


def NML_M_FORM_IS_A_HASHET(form: list) -> bool:
    """Whether given form is a HashSet coll"""
    return form[0].dt().origin() == 'make-hashset'


def NML_M_ASSERT_FORM_IS_A_VECTOR(form: list, message: str) -> None:
    """Should be used only in builtin macros, checks that form is a Vector"""
    assert isinstance(form, list) and form[0].dt().origin() == 'make-vector', message


def NML_M_ASSERT_FORM_IS_A_HASHSET(form: list, message: str) -> None:
    """Should be used only in builtin macros, checks that form is a HashSet"""
    assert isinstance(form, list) and form[0].dt().origin() == 'make-hashset', message


def NML_M_ASSERT_FORM_IS_A_HASHMAP(form: list, message: str) -> None:
    """Should be used only in builtin macros, checks that form is a HashMap"""
    assert isinstance(form, list) and form[0].dt().origin() == 'make-hashmap', message


def NML_M_ASSERT_FORM_IS_A_VALID_HASHMAP(form: list, message: str) -> None:
    """Should be used only in builtin macros, checks that form is a valid HashMap"""
    NML_M_ASSERT_COLL_FORM_ITEMS_COUNT_IS_EVEN(form, message or 'HashMap: ! even items count')


def NML_M_ITERATE_AS_PAIRS(form: list, n: int = 0) -> Generator:
    """Should be called within macro. Allows to iterate through a NanamiLang collection form"""
    if n == 0:
        return (_ for _ in form[1:])
    assert n % 2 == 0, 'NML_M_ITERATE_AS_PAIRS/n: n must be even or 0'
    return plain2partitioned(form[1:])

    # if n equals to 0, just return lazy collection as is, if no, check if even --- iterate using plain2partitioned func

########################################################################################################################
