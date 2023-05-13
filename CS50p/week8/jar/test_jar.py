from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(24)
    assert jar.capacity == 24
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_dposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5

    try:
        jar.deposit(-1)
    except ValueError as e:
        assert str(e) == "Cannot deposit a negative number of cookies"

    try:
        jar.deposit(1)
    except ValueError as e:
        assert str(e) == "Exceeds maximum capacity"

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0

    try:
        jar.withdraw(-1)
    except ValueError as e:
        assert str(e) == "Cannot withdraw a negative number"

    try:
        jar.withdraw(1)
    except ValueError as e:
        assert str(e) == "Not enough cookies in the jar"
