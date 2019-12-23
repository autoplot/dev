class Foo:
   def __init__(self,prefix):
       self.prefix = prefix
         
   def foo(s):
       print(prefix + str(len(s)))

ss = '1234567890'
myfoo= Foo('>>')

for i in range(5,10):
   myfoo.foo( ss[0:i] )
