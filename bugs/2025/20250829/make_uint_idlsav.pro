
pro make_uint_idlsav
; make arrays for Autoplot testing.

my_uint_array = MAKE_ARRAY(10, /UINT) 
my_uint_array[1]=1
my_uint_array[3]=2
my_uint_array[5]=2L^16-1
my_uint_array[7]=-3

print, my_uint_array

; Create a 5x5 unsigned longword integer array with sequential values
my_ulong_seq = INDGEN(5, 5, /ULONG)
my_ulong_seq[0,0]= -1

save, file='/tmp/ap/uint_types.idlsav', my_uint_array, my_ulong_seq

end
