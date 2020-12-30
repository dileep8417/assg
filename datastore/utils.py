import json
import os
import time
import sys

class Utils:
    # To create the database at user mentioned path
    def set_db_path(self,CONFIGURATION):
        print("Enter the absolute(complete) path for storing the data:")
        custom_path = input().strip()
        # Cheking whether custom path exists or not
        if os.path.exists(custom_path) and len(custom_path)>2:
            print("Creating the database file at {}".format(custom_path))
            try:
                # Creating folder for storing database file
                os.mkdir(custom_path+"\db")
                # Creating database file
                custom_path = custom_path+r"\db\filedb.json"
                with open(custom_path,"w") as output:
                    json.dump({"data":{}},output)
            except Exception:
                print("File already exist")
                sys.exit()
            # Updating the Settings
            CONFIGURATION["DatabasePath"] = custom_path
            print("Creating...")
            time.sleep(2)
            print("Database Created")
        else:
            print("Invalid path...")
            return self.set_db_path(CONFIGURATION)


    # To create database at default path
    def set_default_db_path(self,CONFIGURATION):
        print("Creating database file at default path.")
        print("Creating the database file at "+os.getcwd()+r"\db\filedb.json")
        try:
            # Creating the folder at current location for storing database file
            os.mkdir(os.getcwd()+"\db")
            # Creating database file for storing data
            with open(r"db\filedb.json","w") as output:
                json.dump({"data":{}},output)
        except Exception:
            print("File already exist")
            sys.exit()
        # Updating settings
        CONFIGURATION["DatabasePath"] = os.getcwd()+r"\db\filedb.json"
        print("Creating...")
        time.sleep(2)
        print("Database Created")


    # Getting the File Database Configuration data from config.json file
    def get_configuration_data(self):
        # Reading configuration file
        with open("config-db.json") as raw_data:
            return json.load(raw_data)


    # Creates database file if not exist
    def initial_setup(self,CONFIGURATION):
        # Executes the statements if database path is not set in the config-db.json
        if not CONFIGURATION["DatabasePath"]:
            print("Initializing...")
            time.sleep(1)
            print("Hello!")
            choice = input("Do you want to set custom path for the database (Y/N)?")
            choice = choice.upper()
            if choice=="Y" or choice=="YES":
                # Creating database at user specified database
                self.set_db_path(CONFIGURATION)
            else:
                # Create database at default directory
                self.set_default_db_path(CONFIGURATION)
            
            with open("config-db.json","w") as output:
                        json.dump(CONFIGURATION,output)
            

    # Checks whether the application is already running or not
    # Returns boolean value
    def stop_if_running(self,CONFIGURATION):
        # Executes if RunningStatus in Configuration file is False
        if not CONFIGURATION["RunningStatus"]:
            # Update configuaration settings
            # Sets running status to True
            CONFIGURATION["RunningStatus"] = True
            self.write_data("config-db.json",CONFIGURATION)
            return False # Not running parallely
        else:
            print("Application is already running somewhere.")
            choice = input("Do you want to close background process to run this application Y/N :").strip()
            if choice=="Y" or choice=="y":
                # Update configuaration settings
                CONFIGURATION["RunningStatus"] = False
                self.write_data("config-db.json",CONFIGURATION)
                print("Restart the application")
        sys.exit() 
        return True



    # Fetching data from Database File 
    def get_file_db_data(self,DB_PATH):
        with open(DB_PATH) as raw_data:
            return json.load(raw_data)


    # To update the data in the file databse
    def write_data(self,FILE_PATH,data):
        with open(FILE_PATH,"w") as output:
            json.dump(data,output)
        return True


    # Checking whether key exists or not
    def is_key_exist(self,file_db,key):
        if key in file_db["data"].keys():
            return True
        return False
        

    # Checks whether the user entered value is in JSON format or not
    def is_dict(self,value):
        if type(value).__name__=="dict":
            return True
        return False
