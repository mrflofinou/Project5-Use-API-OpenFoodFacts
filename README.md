# Use public data of OpenFoodFacts

This app will help you to choose a healthier food for you.  
Based on the database of OpenFoodFacts, this app use products we can buy in France.

## Find a substitute of a product
This app displays the differents categories of food products we can find in France.   
You can choose a category to display the products of this category.  
When the products are displayed, you can choose one of them to find a substitute healthier.  
If you want, you can save a substitute in the database to see it later.

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

## How to use this app
This app is very easy to use. The app is a cosole display program.  
When you launch the app you have a home menu with three choices:  
 * home menu:
   * 1 - Quel aliment souhaitez-vous remplacer ?
   * 2 - Retrouver mes aliments substitués
   * 3 - Quitter  

To select an option, you must enter the number with the keyboard.

#### 1 - Quel aliment souhaitez-vous remplacer ?
This choice will display the differents categories of food products from the database.  
Choose a category to display every products of the category selected.  
More, choose a product to display five substitues healthier of it.  
To the end you can select the substitute you want to save.  

#### 2 - Retrouver mes aliments substitués
Display the substitues you had saved.

#### 3 - Quitter
To close the app.

## Author
Florian LESCUYER - [mrflofinou](https://github.com/mrflofinou)
