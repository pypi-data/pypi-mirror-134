"""Type aliases for various types and callbacks defined in mypy."""
import typing

from mypy.plugin import ClassDefContext

ClassDecoratorHookCallback = typing.Callable[[ClassDefContext], None]
