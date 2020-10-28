This shows how the old Python templates worked.  Autoplot's Jython is a 
very old version of Python, version 2.2.  There are a number of reasons 
why upgrading to 2.7 is difficult, and this style must be used for now.

~~~~~
'the name is %(n)s' % { 'n':'Bond' }
~~~~~

The new(er) style is to use string.format, but this is not supported:
~~~~~
'the name is {n}' % { n='Bond' }
~~~~~

Other keywords I used while looking for examples were macros and string substitution.
