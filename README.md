# About
The main objective of this project is to create an instance of tor expert that can<br>
be used in the same way as the tor browser.

# Installation
Most important thing is that you have python 3 installed on your machine. 

**Deploy virtual environment for your project**<br>
Install virtualenv library if you didn't already.```pip3.7 install virtualenv```
For this project, I'm using Python 3.7 if you have any other python 3 versions <br>
be sure to change the version number on pip. 
Then create virtual environment ```py -3.7 -m virtualenv Envs/myproject``` <br>
In most cases on WinOS it will be created on path ```C:\Users\YourUsername\Envs```<br>

**Activate virtual environment for your project**<br>
Activate by simply calling this command ```C:\Users\YourUsername\Envs\myproject\Scripts\activate.bat``` from command prompt.

**Installing tor_expert library**<br>
```pip install tor-expert``` 

# Usage
**Usage example in Pycharm**<br>
- open Pycharm and start a new project and name it however you want
- select existing interpreter and then browse to ```C:\Users\YourUsername\Envs\myproject\Scripts\python```
- now in the new project create a new python file
- import tor_expert ```from tor_expert import tor, settings```
- then we need to install tor expert this is only done once or if you want to reinstall it. To do this we need to write the following line ```tor.install()```
- by default tor expert directory will be installed ```C:\Users\YourUsername\Documents\Tor```
- now you are ready to crawl data, check crawler_example.py to see an example of usage.