#!/usr/bin/env python

# Author: Garrett S.(System)
# Last Updated: 2023-04-07
# Version: 1.00
#
# This Program is the field office on street demo

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile
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

loadPrcFile("configrc.prc")

# Create an instance of ShowBase, which will open a window and set up a
# scene graph and camera.
base = ShowBase()

class Street(DirectObject):
    def __init__(self):
        # Our standard title and instructions text
       # self.title = OnscreenText(text="Panda3D: TTR Field Office",
        #                          parent=base.a2dBottomCenter,
        #                          pos=(0, 0.08), scale=0.08,
        #                          fg=(1, 1, 1, 1), shadow=(0, 0, 0, .5))
        #self.escapeText = OnscreenText(text="ESC: Quit", parent=base.a2dTopLeft,
         #3                              fg=(1, 1, 1, 1), pos=(0.06, -0.1),
         #                              align=TextNode.ALeft, scale=.05)

        # Set up the key input
        self.accept('escape', sys.exit)

        # Fix the camera position
        #base.disableMouse()

        # Loading the music
        self.musicBGM = loader.loadMusic('phase_5/audio/bgm/ttr_s_ara_cbe_cogdoStreet.ogg')
        self.musicBGM.setLoop(True)

        # Loading the Sound Effects
        self.officeIdleSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_ara_cbe_cogdoSell_idle2.ogg')
        self.officeIdleSFX.setLoop(True)
        self.officeIdleLookSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_ara_cbe_cogdoSell_idleLook.ogg')
        self.officeIdleLook2SFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_ara_cbe_cogdoSell_idleLook2.ogg')
        self.officeIdleLook4SFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_ara_cbe_cogdoSell_idleLook4.ogg')

        # Enable per-pixel lighting
        base.render.setShaderAuto()

        # load skybox
        self.skybox = loader.loadModel('phase_5/models/props/ttr_m_ara_hol_intSkybox.bam')
        self.skybox.reparentTo(render)
        self.skybox.setPos(-40, 178, 0)

        # load env model
        self.envModel = loader.loadModel('phase_14/models/neighborhoods/ttr_m_ara_dga_kaboomberg.bam')
        self.envModel.reparentTo(render)
        self.envModel.setPos(-60, 140, -30)
        self.envModel.setHpr(230,0,0)

        # load boiler model and animations
        self.officeActor = Actor('phase_5/models/char/ttr_r_ara_cbe_cogdoSell.bam', {
            'Entrance':'phase_5/models/char/ttr_a_ara_cbe_cogdoSell_entrance.bam',
            'Idle':'phase_5/models/char/ttr_a_ara_cbe_cogdoSell_idle2.bam',
            'IdleLook':'phase_5/models/char/ttr_a_ara_cbe_cogdoSell_idleLook.bam',
            'IdleLook2':'phase_5/models/char/ttr_a_ara_cbe_cogdoSell_idleLook2.bam',
            'IdleLook3':'phase_5/models/char/ttr_a_ara_cbe_cogdoSell_idleLook3.bam',
            'IdleLook4':'phase_5/models/char/ttr_a_ara_cbe_cogdoSell_idleLook4.bam',
        })
        self.officeActor.reparentTo(render)
        self.officeActor.setPos(0, 152, -300)
        self.officeActor.setHpr(20,0,0)

        render.setAntialias(AntialiasAttrib.MAuto)

        taskMgr.doMethodLater(12, self.intro, 'intro')

    def intro(self, task):
        self.musicBGM.play()
        self.officeActor.setPos(0, 152, -31)
        self.officeActor.play("Entrance")
        taskMgr.doMethodLater(4.5, self.idle, 'idle')
    
    def idle(self, task):
        self.officeIdleSFX.play()
        self.officeActor.setPos(0, 152, -30)
        self.officeActor.play("Idle")
        self.officeActor.loop("Idle")
        taskMgr.doMethodLater(15, self.idleLook, 'idleLook')
    
    def idleLook(self, task):
        taskMgr.remove('idle')
        self.officeIdleSFX.stop()
        self.officeIdleLookSFX.play()
        self.officeActor.play("IdleLook")
        taskMgr.doMethodLater(4, self.idleLook2, 'idleLook2')
    
    def idleLook2(self, task):
        taskMgr.remove('idleLook')
        self.officeIdleLook2SFX.play()
        self.officeActor.play("IdleLook2")
        taskMgr.doMethodLater(7, self.idleLook3, 'idleLook3')
    
    def idleLook3(self, task):
        taskMgr.remove('idleLook2')
        self.officeActor.play("IdleLook3")
        taskMgr.doMethodLater(3.5, self.idleLook4, 'idleLook4')
    
    def idleLook4(self, task):
        taskMgr.remove('idleLook3')
        self.officeIdleLook4SFX.play()
        self.officeActor.play("IdleLook4")
        taskMgr.doMethodLater(2.5, self.cleanup, 'cleanup')
    
    def cleanup(self, task):
        self.officeActor.stop()
        taskMgr.remove('intro')
        taskMgr.remove('idleLook4')
        taskMgr.remove('cleanup')
        taskMgr.add(self.idle, 'idle')




mb = Street()
base.run()
