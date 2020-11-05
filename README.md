# SOAD_Project  PackUrBags


[![Build Status](https://travis-ci.com/vitthal-inani/SOAD_Project.svg?branch=master)](https://travis-ci.com/github/vitthal-inani/SOAD_Project)

## Cloning the project  
* Run command `https://github.com/vitthal-inani/SOAD_Project.git` and change into the project folder
* Create a virtual environment `env` in the repository (use virtualenv, etc)
* Install the requirements
* Activate virtual environment

To create virtual environment and install requirements run following commands
```shell script
virtualenv env
pip install -r requirements.txt
```

To activate the environment use following commands:
Window: 
```shell script
.\env\Scripts\activate
```
Ubuntu/Linux
```shell script
source env/bin/activate
```

## Making a new branch
```bash
git checkout -b <branch-name>
```
branch-name : can be your name 

For Pushing Changes
```bash
git push -u origin <branch-name>
```


## Version Control Workflow
> After making any changes, follow these steps before pushing to the repo.
1. git add .
2. git commit -m "commit msg"
3. git pull
4. git push
