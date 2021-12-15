# Plant Pal
Cassidy Linhares - 100615025

## Table of Contents
1. [Project Description](#desc)  
2. [Background Information](#bkgd) 
3. [Project Requirements](#req)   
4. [Project Use Case (assignment2)](#usecase) 
5. [Video Demo](#demo)  
6. [Sequence Diagram](#seq) 
7. [Architecture](#arch) 
8. [Architecture & Deployement Decisions](#arch-deploy-des)
9. [Set Up](#setup)  
10. [Get IPv4 Address](#ipv4)  
11. [Set Up Django Backend](#back)  
12. [Set Up React Frontend](#front)  
13. [API Usage](#api)  
14. [Test Cases](#test) 

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

## [Video Demo](https://photos.app.goo.gl/kPCUTtyuuAzvgX7WA) <a name="demo"></a>

## Sequence Diagram <a name="seq"></a>
![Sequence Diagram](https://user-images.githubusercontent.com/30815527/146114710-ca03374f-0959-401f-b283-9dd891e30634.png)

## Architecture <a name="arch"></a>
![Architecture IoT](https://user-images.githubusercontent.com/30815527/144935475-1a68c642-83c5-45c6-9da5-694828a5c8aa.png)

## Architecture & Deployement Decisions <a name="arch-deploy-des"></a>
- Django was chosen as the server framework because it was easy to set up and easy to deploy. It also has an ORM which makes working with the database easy
- Database was chosen as SQLite because it is lightweight, comes pre-built into Djano, and I wanted it to be local to each user.
- Frontend was chosen as React because it has states and is very quick to build a UI and has many graphing UI libraries
- Digital Ocean's Web app was chosen as the cloud service because it has auto-security features, auto-deploy, auto-routing, domain routing and free domain service. It also auto-configures the web application for you.   
- Another reason I didn't use the droplet was because I ran out of time due to my other group projects and I had a lot of trouble trying to get the example from class to work. I had issues with node-red and I had to actaully restart the droplet application 3 separate times because I'd run into security set up issuesn networking issues, or library deprecation issues. I spent like 5-6h a day for 5 days trying to get it working before I ultimately gave up because I had to focus my time on the rest of the project
- Frontend was not run on cloud because that would mean running another cloud instance for it but it can connect perfectly fine to the cloud instance.
- Sensors connected with Http instead of mqtt because connects to cloud easier and easier to secure. I managed to get the sensors to use https to connect to the cloud. 
- I didn't use batteries upon hearing how the nodeMcu fries and drains the battery too fast from the other groups. 

## Set up <a name="setup"></a>
To use the cloud instance, skip to the [Frontend](#front) and just do `npm install` & `npm run start` and don't change the proxy or api address.
The cloud instance of the api can be found at https://plantpal-whv3b.ondigitalocean.app/
1. Clone the repo
### 2. Get your ipv4 address <a name="ipv4"></a>
#### Windows
1. Open command prompt and enter `ipconfig`
2. Look for the wifi ipv4 address and copy it
#### Linux
1. Open terminal and enter `ifconfig`
2. Look for the wifi ipv4 address and copy it

### 3. Set Up Backend Locally <a name="back"></a>
1. Open the `IoTAssignment2Back/` in VS code
2. Make a python virtual env (I used python 3.6) using these steps: https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial
3. Install the requirements with `pip install -r requirements.txt` into the virtual env
4. Open the `settings.py` file
5. In the `ALLOWED_HOSTS` (`line28`) add your ipv4 address
6. Migrate the database with `python manage.py migrate`
7. Run the server with `python manage.py runserver your_ip_addr:8000` 
8. To run the test use `python managae.py test`

### 4. [Set Up Frontend Locally](https://github.com/cassidylinhares/iotProjectWebFront#setup-) <a name="front"></a>

### 5. Set Up IoT Sensor To Cloud <a name="sensor"></a>
https://github.com/cassidylinhares/iotProjectSensor
**Note:** The sensor connects to the cloud service. I didn't upload the code to make it run locally but a tutorial for this can be found here: https://randomnerdtutorials.com/esp8266-nodemcu-http-get-post-arduino/

## API Usagae & Implementation <a name="api"></a>
### `GET /getPlants`
Gets all the options for types of plants to pick from
### `GET /changePlantType/plantId/plantType`
Tells the server to set the ideal moisture for said meter id to be the plant type specified
### `GET /getMoistureLevels/plantId`
Gets all the moisture levels, meter ids, plant types, the timestamp created, and ids for a specific moisture meter
### `GET /getMoistureLevel/plantId/`
Gets a moisture level by moisture meter id. Possible values are ['plant1', 'plant2']. Returns the id, meter id, plant type, moisture level, and timestamp from when it was read
### `POST /insertMoistureLevel`
Inserts moisture level. This is currently inserted every 1 min but the moisture sensor through IoT Post request. The sensor reads the values at that moment and then makes a POST request with application/json content type, the server receives these values and inserts them into the database. The id, timestamp and plant type are auto generated and do not need to be inserted by the device or user
### `PUT updateMoistureLevel/id/`
Updates the moisture level using an existing id. The only thing that can be changed is the moisture level. Returns the id, meter id, plant type, timestamp, and updated moisture level
### `DELETE deleteMoistureLevel/id/`
Deletes a moisture level by id

## Test Cases <a name="test"></a>
The test cases can be found [here](https://github.com/cassidylinhares/iotProject/tree/main/apiAssignment2/tests)   
There are multiple unit test done for 3 separate parts of the backend. It test the models, urls, and api call functions/views
   **To run test cases enter in the terminal: `python manage.py test`**
### Models
This tests the model used by django and SQLite. It test that it can create an object and asserts the entry created exist
### URLs
This tests that the urls can be reached and the correct function gets called. *Please note that not all the urls are tested or properly updated since I ran out of time*
### Views
This tests that the function called by the url returns the right status code and the correct data if anything should be returned. *Please note that not all the views are tested or updated since I ran out of time*
