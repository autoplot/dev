# Unfortunately, svn checkout for a particular time doesn't check out externals at the
# same time, and this must be done manually.

svn co -r {2018-09-26T00:32Z} https://svn.code.sf.net/p/autoplot/code/trunk/
cd autoplot/
rm -fr dasCore/ dasCoreUtil/ dasCoreDatum/
svn co -r {2018-09-26T00:32Z} https://saturn.physics.uiowa.edu/svn/das2/dasCore/community/autoplot2011/trunk/dasCore/
svn co -r {2018-09-26T00:32Z} https://saturn.physics.uiowa.edu/svn/das2/dasCore/community/autoplot2011/trunk/dasCoreDatum
svn co -r {2018-09-26T00:32Z} https://saturn.physics.uiowa.edu/svn/das2/dasCore/community/autoplot2011/trunk/dasCoreUtil

