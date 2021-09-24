# Interoperability with IDL, Matlab, and Python
Autoplot runs within the "Java Virtual Machine" but it can still
be connected to "native" processes like IDL, Matlab, and Python.  Autoplot
provides adapters so that it can be used from these environments.

## data loading

The first service Autoplot provides is data loading.  Autoplot loads data
from many different sources, including obscure sources like Planetary Data 
Systems (PDS) and Radiojove, using concise data URIs.  If groups can use 
Autoplot to get a first look at data needed for an analysis, they can also 
use that same URI to load data into their preferred analysis environment.

http://autoplot.org/idl

http://autoplot.org/matlab

http://autoplot.org/python

These pages show how a bridge object is created that will request data via
Autoplot, moving data from Autoplot's memory space into the IDL or Python process
memory.

Note the Python interface is broken with newer versions of Python, and a new 
"Pythonic" interface is coming.

## plotting from IDL, Matlab, and Python

It's also possible to plot from these environments using Autoplot.  This 
provides a useful tool for getting quick looks of data when working in these 
environments interactively.  




