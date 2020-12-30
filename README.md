# File based key-value data store
## About the application
A file-based key-value data store that supports the basic CRD (create, read, and delete) operations.
This data store is meant to be used as a local storage for one single process on one laptop. 
### Note:
`Add CRD.py, utils.py, config-db.json files to your project for integrating the database`
## File structure
#### CRD.py
   Contains create, read, delete methods.
#### utils.py
   Contains methods for handling file database.
#### main.py
   This file is to initialise and run the application.
#### config-db.json
   Contains JSON data for file database configuration.
#### filedb.json
   This file will be created after initialising the application. It is used to store the data.
## Languages used
  Python
## About the CRD (create,read,delete) operations
#### create(key, value, time_to_live)
  key[type = String], 
  value[type = Dictionary], 
  time_to_live[type = Integer] (Optional)
#### read(key)
#### delete(key)
## Running the application
1. Add the files to a directory in the local machine
2. Open that directory in `CMD` and run `python main.py` for initializing and running the application
