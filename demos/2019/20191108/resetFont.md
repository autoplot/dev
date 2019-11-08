Here's one way to reset the font size, when the screen fonts are very
small and Java is not picking up the changes:

~~~~~
java -Dswing.plaf.metal.controlFont=Dialog-20 -jar ~/autoplot.jar
~~~~~

See https://stackoverflow.com/questions/1043872/are-there-any-built-in-methods-in-java-to-increase-font-size .

