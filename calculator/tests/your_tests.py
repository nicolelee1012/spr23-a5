#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("1+2").output == "3"
assert run("2 * 4").output == "8"

###

print("All tests passed!")
