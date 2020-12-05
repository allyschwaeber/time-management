[![](https://travis-ci.com/ancbro/time-management.svg?branch=master)](https://travis-ci.com/ancbro/time-management)
![](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)
![](https://img.shields.io/badge/python-3.8-blue.svg)
[![Slack](https://img.shields.io/badge/Slack-Join-brightgreen)](https://join.slack.com/t/tm-oma8428/shared_invite/zt-iaflzlpt-VSXSI1RkOKko~CT_riBUaA)


# Time Management
Time Management (TM) helps you to keep track of your day-to-day life as a software developer. Using TM you can:

1. Make notes about daily activities
2. Set tasks to be accomplished
3. Print overdue tasks
4. Print the previous workday's activities for Scrum


## Features include:

1. Work history analytics
2. Enhanced database maintenance
3. User configuration

## Usage:

1. Clone this repository locally on your machine
2. Open the time_management directory (/time-management/time_management) in a terminal
3. run main.py

Once you run main.py, something like this should pop up:

                                          
    Good evening <user>. You have 1 overdue items.
    
                                   
    _|      _|    _|_|    _|_|_|    _|_|_|_|  
    _|_|  _|_|  _|    _|  _|    _|  _|        
    _|  _|  _|  _|    _|  _|    _|  _|_|_|    
    _|      _|  _|    _|  _|    _|  _|        
    _|      _|    _|_|    _|_|_|    _|_|_|_|



    1: Time management
    2: Analytics
    3: Maintenance
    4: Quit


## Here's some sample workflow examples to get an understanding of how this works:

1. Make a note
	- Select 1. Time management
	- Select 1. Make a note
	- Enter your note

2. Set a task
	- Select 1. Time management
	- Select 2. Set a task
	- Enter your task, and the number of days to complete
	
			0 to cancel
		
			Set a task: Finish eating ice cream
			Set number of days to complete: 2


3. Get all your notes or tasks
	- Select 1. Time management
	- Select 3. Print notes (select 4. Print Tasks if you want to print your tasks instead)
	(you can similarly print only your overdue notes by selecting the next option)

4. Delete your history
	- Select 3. Maintainence 
	- Select 1. Delete your history, and confirm (deletes all your notes and tasks)
	
			Are you sure you want to delete your history?
			Submit 'y' to drop table
			Submit 'n' to return to maintenance
			y
			
			Deleting history...
			
			
			_|      _|    _|_|    _|_|_|  _|      _|  _|_|_|_|_|
			_|_|  _|_|  _|    _|    _|    _|_|    _|      _|
			_|  _|  _|  _|_|_|_|    _|    _|  _|  _|      _|
			_|      _|  _|    _|    _|    _|    _|_|      _|
			_|      _|  _|    _|  _|_|_|  _|      _|      _|
			
			
			
			0: Return to MODE
			1: Delete history
			2: Quit


