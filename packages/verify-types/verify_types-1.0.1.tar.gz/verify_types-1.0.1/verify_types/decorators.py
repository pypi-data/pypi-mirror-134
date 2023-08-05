import typing
from verify_types.exceptions import (
    NotTypeHintException,
)


def validate_params(function):
    """
        Decorator to valid params of any functions.
    """
    def wrapper(*args, **kwargs):
        type_hint_type = function.__annotations__
        name = function.__code__.co_varnames

        if len(type_hint_type.keys()) < 1:
            raise NotTypeHintException("Use type hint!")
        # warking with classes
        if name[0] == 'self':
            filter_args = args[1:]
        else:
            filter_args = args

        for param, value in zip(type_hint_type.keys(), filter_args):
            if param == 'return':
                break

            if isinstance(type_hint_type[param], typing.__SpecialForm):
                raise Exception("Special type not coverage!")

            # If type began of typing he has origin tag
            try:
                actual_type = type_hint_type[param].__origin__
            except AttributeError:
                actual_type = type_hint_type[param]

            if not(
                isinstance(value, actual_type) or type(value) == actual_type
            ):
                raise ValueError(
                    "Param: {} has type: {} but type "
                    "must be: {} in path: {}".format(
                        param,
                        type(value),
                        type_hint_type[param],
                        function.__module__ + "." + function.__name__
                    )
                )
            response = function(*args, **kwargs)

            try:
                return_type = type_hint_type["return"].__origin__
            except AttributeError:
                return_type = type_hint_type["return"]

            if response is not None:
                if return_type is None:
                    return_type = type(None)
                if not isinstance(response, return_type):
                    raise ValueError(
                        "Param: {} has type: {} but type "
                        "must be: {} in path: {}".format(
                            "return",
                            type(response),
                            return_type,
                            function.__module__ + "." + function.__name__
                        )
                    )
            else:
                if not isinstance(return_type, type(None)):
                    raise ValueError(
                        "Param: {} has type: {} but type "
                        "must be: {} in path: {}".format(
                            "return",
                            type(response),
                            return_type,
                            function.__module__ + "." + function.__name__
                        )
                    )
            return response


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
