This demos how a more customized digitizer can be added to the PNG Walk Tool.
This script creates a PNGWalkTool and points it to the photos at
https://jfaden.net/~jbf/examplePics/cats/*.jpg, a set of pictures of Jeremy's
cats.  The digitizer script lets the user draw boxes around items in the 
pictures, and attaches a label "Chaos" or "Cleo" to each box.  

<img src='20201120_153056.png' width=600>

This uses nominal data (EnumerationUnits) to store the cat names and image names.
A DataPointRecorder is used to record the data.  The script registers listeners to
it to draw the points and the selected points in the recorder.  A Painter 
(BoxPainter) is used to draw the boxes over the images, and a MouseAdapter is
added to handle mouse events.
