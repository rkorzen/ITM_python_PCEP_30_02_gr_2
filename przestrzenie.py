a = 1      # znajduje się w przestrzeni globalnej

def foo():
    global a
    a = 2  # to a jest w przestrzeni lokalnej
    print("in foo:", a)
    print(locals())
    print(globals())
    
print()
print()
print("before", a)    
foo()
print("after", a)    

print()
print()
print(locals())
print(globals())

