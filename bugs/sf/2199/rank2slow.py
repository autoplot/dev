
import jpype
import numpy as np
import datetime
import os
import time

g_autoplot= '/tmp/autoplot.jar'

# wget -O /tmp/autoplot.jar http://autoplot.org/devel/autoplot.jar
jpype.startJVM(jpype.getDefaultJVMPath(),'-Djava.class.path='+g_autoplot)


org= jpype.JPackage("org")
apds= org.autoplot.idlsupport.APDataSet()
sta= 'vap+inline:findgen(86310,400)'
status= apds.loadDataSet(sta)

print( 'get values' )
t0= time.time()
vv= apds.values()
print( '   got %s in %f seconds' % (  'double array',  time.time()-t0 ) )
print( 'get np.array' )

t0= time.time()
spec= np.array(vv)
print( '   got %s in %f seconds' % (  'nparray', time.time()-t0 ) )

print( 'done' )


