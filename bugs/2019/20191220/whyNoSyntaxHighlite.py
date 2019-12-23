def foo(s):
   print(len(s))

ss = '1234567890'
for i in range(5,10):
   foo( ss[0:i] )
