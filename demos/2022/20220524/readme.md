This demonstrates how Autoplot can use Python to read CDF files where variables within are greater than
2GB and cannot be used with the CDFJ library.  The Python code [extract_subset.py](extract_subset.py) copies part of the
large CDF file into a smaller one which can be read by Autoplot.  The Autoplot jyds script 
[extract_subset.jyds](extract_subset.jyds) calls the python code and then plots data from the smaller CDF file.
