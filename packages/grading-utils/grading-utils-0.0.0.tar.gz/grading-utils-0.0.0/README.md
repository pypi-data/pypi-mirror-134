# Grading Utils
### A collection of utilities for grading Python assignments.
Utilities are based off some common unit testing patterns.
Overall, syntax is modelled off JavaScript's Jest syntax,
with some modifications (hence `camelCase`, for example).

## Design Philosophy:
- security
- simplicity
- immutability

## Matchers and Modifiers
The most common operations with this module will involve matching test values to expected values.
All matchers begin with the `expect(value)` syntax, and are chained by some matcher.
For example, if we want to test $f(x) = x^2$, we write:
```py
from GradingUtils import expect
expect(f(2)).toEqual(4)
```
In this case, we could also write:
```py
expect(f(2)).toBe(4)
```
which will check for referential equality amonst the two objects.
However, **use caution** when using `.toBe()` to compare objects for equality,
as this will not use `obj.__eq__` or `obj.__hash__` to compare objects.
Matchers behave similarly to Python's `assert`, but provide more context on error.

Generally, matchers accept any type for which they are logically defined.
For example, `.toBeApprox(2.5, eps=0.1)` works for numeric types.

#### Matchers with Callable Objects
Typically, we want to check the output of a function,
so we call the function and pass its result to the expectation (`expect(f(x))`).
Occasionally, matchers need to track the way functions behave.
For example, let `avg(l: iter) = sum(iter) / len(iter)`.
If we want to check whether `[]` throws `ZeroDivisionError`,
we can write:
```py
expect(avg).toThrow(ZeroDivisionError, [])
```
Thus, we pass the function (uncalled) to our `expect` call,
then we pass `toThrow`'s custom argument (the exception to `except`),
and then all arguments to the function to the `.toThrow` call.
This is an unfortunate limitation, but this works for the time being.
In the future, some decorator workaround may be implemented.

#### List of Matchers
The following matchers are currently defined:
- `toBe`
- `toEqual`
- `toBeApprox`
- `toMatchType`
- `toMatch`
- `toContain`
- `toBeGreaterThan`
- `toBeLessThan`
- `toThrow`

### Modifiers
Modifiers are used to modify the behavior of matchers, by modifying the underling "Expectation" object.
Most commonly, we may want to expect that a certain condition is *not* met.
We can chain modifiers for thus purpose.
Modifiers use `._modifier_name` syntax, with `()` if arguments are needed.
There are currently only 3 modifiers:
###### `._not`
This modifier negates the expectation. For $$f(x) = x^2$$:
```py
expect(f(2))._not.toBeGreaterThan(2) # throws GradingError
```

###### `._exception(e)`
If we want to throw a custom exception when a matcher fails.
```py
expect(f(2))._exception(UrAnAwfulProgrammerError).toBe(4)
```

###### `._maxtime(s)`
This is one of 3 existing options for timing.
The `_maxtime` modifier should be used similarly to a matcher with callables.
To set a 2-second time limit on `slow_reducer(some_set)`,
and expect a result of `True` we write:
```py
expect(slow_reducer)._maxtime(2, some_set).toBe(True)
```
For all timing semantics, see the dedicated timing section.

###### Looking Forward
`_and` and `_or` are some potential future modifiers.


## Timing
One critical aspect of any timer implementation is that for long running functions,
we want to keep grading time down; execution should be immediately stopped
when the time limit is reached, with a fail error.
This avoids functions from taking needlessly long times when they will fail anyways.
All times are given in seconds.

Three methods are provided for time limiting functions:
```py
with timer(5):
    expect(slow_reducer(some_set)).toBe(True)
```
Or, when defining functions:
```py
@time_limit(5)
def slow_reducer(some_set):
    pass # implementation here
expect(slow_reducer(some_set)).toBe(True)
```
Naturally, this can be easily used to wrap student solutions.

Finally, the `_maxtime` modifier can be used directly:
```py
expect(slow_reducer)._maxtime(2, some_set).toBe(True)
```