#!/usr/bin/python
# coding: utf-8
import sys
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

# parameters
DHT_type      = 11
Temperature_GPIO = 23
LED_GPIO = 24
BUTTON_GPIO = 21

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_GPIO, GPIO.OUT)
	GPIO.output(LED_GPIO, GPIO.HIGH)
	GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback=check_temperature, bouncetime=200)


def check_temperature():
	# read and report dht11 temperature and humidity
	GPIO.output(LED_GPIO, GPIO.HIGH)
	humidity, temperature = Adafruit_DHT.read_retry(DHT_type, Temperature_GPIO)
	print("Humidity {}, Temperature {}".format(humidity, temperature))
	GPIO.output(LED_GPIO, GPIO.LOW)
	return humidity, temperature

def deinit():
	GPIO.output(LED_GPIO, GPIO.HIGH)
	GPIO.cleanup()
