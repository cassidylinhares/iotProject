# Smart Plant Moisture Meter
Cassidy Linhares - 100615025

## Table of Contents
1. [Project Description](#desc)  
1. [Project Requirements](#req)   
1. [Project Use Case (assignment2)](#usecase)  
1. [Set Up](#setup)  
1. [Get IPv4 Address](#ipv4)  
1. [Set Up Django Backend](#back)  
1. [Set Up React Frontend](#front)  
1. [API Usage](#api)  

## Description <a name="desc"></a>
The Smart Plant Moisture Meter will be used for managing indoor plants and when they should be watered. Many plants tend to get over-watered as a result of the top of the soil being dry but the middle being still moist. Having to probe you plant each day is also very annoying and easy to forget. The Smart Plant Moisture Meter helps indoor gardeners keep track of their plant's moisture level and notify gardeners via a phone app when it is time to water.
## Requirements <a name="req"></a>
### General
- Must have moisture meter as device
- moisture meter must be able to withstand water
### Functional
- Must have a dashboard to see moisture status
### Communication
- Must send a notification to phone when moisture is at <20%
### Scalability
- Must be able to handle up to 2 moisture meters
### Security & Connectivity
- must connect to devices within 5s

## Use Case <a name="usecase"></a>
User installed moisture sensor in plant and is on the web application. The moisture sensor posts to the web application every 10min. 
The user can get the data, update or delete, the data.
## Set up <a name="setup"></a>
1. Clone the repo
### 2. Get your ipv4 address <a name="ipv4"></a>
#### Windows
1. Open command prompt and enter `ipconfig`
2. Look for the wifi ipv4 address and copy it
#### Linux
1. Open terminal and enter `ifconfig`
2. Look for the wifi ipv4 address and copy it

### 3. Set Up Backend <a name="back"></a>
1. Open the `IoTAssignment2Back/` in VS code
2. Make a python virtual env (I used python 3.6) using these steps: https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial
3. Install the requirements with `pip install -r requirements.txt` into the virtual env
4. Open the `settings.py` file
5. In the `ALLOWED_HOSTS` (`line28`) add your ipv4 address
6. Migrate the database with `python manage.py migrate`
7. Run the server with `python manage.py runserver your_ip_addr:8000` or `python manage.py runserver 0.0.0.0:8000`
8. To run the test use `python managae.py test`

### 4. [Set Up Frontend](https://github.com/cassidylinhares/iotProjectWebFront#setup-) <a name="front"></a>

### 5. Set Up IoT Sensor <a name="sensor"></a>
1. You need to have the capacitive soil moisture sensor v1.2 and hook it up to the node mcu esp8266
2. Open the iot_moistureSensor in arduino
3. Replace `ssid` to your ssid and `password` to your wifi password
4. Replace `serverName` with your ip address
5. upload to nodemcu and done!

## API Usagae & Implementation <a name="api"></a>
### `getMoistureLevels/`
Gets all the moisture levels, the timestamp created, and id
### `getMoistureLevel/id/`
Gets a moisture level by id. Returns the id, moisture level, and timestamp from when it was read
### `insertMoistureLevel/`
Inserts moisture level. This is currently inserted every 10min but the moisture sensor through IoT Post request. The sensor reads the values at that moment and then makes a POST request with application/json content type, the server receives these values and inserts them into the database. The id and timestamp are auto generated and do not need to be inserted by the device or user
### `updateMoistureLevel/id/`
Updates the moisture level using an existing id. The only thing that can be changed is the moisture level. Returns the id, timestamp, and updated moisture level
### `deleteMoistureLevel/id/`
Deletes a moisture level by id
