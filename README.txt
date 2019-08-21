This project is on docker, it use postgres, redis, django 2, nginx 


to use twillio (to use automatic call on your phone if there are problem) , you have to add on local_settyngs.py on src/panel/local_settings.py
 
TWILIO_PHONE_NUMBER = "your twilio pgone number"
DIAL_NUMBERS = ["number to call",]
TWIML_INSTRUCTIONS_URL = "http://static.fullstackpython.com/phone-calls-python.xml"
TWILLIO_SID ='your TWILLIO SID'
TWILLUIO_AUTHTOKEN = 'your TWILLUIO AUTHTOKEN'



To start :
set your hosts to 127.0.0.1 example.org
docker-compose up --build

it create an superuser 

user:admin
pass:adminpass

go to 
http://example.org/admin/




