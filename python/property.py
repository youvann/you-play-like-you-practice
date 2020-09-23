"""
Resource
========

https://www.programiz.com/python-programming/property

Take away
=========

Whenever we assign or retrieve any object attribute like temperature as shown above,
Python searches it in the object's built-in `__dict__` dictionary attribute. `human.temperature` internally becomes `human.__dict__['temperature']`.

In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:
>>> property(fget=None, fset=None, fdel=None, doc=None)

With property defined, any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up.
Similarly, any code that assigns a value to temperature will automatically call set_temperature().
"""


class CelsiusPropertyClass:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    """
    In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:
    >>> property(fget=None, fset=None, fdel=None, doc=None)
    """
    # Method 1 : creating a property object
    temperature = property(get_temperature, set_temperature)

    # Method 2 : creating a property object
    temperature = property()
    temperature = temperature.getter(get_temperature)
    temperature = temperature.setter(set_temperature)


class CelsiusPropertyDecorator:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


if __name__ == '__main__':
    # human = CelsiusPropertyClass(37)
    human = CelsiusPropertyDecorator(37)

    print(human.temperature)
    print(human.to_fahrenheit())
    human.temperature = -300
