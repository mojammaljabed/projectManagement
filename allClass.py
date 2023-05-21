class projectClass:
    project_name=""
    description=""
    start_date=""
    end_date=""
    status=0

    def __init__(self,project_name,description,start_date,end_date,status):
        self.project_name=project_name
        self.description=description
        self.start_date=start_date
        self.end_date=end_date
        self.status=status
    
    def getProjectName(self):
        return self.project_name
    def getDescription(self):
        return self.description
    def getStartDate(self):
        return self.start_date
    def getEndDate(self):
        return self.end_date
    def getStatus(self):
        return self.status
    
class taskClass:
    task_title=""
    description=""
    estimated_time=""
    start_date=""
    end_date=""
    project_id=0

    def __init__(self,task_title,description,estimated_time,start_date,end_date,project_id):
        self.task_title=task_title
        self.description=description
        self.estimated_time=estimated_time
        self.start_date=start_date
        self.end_date=end_date
        self.project_id=project_id
        
    def getTaskTitle(self):
        return self.task_title
    def getDescription(self):
        return self.description
    def getEstimatedTime(self):
        return self.estimated_time
    def getStartDate(self):
        return self.start_date
    def getEndDate(self):
        return self.end_date
    def getProjectId(self):
        return self.project_id
    

class developerClass:
    developer_name=""
    address=""
    email=""
    status=0
    project_id=0
    task_id=0

    def __init__(self,developer_name,address,email,status,project_id,task_id):
        self.developer_name=developer_name
        self.address=address
        self.email=email
        self.status=status
        self.project_id=project_id
        self.task_id=task_id

    def getDeveloperName(self):
        return self.developer_name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getStatus(self):
        return self.status
    def getProjectId(self):
        return self.project_id
    def getTaskId(self):
        return self.task_id