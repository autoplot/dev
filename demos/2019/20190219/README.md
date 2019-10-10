=demoLongReadAccess.jy=

QDataSets use doubles to access the data, so even if the data is stored internally by integers, 
value() is used to get the value as a double.  This is undesirable in some cases, for example where 
longs are stored in a dataset.  A long is capable of representing numbers which doubles cannot, since
some of the double is used to store the exponent.  For this reason, LongReadAccess can be used to get
at the exact values.

=sumAllSize.jy=

The size command returns an array giving the dimensions (number of rows and columns) of the data.

