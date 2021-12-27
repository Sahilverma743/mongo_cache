# mongo_cache
This is a sample(basic level) mongo cache using Sqlite and mongo cloud

# Pre-requirements
1. Python3.8 or higher.
2. account on mongo cloud.
3. Flask. 

# initial setup (For macintosh) 

Please follow the following steps to complete the install and run the system.

## create a virtual environment 
```
virtualenv env
```

## activate the virtual environment and install the requirements
```
source venv/bin/activate
cd src
pip3 install -r requirements.txt
```

## Create the initial Sqlite Database(Act a cache)
```
python3 initial_script.py
```


## Start the Flask Server
```
python3 run_server.py
```
