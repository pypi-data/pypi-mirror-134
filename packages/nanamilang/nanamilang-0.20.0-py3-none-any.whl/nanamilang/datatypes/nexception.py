"""NanamiLang NException Data Type"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

from typing import Tuple

from .base import Base
from .string import String
from .hashmap import HashMap
from .keyword import Keyword
from ._exports import export

from nanamilang import shortcuts


class NException(Base):
    """NanamiLang NException Data Type Class"""

    _core_traceback: list = None
    _exception: Exception
    _expected_type = HashMap
    name: str = 'NException'
    _position: tuple = ('UNK', 1, 1)
    _python_reference: HashMap
    purpose = 'Encapsulate Python 3 Exception'

    def __init__(self, reference: Tuple[Exception, tuple]) -> None:
        """Initialize a new NException instance"""

        self._exception, self._position = reference
        # remember _what_ the error has been occurred and __where__

        self._position_message = ':'.join(map(str, self._position))
        # compile position message and store in self._position_message

        reference = HashMap(
            (
                Keyword('message'),
                String(self._exception.__str__()),
                Keyword('name'),
                String(self._exception.__class__.__name__),
             ),
        )
        # turn reference into a nanamilang.datatypes.HashMap instance

        super().__init__(reference)
        # and then we can call Base.__init__() through Python super()

        self._core_traceback = []

        _t = self._exception.__traceback__
        while _t is not None:
            _f = _t.tb_frame.f_code.co_filename
            self._core_traceback.append(
                shortcuts.aligned('at', f'{_f}:{_t.tb_lineno}', 70)
            )
            _t = _t.tb_next
        # store self._traceback (because could be used in self.format)

    @export()
    def nominal(self) -> String:
        """NanamiLang NException, nominal() method implementation"""

        return String(self.name)

    def position(self) -> tuple:
        """NanamiLang NException, self._position getter"""

        return self._position

    def exception(self) -> Exception:
        """NanamiLang NException, self,_exception getter"""

        return self._exception

    def get(self, key: Keyword) -> Base:
        """NanamiLang NException, get() method implementation"""

        shortcuts.ASSERT_IS_INSTANCE_OF(
            key,
            Keyword,
            message='NException.get: key must be a Keyword'
        )

        return self._python_reference.get(key)

    def hashed(self) -> int:
        """NanamiLang NException, hashed() method implementation"""

        # Override hashed() to return stored HashMap.hashed() value.
        return self._python_reference.hashed()

    def format(self, **kwargs) -> str:
        """NanamiLang NException, format() method implementation"""

        include_traceback = kwargs.get('include_traceback')
        _ = '\n'.join(list(map(lambda x: '  ' + x, self._core_traceback)))
        _traceback_frmt_included = f'\n{_}\n' if include_traceback else ''

        _indent = ' ' * 2
        _max = 67

        src = kwargs.get('src', '')  # <- if source available, do highlighting :)
        _hl_included = f'\n{_indent}{src}\n{_indent}{(self._position[2]-1)*" "}^\n{_indent}' if src else '\n  '

        n_ref = self._python_reference.get(Keyword("name")).reference()
        m_ref = self._python_reference.get(Keyword("message")).reference()

        n__m_separator = ' ' if len(self._position_message) + len(n_ref) + len(m_ref) < _max else '\n' + _indent

        return f'at {self._position_message}{_hl_included}{n_ref}:{n__m_separator}{m_ref}\n{_traceback_frmt_included}'
