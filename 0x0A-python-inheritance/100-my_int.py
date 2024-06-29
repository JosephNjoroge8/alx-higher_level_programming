#!/usr/bin/python3
class MyInt(int):
    """A rebel integer class"""
    def __eq__(self, other):
        """Inverts == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts != operator"""
        return super().__eq__(other)
