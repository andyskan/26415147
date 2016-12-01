#!/usr/bin/python

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from random import *
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle, Color, Canvas
from functools import partial
#setup graphics
Config.set('graphics','resizeable', 0)
#graphics
Window.clearcolor = (0,0,0.025,1.)
#sound
up=SoundLoader.load('naik.wav')
music=SoundLoader.load('music.wav')

class SmartMenu(Widget):
	buttonList = []
	def __init__(self, **kwargs):
		self.register_event_type('on_button_release')

		super(SmartMenu, self).__init__(**kwargs)
		self.layout = BoxLayout(orientation = 'vertical')
		self.layout.width = Window.width/2
		self.layout.height = Window.height/2
		self.layout.x = Window.width/2 - self.layout.width/2
		self.layout.y = Window.height/2 - self.layout.height/2
		self.add_widget(self.layout)

	def on_button_release(self, *args):
		pass

	def callback(self, instance):
		self.buttonText = instance.text
		self.dispatch('on_button_release')

	def addButtons(self):
		for k in self.buttonList:
			tempbutton = MyButton(text = k)
			tempbutton.background_color = [.4, .4, .4, .4]
			tempbutton.bind(on_release = self.callback)
			self.layout.add_widget(tempbutton)

	def addButtons(self):
		for k in self.buttonList:
			tempbutton = MyButton(text = k)
			tempbutton.background_color = [.4, .4, .4, .4]
			tempbutton.bind(on_release = self.callback)
			self.layout.add_widget(tempbutton)

	def buildUp(self):
		self.addButtons()

class SmartStartMenu(SmartMenu):
	buttonList = ['Easy', 'Medium', 'Hard', 'About']

	def __init__(self, **kwargs):
		super(SmartStartMenu, self).__init__(**kwargs)
		self.layout = BoxLayout(orientation = 'vertical')
		self.layout.width = Window.width/2
		self.layout.height = Window.height/2
		self.layout.x = Window.width/2 - self.layout.width/2
		self.layout.y = Window.height/2 - self.layout.height/2
		self.add_widget(self.layout)

		self.msg = Label(text = 'Flappy Ship')
		self.msg.font_size = Window.width*0.07
		self.msg.pos = (Window.width*0.45,Window.height*0.75)
		self.add_widget(self.msg)
		self.img = Image(source = 'space1.jpg')
		self.img.size = (Window.width*1.5,Window.height*1.5)
		self.img.pos = (-Window.width*0.2,-Window.height*0.2)
		self.img.opacity = 0.35
		self.add_widget(self.img)


class WidgetDrawer(Widget):

	def __init__(self, imageStr, **kwargs):
		super(WidgetDrawer, self).__init__(**kwargs)
		with self.canvas:
			self.size =  (Window.width*.002*25,Window.width*.002*25)
                 #       self.size2=(Window.width*1,Window.width*1)
		#	self.wimg = Image(source='lol.png')
			self.image=Image(source='lol.png')
			self.image.size=(Window.width*1,Window.height*1)
		#	self.image=Rectangle(source='lol.png',pos=self.pos,size=self.size2)
                       #self.image.size=(Window.width,Window.height)
                        self.image.opacity=0.025
			self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size=self.size)
			self.bind(pos=self.update_graphics_pos)
			self.x=self.center_x
			self.y=self.center_y
			self.pos=(self.x, self.y)
			self.rect_bg.pos=self.pos
	def update_graphics_pos(self,instance,value):
		self.rect_bg.pos=value

	def setSize(self,width, height):
		self.size=(width, height)

	def setPos(xpos,ypos):
		self.x=xpos
		self.y=ypos

