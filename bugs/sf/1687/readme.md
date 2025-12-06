These are codes which are used to test completions.  One should be able to trigger completions at any point in these codes and:
* it should not crash
* it should provide the default set of completions if it's lost
* it should refactor the code to a simplified code if possible, providing useful completions.

If you right-click in the autoplot script editor, then developer->"Show simplified script", you can see the script 
it uses to implement completions.

See https://sourceforge.net/p/autoplot/bugs/1687/.

# demoItem14_1.jy
This shows where the getDataSet call is handled differently within a function than within the initial part of the script.


