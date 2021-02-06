"""
This is the helpers module. It contains functions that help.
"""


class Hello(object):
    """
    This is a Hello class docstring
    """

    def __init__(self, name):
        """init method

        Args:
            name (str): The name of the person who will be
            greeted.
        """
        self.name = name

    def say_hello(self):
        """
        Say hello!
        """
        print("Hello %s" % self.name)
