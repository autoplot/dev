Demonstrate how cdfj is used to insert data into an empty CDF.

First, build cdfj.
```
unix> git clone git@github.com:autoplot/cdfj.git
unix> cd cdfj/
unix> ant -Dplatforms.JDK_8.home=/usr/local/jdk1.8 jar
```
Then build the test Java code, which will open the empty CDF and insert data.
```
unix> cd ..
unix> javac -cp cdfj/dist/cdfj.jar:. Demo20230330.java
```
Run skeletoncdf to make an empty CDF file (run in this directory).
```
unix> ls README.md  # verify that we are in the directory containing README.md
unix> ~/local/cdf/bin/skeletoncdf -delete test.skt  # my skeletoncdf is in this location
```
Then run the Java code which inserts data.
```
unix> java -cp cdfj/dist/cdfj.jar:. Demo20230330
```
Last, verify that the CDF was created correctly.
```
unix> ~/local/cdf/bin/cdfdump test.cdf
```
