import typing
from verify_types.exceptions import (
    NotTypeHintException,
)


def validate_params(function):
    """
        Decorator to valid params of any function.
    """
    def wrapper(*args, **kwargs):
        type_hint_type = function.__annotations__
        name = function.__code__.co_varnames

        if len(type_hint_type.keys()) < 1:
            raise NotTypeHintException("Use type hint")
        if name[0] == 'self':
            filter_args = args[1:]
        else:
            filter_args = args

        for param, value in zip(type_hint_type.keys(), filter_args):
            if param == 'return':
                break
            if isinstance(type_hint_type[param], typing._SpecialForm):
                continue
            try:
                actual_type = type_hint_type[param].__origin__
            except AttributeError:
                actual_type = type_hint_type[param]

            if isinstance(actual_type, typing._SpecialForm):
                actual_type = type_hint_type[param].type.__args__

            if not (
                isinstance(value, actual_type) or type(value) == actual_type
            ):
                raise ValueError(
                    "Param: {} has type: {} but type "
                    "must be: {} in path {}".format(
                        param,
                        type(value),
                        type_hint_type[param],
                        function.__module__ + "." + function.__name__
                    )
                )
        response = function(*args, **kwargs)
        try:
            actual_type = type_hint_type["return"].__origin__
        except AttributeError:
            actual_type = type_hint_type["return"]

        if response is not None:
            if actual_type is None:
                actual_type = type(None)
            if not isinstance(response, actual_type):
                mes = "Param: {} has type: {} but type must be: {} in path {}"
                raise ValueError(
                    mes.format(
                        "return",
                        type(response),
                        actual_type,
                        function.__module__ + "." + function.__name__
                    )
                )
        else:
            if not isinstance(actual_type, type(None)):
                raise ValueError(
                    "Return is {} but must be: {} in path: {}".format(
                        type(response),
                        actual_type,
                        function.__module__ + "." + function.__name__
                    )
                )
        return response
    return wrapper


def decorate_all_methods(decorator):
    """
        Decorator para aplicar em todas os métodos um determinado decorator.
    """
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
