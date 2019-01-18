#!/usr/bin/python
# coding: utf-8
import sys
import Adafruit_DHT

# parameters
DHT_type      = 11
Temperature_GPIO = 23
LED_GPIO = 24
BUTTON_GPIO = 21

def check_temperature():
	# read and report dht11 temperature and humidity
	humidity, temperature = Adafruit_DHT.read_retry(DHT_type, Temperature_GPIO)
	print("Humidity {}, Temperature {}".format(humidity, temperature))
	return humidity, temperature
