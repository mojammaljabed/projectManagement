#************************Connection setup********************
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='123456', database='pmanagement')
try:
    print(con.connection_id)
except:
    print("Connection Failure")


#*************************Instatiation of Cursor object*******
curobj = con.cursor()

#*************************Creat Operation*********************
#Create database
#q1="create database pmanagement"
#curobj.execute(q1)

#Table Creation
#q2= 'create table Project(projectid int not null auto_increment primary key, projectname varchar(20), description varchar(50),startDate datetime,endDate datetime,status integer(4))'
#q2= 'create table task(taskid int not null auto_increment primary key, Title varchar(20), description varchar(50),EstimatedHour datetime,startDate datetime,endDate datetime,projectid int,FOREIGN KEY (projectid) REFERENCES project(projectid))'
q2= 'create table developer(developerid int not null auto_increment primary key, Developername varchar(20), address varchar(50),email varchar(20),status int,projectid int,taskid int,FOREIGN KEY (projectid) REFERENCES project(projectid),FOREIGN KEY (taskid) REFERENCES task(taskid))'

curobj.execute(q2)
