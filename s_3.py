# dictionary
# v={1:'java',
# 3:'python',
# 4:'js'}
# print(v[4])   # js
# print(v[1])   # java
# print(v[6])     #  KeyError: 6
# r={2:234,3:675,6:765,9:345}
# print(r[6])    # 765
# print(r[10])KeyError: 10
# g={3:'python',9:'java',7:876,5:987}
# g.clear()
# print(g)    #{}
# m={1:'house',3:'home',6:'building',}
# m.clear()
# print(m)    # {}
# u={654,879,980,672,324}
# print(dict.fromkeys(u,765)) # {672: 765, 324: 765, 980: 765, 654: 765, 879: 765}
# d={546,879,765,234,238}
# print(dict.fromkeys(d,'key'))   # {546: 'key', 234: 'key', 765: 'key', 238: 'key', 879: 'key'}
# p={1,2,3,4,5}
# print(dict.fromkeys(p,"red"))     #{1: 'red', 2: 'red', 3: 'red', 4: 'red', 5: 'red'}
# p={1:'red',2:'pink',3:'yellow',4:'blue'}
# print(p.get(3))    #yellow
# print(p.get(6))     #None
# p.pop(4)
# print(p)    # {1: 'red', 2: 'pink', 3: 'yellow'}
# p.pop(2)
# print(p)    #{1: 'red', 3: 'yellow', 4: 'blue'}
# e={6:'nature',3:'rain',8:'earth',9:'wind'}
# e.popitem()
# print(e)   # {6: 'nature', 3: 'rain', 8: 'earth'}
# w={3:453,6:567,9:354,2:640}
# w.popitem()
# print(w)      #{3: 453, 6: 567, 9: 354}
# u={9:'',4:"",8:"hello",2:'hey',3:987}
# u.update({7:"world"})
# print(u)         #{9: '', 4: '', 8: 'hello', 2: 'hey', 3: 987, 7: 'world'}
# m={2:465,9:432,3:345,4:879}
# m.update({6:"hey"})
# print(m)        # {2: 465, 9: 432, 3: 345, 4: 879, 6: 'hey'}
# m.update({9:546})
# print(m)       # {2: 465, 9: 546, 3: 345, 4: 879}
# t={3:"hello",4:987,6:'hey',8:[2,3]}
# t.setdefault(7,'hi')
# print(t)   # {3: 'hello', 4: 987, 6: 'hey', 8: [2, 3], 7: 'hi'}
# s={1:234,2:897,3:543,4:987}
# s.setdefault(6,123)
# print(s)      # {1: 234, 2: 897, 3: 543, 4: 987, 6: 123}
# r={9:987,8:876,7:765,6:543}
# r.copy()
# print(r)      #{9: 987, 8: 876, 7: 765, 6: 543}
# h={1:980,2:987,3:876,4:765}
# h.values()
# print(h)  # {1: 980, 2: 987, 3: 876, 4: 765}

