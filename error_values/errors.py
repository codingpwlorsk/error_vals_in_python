from enum import Enum, auto
from typing import Generic, TypeVar, Optional, Any
from inspect import isclass


class Result(Enum):
    FAIL = auto()
    PASS = auto()


T = TypeVar("T", bound=Exception)
U = TypeVar("U")


class No_Error(Exception):
    """
    this is no errors and this is created to
    put in the scond type in Potential_Error if there is no error
    """
    pass


class Did_Not_Handeled_Exception(Exception):
    pass


class Attmped_To_Dewrap_While_Have_Error(Exception):
    pass


class Potential_Error(Generic[U, T]):

    def __init__(self, value: U, error: Optional[T] = None):
        self.__val = value
        if error is None:
            self.error = No_Error()
        else:
            self.error = error
        self.handled = False

    def stat(self) -> Result:
        self.Handled = True
        return self.raw_stat()

    def dewrap(self) -> U:
        """this return the value, only if
        you handle the cas that it is an error."""
        if self.Handled:
            return self.__val
        if self.error != No_Error:
            raise Attmped_To_Dewrap_While_Have_Error(
                                                    "you mustn't have errors "
                                                    "inorder to dewrapp")
        raise Did_Not_Handeled_Exception(
                                        "you forgot to handle the "
                                        "speciel case. That case "
                                        "being if an error "
                                        "occured. Inordr to fix "
                                        "this you must call the "
                                        "stat method, then do this")

    def raw_stat(self):
        """
        this makes it so that it deosn't remember that
        it handle the variable.
        """
        if isinstance(self.error, No_Error):
            return Result.PASS
        else:
            return Result.FAIL

    def raise_error(self) -> None:
        raise self.error  # type: ignore


def potential_error_wrap(val: Any):
    if isclass(val) and issubclass(val, Exception):
        return Potential_Error(None, val())
    if issubclass(type(val), Exception):
        return Potential_Error(None, val)  # type:ignore
    else:
        return Potential_Error(val, No_Error())


def func_result_to_potential_error(func):
    """
    this is a wrappr for functions, the reason for this is so
    that you don't have to write potential_error_wrap all the time
    """
    def auto_wrap(*args, **kwargs):
        result = func(args, kwargs)
        return potential_error_wrap(result)
    return auto_wrap


def dangerous_func_to_potntial_error(func):
    """
    this is for functions with raise
    """
    def auto_wrap(*args, **kwargs):
        try:
            result = func(args, kwargs)
            return potential_error_wrap(result)
        except Exception as e:
            return potential_error_wrap(e)
    return auto_wrap