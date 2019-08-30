def solve(eq, var='X'):
    eq1 = eq.replace("=", "-(") + ")"
    c = eval(eq1, {var: 1j})
    print
    eq1, c.real
    return -c.real / c.imag
# "x - 2*x + 5*x - 46*(235-24) = x + 2"
#  X-3+2*X=4-3*X
test=input()
# print (solve(test))
print (int(solve(test)))
