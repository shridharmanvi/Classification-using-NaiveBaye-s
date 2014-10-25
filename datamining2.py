import sys

path=sys.argv[1] #input path from the terminal/command prompt

jobs={}
users={}
apps={}
user_history={}
users2={}

jobs_file=path+'/jobs.tsv'
users_file=path+'/users.tsv'
user2_file=path+'/user2.tsv'
user_history_file=path+'/user_history.tsv'
apps_file=path+'/apps.tsv'

#Import files 
with open(jobs_file,'rw') as job:
    for row in job.readlines():
        row= row.split('\t')
        try:
            row[0]=int(row[0])
            jobs[int(row[0])]=row
        except ValueError:
            x=1
            
with open(apps_file,'rw') as app:
    for row in app.readlines():
        row= row.split('\t')
        try:
            row[0]=int(row[0])
            apps[int(row[0])]=row
        except ValueError:
            x=1

with open(user_history_file,'rw') as uhis:
    for row in uhis.readlines():
        row= row.split('\t')
        try:
            row[0]=int(row[0])
            user_history[int(row[0])]=row
        except ValueError:
            x=1
            
with open(users_file,'rw') as user:
    for row in user.readlines():
        row= row.split('\t')
        try:
            row[0]=int(row[0])
            users[int(row[0])]=row
        except ValueError:
            x=1
            
with open(user2_file,'rw') as user2:
    for row in user2.readlines():
        row= row.split('\t')
        try:
            row[0]=int(row[0])
            users2[int(row[0])]=row
        except ValueError:
            x=1