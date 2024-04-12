
pro make_large_save

   tags= create_struct( 'a', [0,0,0,1,1,1] )
 
   for i=0,99 do begin
      t= create_struct( name='tag'+string(i,format='%03d'), 'var', randomn(s,100000) )
      tags= create_struct( tags, 'tag'+string(i,format='%03d'), t )
   endfor

   save, file='large_save.idlsav', tags

   vvs= ''
   for i=0,99 do begin
      s= 'tag'+string(i,format='%03d')+'=randomn(s,100000)'
      print, s
      _= execute( s )
      vvs= vvs + ',' + 'tag'+string(i,format='%03d')
   endfor
   print, 'save, file="many_variables.idlsav" '+vvs
   _= execute( 'save, file="many_variables.idlsav" '+vvs )
   
end
