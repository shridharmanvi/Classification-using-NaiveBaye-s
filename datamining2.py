# to run this file execute the following command:
# python datamining2.py /Users/shridharmanvi/desktop/Projects/Datamining-2

import sys
import operator

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

final_probabilities={}

jfin=[]

check= job_usr.keys()

l3= list(set(check)&set(j2))#Taking off the jobs to which the users have not applied at all since the probability of
#users in U2 applying to these jobs will be zero


final = [(-1, -1, -1) for t in range(150)]


#the below is main loop that calculates probabilities of each word and adds up the sum and stores it in final_prob dict
for u in users2:
    for j in l3:
        users_applied=job_usr[j]
        c=0
        s=0
        co=0
        d=0
        ci={}
        st={}
        cou={}
        dt={}
        for x in users_applied:
            city=users[u][1]
            state=users[u][2]
            country=users[u][3]
            degree=users[u][5]
            if(main[x,j][0]==city):c+=1
            else: ci[main[x,j][0]]=1
            if(main[x,j][1]==state):s+=1
            else: st[main[x,j][1]]=1
            if(main[x,j][1]==country):co+=1
            else: st[main[x,j][2]]=1
            if(main[x,j][1]==degree):d+=1
            else: st[main[x,j][3]]=1
        if(len(ci.keys())==0):one=1
        else:one= len(ci.keys())
        if(len(st.keys())==0):two=1
        else:two= len(st.keys())
        if(len(cou.keys())==0):thr=1
        else:thr= len(cou.keys())
        if(len(dt.keys())==0):four=1
        else:four= len(dt.keys())
        su= ((c/one)+(s/two)+(co/thr)+(d/four))
        min_su = min(final)
        if su > min_su[0]:
            min_index = final.index(min_su)
            final[min_index] = (su, u, j)
        #final = sorted(final, key=lambda y: y[2], reverse=True)[:150]
        #final_probabilities[u,j]=su



#print 'Probabilities calculation complete!! Finding top 150 values'


#x=sorted(final_probabilities.items(), key=operator.itemgetter(1), reverse=True)[:150]


print sorted(final, reverse=True)[:150]
