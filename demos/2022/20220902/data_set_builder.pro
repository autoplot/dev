; this shows how the DataSetBuilder object can be used to collect data.
; It's easy to assume that the following code will work fine:
;   pro collect_data, n
;      ds= []
;      for i=0,n-1 do begin
;         ds= [ ds, randomn(seed,1) ]
;      endfor
;      help, ds
;   end
; 
; The problem is this copies the data again and again, and instead of operating in 
; order(N) time, it is order(N^2).  When N is small, this is fine, but for bigger
; problems this will grind to a halt.
;
; The solution presented here is to use the Autoplot Java object DataSetBuilder which
; is designed to accumulate data like this.
;
;   pro collect_data, n
;      dsb= OBJ_NEW('IDLjavaObject$DataSetBuilder', 'org.das2.qds.util.DataSetBuilder', 1, 100 )
;      for i=0, n-1 do begin
;         dsb.nextRecord( randomn(seed,1)
;      endfor
;      ds= dsb.getDataSet()
;      help, ds
;   end
; 
; Note this needs the Autoplot jar file to be connected.  In unix:
;  unix$ wget -N http://autoplot.org/latest/autoplot.jar
;  unix$ export CLASSPATH=autoplot.jar
;  unix$ idl
pro collect_data, n
   dsb= OBJ_NEW('IDLjavaObject$DataSetBuilder', 'org.das2.qds.util.DataSetBuilder', 2, 100, 3 )
   for i=0, n-1 do begin
      dsb.nextRecord, randomn(seed,3) 
   endfor
   ds= dsb.getDataSet()
   help, ds
end

