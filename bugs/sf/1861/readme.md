The bug https://sourceforge.net/p/autoplot/bugs/1861/ talks about automatic conversions 
from rank 0 QDataSet to double, when the data is dimensionless.  This is not possible
because Jython is too aggressive about converting things, and I have to remind myself
every year or so why this is the case.  
