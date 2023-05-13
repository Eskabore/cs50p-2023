# Jar Class

The `Jar` class represents a cookie jar that can store cookies, with a specified maximum capacity. The class has methods to deposit cookies, withdraw cookies, and display the contents of the jar. The class also provides properties to access the capacity and the current number of cookies in the jar.

Here's a detailed explanation of the code:

## Class Definition

```python
class Jar:
```

This line defines the class `Jar`.

## Constructor

```python
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0
```

The constructor takes an optional `capacity` parameter, which defaults to 12. It checks if the given capacity is a non-negative integer, raising a `ValueError` if the check fails. The capacity is stored in the `_capacity` instance variable, and the initial number of cookies in the jar is set to 0 in the `_cookies` instance variable.

## String Representation

```python
    def __str__(self):
        return "🍪" * self._cookies
```

This method defines the string representation of a `Jar` object. It returns a string with as many cookie emojis as there are cookies in the jar.

## Deposit Method

```python
    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeds maximum capacity")
        self._cookies += n
```

The `deposit` method takes an integer `n` and adds that number of cookies to the jar. It checks if `n` is negative or if adding `n` cookies would exceed the jar's capacity, raising a `ValueError` in either case. If the checks pass, it increments the `_cookies` instance variable by `n`.

## Withdraw Method

```python
    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number")
        if self._cookies - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._cookies -= n
```

The `withdraw` method takes an integer `n` and removes that number of cookies from the jar. It checks if `n` is negative or if there are not enough cookies in the jar to withdraw `n` cookies, raising a `ValueError` in either case. If the checks pass, it decrements the `_cookies` instance variable by `n`.

## Capacity Property

```python
    @property
    def capacity(self):
        return self._capacity
```

The `capacity` property is a read-only property that returns the maximum capacity of the jar.

## Size Property

```python
    @property
    def size(self):
        return self._cookies
```

The `size` property is a read-only property that returns the current number of cookies in the jar.