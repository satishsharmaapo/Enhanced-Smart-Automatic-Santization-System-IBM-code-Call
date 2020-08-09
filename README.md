# Enhanced-Smart-Automatic-Santization-System-IBM-code-Call

#1. Introduction
With the evolution of perspicacious technologies and every indispensability of mankind moving towards automation, there emerged anurge to devise an automatic sanitizing system that would be perspicacious enough to sanitized the human extensively and specially to the public places like police station,courts,Hospitals,schools,colleges,zoo,parks,convey system like trains ,busses, auto etc. As Convivial distancing without total shutdowns is unthinkable, especially in the astronomically immense cities with crowded streets, trains, buses and offices. Cough hygiene is largely absent. Hand hygiene is equipollently suspect. The latest data from the regime National sample survey organization verbalize that only 36% of Indians wash their hands with soap afore a repast.

1. Even more distressingly, 160 million Indians do not have access to clean water to wash their hands.
2. The research suggests that diabetes and hypertension worsen COVID-19 outcomes: the prevalence among Indian adults of diabetes and hypertension is 10% and 25%, respectively.The smart automatic sanitizer system which would consist of nozzle systems, Passive Infrared and Infrared sensors, air compressors, microcontrollers, Liquid Crystal Display. 
When a person enters the chamber, the PIR sensors located at opposite corners of the chamber will detect the movement of the person and thereby will get activated. The LCD fitted outside the sanitizing chamber will display a relevant message such as ‘occupied’. If the person uses the sanitizer Chamber, the IR sensor will be deactivated (which was initially activated) and remain deactivated till the person is in chamber. from the sanitizing chamber, once the person comes out, the sanitizing chamber will off automatically by the mean of PIR sensor , and relay R1 get reset automatically for next person. When the person leaves the sanitizing chamber, the PIR sensor will be deactivated and the number of person count will be updated. the Sanitizing chamber will accompanied process will begin with the release of pressurized water through nozzles as controlled by relay R1. R2 relay is for future enhanced version of Smart Automatic Sanitizing System for detection of infected COVID people having ,cough and sneezes with high body temperature using camera and python language so that immediate remedies /action for the care could be taken to restrict communal threat.

Table 1:  List of relays


Relay Number	Purpose	Time (in seconds)
R1	Sanitizing	10
R2	Camera	Auto(active)
 	 	 


#Enhanced Smart Automatic Santization System ( COVID 19)
1. basicimage.py is a pure python file which is using opencv-python file and it is very important part to train data set .
2. Hackthon.py is second file which is responsible for face detection and getting detect the image and marked as duration of entrance.

Basically this project have :
•	Passive Infrared Sensor (PIR): A PIR sensor is an electronic sensor that is most often used to detect motion of anything. PIR sensors are commonly used in security alarms and automatic lighting applications. PIR sensors can detect general movement, but cannot specify whether who or what moved. It is used in some security alarm systems to detect motion of an infrared emitting source, usually a human body. 
•	Infrared Sensor (IR): An IR sensor is an electronic device that measures and detects infrared radiation in its surrounding environment. There are two types of infrared sensors: active and passive. They are mostly used in obstacle detection systems (such as in robots).

•	Microcontroller: A microcontroller is a compact integrated circuit designed to perform a specific operation in an embedded system. A typical microcontroller includes a processor, memory and input/output (I/O) peripherals on a single chip. A microcontroller is embedded inside a system to control a singular function in a device. 

•	Relay: A relay is “an electromagnetic device for remote or automatic control that is actuated by variation in conditions of an electric circuit and that operates in turn other devices (such as switches) in the same or a different circuit.” A relay is basically used to control the sequence and the timings of a microcontroller for specific purposes.
•	Software Requirement : 
	Language : C Language as base code for Program for hardware.
	Langauge : Python For future Implementation and  Enhancement .

