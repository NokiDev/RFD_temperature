import sensor
import sys
import time
import json
from bluetooth import *

## CONFIG:
ID = "1"
HOST = "B8:27:EB:40:D6:34" if not len(sys.argv) == 2 else sys.argv[1]
PORT = 3 if not len(sys.argv) == 3 else sys.argv[2]
TIME = 60 if not len(sys.argv) == 4 else sys.argv[3]

## Open bluetooth socket, and connect to HOST, and send the message in parameters.
def send_message_once(message):
	try :
		s=BluetoothSocket( RFCOMM )
		print("Connect to {}:{}".format(HOST, PORT))
		s.connect((HOST, PORT))
		s.send(message)
		s.close()
	except :
		err = sys.exc_info()[0]
		print("Unexpected disconnect REASON : {}".format(err))

## Run the main process.
def run():
	print("Init System")
	try:
		sensor.init()
		while True:
			print("Checking Temperature")
			humidity, temperature = sensor.check_temperature()
			timestamp = time.time()
			message = json.JSONEncoder().encode({"id": ID, "temperature": temperature, "humidity": humidity, "timestamp": timestamp})
			#Connect temporarly when sending the data overbluetooth
			send_message_once(message)
			elapsedTime = time.time() - timestamp
			timeToWait = TIME - elapsedTime if TIME - elapsedTime > 0 else 0 
			time.sleep(TIME)
	except KeyboardInterrupt:
		print("QUITTING")
	sensor.deinit()

if __name__ == "__main__" :
	run()
