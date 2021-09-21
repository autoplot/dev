# ASCII Files 
ASCII files, or text files, are often used to send data.  They are easily 
interpreted by humans and parseable in any programming language.  
But they are also vague, so building software which can parse any ASCII file
is impossible.  Autoplot tries to make an efficient parser which can handle
many types of ASCII files encountered.

Its parser works by identifying records, typically lines of the file, 
and using a record parser to split each line into fields.  These
fields are each handled by field parsers, finally turning the ASCII into
quantities useful for science.

The record parser is typically a "Delimiter parser" which breaks up each
record into fields.  For example, the delimiter parser might be set up to
break the record into fields by splitting it on commas or on white space,
as is typically the case.  Other record parsers are available. For example
there is one for fixed columns and another that uses regular expressions
to identify fields.

All this configuration is stored within the keywords of Autoplot URIs.
With a CDF file, you can just specify the file, ?, and then the name of the
variable you want to plot.  With ASCII URIs there is often more that's needed,
such as the number of lines to skip before parsing or the units of the column
read in.  Note that Autoplot tries to have a reasonable set of assumptions 
that make this easier as well.

This complexity is hidden from the scientist by the ASCII Data Source Editor.
It provides tabs to manage all the things that can be controlled, and 
gives a preview of how the file will be interpretted.  

* image of ascii editor *

## Selecting Columns
Typically one column is read in and corresponds to the Y parameter on the 
plot.  A "depend_0" can be picked as well, and these will be used for the
X values.  Note if the first column contains ISO8601 times (2021-09-21T13:24),
these will automatically be read in for the X values.  

You can click on "Select" next to the column field and then click on the table 
to select the column.  A fill value, which is a place holder for an missing 
measurement, can be selected, and the guess button will try to figure out what
the fill value is assuming it repeats and is distant from the rest of the data
(9999 when most of the data is between 0 and 10).  Valid min and valid max
can also be used to indicate the extent of valid data.

Selecting multiple columns will load in several quantities at once.

# Handling Time Tags
Often the time tags are not one ISO8601 time, but are split out into separate
fields which must be combined to form a time tag.  In this case we use 
the first column to indicate the position, and then a specification indicating
how the following columns are to be interpretted and combined.  For example, 
$Y+$m+$d+$H+$M+$S will read in six columns, combining the components assuming
the first is year, second is month, then day, hour, minute, and second.  
The "Time Format" contains a droplist of examples.  The plus symbol is used 
between fields, so $Y$m$d+$H$M$S means the there will be two columns used
and the first will contain the day, and the second will contain the time of 
day.

Here a 'guess' button will try to guess the components automatically, assuming 
that years will come before days, months have no more than 12 in them, and so on.






