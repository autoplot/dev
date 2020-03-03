from org.das2.graph import Arrow
from java.awt.geom import Point2D
def drawArrows(g):
    ptail= Point2D.Double(100,100)
    phead= Point2D.Double(200,200)
    Arrow.paintArrow( g,phead,ptail,5.,Arrow.HeadStyle.THIN_TRIANGLE )

addTopDecoration( dom.plots[0],drawArrows )
