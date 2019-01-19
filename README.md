# iRobot-Alexa-Integration

iRobot provides a experimental robot called **Create2**[1] for developers and enthusiasts. The Create2 bot comes with serial to USB
cable and a docking station. The cable can be used to interact with the bot programatically. On top of it there are sever python
api modules that makes our life easy and simple us the pre-built packages and interact with the bot.

In this project, I would like mount a **Raspberry Pi**[2] on Create2 bot and control the bot using **Amazon Alexa**[3]. The Raspberry Pi will 
act as a proxy between Create2 and Amazon Alexa. This will make the Create2 a voice controlled robot that can also be controlled
through Alexa App.

Project Resources:
- Management Dashboard: https://github.com/bhargav-nunna/iRobot-Alexa-Integration/projects/1
- Wiki: https://github.com/bhargav-nunna/iRobot-Alexa-Integration/wiki

Current Architecture:

![architecture.png](https://github.com/bhargav-nunna/iRobot-Alexa-Integration/blob/master/architecure.png)

References:
- [1]https://www.irobot.com/about-irobot/stem/create-2.aspx
- [2]https://www.raspberrypi.org/
- [3]https://developer.amazon.com/alexa
- [4]https://bitbucket.org/lemoneer/irobot
