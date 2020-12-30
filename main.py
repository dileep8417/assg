import time
import os
import json 
# Custom modules
from datastore.utils import Utils  
from datastore.CRD import CRD


# Must needed operations to initialise the File Database

# Instantiating Utils class to access the methods in it
utils = Utils()

# Getting database configuration data
CONFIGURATION = utils.get_configuration_data()

# Creates database if not created
utils.initial_setup(CONFIGURATION)

# Terminates the application if it is already running
utils.stop_if_running(CONFIGURATION)


# Database details
DB_PATH = CONFIGURATION["DatabasePath"]
file_data = utils.get_file_db_data(DB_PATH)

#############################################

############ Demo CRD Operations ################
# Instantiating CRD class for create, read, delete operations
database = CRD(DB_PATH,file_data)

# TO create the key-value pair
#
# Without time to live value
database.create("user1",{"name":"Dileep","age":21})
database.create("user2",{"name":"Will be deleted"})
#
# With time to live value
database.create("user3",{"companyName":"Freshworks","location":"Chennai"}, 300)  # Expires after 300 seconds


# Reading value using key
# Returns JSON object if exists
database.read("user1")


# Deletes the key if exists
database.delete("user2")
database.delete("not-in-data")

# Updating the settings when user terminating the application
print()
input("Press a key to exit the application")
# Update configuaration settings
CONFIGURATION["RunningStatus"] = False
utils.write_data("config-db.json",CONFIGURATION)
print("Bye...")

