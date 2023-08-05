import typing

from mypy.plugin import Plugin
from typed_ray import callbacks, constants, mypy_types


class _RayPlugin(Plugin):
    _class_decorator_hook_plugins: typing.Dict[
        str, typing.Callable[[Plugin, str], mypy_types.ClassDecoratorHookCallback]
    ] = {constants.TYPED_RAY_REMOTE_DECORATOR: callbacks.RayWorkerDecoratorCallback}

    def get_class_decorator_hook(
        self, fullname: str
    ) -> typing.Optional[mypy_types.ClassDecoratorHookCallback]:
        if fullname.endswith("typed_ray.remote_cls"):
            return self._class_decorator_hook_plugins[
                constants.TYPED_RAY_REMOTE_DECORATOR
            ](self, fullname)


def plugin(version: str) -> Plugin:
    return _RayPlugin
