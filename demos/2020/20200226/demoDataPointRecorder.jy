setScriptTitle('Demo the Data Point Recorder which allows repeat values for X')

from org.das2.components import DataPointRecorder
dpr= DataPointRecorder()
dpr.setSorted(False)
addTab('dpr',dpr)
#rr= randn(20,2)
rr= bundle( dataset([1,1,2,2,3,3]), dataset([1,2,3,4,5,6])  )
dpr.addDataPoints(rr)
