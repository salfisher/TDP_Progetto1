from Collections.MyList import MyList

foo = MyList(['hey','i\'m','tdp','project'])
foo.append(2)
foo.append(3)
foo.append(4)
foo.append(5)
foo.append(6)
print(len(foo))
print(foo.pop(9))
print(foo)
foo.reverse()
print(foo)
#print(foo.remove(3))
print(len(foo))
foo.insert(5,10)
print(foo)
print(len(foo))
foo2 = [2,3,4,5]
print(len(foo))
foo.extend(iter(foo2))
print(foo)
print(len(foo))
foo3 = [100,121,12,13]
print(foo.__getitem__(13)._value)
print("nuova lista", foo.__add__(foo3))
print(foo.count(5))
print(5 in foo)
print(foo.copy())
print(foo.index(4))
fooeq1=MyList([4,5,9])
fooeq2=MyList([4,5,9])
print(fooeq1 != fooeq2)