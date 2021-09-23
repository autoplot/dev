Aggregation allows Autoplot to treat a files as a long time series, stringing
data from each file together to cover any interval.  There are many servers
that allow the scientist to grab data from an interval without regard to
files, but the problem here that someone has to create the server.  Autoplot's
aggregation works with files that have always been available, for example making 
Voyager data files written in the nineties as useful as data coming from the 
CDAWeb server.

Suppose you have files like:

~~~~~
http://autoplot.org/data/agg/hyd/2000/po_h0_hyd_20000104_v01.cdf
http://autoplot.org/data/agg/hyd/2000/po_h0_hyd_20000105_v01.cdf
~~~~~

You could plot each one, putting them onto the same plot, but another way to
do this is to use aggregation.

Replace the dates on the file names to make it into an aggregation template:
~~~~~
http://autoplot.org/data/agg/hyd/$Y/po_h0_hyd_$Y$m$d_v01.cdf
~~~~~

Now Autoplot can plot data from both files using the URI:
~~~~~
http://autoplot.org/data/agg/hyd/$Y/po_h0_hyd_$Y$m$d_v01.cdf?timerange=2000-01-04/2000-01-06
~~~~~
(Note it rejects the URI because a parameter needs to be selected.)

If you look at the folder http://autoplot.org/data/agg/hyd/2000/, you'll see
that there are some v07 files.  This can be replaced with $v and the largest
version is selected.  For RBSP, files contained versions like 1.7.13 where each
number has a different meaning.  For these, $(v,sep) should be used.  

Here are most of the field types:

| Field | Description | Example File | Aggregation |
| -- | --- | --- | --- |
| $Y | 4-digit year | data_<b>2021</b>0503.dat | data_<b>$Y</b>$m$d.dat |
| $m | 2-digit month | data_2021<b>05</b>03.dat | data_$Y<b>$m</b>$d.dat |
| $d | 2-digit day of month | data_202105<b>03</b>.dat | data_$Y$m<b>$d</b>.dat |
| $j | 3-digit day of year | data_2021_<b>123</b>_040000.dat | data_$Y_<b>$j</b>_$H$M$S.dat |
| $H | 2-digit hour | data_2021_123_<b>04</b>0000.dat |  data_$Y_$j_<b>$H</b>$M$S.dat |
| $M | 2-digit minute | data_2021_123_04<b>00</b>00.dat | data_$Y_$j_$H<b>$M</b>$S.dat |
| $S | 2-digit second | data_2021_123_0400<b>00</b>.dat | data__$Y_$j_$H$M<b>$S</b>.dat |
| $v | version number, alpha sorted | data_20210503_v<b>04</b>.dat | data_$Y$m$d_v<b>$v</b>.dat |
| $(v;sep) |version number, semmantic versioning | data_20210503_v<b>4.1.5</b>.dat | data_$Y$m$d_v<b>$(v,sep)</b>.dat |
| $x | ignore, matching anything | data_20210503_<b>faden</b>.dat | data_$Y$m$d_<b>$x</b>.dat |
| $y | 2-digit year | data_<b>21</b>0503.dat  | data_<b>$y</b>$m$d.dat |

Some missions also use numbers to count off orbit numbers.  These are supported
too, as well as subsecond fields using $(subsec;places=6).  
See https://github.com/hapi-server/uri-templates/wiki/Specification

# Make Aggregation Feature
There's a tool that tries to form aggregations for you, [menubar]&rarr;Tools&rarr;Aggregate.  
This scans through the focus URI looking for things that look like they could be templated.
For example, four digits between 1900 and 2100 are likely to be a year.  This assumes that
templates go from coursest to finest (Year to Minute), 4-digit years, 3-digit day of years 
(003 for Jan 3), and so on.  It's pretty simple logic but works pretty well.  

Note also when "tab" is pressed to get a directory listing, it may also suggest an 
aggregation, using the same logic.


