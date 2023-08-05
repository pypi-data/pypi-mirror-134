import typing
from mypy.nodes import (
    Argument,
    ClassDef as ClassDef,
    FuncDef as FuncDef,
    SymbolTable as SymbolTable,
    TypeInfo as TypeInfo,
)
from mypy.plugin import ClassDefContext as ClassDefContext
from mypy.semanal import SemanticAnalyzer as SemanticAnalyzer
from mypy.types import Type as MypyType, TypeVarLikeType as TypeVarLikeType

def build_options_args(api: SemanticAnalyzer) -> typing.List[Argument]: ...
def build_type_info(
    api: SemanticAnalyzer,
    module_name: str,
    cls_full_name: str,
    column: int = ...,
    line: int = ...,
    class_def: ClassDef = ...,
    class_name: str = ...,
    type_vars: TypeVarLikeType = ...,
) -> TypeInfo: ...
def build_object_ref(ctx: ClassDefContext, wraps: MypyType) -> MypyType: ...
def build_remote_method_info(
    api: SemanticAnalyzer,
    module_name: str,
    column: int,
    line: int,
    cls_full_name: str = ...,
) -> TypeInfo: ...
def build_remote_method(ctx: ClassDefContext, method: FuncDef) -> MypyType: ...
def build_actor_class_info(
    ctx: ClassDefContext, methods: typing.List[FuncDef]
) -> TypeInfo: ...
def build_actor_class_instance(
    ctx: ClassDefContext, methods: typing.List[FuncDef], decorated_cls: MypyType
) -> MypyType: ...
