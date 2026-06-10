Decorators give a way to add additional graphical elements to a plot.  For example, you can
have a canvas draw a vertical line at a particular time or paint polar axis onto a plot.  You
can add a decorator to individual renderers, which are drawn just before or just after a renderer
is painted.  I'd forgotten about this functionality, and it was perfect for the problem we
had where we wanted to paint data for context, then a polar axis, then the data of interest.
This script demonstrates this functionality.

Here's another code which uses a decorator and can be used for testing:

https://github.com/autoplot/dev/blob/master/demos/annotations/strike/strikeDecorator.jy
