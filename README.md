# Smart Plant Moisture Meter
Cassidy Linhares - 100615025

## Table of Contents
1. [Project Description](#desc)  
2. [Background Information](#bkgd) 
3. [Project Requirements](#req)   
4. [Project Use Case (assignment2)](#usecase) 
5. [Architecture](#arch) 
6. [Architecture & Deployement Decisions](#arch-deploy-des)
7. [Set Up](#setup)  
8. [Get IPv4 Address](#ipv4)  
9. [Set Up Django Backend](#back)  
10. [Set Up React Frontend](#front)  
11. [API Usage](#api)  

## Description <a name="desc"></a>
The Smart Plant Moisture Meter will be used for managing indoor plants and when they should be watered. Many plants tend to get over-watered as a result of the top of the soil being dry but the middle being still moist. Having to probe you plant each day is also very annoying and easy to forget. The Smart Plant Moisture Meter helps indoor gardeners keep track of their plant's moisture level and notify gardeners via a phone app when it is time to water.
## Background Info <a name="bkgd"></a>
Many notification systems don’t have a physical aspect and just go by time passed. This is more accurate as it notifies you when the soil is actually at a point where it needs to be watered. The use of IoT will help with connecting the moisture sensors to the internet to get the moisture levels.  Other option is get a moisture sensor but you have to probe the plant each time making this easy to forget and tedious
## Requirements <a name="req"></a>
### General
- Must have moisture meter as device
- moisture meter must be able to withstand water
### Functional
- Must have a dashboard to see moisture status
- Must show history of moisture meter in a graph
### Availability
- Must be available 98% of the time through cloud services
### Communication
- Must send a notification to phone when moisture is below treshold set by plant datasheet
### Scalability
- Must be able to handle up to 2 moisture meters
- Be hosted on the cloud for easy deployabilty and scaling
### Security & Connectivity
- must connect to devices within 5s
- should try to reconnect if connection fails
- secure cloud server using Digital Ocean

## Use Case <a name="usecase"></a>
User installed moisture sensor in plant and is on the web application. The moisture sensor posts to the web application every 10min. 
The user can get the data, change their plant type, and view the history of the moisture meter

## Design Methodology <a name="des-meth"></a>
![Architecture IoT](https://user-images.githubusercontent.com/30815527/144935475-1a68c642-83c5-45c6-9da5-694828a5c8aa.png)

## Architecture <a name="arch"></a>
![Architecture IoT](https://user-images.githubusercontent.com/30815527/144935475-1a68c642-83c5-45c6-9da5-694828a5c8aa.png)

## Architecture & Deployement Decisions <a name="arch-deploy-des"></a>
- Django was chosen as the server framework because it was easy to set up and easy to deploy. It also has an ORM which makes working with the database easy
- Database was chosen as SQLite because it is lightweight, comes pre-built into Djano, and I wanted it to be local to each user.
- Frontend was chosen as React because it has states and is very quick to build a UI and has many graphing UI libraries
- Digital Ocean's Web app was chosen as the cloud service because it has auto-security features, auto-deploy, auto-routing, domain routing and free domain service. It also auto-configures the web application for you.   Another reason I didn't use the droplet was because I ran out of time due to my other group projects and I had a lot of trouble trying to get the example from class to work. I had issues with node-red and I had to actaully restart the droplet application 3 separate times because I'd run into security set up issuesn networking issues, or library deprecation issues. I spent like 5-6h a day for 5 days trying to get it working before I ultimately gave up because I had to focus my time on the rest of the project
- Frontend was not run on cloud because that would mean running another cloud instance for it.
- Sensors connected with Http instead of mqtt because connects to cloud easier and easier to secure. I tried to get the sensor to connect to the cloud service using HTTPs since http didn't work since the cloud is secured. I couldn't get it working and I'm not sure why. One of the challenges of IoT is debugging on the cloud and on the devices.

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
