import signal
import sys
from contextlib import contextmanager
from functools import wraps
from re import Pattern
from typing import TypeVar, Generic, Callable, Any, Union, Type, Iterable, Optional
from unittest.mock import patch

PRIMITIVES = (int, float, complex, str, bool, tuple, list, dict, set, frozenset, iter, bytes, bytearray)
Number = Union[int, float, complex]
ReturnType = TypeVar('ReturnType')


class GradingError(AssertionError):
    pass


class SanitationError(GradingError, ValueError):
    pass


def sanitize(value: ReturnType) -> None:
    pass


def primitive_compare(value: Any, expected: Any, mode: str = 'eq') -> bool:
    if type(value) not in PRIMITIVES:
        raise ValueError(f'Expected a primitive type, got {type(value)}')
    if not is_type(value, type(expected)):
        raise ValueError(f'Expected {type(expected)}, got {type(value)}')
    [type_class] = [t for t in PRIMITIVES if is_type(value, t)]
    if mode == 'eq':
        return type_class.__eq__(value, expected)
    elif mode == 'lt':
        return type_class.__lt__(value, expected)
    elif mode == 'gt':
        return type_class.__gt__(value, expected)


def is_type(value: Any, type_class: Type):
    return id(value.__class__) == id(type_class)


@contextmanager
def timer(seconds: int = 5) -> None:
    def handle_signal(_signum, _frame):
        raise GradingError(f'Time Limit Exceeded (max {seconds}s), exited early.')
    signal.signal(signal.SIGALRM, handle_signal)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def time_limit(func: Callable, seconds: int = 5) -> Callable:
    @wraps(func)
    def timed_func(*args, **kwargs):
        with timer(seconds):
            return func(*args, **kwargs)

    return timed_func


def no_throw(func: Callable) -> Callable[[Any], bool]:
    @wraps(func)
    def no_throw_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True
        except Exception:
            return False

    return no_throw_func


# chaining for ors and ands
def funcpath(func: Callable) -> str:
    return f'{func.__module__}.{func.__name__}'


class Expectation(Generic[ReturnType]):
    value: ReturnType
    success_value: bool
    exception: Type[Exception]

    def __init__(self,
                 value: ReturnType,
                 success_value=True,
                 exception: Type[Exception] = GradingError):
        self.value = value
        self.success_value = success_value
        self.exception = exception
        sanitize(value)

    def __is__(self, expected: ReturnType) -> bool:
        return no_throw(self.toEqual)(expected) == self.success_value

    def toBe(self, expected: ReturnType) -> None:
        self.declare(id(self.value) == id(expected),
                     f'Expected {self.value} to have same reference as {expected}')

    def toEqual(self, expected: ReturnType, compare: Optional[Callable[[Any, Any], bool]]) -> None:
        err = f'Expected {self.value} to equal {expected}'
        try:
            self.declare(primitive_compare(self.value, expected, 'eq'), err)
        except ValueError as e:
            if is_type(self.value, expected.__class__):
                self.declare(self.value == expected and expected == self.value, err)
            if type(compare) == 'function':
                self.declare(compare(self.value, expected), f'{err}, using provided compare argument.')
            self.toBe(expected)

    def toSatisfy(self, predicate: Callable[[ReturnType], bool]) -> None:
        self.declare(predicate(self.value),
                     f'Expected {self.value} to satisfy {predicate}')

    def toBeApprox(self, expected: Number, eps: Number = 0.001) -> None:
        self.declare(abs(self.value - expected) <= eps,
                     f'Expected {self.value} to be approx {expected} with ε={eps}')

    def toMatchType(self, expected: Any) -> None:
        self.declare(is_type(self.value, expected.__class__),
                     f'Expected {self.value} to be of type {type(expected)}, got {type(self.value)}')

    def toMatch(self, regex: Pattern) -> None:
        self.declare(regex.match(self.value) is not None,
                     f'Expected {self.value} to partially match {regex}')

    def toBeEmpty(self) -> None:
        self.declare(len(self.value) == 0, f'Expected {self.value} to be empty')

    def toIncludeSomeOf(self, members: Iterable[Any]) -> None:
        self.declare(any(e in self.value for e in members),
                     f'Expected {self.value} to include some of {members}')

    def toIncludeAllOf(self, members: Iterable[Any]) -> None:
        self.declare(all(e in self.value for e in members),
                     f'Expected {self.value} to include all of {members}')

    def toIncludeSameOf(self, members: Iterable[Any]) -> None:
        # I haven't proofed this implementation, but I think it's correct?
        self.toIncludeAllOf(members)
        self.declare(len(set(self.value)) == len(set(members)),
                     f'Expected {self.value} to include only the elements of {members}')

    def toSatisfyAll(self, predicate: Callable[[Any], bool]) -> None:
        self.declare(all(predicate(e) for e in self.value),
                     f'Expected all elements of {self.value} to satisfy predicate {predicate}')

    def toSatisfySome(self, predicate: Callable[[Any], bool]) -> None:
        self.declare(any(predicate(e) for e in self.value),
                     f'Expected some elements of {self.value} to satisfy predicate {predicate}')

    def toContain(self, element: Any, at_least: int = 1, at_most: int = sys.maxsize) -> None:
        # should builtin count be used or a custom one?
        cnt = self.value.count(element)
        self.declare(at_least <= cnt <= at_most,
                     f'Expected {self.value} to contain {element} at least {at_least} times, got {cnt}')

    def toBeEven(self) -> None:
        self.declare(Expectation(self.value % 2).__is__(0),
                     f'Expected {self.value} to be even')

    def toBeOdd(self) -> None:
        self.declare(Expectation(self.value % 2).__is__(1),
                     f'Expected {self.value} to be odd')

    def toBeGreaterThan(self, expected: Number) -> None:
        self.declare(primitive_compare(self.value, expected, 'gt'),
                     f'Expected {self.value} to be greater than {expected}')

    def toBeLessThan(self, expected: Number) -> None:
        self.declare(primitive_compare(self.value, expected, 'lt'),
                     f'Expected {self.value} to be less than {expected}')

    def toThrow(self, exception: Type[Exception] = Exception, *args, **kwargs) -> None:
        try:
            self.value(*args, **kwargs)
            self.declare(False, f'Expected {self.value} to throw {exception}')
        except exception:
            pass

    def declare(self, condition: bool, message: str = 'Failed Assertion.') -> None:
        if condition != self.success_value:
            raise self.exception(f'{"[NOT] " if not self.success_value else ""} {message}')

    def toMakeRecursiveCalls(self, *args, **kwargs) -> None:
        self._calls(self.value, *args, **kwargs).toBeGreaterThan(1)

    @property
    def _not(self) -> 'Expectation':
        return Expectation(self.value, not self.success_value, self.exception)

    def _exception(self, exception: Type[Exception]) -> 'Expectation':
        return Expectation(self.value, self.success_value, exception)

    def _maxtime(self, time: Number, *args, **kwargs) -> 'Expectation':
        with timer(time):
            return Expectation(self.value(*args, **kwargs), self.success_value, self.exception)

    def _satisfying(self, predicate: Callable[[Any], bool]) -> 'Expectation':
        return Expectation(len(list(filter(predicate, self.value))), self.success_value, self.exception)

    def _calls(self, func: Callable[[Any], Any], *args, **kwargs) -> 'Expectation':
        with patch(funcpath(func), wraps=func) as mock_func:
            self.value(*args, **kwargs)
            return Expectation(int(mock_func.call_count), self.success_value, self.exception)


expect = Expectation
