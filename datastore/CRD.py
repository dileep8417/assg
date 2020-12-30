import json
import os
from time import time
from .utils import Utils    # Contains Custom functions

utils = Utils()

# To perform CRD Operations 
class CRD:
    def __init__(self,DB_PATH,file_db):
        self.DB_PATH = DB_PATH
        self.file_db = file_db
    # To create a new key-value data 
    # Returns boolean value
    def create(self,key,value,timeout=0):
        # Validation
        # Checking database file size
        if self.file_db.__sizeof__()>=1000000000:
            print("Database Storage Error")
            print("Database Out of memory")
            return False
        # Checking Key-Value sizes
        if(len(key)>32 or value.__sizeof__()>16000):
            print("Ooops..Memory Limit Exceeded")
            print("Key cannot exceed 32 characters..")
            print("Value cannot exceed 16KB.")
            return False

        key = key.upper() # Modifying key to UpperCase

        # Checking key is exist or not
        if utils.is_key_exist(self.file_db,key):
            print("Terminating...")
            print("Key with name \"{}\" is already exist in the data store".format(key))
            return False

        # Checking whether the value is in JSON Object [dictionary] format or not
        if not utils.is_dict(value):
            print("Terminating...")
            print("Value must be in JSON format")
            return False

        # Setting the Time to Live value if mentioned
        if timeout>0:
            # Getting current timestamp in seconds and adding the user mentioned seconds
            timeout = int(time()) + timeout 

        # Adding the key and value data 
        self.file_db["data"][key] = [] # Ininitialising an empty array for the given key
        self.file_db["data"][key].append(value) # To store value in JSON array 
        self.file_db["data"][key].append(timeout) # To store the Time To Live value
       
        # Writing data to the JSON file 
        utils.write_data(self.DB_PATH,self.file_db)
        print("Key-Value pair added to the database")
        return True


    # To get the value based on the key
    # Returns JSON Object if key exist
    def read(self,key):
        key  = key.upper() 
        # Checks key exist or not
        if utils.is_key_exist(self.file_db,key):
            # Checks key is expired or not
            current_timestamp = int(time())
            timeout = self.file_db["data"][key][1]
            if timeout!=0 and timeout<current_timestamp:
                print("\"{}\" key is expired.".format(key))
            else:
                print(self.file_db["data"][key][0])
        else:
            print("Key dosen't exist...")

    
    def delete(self,key):
        key = key.upper()
        # Checks key exist or not
        if utils.is_key_exist(self.file_db,key):
            del self.file_db["data"][key]
            # Updates the file database
            utils.write_data(self.DB_PATH,self.file_db)
            print("\"{}\" key is deleted successfully".format(key))
        else:
             print("\"{}\" key dosen't exist".format(key))