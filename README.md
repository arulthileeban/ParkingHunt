# ParkingHunt - Automation with Parking

Finding open parking spots is an issue in the modern day, particularly in cities. To tackle this, JBHunt proposed a problem statement in VTHacks - set up a navigation system for users to get to open parking spots directly. 

We set up a system which uses a CNN Model through security cam feed focused over the parking area to get a list of open parking spots. These are then fed to our Flask API which is used by our android app/ Alexa skill to help navigate the user via GPS to the closest parking spot with the assistance of the Google Maps API.

We created a CNN Model, an Alexa skill, an Android app and a flask API in a span of 36 hours which led us to win the "Best Use of Google cloud" award in VTHacks

## Files
- API - Traditional Flask based API for inputting the security feed, processing and outputting co-ordinates
- Model - Contains the CNN model and the weight save file 
- Data - Contains the dataset
- Alexa Skill - Alexa skill to help navigate to the open spot

## References 

- <a href="https://devpost.com/software/parkinghunt">Devpost</a>

