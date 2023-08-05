import typing
from pprint import pformat, pprint

from mypy.nodes import (
    ARG_NAMED,
    ARG_OPT,
    ARG_POS,
    MDEF,
    ArgKind,
    Argument,
    Block,
    ClassDef,
    FuncDef,
    PassStmt,
    SymbolTableNode,
    TypeInfo,
    TypeVarExpr,
    Var,
)
from mypy.plugin import ClassDefContext, DynamicClassDefContext
from mypy.semanal import SemanticAnalyzer
from mypy.semanal_shared import set_callable_name
from mypy.types import AnyType, CallableType, Instance, NoneType
from mypy.types import Type as MypyType
from mypy.types import TypeOfAny, TypeVarType, UnboundType, UnionType
from mypy.typevars import fill_typevars


def build_argument(
    name: str,
    type_: typing.Optional[MypyType] = None,
    arg_type: ArgKind = ARG_POS,
) -> Argument:
    """Builds a function argument."""
    if type_ is None:
        type_ = AnyType(TypeOfAny.unannotated)
    return Argument(Var(name, type_), type_, None, arg_type)


def build_func_def(
    args: typing.List[Argument],
    return_type: MypyType,
    fallback: Instance,
    func_info: TypeInfo,
    name: str,
    tvar_def: typing.Optional[TypeVarType] = None,
    self_type: MypyType = None,
    is_static: bool = False,
    is_property: bool = False,
    body: Block = None,
) -> FuncDef:
    if not is_static:
        self_type = self_type or fill_typevars(func_info)
        args = [Argument(Var("self"), self_type, None, ARG_POS)] + args
    arg_types, arg_names, arg_kinds = [], [], []
    for arg in args:
        assert arg.type_annotation, "All arguments must be fully typed."
        arg_types.append(arg.type_annotation)
        arg_names.append(arg.variable.name)
        arg_kinds.append(arg.kind)

    signature = CallableType(arg_types, arg_kinds, arg_names, return_type, fallback)
    if tvar_def:
        signature.variables = [tvar_def]
    if not body:
        body = Block([PassStmt()])
    func = FuncDef(name, args, body)
    func.info = func_info
    func.type = set_callable_name(signature, func)
    func._fullname = func_info.fullname + "." + name
    func.line = func_info.line
    func.is_static = is_static
    func.is_property = is_property
    return func


def add_method(name: str, func: FuncDef, cls_info: TypeInfo, replace=False) -> None:
    # First remove any previously generated methods with the same name
    # to avoid clashes and problems in the semantic analyzer.
    if name in cls_info.names:
        sym = cls_info.names[name]
        if sym.plugin_generated and isinstance(sym.node, FuncDef):
            cls_info.defn.defs.body.remove(sym.node)
    # NOTE: we would like the plugin generated node to dominate, but we still
    # need to keep any existing definitions so they get semantically analyzed.
    if name in cls_info.names and not replace:
        # Get a nice unique name instead.
        return
        # r_name = get_unique_redefinition_name(name, cls_info.names)
        # cls_info.names[r_name] = cls_info.names[name]

    cls_info.names[name] = SymbolTableNode(MDEF, func, plugin_generated=True)
    cls_info.defn.defs.body.append(func)


def add_attribute(name: str, cls: ClassDef, type_: MypyType) -> None:
    var = Var(name)
    var.info = cls.info
    var.type = type_
    var._fullname = cls.info.fullname + "." + name
    cls.info.names[name] = SymbolTableNode(MDEF, var)


def add_global(
    ctx: typing.Union[ClassDefContext, DynamicClassDefContext],
    module: str,
    symbol_name: str,
    asname: str,
) -> None:
    module_globals = ctx.api.modules[ctx.api.cur_mod_id].names
    if asname not in module_globals:
        lookup_sym: SymbolTableNode = ctx.api.modules[module].names[symbol_name]

        module_globals[asname] = lookup_sym


def add_remote_method_to_context(ctx: ClassDefContext) -> None:
    add_global(
        ctx,
        "typed_ray.ray_types",
        "RemoteFunction",
        "__tr_RemoteMethod",
    )


def add_actor_class_to_context(ctx: ClassDefContext) -> None:
    add_global(
        ctx,
        "typed_ray.ray_types",
        "ActorClass",
        "__tr_ActorClass",
    )


def add_object_ref_to_context(ctx: ClassDefContext) -> None:
    add_global(
        ctx,
        "typed_ray.ray_types",
        "ObjectRef",
        "__tr_ObjectRef",
    )


def is_magic_method(name: str) -> bool:
    return name.startswith("__") and name.endswith("__")


def get_return_type(method: FuncDef) -> MypyType:
    try:
        return method.type.ret_type
    except AttributeError:
        return AnyType(TypeOfAny.unannotated)


def var_to_type(var: Var) -> MypyType:
    return var.type or AnyType(TypeOfAny.unannotated)


def unbound_to_instance(api: SemanticAnalyzer, type_: UnboundType) -> MypyType:
    if not isinstance(type_, UnboundType):
        return type_

    if type_.name == "Optional":
        # convert from "Optional?" to the more familiar
        # UnionType[..., NoneType()]
        return unbound_to_instance(
            api,
            UnionType(
                [unbound_to_instance(api, typ_arg) for typ_arg in type_.args]
                + [NoneType()]
            ),
        )
    TypeVarExpr

    node = api.lookup(type_.name, type_)

    if node is None or not isinstance(node, SymbolTableNode):
        return type_
    bound_type = node.node
    if isinstance(bound_type, Var) and bound_type.name == "None":
        return NoneType()
    if isinstance(bound_type, Var):
        bound_type = var_to_type(bound_type)
    args = []
    for arg in type_.args:
        if isinstance(arg, UnboundType):
            args.append(unbound_to_instance(api, arg))
        elif isinstance(arg, TypeVarExpr):
            args.extend(arg.values)
        else:
            args.append(arg)
    return Instance(bound_type, args)


def pformat_(x: typing.Any, seen=None) -> typing.Any:
    if seen is None:
        seen = set()
    if isinstance(x, list):
        if not x:
            return "[]"
        result = []
        for y in x:
            result.append(pformat_(y, seen))
            seen.add(id(y))
        return result
    if isinstance(x, str):
        return x
    result = {}
    for name in dir(x):
        try:
            value = getattr(x, name)
        except (AttributeError, AssertionError):
            continue
        value_id = id(value)
        if name.startswith("__") and name.endswith("__"):
            continue
        if value_id in seen:
            continue
        seen.add(value_id)
        result[name] = pformat_(value, seen)
    result["class"] = type(x)
    result["id"] = id(x)
    return result


def print_(x: typing.Any) -> None:
    as_str = f"----------{type(x)}----------\n"
    as_str += pformat(pformat_(x))
    as_str += "\n"
    as_str += "-----------------------------"
    pprint(as_str)
