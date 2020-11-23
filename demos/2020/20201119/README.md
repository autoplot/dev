The <a href='pngwalkCustomDigitizer.jy'>script</a> demos how a more customized digitizer can be added to the PNG Walk Tool.
This creates a PNGWalkTool and points it to the photos at
https://jfaden.net/~jbf/examplePics/cats/*.jpg, a set of pictures of Jeremy's
cats.  The digitizer script lets the user draw boxes around items in the 
pictures, and attaches a label "Chaos" or "Cleo" to each box.  

<img src='20201120_153056.png' width=600>

This uses nominal data (EnumerationUnits) to store the cat names and image names.
A DataPointRecorder is used to record the data.  The script registers listeners to
it to draw the points and the selected points in the recorder.  A Painter 
(BoxPainter) is used to draw the boxes over the images, and a MouseAdapter is
added to handle mouse events.

This requires Autoplot version 20201120a or v2020a_13 to run.

# Making your own versions of this
A couple things to know if you want to start with this script and modify it to meet 
your own needs.  

First, if you need data coordinates and not pixel coordinates, rich PNG 
metadata can be used to perform the axis transformations.

Second, if you want to handle left click differently than middle click, you can
get the button property for on the event:
~~~~~
    print 'button=', evt.button
    print 'modifiers=', evt.modifiers
    print 'modifiersText=', evt.getMouseModifiersText(evt.modifiers)
~~~~~

This script works in two halfs.  With any control system, there are open-loop 
and closed-loop controls.  In a closed-loop system, the first half of the loop 
is an action takes place to modify the state, and the second half is to 
represent the state (providing feedback).  

The feedback part of the script are
the <a href='https://github.com/autoplot/dev/blob/9cec11b4e74381c87ddf3c5cb80e623ef25c6ead/demos/2020/20201119/pngwalkCustomDigitizer.jy#L39'>
paintBox</a> and <a href='https://github.com/autoplot/dev/blob/9cec11b4e74381c87ddf3c5cb80e623ef25c6ead/demos/2020/20201119/pngwalkCustomDigitizer.jy#L70'>
BoxPainter</a> routines in the script.  BoxPainter is a Painter which draws
the boxes represented in the DataPointRecorder.  (A Painter is an object which
draws something onto a graphics context, and is added with PngWalkTool's 
addTopDecorator, which calls the painters each time a single-png view is drawn. 
The graphics context, g, is in the image reference frame.)  The routine 
paintBox simply draws a box with white 
and black lines so there is always contrast, and draws a label on each box.

The forward part of the loop is lines <a href='https://github.com/autoplot/dev/blob/9cec11b4e74381c87ddf3c5cb80e623ef25c6ead/demos/2020/20201119/pngwalkCustomDigitizer.jy#L93'>
93</a> through <a href='https://github.com/autoplot/dev/blob/9cec11b4e74381c87ddf3c5cb80e623ef25c6ead/demos/2020/20201119/pngwalkCustomDigitizer.jy#L128'>
128</a>, where a mouse adapter receives mouse clicks from the PngWalkTool and loads them into the DataPointRecorder.  Note there is a pair of points,
startSelect and stopSelect which are used for feedback as well, to show a box as it is selected by dragging the mouse.




