#!/usr/bin/env python

# Author: Garrett S.(System)
# Last Updated: 2023-04-06
# Version: 3.00
#
# This Program is the anim01 scened

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
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from direct.actor.Actor import Actor
from panda3d.core import CardMaker
from panda3d.core import AntialiasAttrib
import sys
import time

loadPrcFile("configrc.prc")

# Create an instance of ShowBase, which will open a window and set up a
# scene graph and camera.
base = ShowBase()

class AnimScene(DirectObject):
    def __init__(self):
        # Set up the key input
        self.accept('escape', sys.exit)

        # Fix the camera position
        #base.disableMouse()

        # Enable per-pixel lighting and Antialias
        base.render.setShaderAuto()
        render.setAntialias(AntialiasAttrib.MAuto)

        self.LoadGame()

    def LoadGame(self):
        self.toonShirt = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg')
        self.toonSleeves = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg')
        self.toonShorts = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg')
        self.toon_head = loader.loadModel('phase_3/models/char/duck-heads-1000.bam')
        self.toon_head.find('**/joint_pupilR_long').hide()
        self.toon_head.find('**/joint_pupilL_long').hide()
        self.toon_head.find('**/eyes-long').hide()
        self.toon_head.find('**/head-front-long').hide()
        self.toon_head.find('**/head-long').hide()
        self.toon_head.find('**/muzzle-long-laugh').hide()
        self.toon_head.find('**/muzzle-long-angry').hide()
        self.toon_head.find('**/muzzle-long-smile').hide()
        self.toon_head.find('**/muzzle-long-sad').hide()
        self.toon_head.find('**/muzzle-long-surprise').hide()
        self.toon_head.find('**/muzzle-long-neutral').hide()
        self.toon_head.find('**/muzzle-short-laugh').hide()
        self.toon_head.find('**/muzzle-short-smile').hide()
        self.toon_head.find('**/muzzle-short-sad').hide()
        self.toon_head.find('**/muzzle-short-surprise').hide()
        self.toon_head.find('**/muzzle-short-angry').hide()
        self.toon_torso = Actor('phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', {'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam',
         'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam',
         'walk': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_walk.bam',
         'pie': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_pie-throw.bam',
         'fallb': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_slip-backward.bam',
         'fallf': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_slip-forward.bam',
         'lose': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_lose.bam',
         'win': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_victory-dance.bam'})
        self.toon_legs = Actor('phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam', {'neutral': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam',
         'run': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_run.bam',
         'walk': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_walk.bam',
         'pie': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_pie-throw.bam',
         'fallb': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_slip-backward.bam',
         'fallf': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_slip-forward.bam',
         'lose': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_lose.bam',
         'win': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_victory-dance.bam'})
        self.shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
        shadowcm = CardMaker('shadow')
        shadowcm.setFrame(2, -2, 2, -2)
        shadow = render.attachNewNode(shadowcm.generate())
        shadow.reparentTo(self.toon_legs.find('**/joint_shadow'))
        shadow.setTexture(self.shadowtex)
        shadow.setP(270)
        shadow.setTransparency(True)
        shadow.setZ(0.01)
        shadow.setBin('fixed', 40)
        shadow.setColor(1, 1, 1, 0.6)
        self.toon_legs.setBin('fixed', 50)
        self.toon_legs.setDepthWrite(True)
        self.toon_legs.setDepthTest(True)
        shadow.setDepthWrite(False)
        shadow.setDepthTest(False)
        self.initScene()

    def initScene(self):
        self.toon_legs.reparentTo(render)
        self.toon_legs.find('**/boots_long').hide()
        self.toon_legs.find('**/boots_short').hide()
        self.toon_legs.find('**/shoes').hide()
        self.toon_legs.find('**/legs').setColor(255, 255, 255, 1.0)
        self.toon_legs.find('**/feet').setColor(255, 255, 255, 1.0)
        self.toon_torso.reparentTo(self.toon_legs.find('**/joint_hips'))
        self.toon_torso.find('**/arms').setColor(255, 255, 255, 1.0)
        self.toon_torso.find('**/neck').setColor(255, 255, 255, 1.0)
        self.toon_torso.find('**/torso-top').setTexture(self.toonShirt, 1)
        self.toon_torso.find('**/torso-bot').setTexture(self.toonShorts, 1)
        self.toon_torso.find('**/sleeves').setTexture(self.toonSleeves, 1)
        self.toon_head.reparentTo(self.toon_torso.find('**/def_head'))
        self.toon_head.find('**/head-front-short').setColor(255, 255, 255, 1.0)
        self.toon_head.find('**/head-short').setColor(255, 255, 255, 1.0)
        self.localAvatar = localAvatar(self.toon_head, self.toon_torso, self.toon_legs)
        self.animSceneState1()
    
    def animSceneState1(self):
        self.localAvatar.setAnimStateLoop('neutral')

class localAvatar:
    def __init__(self, head, torso, legs):
        self.head = head
        self.torso = torso
        self.legs = legs
    
    def setAnimStateLoop(self, anim):
        if anim == 'neutral':
            try:
                self.head.loop('neutral')
            except:
                pass

            self.torso.loop('neutral')
            self.legs.loop('neutral')
        elif anim == 'run':
            try:
                self.head.loop('run')
            except:
                pass

            self.torso.loop('run')
            self.legs.loop('run')
        elif anim == 'walk':
            try:
                self.head.loop('walk')
            except:
                pass

            self.torso.loop('walk')
            self.legs.loop('walk')
        elif anim == 'pie':
            try:
                self.head.loop('pie')
            except:
                pass

            self.torso.loop('pie')
            self.legs.loop('pie')
        elif anim == 'fallb':
            try:
                self.head.loop('fallb')
            except:
                pass

            self.torso.loop('fallb')
            self.legs.loop('fallb')
        elif anim == 'fallf':
            try:
                self.head.loop('fallf')
            except:
                pass

            self.torso.loop('fallf')
            self.legs.loop('fallf')

    def setAnimStateNoLoop(self, anim):
        if anim == 'neutral':
            try:
                self.head.play('neutral')
            except:
                pass

            self.torso.play('neutral')
            self.legs.play('neutral')
        elif anim == 'run':
            try:
                self.head.play('run')
            except:
                pass

            self.torso.play('run')
            self.legs.play('run')
        elif anim == 'walk':
            try:
                self.head.play('walk')
            except:
                pass

            self.torso.play('walk')
            self.legs.play('walk')
        elif anim == 'pie':
            try:
                self.head.play('pie')
            except:
                pass

            self.torso.play('pie')
            self.legs.play('pie')
        elif anim == 'fallb':
            try:
                self.head.play('fallb')
            except:
                pass

            self.torso.play('fallb')
            self.legs.play('fallb')
        elif anim == 'fallf':
            try:
                self.head.play('fallf')
            except:
                pass

            self.torso.play('fallf')
            self.legs.play('fallf')

ac = AnimScene()
base.run()
