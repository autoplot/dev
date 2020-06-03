The bug https://sourceforge.net/p/autoplot/bugs/1861/ talks about automatic conversions 
from rank 0 QDataSet to double, when the data is dimensionless.  This is not possible
because Jython is too aggressive about converting things, and I have to remind myself
every year or so why this is the case.  

The code which would need changing is the __tojava__ code.  The problem is that if there 
are two codes jython could use, it will pick the double version and remove titles etc, when
a rank0 version was available as well.
