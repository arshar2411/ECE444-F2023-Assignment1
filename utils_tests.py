from utils import *


print("Testing reversed()")
# int input
assert(utils.reversed(345) == 543)
print("int reversed")
# str input
try:
    utils.reversed("345")
except TypeError:
    print("TypeError raised, make sure input is integer")
# float input
try:
    utils.reversed(345.5) == TypeError
except TypeError:
    print("TypeError raised, make sure input is integer")

print("Testing formatter()")
# int input
assert(utils.formatter(10) == ('0o1010', '0b12'))
print("int formatted")
# str input
try:
    utils.formatter("10")
except TypeError:
    print("TypeError raised, make sure input is integer")
# float input
try:
    utils.formatter(10.5) == TypeError
except TypeError:
    print("TypeError raised, make sure input is integer")