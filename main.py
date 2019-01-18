import sensor
import sys
import time
from bluetooth import *

## CONFIG:
ID = "1"
HOST = "B8:27:EB:40:D6:34"#sys.argv[1]
PORT = 3
TIME = 2


def run():
	print("Init System")
	#sensor.init()
	while True:
		print("Checking Temperature")
		humidity, temperature = sensor.check_temperature()
		timestamp = time.time()
	#Connect temporarly when sending the data overbluetooth
		try :
			s=BluetoothSocket( RFCOMM )
			print("Connect to {}:{}".format(HOST, PORT))
			s.connect((HOST, PORT))
			message = "id:{},humidity:{},temperature:{},timestamp:{}".format(ID, humidity, temperature, timestamp)
			s.send(message)
			s.close()
		except :
			err = sys.exc_info()[0]
			print("Unexpected disconnect REASON : {}".format(err))

		time.sleep(TIME)

if __name__ == "__main__" :
	run()