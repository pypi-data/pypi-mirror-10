argy
====
Argy is a simple tool for creating CLI programs using python, it tries to remove all the fuzz that comes with the standard library.

Usage
=====

.. code::
   
    import argy


    @argy
    def add_numbers(x, y, subtract=False):
        """Adder of numbers
        Just adds two numbers, nothing really special about it

        :param x: The first number
        :type x: int
        :param y: The second number
        :type y: int
        :param subtract: Should we subtract instead?
        :type subtract: bool
        """
        if not subtract:
            return x + y
        else:
            return x - y

This will create a CLI-program with the expected arguments, see also example.py

.. code::

    $ python example.py -h
    usage: example.py [-h] [--subtract SUBTRACT] x y

    positional arguments:
    x                    The first number
    y                    The second number

    optional arguments:
    -h, --help           show this help message and exit
    --subtract SUBTRACT  Should we subtract instead?

Contributions
=============

Contributions are welcome!
