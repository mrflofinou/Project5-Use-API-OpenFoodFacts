# Use public data of OpenFoodFacts

This app will help you to choose a healthier food for you.  
Based on the database of OpenFoodFacts, this app use products we can buy in France.

## Find a substitute of a product
This app displays the differents categories of food products we can find in France.   
You can choose a category to display the products of this category.  
When the products are displayed, you can choose one of them to find a substitute healthier.  
If you want, you can save a substitute in the database to see it later.

## How to use this app


## What do you need ?
To use this app you need:  
  * [Python3.5 or more](https://www.python.org/downloads/)
  * [MySQL](https://dev.mysql.com/downloads/mysql/)
  * A python virtual environment like, for exemple, [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

## Install
 * Install python 3.5 or more  
  `sudo apt-get install python3`  
    
 * Install MySQL: Install the .db file from [MySQL](https://dev.mysql.com/downloads/mysql/)  

 * Install the virtual environment  
  `[sudo] pip install virtualenv`  
    
 * Create a virtual environment  
  `virtualenv -p python3 env`  
    
 * Activate your virtual environment (in the current folder)  
  `source env/bin/activate`  
    
 * Download dependencies  
  `pip install -r requirements.txt`  
   
 * In MySQL create the database  
  `CREATE DATABASE openfoodfacts CHARACTER SET 'utf8';`
   
 * In the file 'settings.py' modify the connection parameters of your MySQL account  
   
 * To launch the app  
  `python3 openfoodfacts.py`

## Author
Florian LESCUYER - [mrflofinou](https://github.com/mrflofinou)
