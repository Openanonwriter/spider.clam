# Spider-Clam

**This is a work in progress and not operational**

I want to to start a web UI for ClamAV, or at least get the ball rolling.

This is a frontend for clamscan and freshclam on linux using flask, python, html, and css. This my ultimatly change.  

What does the project do?

 - At the moment you can run a full scan on your system, and update fresh clams. 

![alt text](https://github.com/Openanonwriter/spider.clam/blob/master/concpet%231.png)

How does this project work?

 - Currently there is a python 3 flask server running, hosting a website which does form html/flask calls, that then run the command associated with them on the termianl so you dont have to... 

 ## Create a user called spiderweb and add them to sudoers

Create a user 
 ```
 sudo adduser --system --no-create-home spiderweb
 ```
 Add the user to sudoers file
 ```
 sudo usermod -aG sudo spiderweb
 ```
 Run the command to edit the sudoers file
 ```
 sudo visudo
 ```
 Add this line to the bottom. 

 ``` 
 spiderweb ALL=(ALL) NOPASSWD:/usr/bin/freshclam, /usr/bin/clamscan 
 ```

![alt text](https://github.com/Openanonwriter/spider.clam/blob/master/spiderclam.concept.png)

 - My current goal for this project is to have this project servered in a docker container, and have that docker container running the website and send back commands over ssh to localhost using a key instead of a password, with out any ports exposed outside of system. Their for client can see website, and with sudo we can give only the commands needed for clamav/fresh clam or what have you built in. 

Why the project is useful.
- Most modren antivirus's may it be form a large box company to a scammy AV's have a pretty nice UI. Larger AV's for enterprise have a web interface. I belive clam av could have a Web UI to access which would be great for headless servers with out the need to access the command line.  

How users can get started with the project
-  All users are welcome to help this project come to life. 

Who maintains and contributes to the project
- Me, and who ever can code, and contribute. Come one come all.


Todo
1.) Get layout concept completed
- Get multiple buttons working
2.) Build a docker container
- Container must have no exposed ports execpt ssh and web port for web server.
- Docker container must be under 20MB/s
3.) create script to create user profile build. 
4.) Create spider clam logo
