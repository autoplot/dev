This PDS data source is a nice one for demonstrating when a bit of Jython code is
needed to access the data.  The timetags for the data are stored as decomposed 
year, day-of-year, hour, minute, and second components, and with the PDS reader
they need to be combined into a time tag for Autoplot.  Second, there's a mysterious
cadence parameter in the file names, and this is controlled with another parameter.

* [read_messenger_bfield.jyds](read_messenger_bfield.jyds) - reads one file and returns the data
* [read_messenger_bfield_agg.jyds](read_messenger_bfield_agg.jyds) - reads using aggregation and adds a cadence parameter
* [read_messenger_bfield_oneday.jyds](read_messenger_bfield_oneday.jyds) - reads one file and allows for Autoplot's aggregation to combine the data.
