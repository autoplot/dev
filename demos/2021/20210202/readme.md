# Autoplot used to download files from HTTP for IDL

For years, we're used Autoplot to load data into IDL, and there are many other
useful things Autoplot's Java codes can do.  For example, if one wants to
download a file, Autoplot's "getFile" can be called from IDL and all the
mechanics of checking for file freshness and downloading are handled transparently.
See https://github.com/autoplot/dev/blob/master/demos/2021/20210202/idl_get_file.idl
for command which when entered at the IDL command line will download a file.

The routine ap_get_file.pro is intended to make this a little easier, providing
a one-line method for downloading a resource:

    fln= ap_get_file(  'https://emfisis.physics.uiowa.edu/events/rbsp-a/misc-support-files/rbspa-half-orbit-periods2.txt' )


