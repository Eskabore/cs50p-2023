class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeds maximum capacity")
        self._cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number")
        if self._cookies - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

# Optional
def main():
    jar = Jar()
    print("Initial cookie jar: ", jar)

    jar.deposit(5)
    print("After depositing 5 cookies: ", jar)

    jar.withdraw(2)
    print("After withdrawing 2 cookies: ", jar)

    print("Cookies jar capacity: ", jar.capacity)
    print("Number of cookies in the jar: ", jar.size)

if __name__ == "__main__":
    main()
