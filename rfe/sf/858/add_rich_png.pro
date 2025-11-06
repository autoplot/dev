FUNCTION crc32_bytes, b
  ; Returns unsigned long CRC32 of byte array b
  return, ZLIB_CRC32(b)
END

PRO add_png_text_chunk, in_png, out_png, key, value
  COMPILE_OPT idl2
  ; Read file
  OPENR, lu, in_png, /GET_LUN, /BINARY
  sz = (FILE_STAT(in_png)).size
  buf = BYTARR(sz, /NOZERO)
  READU, lu, buf
  FREE_LUN, lu

  ; Walk chunks to find IEND offset
  off = 8L  ; skip PNG signature
  iend_off = -1L
  WHILE off LT (sz-12) DO BEGIN
    len = ( (ULONG(buf[off+0]) << 24) + (ULONG(buf[off+1]) << 16) + $
            (ULONG(buf[off+2]) <<  8) +  ULONG(buf[off+3]) )
    typ = STRING(buf[off+4:off+7])
    IF typ EQ 'IEND' THEN BEGIN
      iend_off = off
      BREAK
    ENDIF
    off += 12L + len   ; length(4) + type(4) + data(len) + crc(4)
  ENDWHILE
  IF iend_off LT 0 THEN MESSAGE, 'Invalid PNG: IEND not found.'

  ; Build tEXt data = key + NUL + value (latin-1 per spec)
  kbytes = BYTE(key)
  vbytes = BYTE(value)
  data   = [kbytes, BYTARR(1), vbytes]  ; NUL separator
  len_b  = ULONG(N_ELEMENTS(data))

  ; Chunk type
  ctype  = BYTE('tEXt')

  ; Length field (big-endian)
  len_be = [ BYTE((len_b >>> 24) MOD 256), BYTE((len_b >>> 16) MOD 256), $
             BYTE((len_b >>>  8) MOD 256), BYTE(len_b MOD 256) ]

  ; CRC over type+data
  crc_ul = crc32_bytes([ctype, data])
  crc_be = [ BYTE((crc_ul >>> 24) MOD 256), BYTE((crc_ul >>> 16) MOD 256), $
             BYTE((crc_ul >>>  8) MOD 256), BYTE(crc_ul MOD 256) ]

  chunk = [len_be, ctype, data, crc_be]

  ; Splice: insert before IEND
  newbuf = [ buf[0L:iend_off-1L], chunk, buf[iend_off:*] ]

  ; Write out
  OPENW, lu, out_png, /GET_LUN, /BINARY
  WRITEU, lu, newbuf
  FREE_LUN, lu
END
