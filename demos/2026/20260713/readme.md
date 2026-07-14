This PDS data source is a nice one for demonstrating when a bit of Jython code is
needed to access the data.  The timetags for the data are stored as decomposed 
year, day-of-year, hour, minute, and second components, and with the PDS reader
they need to be combined into a time tag for Autoplot.  Second, there's a mysterious
cadence parameter in the file names, and this is controlled with another parameter.

