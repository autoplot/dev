Demonstrate how cdfj is used to insert data into an empty CDF.

# build cdfj
unix> git clone git@github.com:autoplot/cdfj.git
unix> cd cdfj/
unix> ant -Dplatforms.JDK_8.home=/usr/local/jdk1.8 jar

# build test code
unix> cd ..
unix> javac -cp cdfj/dist/cdfj.jar:. Demo20230330.java

# run skeletoncdf to make an empty CDF file (run in this directory)
unix> ls README.md  # verify that we are in the directory containing README.md
unix> ~/local/cdf/bin/skeletoncdf -delete test.skt  # my skeletoncdf is in this location

# run the Java code which inserts data
unix> java -cp cdfj/dist/cdfj.jar:. Demo20230330

# verify that the CDF was created correctly.
unix> ~/local/cdf/bin/cdfdump test.cdf

