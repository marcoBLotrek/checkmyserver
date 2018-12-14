import socket
import os

from panel.models import *
from twilio.rest import TwilioRestClient
from datetime import date, time, datetime

from panel.local_settings import *

class bcolors:
    HEADER = '\033[94m'
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def checkPort (port,ip):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(2)  
	result = sock.connect_ex((ip, 80))
	if result == 0:
	   return 1
	else:
	   return 0

def ping(ip):
	response = os.system("ping -c 1 " + ip + '> /dev/null')

	#and then check the response...
	if response == 0:
	  return 1
	else:
	  return 0 

def checkIfUp(ip):
	
	res = checkPort (80,ip)  
	return res	   


def checkservers():
    # Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
        # and use the E.164 format, for example: "+12025551234"
        #TWILIO_PHONE_NUMBER = "+390550620681"
        # list of one or more phone numbers to dial, in "+19732644210" format
        #DIAL_NUMBERS = ["+393703443027",]
        # URL location of TwiML instructions for how to handle the phone call
        #TWIML_INSTRUCTIONS_URL = "http://static.fullstackpython.com/phone-calls-python.xml"

        # replace the placeholder values with your Account SID and Auth Token
        # found on the Twilio Console: https://www.twilio.com/console
        client = TwilioRestClient(TWILLIO_SID, TWILLUIO_AUTHTOKEN)
        today=date.today()
        timeNow=datetime.time(datetime.now())
        weekDayNumberNow = today.weekday()
        print('Week number:'+str(weekDayNumberNow))
        print('Time:'+str(timeNow.hour)+':'+str(timeNow.minute)+':'+str(timeNow.second))
        
        timeNowSecond=timeNow.hour*3600+timeNow.minute*60+timeNow.second
        print('Time now in secodn '+str(timeNowSecond))
        servers = Server.objects.all()
        
        PROBLEM=0
        ABILITOCHIAMATA = 0

        for server in servers:
            ip = server.server_address
            print(bcolors.HEADER+'-------------------------')   
            print (bcolors.HEADER+'Server '+ip)
            print(bcolors.HEADER+'-------------------------')

            item = History.objects.create(server=server)    
            item.save()
            for mytime in server.PhoneTime.all():
                for daysweek in mytime.dayOfTheWeek.all():
                    if daysweek.dayIndex == weekDayNumberNow :
                       # print('ok, oggi'+daysweek.dayName+' posso disturbare')
                        fromHourSecond = mytime.from_hour.hour*3600+mytime.from_hour.minute*60+mytime.from_hour.second
                        toHourSecond = mytime.to_hour.hour*3600+mytime.to_hour.minute*60+mytime.to_hour.second
                        #print(mytime.name)
                        #print(mytime.from_hour)
                        #print('->'+str(fromHourSecond))
                        #print(mytime.to_hour)
                        #print('->'+str(toHourSecond))
                        if timeNowSecond >= fromHourSecond and timeNowSecond < toHourSecond :
                            ABILITOCHIAMATA = 1
                        # print('al caso posso chiamare')
            if server.ping_test == 1 :
                try:
                    res = ping(ip)
                    if res == 1 :
                        print(bcolors.OK + ' Server ok on ping test ')
                    else :  
                        print(bcolors.WARNING + ' Server not ok on ping test ')
                        PROBLEM = 1
                except Exception as e:
                    print(bcolors.FAIL + ' cant ping server')
            else :
                print('ping non richiesto') 
            for port in server.ports.all():
                try:
                    res = checkPort (port.name,ip)
                    if res == 1 :
                        print(bcolors.OK +' Server ok on port '+port.name)
                    else :  
                        print(bcolors.WARNING + ' Server not ok on port'+port.name)
                        PROBLEM = 1
                except:
                    print(bcolors.FAIL + ' cant connect on server') 
            
        if PROBLEM == 1  and ABILITOCHIAMATA == 1 :
           
            for number in DIAL_NUMBERS:
                print("Dialing " + number)
                #try:
                #client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")
                #except:
                #    print (bcolors.FAIL +"Can't use twillio")    
                    

        print(bcolors.ENDC+' End Test ')            
                