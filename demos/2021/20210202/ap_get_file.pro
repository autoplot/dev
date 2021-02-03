function ap_get_file, s_url, monitor=monitor
   setenv, 'CLASSPATH=autoplot.jar'  ; download from http://autoplot.org/latest/autoplot.jar
   if ( not keyword_set(monitor) ) then begin
       monitor= OBJ_NEW()
   endif
   
   ; get the Java class so we can use its static methods.
   DataSetURI= OBJ_NEW( 'IDLJavaObject$Static$DataSetURI', 'org.autoplot.datasource.DataSetURI' )

   ff= DataSetURI.getFile(s_url,monitor)
   return, ff
end
