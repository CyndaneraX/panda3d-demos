# Programmed mostly by Garrett.S and base animation is done by Fake Honeigh

from direct.actor.Actor import Actor
from panda3d.core import *
from direct.task import Task
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from panda3d.core import loadPrcFileData
from direct.interval.IntervalGlobal import *
from panda3d.core import AntialiasAttrib
import sys
import time

loadPrcFile("configrc.prc")

base = ShowBase()

class ToonsVsCogsTheUltimate(DirectObject):
    def __init__(self):
        self.accept('escape', sys.exit)

        self.musicBGM = loader.loadMusic('phase_3.5/audio/bgm/TC_SZ_activity.ogg')
        self.musicBGM.setLoop(True)

        # Enable per-pixel lighting, etc.

        ambientLight = AmbientLight('ambientLight')
        ambientLight.setColor((1, 1, 1, 1))
        ambientLightNP = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNP)

        base.render.setShaderAuto()
        base.disableMouse()
        render.setAntialias(AntialiasAttrib.MAuto)

        interior = loader.loadModel('phase_3.5/models/modules/toon_interior_T.bam')
        interior.reparentTo(render)

        #Camera
        camera.setPosHpr(15, 4.00, 4.00, 90.00, 0.00, 0.00)
        #camera.place()

        chair = loader.loadModel('phase_3.5/models/modules/chair.bam')
        chair.reparentTo(render)
        chair.setPos(11.00, -1.00, 0.00)
        chair.setHpr(276.29, 0.00, 0.00)
        # chair.place()

        chair = loader.loadModel('phase_3.5/models/modules/chair.bam')
        chair.reparentTo(render)
        chair.setPosHpr(10.00, 2.00, 0.00, 267.61, 0.00, 0.00)
        # chair.place()

        chair = loader.loadModel('phase_3.5/models/modules/chair.bam')
        chair.reparentTo(render)
        chair.setPosHpr(10.00, 5.00, 0.00, 265.49, 0.00, 0.00)
        # chair.place()

        chair = loader.loadModel('phase_3.5/models/modules/chair.bam')
        chair.reparentTo(render)
        chair.setPosHpr(10.00, -3.30, 0.00, 277.82, 0.00, 0.00)
        # chair.place()

        chair = loader.loadModel('phase_3.5/models/modules/chair.bam')
        chair.reparentTo(render)
        chair.setPosHpr(3.00, 1.00, 0.00, 270.00, 0.00, 0.00)
        # chair.place()

        desk = loader.loadModel('phase_3.5/models/modules/desk_only.bam')
        desk.reparentTo(render)
        desk.setPosHpr(6.20, 2.00, 0.00, 265.60, 0.00, 0.00)
        # desk.place()

        desk = loader.loadModel('phase_3.5/models/modules/desk_only.bam')
        desk.reparentTo(render)
        desk.setPosHpr(-0.30, -1.00, 0.00, 270.00, 0.00, 0.00)
        # desk.place()

        desk = loader.loadModel('phase_3.5/models/modules/desk_only.bam')
        desk.reparentTo(render)
        desk.setPosHpr(7.00, -4.00, 0.00, 270.00, 0.00, 0.00)
        # desk.place()

        desk = loader.loadModel('phase_3.5/models/modules/desk_only.bam')
        desk.reparentTo(render)
        desk.setPosHprScale(-5.00, 2.00, 0.00, 271.00, 0.00, 0.00, 1.20, 1.20, 1.20)
        # desk.place()

        self.Mouse = Actor({'torso':'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', \
                     'legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
                     {'torso':{'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam', \
                     'walk':'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk.bam', \
                     'run':'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam'}, \
                     'legs':{'sit':'phase_4/models/char/tt_a_chr_dgm_shorts_legs_sit.bam',
                     'walk':'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_walk.bam',  \
                     'run':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_run.bam'}})

        self.Mouse.attach('torso', 'legs', 'joint_hips')

        #Pos, Hpr, Scale, ReparentTo
        self.Mouse.setPos(0, 0, 0)
        self.Mouse.setHpr(0, 0, 0)
        self.Mouse.setScale(1.0)
        self.Mouse.reparentTo(render)

        #Head
        Head = loader.loadModel('phase_3/models/char/mouse-heads-1000.bam')
        Head.find('**/muzzle-short-surprise').hide()
        Head.find('**/muzzle-short-sad').hide()
        Head.find('**/muzzle-short-smile').hide()
        Head.find('**/muzzle-short-angry').hide()
        Head.find('**/muzzle-short-laugh').hide()
        Head.find('**/head-long').hide()
        Head.find('**/head-front-long').hide()
        Head.find('**/eyes-long').hide()
        Head.find('**/joint_pupilL_long').hide()
        Head.find('**/joint_pupilR_long').hide()
        Head.find('**/ears-long').hide()

        Neck = self.Mouse.find('**/def_head')
        Head.reparentTo(Neck)

        #******************************Clothes******************************

        #Gloves
        Gloves = self.Mouse.find('**/hands')
        Gloves.setColor(0.11, 0.12, 0.13)

        #Sleeves
        Sleeves = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_winter03.jpg')
        self.Mouse.find('**/sleeves').setTexture(Sleeves, 1)

        #Shirts
        Shirt = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_winter03.jpg')
        self.Mouse.find('**/torso-top').setTexture(Shirt, 1)

        #Shorts
        Shorts = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_pirate.jpg')
        self.Mouse.find('**/torso-bot').setTexture(Shorts, 1)

        #Shoes/Boots
        Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_oxfords.jpg')
        self.Mouse.find('**/shoes').setTexture(Shoes, 1)
        self.Mouse.find('**/boots_long').hide()
        self.Mouse.find('**/boots_short').hide()
        self.Mouse.find('**/feet').hide()

        #Colors
        Head.find('**/head-short').setColor(77,166,255)
        Head.find('**/head-front-short').setColor(77,166,255)
        Head.find('**/ears-short').setColor(77,166,255)
        self.Mouse.find('**/neck').setColor(77,166,255)
        self.Mouse.find('**/arms').setColor(77,166,255)
        self.Mouse.find('**/legs').setColor(77,166,255)
        self.Mouse.find('**/feet').setColor(77,166,255)
        #Hat.setColor(0, 0, 0)
        #Glasses.setColor(255, 255, 255)

        self.Mouse.setPosHpr(1.30, 1.00, 0.00, 90.00, 0.00, 0.00)
        # self.Mouse.place()

        self.Whiskers = Actor({'torso':'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', \
                     'legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
                     {'torso':{'idle': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam'}, \
                     'legs':{'idle':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam'}})

        self.Whiskers.attach('torso', 'legs', 'joint_hips')

        #Pos, Hpr, Scale, ReparentTo
        self.Whiskers.setPos(-6.00, 4.00, 0.00)
        self.Whiskers.setHpr(270.00, 0.00, 0.00)
        self.Whiskers.setScale(1.0)
        self.Whiskers.reparentTo(render)
        # self.Whiskers.place()


        #Head
        Head = loader.loadModel('phase_3/models/char/cat-heads-1000.bam',)
        Head.find('**/muzzle-short-surprise').hide()
        Head.find('**/muzzle-short-sad').hide()
        Head.find('**/muzzle-short-smile').hide()
        Head.find('**/muzzle-short-angry').hide()
        Head.find('**/muzzle-short-laugh').hide()
        Head.find('**/muzzle-long-surprise').hide()
        Head.find('**/muzzle-long-sad').hide()
        Head.find('**/muzzle-long-smile').hide()
        Head.find('**/muzzle-long-angry').hide()
        Head.find('**/muzzle-long-laugh').hide()
        Head.find('**/muzzle-long-neutral').hide()
        Head.find('**/head-front-long').hide()
        Head.find('**/head-long').hide()
        Head.find('**/head-front-long')
        Head.find('**/eyes-long').hide()
        Head.find('**/joint_pupilL_long').hide()
        Head.find('**/joint_pupilR_long').hide()
        Head.find('**/ears-long').hide()
        Neck = self.Whiskers.find('**/def_head')
        Head.reparentTo(Neck)

        #******************************Clothes******************************

        #Gloves
        Gloves = self.Whiskers.find('**/hands')
        Gloves.setColor(255, 255, 255)

        #Sleeves
        Sleeves = loader.loadTexture('phase_4/maps/male_sleeveNew12.jpg')
        self.Whiskers.find('**/sleeves').setTexture(Sleeves, 1)

        #Shirts
        Shirt = loader.loadTexture('phase_4/maps/male_shirtNew12.jpg')
        self.Whiskers.find('**/torso-top').setTexture(Shirt, 1)

        #Shorts
        Shorts = loader.loadTexture('phase_4/maps/shortsCat7_01.jpg')
        self.Whiskers.find('**/torso-bot').setTexture(Shorts, 1)

        #Shoes/Boots
        Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_oxfords.jpg')
        self.Whiskers.find('**/shoes').setTexture(Shoes, 1)
        self.Whiskers.find('**/boots_long').hide()
        self.Whiskers.find('**/boots_short').hide()
        self.Whiskers.find('**/feet').hide()

        #Colors
        #Teacher
        Head.find('**/head-short').setColor(0.23, 0.68, 0.48, 1.0)
        Head.find('**/head-front-short').setColor(0.23, 0.68, 0.48, 1.0)
        Head.find('**/ears-short').setColor(0.23, 0.68, 0.48, 1.0)
        self.Whiskers.find('**/neck').setColor(0.23, 0.68, 0.48, 1.0)
        self.Whiskers.find('**/arms').setColor(0.23, 0.68, 0.48, 1.0)
        self.Whiskers.find('**/legs').setColor(0.23, 0.68, 0.48, 1.0)
        self.Whiskers.find('**/feet').setColor(0.23, 0.68, 0.48, 1.0)
        self.Whiskers.setPosHpr(-6.30, 4.00, 0.00, 271.00, 0.00, 0.00)

        #SFX And Dial
        self.Cat_Long = base.loader.loadSfx("phase_3.5/audio/dial/AV_cat_long.ogg")
        self.Cat_Exclaim = base.loader.loadSfx("phase_3.5/audio/dial/AV_cat_exclaim.ogg")
        self.Mouse_Long = base.loader.loadSfx("phase_3.5/audio/dial/AV_mouse_long.ogg")
        self.Dog_Exclaim = base.loader.loadSfx("phase_3.5/audio/dial/AV_dog_exclaim.ogg")
        self.Mouse_Medium = base.loader.loadSfx("phase_3.5/audio/dial/AV_mouse_med.ogg")
        self.Mouse_Question = base.loader.loadSfx("phase_3.5/audio/dial/AV_mouse_question.ogg")
        self.Mouse_Laugh = base.loader.loadSfx("phase_4/audio/sfx/avatar_emotion_laugh.ogg")
        self.Duck_Short = base.loader.loadSfx("phase_3.5/audio/dial/AV_duck_short.ogg")
        self.DoorOpen = base.loader.loadSfx("phase_3.5/audio/sfx/Door_Open_1.ogg")
        self.DoorClose = base.loader.loadSfx("phase_3.5/audio/sfx/Door_Close_1.ogg")
        self.FART = base.loader.loadSfx("phase_15/audio/sfx/fart_fx.ogg")
        self.YEET = base.loader.loadSfx("phase_15/audio/sfx/yeet.ogg")
        self.AV_RUN = base.loader.loadSfx("phase_3.5/audio/sfx/AV_footstep_runloop.ogg")
        self.AV_RUN.setLoop(True)

        self.Lomaton = Actor({'torso':'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', \
                     'legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
                     {'torso':{'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam'}, \
                     'legs':{'sit':'phase_4/models/char/tt_a_chr_dgm_shorts_legs_sit.bam'}})

        self.Lomaton.attach('torso', 'legs', 'joint_hips')

        #Pos, Hpr, Scale, ReparentTo
        self.Lomaton.setPos(0, 0, 0)
        self.Lomaton.setHpr(0, 0, 0)
        self.Lomaton.setScale(1.1)
        self.Lomaton.reparentTo(render)

        #Head
        Head = Actor('phase_3/models/char/tt_a_chr_dgm_skirt_head_1000.bam',
                    {'anim':'phase_3/models/char/tt_a_chr_dgm_skirt_head_neutral.bam'})

        Head.setColor(1, 1, 1)
        Head.loop('anim')
        Head.find('**/ears').setColor(0)
        Head.find('**/muzzle').setColor(0.87, 0.65, 0.47)
        Top_Head = Head.find('**/head')
        Bot_Head = Head.find('**/head-front')

        Neck = self.Lomaton.find('**/def_head')
        Head.reparentTo(Neck)

        #******************************Clothes******************************

        #Gloves
        Gloves = self.Lomaton.find('**/hands')
        Gloves.setColor(0.99, 0.99, 0.99)

        #Sleeves
        Sleeves = loader.loadTexture('phase_4/maps/male_sleeve1.jpg')
        self.Lomaton.find('**/sleeves').setTexture(Sleeves, 1)

        #Shirts
        Shirt = loader.loadTexture('phase_4/maps/male_shirt1.jpg')
        self.Lomaton.find('**/torso-top').setTexture(Shirt, 1)

        #Shorts
        Shorts = loader.loadTexture('phase_4/maps/Purple_shorts_1.jpg')
        self.Lomaton.find('**/torso-bot').setTexture(Shorts, 1)

        #Shoes/Boots
        Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_wingtips.jpg')
        self.Lomaton.find('**/shoes').setTexture(Shoes, 1)
        self.Lomaton.find('**/boots_long').hide()
        self.Lomaton.find('**/boots_short').hide()
        self.Lomaton.find('**/feet').hide()

        #Hats
        Hat = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_hat_topHat.bam')
        Hat.reparentTo(Head.find('**/head'))
        Hat.setZ(0.30)
        Hat.setHpr(180.00, 330.00, 0.00)
        Hat.setScale(0.35)

        #Colors
        #Dog
        Top_Head.setColor(0.992188, 0.992188, 0.992188, 1.0)
        Bot_Head.setColor(0.992188, 0.992188, 0.992188, 1.0)
        self.Lomaton.find('**/neck').setColor(0.101248, 0.101248, 0.101248, 1.0)
        self.Lomaton.find('**/arms').setColor(0.101248, 0.101248, 0.101248, 1.0)
        self.Lomaton.find('**/legs').setColor(0.101248, 0.101248, 0.101248, 1.0)
        self.Lomaton.find('**/feet').setColor(0.101248, 0.101248, 0.101248, 1.0)
        Hat.setColor(0.99, 0.99, 0.99)

        self.Lomaton.setPosHpr(8.00, 5.00, 0.00, 90.00, 0.00, 0.00)

        self.Mellow = Actor({'torso':'phase_3/models/char/tt_a_chr_dgm_skirt_torso_1000.bam', \
             'legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
             {'torso':{'sit': 'phase_4/models/char/tt_a_chr_dgm_skirt_torso_sit.bam'}, \
             'legs':{'sit':'phase_4/models/char/tt_a_chr_dgm_shorts_legs_sit.bam'}})


        self.Mellow.attach('torso', 'legs', 'joint_hips')

        #Pos, Hpr, Scale, ReparentTo
        self.Mellow.setPos(0, 0, 0)
        self.Mellow.setHpr(0, 0, 0)
        self.Mellow.setScale(1.0)
        self.Mellow.reparentTo(render)

        #Head
        Head = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
        eyelash = loader.loadModel('phase_3/models/char/cat-lashes.bam')
        openString = 'open-short'
        closedString = 'closed-short'
        eyelashOpen = eyelash.find('**/' + openString).copyTo(Head)
        eyelashClosed = eyelash.find('**/' + closedString).copyTo(Head).hide()
        eyelash.removeNode()
        Head.find('**/muzzle-short-surprise').hide()
        Head.find('**/muzzle-short-sad').hide()
        Head.find('**/muzzle-short-smile').hide()
        Head.find('**/muzzle-short-angry').hide()
        Head.find('**/muzzle-short-laugh').hide()
        Head.find('**/muzzle-long-surprise').hide()
        Head.find('**/muzzle-long-sad').hide()
        Head.find('**/muzzle-long-smile').hide()
        Head.find('**/muzzle-long-angry').hide()
        Head.find('**/muzzle-long-laugh').hide()
        Head.find('**/muzzle-long-neutral').hide()
        Head.find('**/head-front-long').hide()
        Head.find('**/head-long').hide()
        Head.find('**/head-front-long')
        Head.find('**/eyes-long').hide()
        Head.find('**/joint_pupilL_long').hide()
        Head.find('**/joint_pupilR_long').hide()
        Head.find('**/ears-long').hide()
        Neck = self.Mellow.find('**/def_head')
        Head.reparentTo(Neck)

        #******************************Clothes******************************

        #Gloves
        Gloves = self.Mellow.find('**/hands')
        Gloves.setColor(255, 255, 255)

        #Sleeves
        Sleeves = loader.loadTexture('phase_4/maps/shirt_sleeveCat7_02.jpg')
        self.Mellow.find('**/sleeves').setTexture(Sleeves, 1)

        #Shirts
        Shirt = loader.loadTexture('phase_4/maps/shirt_Cat7_02.jpg')
        self.Mellow.find('**/torso-top').setTexture(Shirt, 1)

        #Skirts
        Shorts = loader.loadTexture('phase_4/maps/skirtCat7_01.jpg')
        self.Mellow.find('**/torso-bot').setTexture(Shorts, 1)

        #Shoes/Boots
        Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_winterBootsPink.jpg')
        self.Mellow.find('**/shoes').setTexture(Shoes, 1)
        self.Mellow.find('**/boots_long').hide()
        self.Mellow.find('**/boots_short').hide()
        self.Mellow.find('**/feet').hide()

        #Colors
        #Cat2
        Head.find('**/head-short').setColor(0.60, 0.60, 0.60, 1.0)
        Head.find('**/head-front-short').setColor(0.60, 0.60, 0.60, 1.0)
        Head.find('**/ears-short').setColor(0.60, 0.60, 0.60, 1.0)
        self.Mellow.find('**/neck').setColor(0.60, 0.60, 0.60, 1.0)
        self.Mellow.find('**/arms').setColor(0.60, 0.60, 0.60, 1.0)
        self.Mellow.find('**/legs').setColor(0.60, 0.60, 0.60, 1.0)
        self.Mellow.find('**/feet').setColor(0.60, 0.60, 0.60, 1.0)
        self.Mellow.setPosHpr(8.00, 2.00, 0.00, 90.00, 0.00, 0.00) 

        self.Diwant = Actor({'torso':'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', \
                     'legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
                     {'torso':{'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam'}, \
                     'legs':{'sit':'phase_4/models/char/tt_a_chr_dgm_shorts_legs_sit.bam'}})


        self.Diwant.attach('torso', 'legs', 'joint_hips')

        #Pos, Hpr, Scale, ReparentTo
        self.Diwant.setPos(0, 0, 0)
        self.Diwant.setHpr(0, 0, 0)
        self.Diwant.setScale(1.0)
        self.Diwant.reparentTo(render)

        #Head
        Head = loader.loadModel('phase_3/models/char/duck-heads-1000.bam')
        Head.find('**/muzzle-short-surprise').hide()
        Head.find('**/muzzle-short-sad').hide()
        Head.find('**/muzzle-short-smile').hide()
        Head.find('**/muzzle-short-angry').hide()
        Head.find('**/muzzle-short-laugh').hide()
        Head.find('**/muzzle-long-surprise').hide()
        Head.find('**/muzzle-long-sad').hide()
        Head.find('**/muzzle-long-smile').hide()
        Head.find('**/muzzle-long-angry').hide()
        Head.find('**/muzzle-long-laugh').hide()
        Head.find('**/muzzle-long-neutral').hide()
        Head.find('**/head-front-long').hide()
        Head.find('**/head-long').hide()
        Head.find('**/head-front-long').hide
        Head.find('**/eyes-long').hide()
        Head.find('**/joint_pupilL_long').hide()
        Head.find('**/joint_pupilR_long').hide()
        Neck = self.Diwant.find('**/def_head')
        Head.reparentTo(Neck)

        #******************************Clothes******************************

        #Gloves
        Gloves = self.Diwant.find('**/hands')
        Gloves.setColor(255, 255, 255)

        #Sleeves
        Sleeves = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding4.jpg')
        self.Diwant.find('**/sleeves').setTexture(Sleeves, 1)

        #Shirts
        Shirt = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_saveBuilding4.jpg')
        self.Diwant.find('**/torso-top').setTexture(Shirt, 1)

        #Shorts
        Shorts = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_saveBuilding1.jpg')
        self.Diwant.find('**/torso-bot').setTexture(Shorts, 1)

        #Shoes/Boots
        Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_deckShoes.jpg')
        self.Diwant.find('**/shoes').setTexture(Shoes, 1)
        self.Diwant.find('**/boots_long').hide()
        self.Diwant.find('**/boots_short').hide()
        self.Diwant.find('**/feet').hide()

        #Colors
        #Duck
        self.Diwant.find('**/neck').setColor(1.00, 1.00, 1.00, 1.0)
        self.Diwant.find('**/arms').setColor(1.00, 1.00, 1.00, 1.0)
        self.Diwant.find('**/legs').setColor(1.00, 1.00, 1.00, 1.0)
        self.Diwant.find('**/feet').setColor(1.00, 1.00, 1.00, 1.0)
        self.Diwant.setPosHpr(9.00, -3.30, 0.00, 90.00, 0.00, 0.00)

        self.Komoso = Actor({'torso':'phase_3/models/char/tt_a_chr_dgm_skirt_torso_1000.bam', \
                     'legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
                     {'torso':{'sit': 'phase_4/models/char/tt_a_chr_dgm_skirt_torso_sit.bam'}, \
                     'legs':{'sit':'phase_4/models/char/tt_a_chr_dgm_shorts_legs_sit.bam'}})
             
        self.Komoso.attach('torso', 'legs', 'joint_hips')

        #Pos, Hpr, Scale, ReparentTo
        self.Komoso.setScale(1.0)
        self.Komoso.reparentTo(render)

        #Head
        Head = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
        eyelash = loader.loadModel('phase_3/models/char/cat-lashes.bam')

        self.SadEyes = loader.loadTexture('phase_3/maps/eyesSad.jpg','phase_3/maps/eyesSad_a.rgb')
        self.SadEyes.setMinfilter(Texture.FTLinear)
        self.SadEyes.setMagfilter(Texture.FTLinear)

        self.NeutralEyes = loader.loadTexture('phase_3/maps/eyes.jpg','phase_3/maps/eyes_a.rgb')
        self.NeutralEyes.setMinfilter(Texture.FTLinear)
        self.NeutralEyes.setMagfilter(Texture.FTLinear)

        openString = 'open-short'
        closedString = 'closed-short'
        eyelashOpen = eyelash.find('**/' + openString).copyTo(Head)
        eyelashClosed = eyelash.find('**/' + closedString).copyTo(Head).hide()
        eyelash.removeNode()
        Head.find('**/muzzle-short-surprise').hide()
        Head.find('**/muzzle-short-sad').hide()
        Head.find('**/muzzle-short-smile').hide()
        Head.find('**/muzzle-short-angry').hide()
        Head.find('**/muzzle-short-laugh').hide()
        Head.find('**/muzzle-long-surprise').hide()
        Head.find('**/muzzle-long-sad').hide()
        Head.find('**/muzzle-long-smile').hide()
        Head.find('**/muzzle-long-angry').hide()
        Head.find('**/muzzle-long-laugh').hide()
        Head.find('**/muzzle-long-neutral').hide()
        Head.find('**/head-front-long').hide()
        Head.find('**/head-long').hide()
        Head.find('**/head-front-long')
        Head.find('**/eyes-long').hide()
        Head.find('**/joint_pupilL_long').hide()
        Head.find('**/joint_pupilR_long').hide()
        Head.find('**/ears-long').hide()
        Neck = self.Komoso.find('**/def_head')
        Head.reparentTo(Neck)

        #******************************Clothes******************************

        #Gloves
        Gloves = self.Komoso.find('**/hands')
        Gloves.setColor(255, 255, 255)

        #Sleeves
        Sleeves = loader.loadTexture('phase_4/maps/female_sleeve5New.jpg')
        self.Komoso.find('**/sleeves').setTexture(Sleeves, 1)

        #Shirts
        Shirt = loader.loadTexture('phase_4/maps/female_shirt5New.jpg')
        self.Komoso.find('**/torso-top').setTexture(Shirt, 1)

        #Shorts
        Shorts = loader.loadTexture('phase_3/maps/desat_skirt_7.jpg')
        self.Komoso.find('**/torso-bot').setTexture(Shorts, 1)

        #Shoes/Boots
        Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_fashionBootsPurple.jpg')
        self.Komoso.find('**/shoes').setTexture(Shoes, 1)
        self.Komoso.find('**/boots_long').hide()
        self.Komoso.find('**/boots_short').hide()
        self.Komoso.find('**/feet').hide()

        #Colors
        Head.find('**/head-short').setColor(0.241680, 0.241680, 0.241680, 1.0)
        Head.find('**/head-front-short').setColor(0.241680, 0.241680, 0.241680, 1.0)
        Head.find('**/ears-short').setColor(0.241680, 0.241680, 0.241680, 1.0)
        self.Komoso.find('**/neck').setColor(0.241680, 0.241680, 0.241680, 1.0)
        self.Komoso.find('**/arms').setColor(0.241680, 0.241680, 0.241680, 1.0)
        self.Komoso.find('**/legs').setColor(0.241680, 0.241680, 0.241680, 1.0)
        self.Komoso.find('**/feet').setColor(0.241680, 0.241680, 0.241680, 1.0)
        self.Komoso.setPosHpr(9.00, -1.00, 0.00, 90.00, 0.00, 0.00)
        # self.Komoso.place()

        self.KomosoEyes = Head.find('**/eyes-short')

        # Chat box
        # Teacher Cat
        self.ChatBox = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.ChatBox.reparentTo(self.Whiskers.find('**/joint_nameTag'))
        self.ChatBox.setScale(0.3)
        self.ChatBox.setPos(0.00, 0.00, 5.00)
        self.ChatBox.setHpr(360, 0.00, 0.00)
        self.ChatBox.setBillboardPointEye(2)

        font = loader.loadFont('phase_3/fonts/ImpressBT.ttf')
        self.text = TextNode('name')
        self.text.setFont(font)
        self.text.setTextColor(0, 0, 0, 1)
        self.text.setWordwrap(12)
        textNodePath = aspect2d.attachNewNode(self.text)
        textNodePath.setScale(0.8)
        textNodePath.reparentTo(self.ChatBox)
        textNodePath.setPos(1, -0.1, 3.0)

        # Chat box 2
        # Mouse
        self.ChatBox2 = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.ChatBox2.reparentTo(self.Mouse.find('**/joint_nameTag'))
        self.ChatBox2.setScale(0.3)
        self.ChatBox2.setPos(0.00, 0.00, 4.70)
        self.ChatBox2.setHpr(0.00, 0.00, 0.00)
        self.ChatBox2.setBillboardPointEye(2)

        self.text2 = TextNode('random')
        self.text2.setFont(font)
        self.text2.setTextColor(0, 0, 0, 1)
        self.text2.setWordwrap(12)
        textNodePath2 = aspect2d.attachNewNode(self.text2)
        textNodePath2.setScale(1.20, 1.20, 1.20)
        textNodePath2.reparentTo(self.ChatBox2)
        textNodePath2.setPos(1.00, -0.10, 2.20)
        # textNodePath2.place()

        # Black Cat
        self.ChatBox3 = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.ChatBox3.reparentTo(self.Komoso.find('**/joint_nameTag'))
        self.ChatBox3.setScale(0.3)
        self.ChatBox3.setBillboardPointEye(2)
        self.ChatBox3.setPos(0.00, 0.00, 4.1)

        self.text3 = TextNode('random1')
        self.text3.setFont(font)
        self.text3.setTextColor(0, 0, 0, 1)
        self.text3.setWordwrap(12)
        textNodePath3 = aspect2d.attachNewNode(self.text3)
        textNodePath3.setScale(0.8)
        textNodePath3.reparentTo(self.ChatBox3)
        textNodePath3.setPos(0.2, -12, 2.1)

        # Dog
        self.ChatBox4 = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.ChatBox4.reparentTo(self.Lomaton.find('**/joint_nameTag'))
        self.ChatBox4.setBillboardPointEye(2)
        # self.ChatBox4.place()
        self.ChatBox4.setPos(0.00, 0.00, 5.10)
        self.ChatBox4.setScale(0.30, 0.30, 0.30)

        self.text4 = TextNode('random1')
        self.text4.setFont(font)
        self.text4.setTextColor(0, 0, 0, 1)
        self.text4.setWordwrap(12)
        textNodePath4 = aspect2d.attachNewNode(self.text4)
        textNodePath4.setScale(0.8)
        textNodePath4.reparentTo(self.ChatBox4)
        textNodePath4.setPos(1.75, -4.20, 1.30)
        textNodePath4.setScale(1.50, 1.50, 1.50)
        # textNodePath4.place()

        # Cat 2
        self.ChatBox5 = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.ChatBox5.reparentTo(self.Lomaton.find('**/joint_nameTag'))
        self.ChatBox5.setBillboardPointEye(2)
        # self.ChatBox5.place()
        self.ChatBox5.setPos(-2.5, 0.00, 4.10)
        self.ChatBox5.setScale(0.30, 0.30, 0.30)

        self.text5 = TextNode('random1')
        self.text5.setFont(font)
        self.text5.setTextColor(0, 0, 0, 1)
        self.text5.setWordwrap(12)
        textNodePath5 = aspect2d.attachNewNode(self.text5)
        textNodePath5.setScale(0.3)
        textNodePath5.reparentTo(self.ChatBox5)
        textNodePath5.setPos(1.40, -6.20, 1.30)
        textNodePath5.setScale(1, 1.30, 1.50)
        # textNodePath5.place()

        # Duck
        self.ChatBox6 = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.ChatBox6.reparentTo(self.Lomaton.find('**/joint_nameTag'))
        self.ChatBox6.setBillboardPointEye(2)
        # self.ChatBox6.place()
        self.ChatBox6.setPos(-6.2, 0.5, 5.10)
        self.ChatBox6.setScale(0.30, 0.30, 0.30)

        self.text6 = TextNode('random1')
        self.text6.setFont(font)
        self.text6.setTextColor(0, 0, 0, 1)
        self.text6.setWordwrap(12)
        textNodePath6 = aspect2d.attachNewNode(self.text6)
        textNodePath6.setScale(0.8)
        textNodePath6.reparentTo(self.ChatBox6)
        textNodePath6.setPos(1, -4.20, 1.30)
        textNodePath6.setScale(1.50, 1.50, 1.50)
        # textNodePath6.place()

        # Moving Around Mouse
        Spin1 = LerpHprInterval(self.Mouse, duration=0.5, hpr=(176.42, 0, 0), blendType='easeInOut')
        Run1 = LerpPosInterval(self.Mouse, duration=0.5, pos=(1.30, -3.00, 0.00), blendType='easeInOut')
        Spin2 = LerpHprInterval(self.Mouse, duration=0.5, hpr=(95.71, 0, 0), blendType='easeInOut')
        Run2 = LerpPosInterval(self.Mouse, duration=0.5, pos=(-3.00, -3.00, 0.00), blendType='easeInOut')
        Spin3 = LerpHprInterval(self.Mouse, duration=0.5, hpr=(181.97, 0, 0), blendType='easeInOut')
        Run3 = LerpPosInterval(self.Mouse, duration=0.5, pos=(-3.00, -17.00, 0.00), blendType='easeInOut')
        self.Walking = Sequence(Func(self.Mouse.loop, 'run'), Spin1, Run1, Spin2, Run2, Spin3, Run3)
        self.ChatBox.hide()
        self.ChatBox2.hide()
        self.ChatBox3.hide()
        self.ChatBox4.hide()
        self.ChatBox5.hide()
        self.ChatBox6.hide()
        self.Mouse.setPlayRate(1, 'run')

        self.Komoso.loop('sit')
        self.Diwant.loop('sit')
        self.Mellow.loop('sit')
        self.Lomaton.loop('sit')
        self.Whiskers.loop('idle')
        self.Mouse.loop('sit')

        movementSequence = Sequence(Wait(2.0), Wait(1.8),
                            Wait(0.5), LerpPosInterval(camera, 0, (13, 4, 4)),  # Move backwards over a single second
                            Parallel(  # Now focus on Mousey
                            LerpPosInterval(camera, 0, (-10, 0, 4)),  # Start moving forward
                            Wait(0), LerpHprInterval(camera, 0, (270, 0, 0))),
                            Wait(12.7), LerpPosInterval(camera, 0, (-10, -10, 4)),
                            Wait(3.5), LerpHprInterval(camera, 0, (90, 0, 0)), # Mouse running scene
                            Wait(0), LerpPosInterval(camera, 0, (13, 4, 4)),
                            Wait(1), LerpHprInterval(camera, 0, (90, 0, 0)),
                            Wait(1.5), LerpPosInterval(camera, 0, (-10, 0, 4)),
                            Wait(0), LerpHprInterval(camera, 0, (270, 0, 0)) 
                            )
        movementSequence.start()

        mainIval = Sequence(
            Wait(2.0),
            Func(base.playMusic, self.musicBGM),
            Func(self.ChatBox4.hide),
            Func(self.ChatBox2.hide),
            Func(self.ChatBox3.hide),
            Func(self.ChatBox.show),
            Func(self.doTalk, self.text, "Class we are going to start this test.", self.Cat_Long),
            Wait(2.0),
            Func(self.ChatBox.hide),
            Wait(1.0),
            Func(self.ChatBox4.show),
            Func(self.doTalk, self.text4, "Okay!", self.Dog_Exclaim),
            Wait(1.0),
            Func(self.ChatBox4.hide),
            Wait(0.5),
            Func(self.ChatBox2.show),
            Func(self.doTalk, self.text2, "I farted.", self.Mouse_Medium),
            Func(base.playSfx, self.FART),
            Wait(1.0),
            Func(self.ChatBox2.hide),
            Wait(1.0),
            Func(self.ChatBox2.show),
            Func(self.doTalk, self.text2, "GOTTA GO.", self.Mouse_Medium),
            Func(self.Mouse.find('**/muzzle-short-laugh').show),
            Wait(0.5),
            Func(base.playSfx, self.Mouse_Laugh),
            Wait(1.0), 
            Func(self.Mouse.find('**/muzzle-short-laugh').hide),
            Wait(1.0),
            Func(self.ChatBox2.hide), 
            Func(self.KomosoEyes.setTexture, self.SadEyes, 1),
            Func(self.ChatBox3.show),
            Func(self.doTalk, self.text3, "EWWWW YOU ARE DISGUSTING WHY.", self.Cat_Long),
            Wait(2.0),
            Func(self.ChatBox4.show),
            Func(self.doTalk, self.text4, "DUDE!", self.Dog_Exclaim),
            Func(self.KomosoEyes.setTexture, self.NeutralEyes, 1),
            Wait(1.0),
            Func(self.ChatBox4.hide),
            Wait(1.8),
            Func(self.ChatBox3.hide),
            Func(self.Walking.start),
            Func(base.playSfx, self.AV_RUN),
            Wait(2.5),
            Func(base.playSfx, self.YEET),
            Wait(2.5),
            Func(base.playSfx, self.DoorOpen),
            Wait(1.0),
            Func(base.playSfx, self.DoorClose),
            Func(self.ChatBox.show),
            Func(self.doTalk, self.text, "Alright then cool I guess.", self.Cat_Long),
            Wait(3.0),
            Func(self.ChatBox.hide),
            Func(self.ChatBox5.show),
            Func(self.doTalk, self.text5, "Ok then????", self.Cat_Long),
            Wait(2.5),
            Func(self.ChatBox5.hide),
            Func(self.ChatBox6.show),
            Func(self.doTalk, self.text6, "WOOOW", self.Duck_Short),
            Wait(1.8),
            Func(self.ChatBox6.hide)
            )
        mainIval.start()

    def doTalk(self, bubble, text, sound):
        bubble.setText(text)
        sound.play()

tvc = ToonsVsCogsTheUltimate()
base.run()