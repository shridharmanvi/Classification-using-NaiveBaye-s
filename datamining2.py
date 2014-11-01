# to run this file execute the following command:
# python datamining2.py /Users/shridharmanvi/desktop/Projects/Datamining-2

import sys

path=sys.argv[1] #input path from the terminal/command prompt

jobs={}
users={}
apps={}
user_history={}
users2=[]
j2=[]

jobs_file=path+'/jobs.tsv'
users_file=path+'/users.tsv'
user2_file=path+'/user2.tsv'
user_history_file=path+'/user_history.tsv'
apps_file=path+'/apps.tsv'

#Import files 
job=open(jobs_file,'rw')

for row in job.readlines():
    row= row.split('\t')
    try:
        row[0]=int(row[0])
        jobs[int(row[0])]=row
    except ValueError:
        x=1
 
            
app=open(apps_file,'rw')

for row in app.readlines():
    row= row.split('\t')
    try:
        row[0]=int(row[0])
        row[2]=int(row[2])
        apps[int(row[0]),int(row[2])]=row
    except ValueError:
        x=1


uhis=open(user_history_file,'rw')

for row in uhis.readlines():
    row= row.split('\t')
    try:
        row[0]=int(row[0])
        user_history[int(row[0])]=row
    except ValueError:
        x=1
     
            
user=open(users_file,'rw')

for row in user.readlines():
    row= row.split('\t')
    try:
        row[0]=int(row[0])
        users[int(row[0])]=row
    except ValueError:
        x=1
            
user2=open(user2_file,'rw') #NOTE: There are only 10 users in the file: for testing

for row in user2.readlines():
    users2.append(int(row))
            

print 'Step1:Reading files and storing in inbuilt datastructures complete! .Starting step 2....'

#Buiding J2 (All the jobs whose end date is after 29-04-09)
#j2 will have the jobIds of all the jobs whose end date is greater than '2012-04-09 00:00:00'


for key in jobs.keys():
    date=jobs[key][9] 
    if(date >'2012-04-09 00:00:00'):
        j2.append(int(key))


main={}# the dataset which consists of attributes being considered for probability calculation (ranking documents)

#the main dictionary is populated in the below loop
for u,j in apps.keys():
    k=[users[u][1]]
    k.append(users[u][2])#User City
    k.append(users[u][3])#User State
    k.append(users[u][5])#User Country
    k.append(users[u][6])#User Degree type
    k.append(jobs[j][1])#Job title
    if(users[u][9]<=5): k.append('One')
    elif(users[u][9] >5 <=10):k.append('Two')
    elif(users[u][9] >10 <=15):k.append('Three')
    elif(users[u][9] >15 <=20):k.append('Four')
    elif(users[u][9] >20 <=25):k.append('Five')
    elif(users[u][9] >25 <=30):k.append('Six')
    else: k.append('Seven') #Experience
    main[u,j]= k
#the main dictionary now has user location, education and experience information


job_usr={}#Contains all the users who have applied for each job

#In the below loop, the above created dictionary(job_usr) will be populated
for u,j in apps.keys():
    k=[]
    k.append(u)
    try:
        job_usr[j].extend(k)
    except KeyError:
        job_usr[j]=k
        
        

