import dis
import math
import multiprocessing

def display_step(*args):
    x = 1
    y = 2
    z = x + y
    print("HI THERE", z, args)

code = """
print(0)
a = 1
print(a)
b = 0
for i in range(10):
    b = b + 1
print(b)
c = a + b
print(c)
"""

dis.dis(code)

print("a")
exec(code, {"_pyvcs_display_step": display_step})
print("b")
exec(code, {"_pyvcs_display_step": display_step})

for i in range(10):
    print(math.ceil(3.9))
