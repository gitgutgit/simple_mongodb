# simple_mongodb

simple_mongodb_guideline for project

# Setting

pip or conda both works! (but recommend to make new virtual environment)

conda create -n myenv ... like this (recommended)

conda install pymongo

===================for cloud version=====
conda install toml

must need to create secrets.toml files on same directory (if you want to change the toml files ,then also need to change the .gitignore)

(!!in secrets.toml only one line space between each line)

below is content of secrets.toml

[database]

url = "URLURLLLLLL"

# explanation

example_data_put_local and retrive_from_data_local <- for testing on local machine

example_data_put and retrive_from_data<- for server

please change the database name and collection name in the code as per your requirement

!! If error likes "ID already exists" then please change the ID name in the code or use other collection
