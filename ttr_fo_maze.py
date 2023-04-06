#!/usr/bin/env python

# Author: Garrett S.(System)
# Last Updated: 2023-04-05
#
# This Program is the mega movers maze test Scene

from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath, TextNode
from panda3d.core import PointLight, AmbientLight
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.interval.SoundInterval import SoundInterval
from direct.gui.DirectSlider import DirectSlider
from direct.gui.DirectButton import DirectButton
from direct.interval.MetaInterval import Parallel
from direct.interval.LerpInterval import LerpHprInterval
from direct.actor.Actor import Actor
from panda3d.core import AntialiasAttrib
import sys
import time

# Create an instance of ShowBase, which will open a window and set up a
# scene graph and camera.
base = ShowBase()

class Maze(DirectObject):
    def __init__(self):
        # Our standard title and instructions text
        self.title = OnscreenText(text="Panda3D: TTR Mega Movers Maze",
                                  parent=base.a2dBottomCenter,
                                  pos=(0, 0.08), scale=0.08,
                                  fg=(1, 1, 1, 1), shadow=(0, 0, 0, .5))
        self.escapeText = OnscreenText(text="ESC: Quit", parent=base.a2dTopLeft,
                                       fg=(1, 1, 1, 1), pos=(0.06, -0.1),
                                       align=TextNode.ALeft, scale=.05)

        # Set up the key input
        self.accept('escape', sys.exit)

        # Fix the camera position
        #base.disableMouse()

        # Loading the music
        self.musicBGM = loader.loadMusic('phase_5/audio/bgm/ttr_s_ara_cmg_default.ogg')
        self.musicBGM.setLoop(True)

        # Enable per-pixel lighting
        base.render.setShaderAuto()
        render.setAntialias(AntialiasAttrib.MAuto)

        # load env model
        self.envModel = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_cmg_level.bam')
        self.envModel.reparentTo(render)
        self.envModel.setPos(0, 150, -30)

        taskMgr.doMethodLater(2, self.intro, 'intro')

    def intro(self, task):
        self.musicBGM.play()

mb = Maze()
base.run()
