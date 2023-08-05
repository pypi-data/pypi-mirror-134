import typing
from mypy.nodes import (
    ArgKind,
    Argument as Argument,
    Block as Block,
    ClassDef as ClassDef,
    FuncDef as FuncDef,
    TypeInfo as TypeInfo,
    Var as Var,
)
from mypy.plugin import (
    ClassDefContext as ClassDefContext,
    DynamicClassDefContext as DynamicClassDefContext,
)
from mypy.semanal import SemanticAnalyzer as SemanticAnalyzer
from mypy.types import (
    Instance as Instance,
    Type as MypyType,
    TypeVarType as TypeVarType,
    UnboundType as UnboundType,
)
from typing import Any

def build_argument(
    name: str,
    type_: typing.Optional[MypyType] = ...,
    arg_type: ArgKind = ...
) -> typing.List[Argument]: ...
def build_func_def(
    args: typing.List[Argument],
    return_type: MypyType,
    fallback: Instance,
    func_info: TypeInfo,
    name: str,
    tvar_def: typing.Optional[TypeVarType] = ...,
    self_type: MypyType = ...,
    is_static: bool = ...,
    is_property: bool = ...,
    body: Block = ...,
) -> FuncDef: ...
def add_method(
    name: str, func: FuncDef, cls_info: TypeInfo, replace: bool = ...
) -> None: ...
def add_attribute(name: str, cls: ClassDef, type_: MypyType) -> None: ...
def add_global(
    ctx: typing.Union[ClassDefContext, DynamicClassDefContext],
    module: str,
    symbol_name: str,
    asname: str,
) -> None: ...
def add_remote_method_to_context(ctx: ClassDefContext) -> None: ...
def add_actor_class_to_context(ctx: ClassDefContext) -> None: ...
def add_object_ref_to_context(ctx: ClassDefContext) -> None: ...
def is_magic_method(name: str) -> bool: ...
def get_return_type(method: FuncDef) -> MypyType: ...
def var_to_type(var: Var) -> MypyType: ...
def unbound_to_instance(api: SemanticAnalyzer, type_: UnboundType) -> MypyType: ...
def pformat_(x: typing.Any, seen: typing.Union[Any, None] = ...) -> typing.Any: ...
def print_(x: typing.Any) -> None: ...
