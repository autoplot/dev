Here's one way to reset the font size, when the screen fonts are very
small and Java is not picking up the changes:

~~~~~
java -Dswing.plaf.metal.controlFont=Dialog-20 -jar ~/autoplot.jar
~~~~~


