from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *



def drawCir(r=0.5 , xc=0 , yc=0):

    glBegin(GL_POLYGON)
    for c in np.arange (0,6,0.1):
        glColor3f(0,0,.3)
        x = r * cos(c)
        y = r * sin(c)
        glVertex(x+xc,y+yc)

    glEnd()

def drawEli(r=0.5 , xc=0 , yc=0):

    glBegin(GL_POLYGON)
    for c in np.arange (0,2*pi,0.001):
        glColor3f(.1,.2,.4)
        x = r * cos(c)
        y = r * sin(c)
        glVertex((x/2)+xc,(y/3)+yc)

    glEnd()




def draw():
    glClearColor(1,1,1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(220,220,220)


    #BODY

    glBegin(GL_POLYGON)
    glColor3f(1,.9,.2)
    glVertex(.2,.4)
    glVertex(.2,0)
    glVertex(-.2,0)
    glVertex(-.2,.4)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,.4)
    glVertex(.2,.4)
    glVertex(.2,0)
    glVertex(-.2,0)
    glVertex(-.2,.4)
    glEnd()




    glBegin(GL_POLYGON)
    glColor3f(1,.9,.2)
    glVertex(-.1,.6)
    glVertex(.1, .6)
    glVertex(0.04, .5)
    glVertex(-0.04, .5)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(1,.7,.2)
    glVertex(.02,.5)
    glVertex(.02,.47)
    glVertex(-.02,.47)
    glVertex(-.02,.5)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,.9,.2)
    glVertex(.03,.47)
    glVertex(.03,.4)
    glVertex(-.03,.4)
    glVertex(-.03,.47)
    glEnd()


    drawEli(.17, .1, .625)
    drawEli(.17, -.1, .625)
    drawCir(.02,.1,.625)
    drawCir(.02,-.1,.625)

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(.25, -.2)
    glVertex(.35, -.2)
    glVertex(.35, .1)
    glVertex(.25, .1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,.3)
    glVertex(.25, -.2)
    glVertex(.35, -.2)
    glVertex(.35, .1)
    glVertex(.25, .1)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(-.25, -.2)
    glVertex(-.35, -.2)
    glVertex(-.35, .1)
    glVertex(-.25, .1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,.3)
    glVertex(-.25, -.2)
    glVertex(-.35, -.2)
    glVertex(-.35, .1)
    glVertex(-.25, .1)
    glEnd()

    #Morb3 el regl


    glBegin(GL_LINES)
    glColor3f(0,0,.3)
    glVertex(.2,.05)
    glVertex(.25,.05)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-.2,.05)
    glVertex(-.25,.05)
    glEnd()

    glBegin(GL_LINES)
    glVertex(.25,-.1)
    glVertex(.1,-.1)
    glEnd()

    glBegin(GL_LINES)
    glVertex(.1,0)
    glVertex(.1,-.1)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-.25,-.1)
    glVertex(-.1,-.1)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-.1,0)
    glVertex(-.1,-.1)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex(.1, -.05)
    glVertex(.15,-.05)
    glVertex(.15, -.1)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex(-.1, -.05)
    glVertex(-.15,-.05)
    glVertex(-.15, -.1)
    glEnd()

    drawCir(.012, .12, -.07)
    drawCir(.012, -.12, -.07)


    glBegin(GL_LINES)
    glVertex(.2,.3)
    glVertex(-.2,.3)
    glEnd()

    glBegin(GL_LINES)
    glVertex(.1,.3)
    glVertex(.1,.4)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-.1,.3)
    glVertex(-.1,.4)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0,.5,.8)
    glVertex(-.07,.37)
    glVertex(0,.37)
    glVertex(0,.33)
    glVertex(-.07,.33)
    glEnd()



    glBegin(GL_POLYGON)
    for c in np.arange (0,6,0.1):
        glColor3f(1,0,.3)
        x = .02 * cos(c)
        y = .02 * sin(c)
        glVertex(x+.05,y+.35)

    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,.3)
    glVertex(.2,.35)
    glVertex(.1,.35)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-.2,.35)
    glVertex(-.1,.35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(.08,.33)
    glVertex(.23,.33)
    glVertex(.23,.29)
    glVertex(.08,.29)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(.23,.33)
    glVertex(.23,.23)
    glVertex(.2,.23)
    glVertex(.2,.33)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(.08,.23)
    glVertex(.23,.23)
    glVertex(.23,.19)
    glVertex(.08,.19)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(-.08,.33)
    glVertex(-.23,.33)
    glVertex(-.23,.29)
    glVertex(-.08,.29)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(-.23,.33)
    glVertex(-.23,.23)
    glVertex(-.2,.23)
    glVertex(-.2,.33)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.1,.2,.4)
    glVertex(-.08,.23)
    glVertex(-.23,.23)
    glVertex(-.23,.19)
    glVertex(-.08,.19)
    glEnd()



    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Tea pot Program")
glutDisplayFunc(draw)
glutMainLoop()
