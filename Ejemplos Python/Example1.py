#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from multiprocessing import Process
from tools import blink, led_on, play_audio
from rythms import rythms_test1
import random

class GPIO_DEA(object):
	"""docstring for GPIO_DEA"""
	def __init__(self, pin_led, pin_onoff, pin_switch_shock, pin_cable, pin_shock):
		super(GPIO_DEA, self).__init__()
		self.pin_led = pin_led
		self.pin_onoff = pin_onoff
		self.pin_switch_shock = pin_switch_shock
		selg.pin_cable = pin_cable
		self.pin_shock = pin_shock
		self.setup()

	def setup(self):
		"""
		This is the output/input and callbacks setup for buttons and leds.
		"""
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin_led, GPIO.OUT) # led, usos varios
		GPIO.setup(self.pin_switch_shock, GPIO.IN) # palanca para saber si se aplica shock
		GPIO.setup(self.pin_onoff, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # boton ON/ OFF
		GPIO.setup(self.pin_shock, GPIO.IN, pull_up_down = GPIO.PUD_UP) # boton shock
		# TODO implementar efecto de cable enchufado
		GPIO.add_event_detect(self.pin_onoff, GPIO.RISING, callback=self.button_on, bouncetime=300)
		GPIO.add_event_detect(self.shock, GPIO.RISING, callback=self.shock_button_pressed, bouncetime=300)
		GPIO.add_event_detect(self.pin_cable, callback=self.pluged_in)

	def get_switch_shock(self):
		"""
		Check if in this turn you should use shock or not
		"""
		return GPIO.input(self.pin_switch_shock)

	def button_on(self, audios_inicial=['audio/audio1.ogg','audio/audio2.ogg','audio/audio3.ogg'
										'audio/audio4.ogg', 'audio/audio5.ogg', 'audio/audio6.ogg']):
		"""
		callback for on/off button
		"""
		map(play_audio(), audios_inicial)

	def pluged_in(self, audio_analisis='audio/audio7.ogg', audio_no_shock = ['audio/audio10.ogg'],
														   audio_shock=['audio/audio9a.ogg',
																		'audio/audio9b.ogg',
																		'audio/audio9c.ogg',
																		'audio/audio11.ogg']):
		"""
		When the cable is plugedin check if the shock button
		to look which set of rhythms we should use,
		and if we should turn on the leds
		"""
		play_audio(audio_analisis)
		self.led_on()
		if self.get_switch_shock():
			audios_file = audio_shock
			# TODO colocar delay, programar random para 2 o 3 shocks seguidos
			rythm = rythms_shock[random.choice(rythms_shock.keys())]
			p_blink = Process(target=self.blink, args=(10, 10, 19,))
			p_audio.start()
		else:
			audios_file = audio_no_shock
			rythm = rythms_no_shock[random.choice(rythms_no_shock.keys())]
		p_audio = Process(target=play_audio, args=(audios_file,))
		# TODO fix this to several files
		p_audio.start()
		p_plot = Process(target=plot_ritmo, args=(ritmo,))
		p_plot.start()

	def shock_button_pressed(self, after_shock_audio=['audio/audio12.ogg',
													  'audio/audio13.ogg',
													  'audio/audio14.ogg' ]
									emergency_audio=['audio/audio15.ogg']):
		"""
		after resolving the shock phase you should wait 2'
		and go back again to plugedIn fuction
		"""
		# TODO fix counter for diferent audios
		play_audio(after_shock_audio)
		time.sleep(120)
		self.pluged_in()

	def blink(self, num_times, speed):
		"""
		blink #num_times times at a #speed in the pin #output_pin
		"""
		for i in range(num_times):
			GPIO.output(self.pin_led, True)
			time.sleep(speed)
			GPIO.output(self.pin_led, False)
			time.sleep(speed)
		GPIO.cleanup()

	def led_on(self):
		"""
		set on 1 the led at the #output_pin
		"""
		GPIO.output(self.pin_led, True)

# TODO this should have the heart fuctions
rythms_shock = {'FV':, 'TV': }  # fibrilacion ventricular (FV) y la taquicardia ventricular
rythms_no_shock = {'r1':rythms_test1, 'r2':}

def main():
	# TODO var with num of pins
	my_dea_gpio = GPIO_DEA(pin_led=19, pin_onoff=23, pin_switch_shock=24, pin_cable=, pin_shock=)


if __name__ == '__main__':
	main()
