# Spider-Clam

I want to to start a web UI for ClamAV, or at least get the ball rolling.

This is a frontend for clamscan and freshclam on linux using flask, python, html, and css. This my ultimatly change.  

What does the project do?

 - At the moment you can run a full scan on your system, no other buttons work. 

![alt text](https://github.com/Openanonwriter/spider.clam/blob/master/concpet%231.png)

How does this project work?

 - Currently there is a python 3 flask server running, hosting a website which does form html/flask calls, that then run the command associated with them on the termianl so you dont have to... 

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
3.) Build user profile
- User profile must have only access to only commands needed. Cat, Clamscan, Freshclams.
- Set up sudo to only give access to the three commands above. 
4.) create script to create user profile build. 
5.) Create spider clam logo
