from Collections.MyList import MyList

foo = MyList(['hey','i\'m','tdp','project'])
foo.append(2)
foo.append(3)
foo.append(4)
foo.append(5)
foo.append(6)
"""print(len(foo))
print(foo.pop(9))
print(foo)
foo.reverse()
print(foo)
#print(foo.remove(3))
print(len(foo))
foo.insert(5,100)
print('aggiunto',foo)
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
fooeq1=MyList([2,12,9])
fooeq2=MyList([4,5,9])
fooeq3=[5,22,200]
fooeq4=[5,22,90]
print(fooeq1 != fooeq3)
print(fooeq1 == fooeq3)
"""


print('lista da suffis')
print(foo)
print('inizio suffissi')
print(foo.suffix())
print(foo.suffix_rec())








"""print(fooeq1 <= fooeq3)
foo4 =  MyList(2,3,44,5,6,7,8,fooeq4,fooeq3)
print(foo4)
foo4.sort()
print(foo4)
print('ciao')
foo4.suffix_rec()"""