import Adafruit_BBIO.GPIO as GPIO
import time
import urllib2,json
import httplib,urllib
from displaywelcome import display
from displaynonregistereduser import display1
p1='P8_7'
p2='P8_8'
p3='P8_9'
p4='P8_10'
val1='0'
val2='0'
val3='0'
val4='0'
GPIO.setup(p1,GPIO.IN)
GPIO.setup(p2,GPIO.IN)
GPIO.setup(p3,GPIO.IN)
GPIO.setup(p4,GPIO.IN)
key='1'
c_key=''
prev_v1='0'
prev_v2='0'
prev_v3='0'
prev_v4='0'
def native_check_passcode(passcode):
    file=open('native_passcode_base.txt','r+')
    no=0
    while(True):
        print('Checking passcode validity...')
	code=file.readline()
	passcode+='\n'
	if(passcode==code):
	    file.close()
	    print(no)
	    return no 
	    break
	elif(code=='end\n'):
	    file.close()
	    return -999
	    break
	no+=1
def native_check_name(line_no):
    file=open('native_name_base.txt','r+')
    i=0
    while(True):
        n=file.readline()
	print(n)
	if(i==line_no):
	    file.close()
	    print('Found')
	    return n
	    break
def check():
    cc1=0
    '''
    params=urllib.urlencode({'field1':-1,'key':'KEZIHMSS197N0GQ6'})
    header={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
    conn=httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST","/update",params,header)
        response=conn.getresponse()
        print('data uploaded...')
        data=response.read()
        conn.close()
    except:
        print('Failed...')
    '''
    c_key=''
    prev_v1='0'
    prev_v2='0'
    prev_v3='0'
    prev_v4='0'
    print('start...')
    while(True):
	val1=str(GPIO.input(p1))
        val2=str(GPIO.input(p2))
        val3=str(GPIO.input(p3))
        val4=str(GPIO.input(p4))
        if ((prev_v1!=val1 or prev_v2!=val2 or prev_v3!=val3 or prev_v4!=val4) and cc1!=1):
            if(val1=='1'):
                c_key+='1'
                print c_key
            if(val2=='1'):
                c_key+='2'
                print c_key
            if(val3=='1'):
                c_key+='3'
                print c_key
            if(val4=='1'):
                c_key+='4'
                print c_key
            if(len(c_key)==4):
		display('Logging in...',2)
		ccc=native_check_passcode(c_key)
		if(ccc!=-999):
		    print('Passcode valid')
		    nnn='Welcome '+native_check_name(ccc)
		    display1(nnn,4)
		    break
		else:
		    print('Invalid Passcode')
		display1('Not registered on device',5)
		break
		params=urllib.urlencode({'field1':1,'field2':'WB069102','field3':c_key,'field4':'a','key':'KEZIHMSS197N0GQ6'})
	    	header={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
		conn=httplib.HTTPConnection("api.thingspeak.com:80")
		try:
		    conn.request("POST","/update",params,header)
		    response=conn.getresponse()
		    print('data uploaded...')
		    data=response.read()
		    conn.close()
		except:
		    print('Failed...')
		display('Contacting Server...',10)
		conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (304999,'2RG8K9J03JVIZPK0'))
		response=conn.read()
		print ("data recieved...")
		data=json.loads(response)
		name_to_be_displayed=data['field5']
		x=data['field6']
		if(x=='10'):
		    #name_to_be_displayed=c_key
		    if(key==c_key):
		        message='Welcome '+name_to_be_displayed
			print('Success')
                    	return message
                    	break
                    else:
                    	message='Pin not recognised'
			print(message)
                    	return message
                    	break
		else:
		    print('lol wtf')
		    cc1=1
		    continue
	if(cc1==1):
	    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (304999,'2RG8K9J03JVIZPK0'))
            response=conn.read()
            print ("data recieved...")
            data=json.loads(response)
            name_to_be_displayed=data['field5']
            x=data['field6']
            if(x=='10'):
                #name_to_be_displayed=c_key
                if(key==c_key):
                    message='Welcome '+name_to_be_displayed
                    print('Success')
                    return message
                    break
                else:
                    message='Pin not recognised'
                    print(message)
                    return message
                    break
        prev_v1=val1
        prev_v2=val2
        prev_v3=val3
        prev_v4=val4
