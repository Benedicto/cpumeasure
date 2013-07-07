import psutil
import platform
import getpass
import json
import urllib2
import datetime
import sys
#Periodically check cpu usage and send data to server
def main():
    while True:
        #Collect usage data
        payload = {
	    'timeStamp' : str(datetime.datetime.utcnow()),
            'cpu' : psutil.cpu_percent(interval=5),       
            'system' : platform.system(),
            'release' : platform.release(),
            'version' : platform.version(),
            'userName' : getpass.getuser()
        }
        
        #Send data to server
        url = 'http://localhost:8080/cpustore'
        headers = {'content-type': 'application/json'}
        request = urllib2.Request(url, json.dumps(payload), headers)
        response = urllib2.urlopen(request).read()
        print json.dumps(payload)
        sys.stdout.flush()

    
if __name__ == '__main__':
    main()

    