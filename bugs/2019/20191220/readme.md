This shows a bug Ivar saw where the vertical slicer didn't work when there was only one record.  This bug was fixed 
in 20191221a.  Also, I notice that 
<br>
https://github.com/autoplot/dev/blob/master/bugs/2019/20191220/b1.vap does not load properly, while
<br>
https://github.com/autoplot/dev/bugs/2019/20191220/b1.vap does.  Either one should load properly.

The two other scripts, "whyNoSyntaxHighlite", were an experiment to figure out why some scripts are not highlited.  Here, both 
are highlited and GitHub jump-to-source also works.  An example of where it doesn't work is https://github.com/autoplot/dev/blob/master/bugs/sf/2208/demoBug2208.jy.
