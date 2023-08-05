"""Build the types in ray_types using Mypy."""
import typing

from mypy.nodes import ARG_OPT, Argument, Block, ClassDef, FuncDef, SymbolTable, TypeInfo
from mypy.plugin import ClassDefContext
from mypy.semanal import SemanticAnalyzer
from mypy.types import Instance
from mypy.types import Type as MypyType
from mypy.types import TypeVarLikeType
from typed_ray import ray_types, utils


def build_options_args(
    api: SemanticAnalyzer
) -> typing.List[Argument]:
    """Build the arguments for the ActorHandle.options method."""
    return [
        utils.build_argument(
            arg_name, api.named_type(arg_type_str), arg_type=ARG_OPT
        )
        for arg_name, arg_type_str in ray_types.OPTIONS_KWARGS.items()
    ]


def build_type_info(
    api: SemanticAnalyzer,
    module_name: str,
    cls_full_name: str,
    column: int = -1,
    line: int = -1,
    class_def: ClassDef = None,
    class_name: str = None,
    type_vars: TypeVarLikeType = None,
) -> TypeInfo:
    """Build a well constructed TypeInfo object."""
    if type_vars is None:
        type_vars = []
    if class_def is None:
        assert (
            class_name is not None
        ), "One of class_def and class_name must be specified"
        class_def = ClassDef(
            name=class_name,
            defs=Block([]),
            type_vars=type_vars,
        )
        class_def.column = column
        class_def.line = line
        class_def.fullname = cls_full_name
    result = TypeInfo(
        names=SymbolTable(),
        defn=class_def,
        module_name=module_name,
    )
    class_def.info = result
    result._fullname = cls_full_name
    result.bases = [api.named_type("builtins.object")]
    result.mro = [result, api.named_type("builtins.object").type]
    return result


def build_object_ref(ctx: ClassDefContext, wraps: MypyType) -> MypyType:
    """Build the type of the object reference."""
    utils.add_object_ref_to_context(ctx)
    api: SemanticAnalyzer = ctx.api
    obj_ref_info: TypeInfo = api.lookup_fully_qualified(
        ray_types.ObjectRefFullName
    ).node
    return Instance(obj_ref_info, [wraps])


def build_remote_method_info(
    api: SemanticAnalyzer,
    module_name: str,
    column: int,
    line: int,
    cls_full_name: str = None,
) -> TypeInfo:
    return build_type_info(
        api=api,
        module_name=module_name,
        cls_full_name=cls_full_name,
        column=column,
        line=line,
        class_name="RemoteFunction",
    )


def build_remote_method(
    ctx: ClassDefContext,
    method: FuncDef,
) -> MypyType:
    api: SemanticAnalyzer = ctx.api
    remote_method_info = build_remote_method_info(
        api=api,
        module_name=method.info.module_name,
        cls_full_name=method.info._fullname,
        column=method.column,
        line=method.line,
    )
    method_ret_type = utils.get_return_type(method)
    bound_method_ret_type = utils.unbound_to_instance(api, method_ret_type)
    return_type = build_object_ref(ctx, bound_method_ret_type)
    remote_method = utils.build_func_def(
        args=method.arguments[1:],
        return_type=return_type,
        fallback=api.named_type("builtins.function"),
        func_info=remote_method_info,
        name="remote",
        body=method.body,
    )
    utils.add_method(
        name="remote", func=remote_method, cls_info=remote_method_info, replace=True
    )
    return Instance(remote_method_info, [bound_method_ret_type])


def build_actor_class_info(
    ctx: ClassDefContext,
    methods: typing.List[FuncDef],
) -> TypeInfo:
    """Build the Actor class TypeInfo for an object having methods `methods`."""
    api: SemanticAnalyzer = ctx.api
    result = build_type_info(
        api=api,
        module_name="typed_ray.ray_types",
        cls_full_name="typed_ray.ray_types.ActorHandle",
        class_name="ActorHandle",
    )
    for method in methods:
        type_ = build_remote_method(ctx, method)
        utils.add_attribute(name=method.name, cls=result.defn, type_=type_)
    return result


def build_actor_class_instance(
    ctx: ClassDefContext,
    methods: SymbolTable,
    decorated_cls: MypyType,
) -> MypyType:
    """Build the Actor class instance for an object having methods `methods`."""
    return Instance(build_actor_class_info(ctx=ctx, methods=methods), [decorated_cls])
