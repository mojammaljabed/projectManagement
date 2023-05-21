#************************Connection setup********************
import mysql.connector
from allClass import projectClass 
from allClass import taskClass 
from allClass import developerClass

con=mysql.connector.connect(host='localhost',user='root',password='123456', database="pmanagement")
try:
    print(con.connection_id)
except:
    print("Connection Failure")


#********************Create project function**************
def create_project(project):
    q1="insert into project(projectname,description,startDate,endDate,status) values(%s, %s, %s, %s, %s)"
    rec=(project.getProjectName(),project.getDescription(),project.getStartDate(),project.getEndDate(),project.getStatus())
    curobj.execute(q1,rec)
    con.commit()

#********************Create Task function**************
def create_task(task):
    
    q1="insert into task(Title,description,EstimatedHour,startDate,endDate,projectid) values(%s, %s, %s, %s, %s, %s)"
    rec1=(task.getTaskTitle(),task.getDescription(),task.getEstimatedTime(),task.getStartDate(),task.getEndDate(),task.getProjectId())
    curobj.execute(q1,rec1)
    con.commit()

#********************Create Developer function**************
def create_developer(developer):
    
    q1="insert into developer(Developername,address,email,status,projectid,taskid) values(%s, %s, %s, %s, %s, %s)"
    rec1=(developer.getDeveloperName(),developer.getAddress(),developer.getEmail(),developer.getStatus(),developer.getProjectId(),developer.getTaskId())
    curobj.execute(q1,rec1)
    con.commit()

#********************Print project table***************
def print_table(tName):
    q4="select * from "+tName
    curobj.execute(q4)
    res=curobj.fetchall()
    for val in res:
        print(val)

#*********************Project details**************
def project_details():
    projectid=input("Enter the project ID: ")
    q4="select projectname from project where projectid="+projectid
    curobj.execute(q4)
    res=curobj.fetchall()
    print("\nThe project name is: "+res[0][0])

    q5="select task.Title, developer.Developername from task,developer where task.projectid="+projectid+" and developer.projectid="+projectid+" and task.taskid=developer.taskid"
    curobj.execute(q5)
    res=curobj.fetchall()
    for val in res:
        print('''The task name is: "'''+val[0]+'''" And the developer is: '''+val[1])



#*************************Instatiation of Cursor object*******
curobj = con.cursor()


#************************Option selection and user input part ***************
while 1:
    print("Select an Option\n1. Create Project\n2. Create Task\n3. Create Developer\n4. Print the project table\n5. print the task table\n6. print the developer table\n7. See a project with all its tasks and associated developers.\n0. For Exit")
    userInput=int(input())
    if userInput==1:
        print("You selected to create new project")
        project_name=input("Enter the project name: ")
        description=input("Enter the Description: ")
        start_date=input("Enter the start date in the formate YYYY-MM-DD HH:MM:SS: ")
        end_date=input("Enter the end date in the formate YYYY-MM-DD HH:MM:SS: ")
        status=int(input("Enter the status: "))
        project=projectClass(project_name,description,start_date,end_date,status)
        create_project(project)
    elif userInput==2:
        print("You selected to create new Task")
        task_title=input("Enter the task Title: ")
        description=input("Enter the Description: ")
        estimated_time=input("Enter Estimated time: ")
        start_date=input("Enter the start date in the formate YYYY-MM-DD HH:MM:SS: ")
        end_date=input("Enter the end date in the formate YYYY-MM-DD HH:MM:SS: ")
        project_id=int(input("Enter the project id: "))

        task=taskClass(task_title,description,estimated_time,start_date,end_date,project_id)
        create_task(task)

    elif userInput==3:
        print("You selected to create new Develoloper")

        developer_name=input("Enter the developer Name: ")
        address=input("Enter the Address: ")
        email=input("Enter email address: ")
        status=int(input("Enter the status: "))
        project_id=int(input("Enter the project id: "))
        task_id=int(input("Enter the task id: "))

        developer=developerClass(developer_name,address,email,status,project_id,task_id)

        create_developer(developer)
    elif userInput==4:
        print("You select print project table")
        print_table("project")
    elif userInput==5:
        print("You select print task table")
        print_table("task")
    elif userInput==6:
        print("You select print developer table")
        print_table("developer")
    elif userInput==7:
        print("You select project with all its tasks and associated developers")
        project_details()
    elif userInput==0:
        break
    else:
        print("Please Enter a Number from the list")

        

