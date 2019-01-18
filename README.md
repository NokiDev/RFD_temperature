# RFD_temperature
Retrieve temperature through sensor and send it through bluetooth to another raspberry pi

## Hardware

### Hardware Requirements

- A raspberry pi (tested on rpi 3B+)
- Temperature / Humidity sensor DHT
- One Led
- few wires
- 4k resistor

### Hardware Setup

#### GPIO Used

- Led is connected through GPIO24 (pin 18)
- DHT sensor is connected though GPIO23 (pin16)

![alt text](https://github.com/NokiDev/RFD_Temperature/raw/master/doc/all.jpg "raspbery pi + board")
![alt text](https://github.com/NokiDev/RFD_Temperature/raw/master/doc/Board.jpg "board")

## Software

### Software Requirements

- python 3.X (not tested with python 2.X)
- py-bluez (python package)
- bluez (raspbian package)
- lib-bluetooth (raspbian package)

### Install and run 

```
git clone https://github.com/NokiDev/RFD_Temperature
cd RFD_Temperature
python3 main.py
```

main.py accepts few command line arguments

- 1: remote bluetooth device MAC Address
- 2: remote bluetooth device Port
- 3: Time to wait between temperature checks

### TODOS

- Add reference to packages required.
- Add an electric graph.
- Make Manual Temperature checking by pressing the button. 
