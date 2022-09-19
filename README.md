# Live-database-temperature

This is simple temperature reading app, using sqlite  to show data in web browser. First python reads serial, sends the data to sqlite , then reads it from sqlite into json file, and webpage picks the rest. 
video: 


### How I started:

* Make code for microbit, basic serial connection, sending only temperature.
* test connection with external device with minicom program in ubuntu.
* made database with sqlite browser in ubuntu.
* Python program that connects and sends nonstop data into sqlite. Can be seen directly from sqlite browser.
* Python reads the data back from sqlite, and writes it into json file.
* Html reads the json file in loop, and updates that into browser page. 


* script file (.py) must be in gci folder and executable
* file permissions are important


### Executing program

* Ubuntu 
* Apache2
* Ajax
* Json
* Python
* minicom useful to test serial connection