class ScoreWidget(Widget):
	def __init__(self, **kwargs):
		super(ScoreWidget, self).__init__(**kwargs)
		self.skorasteroid = 0
		self.skorsekarang = 0
		with self.canvas:
			temppos = (Window.width*0.25,Window.height*0.25)
			tempsize = (Window.width*0.5,Window.height*0.5)
			Color(0.1,.1,.1)
			self.scoreRect = Rectangle(pos = temppos, size = tempsize)

	def prepare(self):
		try:
			self.finalScore = self.skorasteroid*100

		except:
			print 'Tidak bisa dapat skor'
		self.animateScore()

	def animateScore(self):
		scoreText = 'Score : 0' # + str(self.FinalScore)
		self.scoreLabel = Label(text = scoreText, font_size = '20sp')
		self.scoreLabel.x = Window.width*0.3
		self.scoreLabel.y = Window.height*0.25
		self.add_widget(self.scoreLabel)
		Clock.schedule_once(self.updateScore, .1)
	def updateScore(self,dt):
		self.skorsekarang = self.skorsekarang + 100
		self.scoreLabel.text = 'Score : ' + str(self.skorsekarang)
		if self.skorsekarang < self.finalScore:
			Clock.schedule_once(self.updateScore, 0.1)

class Asteroid(WidgetDrawer):
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	cek= False


	def move(self):
		self.x = self.x + self.velocity_x
		self.y = self.y + self.velocity_y

	def update(self):
		self.move()

class Ship(WidgetDrawer):
	impulse = 3
	grav = -0.1

	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)

	def move(self):
		self.x = self.x + self.velocity_x
		self.y = self.y + self.velocity_y

		if self.y == Window.height*0.95:
			self.impulse = -3

                if self.y < Window.height*0.05:
			self.impulse = 3
			self.grav = -0.1

		if self.y > Window.height*0.95:
			self.impulse = -3

	def determineVelocity(self):
		self.grav = self.grav*1.05
		if self.grav < -300:
			self.grav = -300

		self.velocity_y = self.impulse + self.grav
		self.impulse = 0.95*self.impulse

	def update(self):
		self.determineVelocity()
		self.move()

class MyButton(Button):
	def __init__(self, **kwargs):
		super(MyButton, self).__init__(**kwargs)
		self.font_size = Window.width*0.018

class GUI(Widget):
	asteroidList=[]
	atas=NumericProperty(1)
	cek=NumericProperty(0)
	atashard=NumericProperty(45)
	bawahhard=NumericProperty(125)
	bawah=NumericProperty(25)
	atasMed=NumericProperty(20)
	bawahMed=NumericProperty(80)
	asteroidScore=NumericProperty(0)
	minProb = 1780#asteroid
	def __init__(self, **kwargs):
		super(GUI, self).__init__(**kwargs)
		l = Label(text='Flappy Ship')
		l.x = Window.width/2 - l.width/2
		l.y = Window.height*0.8
		self.add_widget(l)
		self.ship = Ship(imageStr = './ship.png')
		self.ship.x = Window.width/4
		self.ship.y = Window.height/2
		self.add_widget(self.ship)

	def addAsteroid(self):
		 imageNumber = randint(1,4)
		 imageStr = './sandstone_'+str(imageNumber)+'.png'
		 tmpAsteroid = Asteroid(imageStr)
		 tmpAsteroid.x = Window.width*0.99
		 ypos = randint(1,16)
		 ypos = ypos*Window.height*.0625
		 tmpAsteroid.y = ypos
		 tmpAsteroid.velocity_y = 0
		 if self.cek == 0:
			 vel=randint(self.atas,self.bawah)
		 if self.cek == 1:
		 	vel=randint(self.atasMed,self.bawahMed)
		 if self.cek == 2:
			vel=randint(self.atashard,self.bawahhard)
		 tmpAsteroid.velocity_x = -0.1*vel
		 self.asteroidList.append(tmpAsteroid)
		 self.add_widget(tmpAsteroid)

	def on_touch_down(self, touch):
		up.play()
		self.ship.impulse = 3
		self.ship.grav = -0.1
	def showScore(self):
		self.scoreWidget=ScoreWidget()
		self.scoreWidget.skorasteroid=self.asteroidScore
		self.scoreWidget.prepare()
		self.add_widget(self.scoreWidget)
	def removeScore(self):
		self.remove_widget(self.scoreWidget)
	def gameOver(self):
		restartButton = MyButton(text='Restart')
		backButton = MyButton(text='Exit')

		def restart_button(obj):
			print 'Restart button pushed'
			self.removeScore()
			for k in self.asteroidList:
				self.remove_widget(k)
				self.ship.xpos = Window.width*0.25
				self.ship.ypos = Window.height*0.5
				self.minProb = 1700
				self.asteroidScore=0
				self.asteroidList=[]

			self.parent.remove_widget(restartButton)
			self.parent.remove_widget(backButton)
			Clock.unschedule(self.update)
			Clock.schedule_interval(self.update, 1.0/60.0)
		def back_button(obj):
			print 'Keluar'
			self.parent = Widget()
			self.app = GUI()
			self.sm = SmartStartMenu()
			self.sm.buildUp()
			for k in self.asteroidList:
					self.remove_widget(k)
					self.ship.xpos = Window.width*0.25
					self.ship.ypos = Window.height*0.5
					self.minProb = 1700
					self.asteroidScore=0
					self.asteroidList=[]
			self.parent.remove_widget(restartButton)
			self.parent.remove_widget(backButton)
			self.sm.bind(on_button_release = self.check_button)
			self.parent.add_widget(self.sm)
			self.parent.add_widget(self.app)
			return self.parent
		restartButton.size = (Window.width*.3, Window.width*.1)
		restartButton.pos = Window.width*0.5-restartButton.width/2, Window.height*0.5
		restartButton.bind(on_release=restart_button)
		backButton.size = (Window.width*.3, Window.width*.1)
		backButton.pos = Window.width*0.5-restartButton.width/2, Window.height*0.5-restartButton.height/1.2
		backButton.bind(on_release=back_button)
		self.parent.add_widget(restartButton)
		self.parent.add_widget(backButton)
		self.showScore()

	def update(self,dt):
		print "jalan"
		self.ship.update()
		tmpCount = randint(1,1800)
		if tmpCount > self.minProb:
			self.addAsteroid()
			if self.minProb < 1500:
				self.minProb = 1500
			self.minProb = self.minProb -1
		for k in self.asteroidList:
			if k.collide_widget(self.ship):
				print 'Game Over'
				self.gameOver()
				Clock.unschedule(self.update)
			k.update()

			if k.x < self.ship.x and k.cek == False:
				self.asteroidScore=self.asteroidScore+1
				k.cek=True
			if k.x < -100:
				self.remove_widget(k)
				tmpAsteroidList=self.asteroidList
				tmpAsteroidList[:]=[x for x in tmpAsteroidList if ((x.x > -100))]
				self.aster=tmpAsteroidList

