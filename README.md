This project contains two parts:
1. A monitor program to periodically measure cpu usage data of a client and send data to server.
2. An APP ENGINE server that collects data and provide simple query functionality

To run this project:

SET UP SERVER
1. Download lastest APP ENGINE SDK for Python https://developers.google.com/appengine/downloads
2. Install SDK and run Google App Engine Launcher
3. File => Add Existing Application
4. Browser to cpumeasure folder
5. Make sure "port" is 8080
6. Click OK
7. In Google App Engine Launcher, choose cpumeasure and click Run

CLIENT PROGRAM
1. Open cpumeasure/monitor folder
2. Run monitor.py, it will collect cpu usage every 5 seconds and send it to the server.
3. Note that the port is hardcoded as 8080 so the server must be running at 8080too.



