#!/usr/bin/env python

# Author: Garrett S.(System)
# Last Updated: 2023-04-06
# Version: 3.00
#
# This Program is the boiler test Scene

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

class Boiler(DirectObject):
    def __init__(self):
        # Our standard title and instructions text
        self.title = OnscreenText(text="Panda3D: TTR Boiler",
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
        self.musicBGM = loader.loadMusic('phase_5/audio/bgm/ttr_s_ara_csa_boilerOffense.ogg')
        self.musicBGM.setLoop(True)

        # Loading the Sound Effects
        self.boilerIntroSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_chr_cbg_boss_intro.ogg')
        self.boilerOffenseIdleSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_chr_cbg_boss_offenseIdle.ogg')
        self.boilerOffenseIdleSFX.setLoop(True)
        self.boilerOffenseAttackSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_chr_cbg_boss_offenseAttack.ogg')
        self.boilerGoIntoOffenseSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_chr_cbg_boss_offenseIntoDefense.ogg')
        self.boilerDefenseIdleSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_chr_cbg_boss_defenseIdle.ogg')
        self.boilerDefenseIdleSFX.setLoop(True)
        self.boilerDeadSFX = base.loader.loadSfx('phase_5/audio/sfx/ttr_s_chr_cbg_boss_lose.ogg')
        self.cogDeadSFX = base.loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')

        # Enable per-pixel lighting
        base.render.setShaderAuto()

        # load skybox
        self.skybox = loader.loadModel('phase_5/models/props/ttr_m_ara_hol_intSkybox.bam')
        self.skybox.reparentTo(render)
        self.skybox.setPos(0, 150, -30)

        # load env model
        self.envModel = loader.loadModel('phase_5/models/cogdominium/ttr_m_ara_crg_boiler.bam')
        self.envModel.reparentTo(render)
        self.envModel.setPos(0, 150, -30)

        # load left elevator model
        self.envElevatorLeftModel = loader.loadModel('phase_5/models/cogdominium/ttr_m_ara_csa_elevatorSellbot.bam')
        self.envElevatorLeftModel.reparentTo(render)
        self.envElevatorLeftModel.setPos(35, 184, -30)

        # load right elevator model
        self.envElevatorLeftModel = loader.loadModel('phase_5/models/cogdominium/ttr_m_ara_csa_elevatorSellbot.bam')
        self.envElevatorLeftModel.reparentTo(render)
        self.envElevatorLeftModel.setPos(-35, 184, -30)

        # load entrance elevator model
        self.envElevatorEntranceModel = loader.loadModel('phase_5/models/cogdominium/ttr_m_ara_csa_elevatorSellbot.bam')
        self.envElevatorEntranceModel.reparentTo(render)
        self.envElevatorEntranceModel.setPos(0, 19, -32.9)
        self.envElevatorEntranceModel.setHpr(180,0,0)

        # load boiler model and animations
        self.boilerActor = Actor('phase_5/models/char/ttr_r_chr_cbg_boss.bam', {
            'Intro':'phase_5/models/char/ttr_a_chr_cbg_boss_intro.bam',
            'OffenseIdle':'phase_5/models/char/ttr_a_chr_cbg_boss_offenseIdle.bam',
            'GoIntoDefense':'phase_5/models/char/ttr_a_chr_cbg_boss_offenseIntoDefense.bam',
            'DefenseIdle':'phase_5/models/char/ttr_a_chr_cbg_boss_defenseIdle.bam',
            'Dead':'phase_5/models/char/ttr_a_chr_cbg_boss_lose2.bam',
        })
        self.boilerActor.reparentTo(render)
        self.boilerActor.setPos(0, 175, -30)

        # load cog1 model and animations
        self.cogActor1 = Actor('phase_5/models/char/tt_a_ene_scb_zero.bam', {
            'Idle':'phase_5/models/char/tt_a_ene_cgb_lured.bam',
        })
        self.cogActor1.reparentTo(render)
        self.cogActor1.setPos(10, 150, -30)
        self.cogActor1.setHpr(180,0,0)

        # load cog2 model and animations
        self.cogActor2 = Actor('phase_5/models/char/tt_a_ene_scc_zero.bam', {
            'Idle':'phase_5/models/char/tt_a_ene_cgc_lured.bam',
        })
        self.cogActor2.reparentTo(render)
        self.cogActor2.setPos(5, 150, -30)
        self.cogActor2.setHpr(180,0,0)

        # load cog3 model and animations
        self.cogActor3 = Actor('phase_5/models/char/tt_a_ene_scb_zero.bam', {
            'Idle':'phase_5/models/char/tt_a_ene_cgb_lured.bam',
        })
        self.cogActor3.reparentTo(render)
        self.cogActor3.setPos(-5, 150, -30)
        self.cogActor3.setHpr(180,0,0)

        # load cog4 model and animations
        self.cogActor4 = Actor('phase_5/models/char/tt_a_ene_sca_zero.bam', {
            'Idle':'phase_5/models/char/tt_a_ene_cga_lured.bam',
        })
        self.cogActor4.reparentTo(render)
        self.cogActor4.setPos(-10, 150, -30)
        self.cogActor4.setHpr(180,0,0)

        render.setAntialias(AntialiasAttrib.MAuto)
        taskMgr.doMethodLater(2, self.intro, 'intro')
    
    def intro(self, task):
        self.cogActor1.play('Idle')
        self.cogActor1.loop('Idle')
        self.cogActor2.play('Idle')
        self.cogActor2.loop('Idle')
        self.cogActor3.play('Idle')
        self.cogActor3.loop('Idle')
        self.cogActor4.play('Idle')
        self.cogActor4.loop('Idle')
        self.boilerActor.play('Intro')
        self.musicBGM.play()
        self.boilerIntroSFX.play()
        taskMgr.doMethodLater(0.5, self.intro2, 'intro2')
        
    def intro2(self, task):
        self.boilerOffenseAttackSFX.play()
        taskMgr.doMethodLater(5.8, self.offenseIdle, 'offenseIdle')
        taskMgr.doMethodLater(10, self.goIntoDefense, 'goIntoDefense')
    
    def offenseIdle(self, task):
        self.boilerActor.play('OffenseIdle')
        self.boilerActor.loop('OffenseIdle')
        self.boilerOffenseIdleSFX.play()
    
    def goIntoDefense(self, task):
        self.boilerOffenseIdleSFX.stop()
        self.boilerGoIntoOffenseSFX.play()
        self.boilerActor.play('GoIntoDefense')
        taskMgr.doMethodLater(4, self.defenseIdle, 'defenseIdle')

    def defenseIdle(self, task):
        self.boilerActor.play('DefenseIdle')
        self.boilerActor.loop('DefenseIdle')
        self.boilerDefenseIdleSFX.play()
        taskMgr.doMethodLater(9.2, self.dead, 'dead')
    
    def dead(self, task):
        self.boilerDefenseIdleSFX.stop()
        self.boilerActor.play('Dead')
        self.boilerDeadSFX.play()
        taskMgr.doMethodLater(9.2, self.cleanup, 'cleanup')
    
    def cleanup(self, task):
        self.boilerActor.stop()
        self.cogDeadSFX.play()
        self.cogActor1.delete()
        self.cogActor2.delete()
        self.cogActor3.delete()
        self.cogActor4.delete()

mb = Boiler()
base.run()
