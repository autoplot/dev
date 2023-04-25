# Demo use of Java/Autoplot/QDataSet DataSetBuilder object in Python.

import autoplot,jpype,random

# download autoplot.jar, add it to the classpath, and start JPype's Java Virtual Machine (JVM)
autoplot.javaaddpath()

# Get the Java class for building data, and create a new builder with 2 indices, initially 100 records, and 2 fields per record.
DataSetBuilder=jpype.JClass('org.das2.qds.util.DataSetBuilder')
dsb=DataSetBuilder(2,100,2)

n=1000
for i in range(n):
   dsb.nextRecord(['2003-04-05T00:00Z',random.gauss(1,2)])
ds= dsb.getDataSet()
applot(ds)