class ClientApp(App):
	music.play()
	def build(self):
		self.parent = Widget()
		self.app = GUI()
		self.sm = SmartStartMenu()
		self.sm.buildUp()
		def check_button(obj):
			if self.sm.buttonText == 'Easy':
				self.parent.remove_widget(self.sm)
				print 'Mulai game'
				music.play()
				Clock.unschedule(self.app.update)
				Clock.schedule_interval(self.app.update, 1.0/60.0)
				try:
					self.parent.remove_widget(self.aboutText)
				except:
					pass
			if self.sm.buttonText == 'Medium':
				#self.app.atas=1
				self.app.cek=1
				#self.app.bawah=25
				self.parent.remove_widget(self.sm)
				print 'Mulai medium'
				music.play()
				Clock.unschedule(self.app.update)
				Clock.schedule_interval(self.app.update, 1.0/440.0)
				try:
					self.parent.remove_widget(self.aboutText)
				except:
					pass
			if self.sm.buttonText == 'Hard':
				#self.app.atas=1
				self.app.cek=2
				#self.app.bawah=25
				self.parent.remove_widget(self.sm)
				print 'Mulai Hard'
				music.play()
				Clock.unschedule(self.app.update)
				Clock.schedule_interval(self.app.update, 1.0/550.0)
				try:
					self.parent.remove_widget(self.aboutText)
				except:
					pass
			if self.sm.buttonText == 'About':
				self.aboutText = Label(text = 'Proyek TOS')
				self.aboutText.pos = (Window.width*1.78/4,Window.height/4)
				self.parent.add_widget(self.aboutText)
		self.sm.bind(on_button_release = check_button)
		self.parent.add_widget(self.sm)
		self.parent.add_widget(self.app)
		return self.parent

if __name__ == '__main__' :
	ClientApp().run()
