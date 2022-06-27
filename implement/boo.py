def foo(h):
    if h == 0:
        return 1
    elif h == 1:
        return 2
    k = foo(h-1) + foo(h-2)
    return k

print(foo(7))