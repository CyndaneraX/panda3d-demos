#!/usr/bin/env python

# Author: Garrett S.(Milo Charming Magician)
# Last Updated: 2024-06-03
# Version: 4.00
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

        # Enable per-pixel lighting
        ambientLight = AmbientLight('ambientLight')
        ambientLight.setColor((1, 1, 1, 1))
        ambientLightNP = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNP)
        
        base.render.setShaderAuto()

        # load boiler model and animations
        self.boilerActor = Actor('phase_5/models/char/ttr_r_chr_cbg_boss.bam', {
            'Intro':'phase_5/models/char/ttr_a_chr_cbg_boss_intro.bam',
            'OffenseIdle':'phase_5/models/char/ttr_a_chr_cbg_boss_offenseIdle.bam',
            'GoIntoDefense':'phase_5/models/char/ttr_a_chr_cbg_boss_offenseIntoDefense.bam',
            'DefenseIdle':'phase_5/models/char/ttr_a_chr_cbg_boss_defenseIdle.bam',
            'Lose':'phase_5/models/char/ttr_a_chr_cbg_boss_lose.bam',
            'Dead':'phase_5/models/char/ttr_a_chr_cbg_boss_lose2.bam',
            'DefenseAttack':'phase_5/models/char/ttr_a_chr_cbg_boss_defenseAttack.bam',
            'DefenseRetentionPlan':'phase_5/models/char/ttr_a_chr_cbg_boss_defenseRetentionPlan.bam',
            'Hurt':'phase_5/models/char/ttr_a_chr_cbg_boss_hurt.bam',
        })
        self.boilerActor.reparentTo(render)
        self.boilerActor.setPos(0, 175, -30)

        render.setAntialias(AntialiasAttrib.MAuto)

        taskMgr.doMethodLater(3, self.intro, 'intro')
    
    def intro(self, task):
        self.boilerActor.play('Intro')
        #self.musicBGM.play()
        self.boilerIntroSFX.play()
        taskMgr.doMethodLater(0.5, self.intro2, 'intro2')
        
    def intro2(self, task):
        self.boilerOffenseAttackSFX.play()
        taskMgr.doMethodLater(5.8, self.offenseIdle, 'offenseIdle')
        taskMgr.doMethodLater(12, self.goIntoDefense, 'goIntoDefense')
    
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
        taskMgr.doMethodLater(12, self.dead, 'dead')
    
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
