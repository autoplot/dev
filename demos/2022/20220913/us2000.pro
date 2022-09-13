; demo how autoplot.jar can be used to handle datums and units like microseconds since 2000-01-01 (us2000).
; in unix, export CLASSPATH=autoplot.jar

units= obj_new( 'IDLJavaObject$Static$Units', 'org.das2.datum.Units' )
us2000= units.getByName('us2000')
tu= obj_new( 'IDLJavaObject$Static$TimeUtil', 'org.das2.datum.TimeUtil' )
d= us2000.createDatum(0)
print, d.toString()
; 2000-01-01T00:00:00.000Z
print, tu.fromDatum(d)                                                          
;        2000           1           1           0           0           0           0


