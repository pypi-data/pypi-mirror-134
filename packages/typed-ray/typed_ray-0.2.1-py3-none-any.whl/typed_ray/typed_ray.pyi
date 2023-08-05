import typing
from typing_extensions import ParamSpec
from typed_ray.ray_types import ObjectRef as ObjectRef, RemoteFunction as RemoteFunction

T = typing.TypeVar("T")
_ArgsT = ParamSpec("_ArgsT")
_ReturnT = typing.TypeVar("_ReturnT")

def put(value: T) -> ObjectRef[T]: ...
@typing.overload
def get(object_refs: ObjectRef[T]) -> T: ...
@typing.overload
def get(object_refs: typing.List[ObjectRef[T]]) -> typing.List[T]: ...
def remote_func(
    func: typing.Callable[_ArgsT, _ReturnT]
) -> RemoteFunction[_ArgsT, _ReturnT]: ...
def remote_cls(cls: typing.Type[typing.Any]) -> typing.Any: ...
