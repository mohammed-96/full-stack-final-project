# Item Catalog
This is the secend project for the Udacity Full Stack Nanodegree. The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.

A user does not need to be logged in in order to read the categories or items uploaded. However, users who created an item are the only users allowed to update or delete the item that they created.

This program uses third-party auth with Google. Some of the technologies used to build this application include Flask, Bootsrap, Jinja2, and SQLite.

## PreRequisites:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. install [Python3](https://www.python.org)
1. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.



## Installation:
Once you get the above software installed, follow the insturctions detailed below:
1. Open Terminal and navigate to the project folders we setup above.
1. run  ``` cd vagrant ```  
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant ```
1. Download or clone this repository, and navigate to it.
1. run ```pip install flask ```
1. run ``` pip install oauth2client ```
1. run  ``` python database.py ``` to set up the database
1. run  ``` python fillDataBase.py ``` to fill the database
1. ``` python app.py```  to run the  application.
1. Open `http://localhost:5000/` 




## Helpful Resources:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. install [Python3](https://www.python.org)
