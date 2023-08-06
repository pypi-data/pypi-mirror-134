import os
import subprocess
import csv
from datetime import datetime
import calendar

TASK_CODECS_HEX = {
    "0x00000000": "The operation completed successfully.",
    "0x00000001": "Incorrect function called or unknown function called.",
    "0x00000002": "File not found.",
    "0x00000010": "The environment is incorrect.",
    "0x00041300": "Task is ready to run at its next scheduled time.",
    "0x00041301": "The task is currently running.",
    "0x00041302": "The task has been disabled.",
    "0x00041303": "The task has not yet run.",
    "0x00041304": "There are no more runs scheduled for this task.",
    "0x00041305": "One or more of the properties that are needed to run this task have not been set.",
    "0x00041306": "The last run of the task was terminated by the user.",
    "0x00041307": "Either the task has no triggers or the existing triggers are disabled or not set.",
    "0x00041308": "Event triggers do not have set run times.",
    "0x80010002": "Call was canceled by the message filter",
    "0x80041309": "A task's trigger is not found.",
    "0x8004130A": "One or more of the properties required to run this task have not been set.",
    "0x8004130B": "There is no running instance of the task.",
    "0x8004130C": "The Task Scheduler service is not installed on this computer.",
    "0x8004130D": "The task object could not be opened.",
    "0x8004130E": "The object is either an invalid task object or is not a task object.",
    "0x8004130F": "No account information could be found in the Task Scheduler security database for the task indicated.",
    "0x80041310": "Unable to establish existence of the account specified.",
    "0x80041311": "Corruption was detected in the Task Scheduler security database",
    "0x80041312": "Task Scheduler security services are available only on Windows NT.",
    "0x80041313": "The task object version is either unsupported or invalid.",
    "0x80041314": "The task has been configured with an unsupported combination of account settings and run time options.",
    "0x80041315": "The Task Scheduler Service is not running.",
    "0x80041316": "The task XML contains an unexpected node.",
    "0x80041317": "The task XML contains an element or attribute from an unexpected namespace.",
    "0x80041318": "The task XML contains a value which is incorrectly formatted or out of range.",
    "0x80041319": "The task XML is missing a required element or attribute.",
    "0x8004131A": "The task XML is malformed.",
    "0x0004131B": "The task is registered, but not all specified triggers will start the task.",
    "0x0004131C": "The task is registered, but may fail to start. Batch logon privilege needs to be enabled for the task principal.",
    "0x8004131D": "The task XML contains too many nodes of the same type.",
    "0x8004131E": "The task cannot be started after the trigger end boundary.",
    "0x8004131F": "An instance of this task is already running.",
    "0x80041320": "The task will not run because the user is not logged on.",
    "0x80041321": "The task image is corrupt or has been tampered with.",
    "0x80041322": "The Task Scheduler service is not available.",
    "0x80041323": "The Task Scheduler service is too busy to handle your request. Please try again later.",
    "0x80041324": "The Task Scheduler service attempted to run the task, but the task did not run due to one of the constraints in the task definition.",
    "0x00041325": "The Task Scheduler service has asked the task to run.",
    "0x80041326": "The task is disabled.",
    "0x80041327": "The task has properties that are not compatible with earlier versions of Windows.",
    "0x80041328": "The task settings do not allow the task to start on demand.",
    "0xC000013A": "The application terminated as a result of a CTRL+C.",
    "0xC0000142": "The application failed to initialize properly."
}

class windows_task_scheduler():
    def __init__(self,task_root_path:str = "\\",temp_path_root:str=f"{os.getcwd()}\\temp\\"):
        '''
        'task_root_path': can't be empty and must end with double backslash
        '''
        self.task_root_path = task_root_path
        self.temp_path_root = temp_path_root

        '''
        Create the path if not exists
        '''
        if not os.path.exists(self.temp_path_root):
            os.mkdir(self.temp_path_root)

    def get_status_desc(self,hexcode:str)->str:
        try:
            desc = TASK_CODECS_HEX[hexcode]
            return desc
        except KeyError:
            return ""

    def run_command(self,cmd):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed

    def get_now_timestamp(self)->dict:
        d = datetime.utcnow()
        unixtime = calendar.timegm(d.utctimetuple())
        return {"int": unixtime, "string": str(unixtime)}

    def get_task_scheduler_status(self)->list:
        '''
        Returns all states of scheduled tasks of windows
        '''
        path = f"'{self.task_root_path}\\*'"
        csv_temp = f"{self.temp_path_root}{self.get_now_timestamp()['string']}_tasks.csv"
        csv_temp_command = csv_temp.replace("\\","/")
        command = f'powershell -command "Get-ScheduledTask -TaskPath {path} | Select-Object TaskName, State, '+"@{Name='LastRunTime'; Expression={(Get-ScheduledTaskInfo $_).LastRunTime}}, @{Name='LastTaskResult'; Expression={(Get-ScheduledTaskInfo $_).lastTaskResult}}, @{Name='LastTaskResultHex'; Expression={'0x{0:X8}' -f (Get-ScheduledTaskInfo $_).lastTaskResult}}, @{Name='NextRunTime'; Expression={(Get-ScheduledTaskInfo $_).NextRunTime}}"+f" | Export-Csv -Path '{csv_temp_command}' -NoTypeInformation -Delimiter ';'"+'"'
        subprocess.call(command, shell=True)
        last_check = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = []
        with open(csv_temp, "r", encoding="utf-8") as csvfile:
            csv_data = csv.reader(csvfile,delimiter=";")
            next(csv_data)
            for d in csv_data:
                alert = True
                if d[4] == "0x00000000":
                    alert = False
                data.append({'task_path': self.task_root_path, 'task_full_path': self.task_root_path+"\\"+d[0],'task_name': d[0], 'state': d[1], 'last_runtime': d[2], 'last_task_result': d[3], 'last_task_result_hex': d[4], 'next_run_time': d[5], 'active_alert': alert, 'result_description': self.get_status_desc(d[4]), 'last_check': last_check})
        os.remove(csv_temp)
        return data

    def enable_task(self,task_path:str):
        '''
        Enables task in task scheduler
        task_path = full path of the task
        '''
        path = f"'{task_path}'"
        command = f'powershell -command "Get-ScheduledTask -TaskPath {path} |enable-ScheduledTask"'
        subprocess.call(command, shell=True)

    def disable_task(self,task_path:str):
        '''
        Disable task in task scheduler
        task_path = full path of the task
        '''
        path = f"'{task_path}'"
        command = f'powershell -command "Get-ScheduledTask -TaskPath {path} |disable-ScheduledTask"'
        subprocess.call(command, shell=True)

    def start_task(self,task_path:str):
        '''
        Enables task in task scheduler
        task_path = full path of the task
        '''
        path = f"'{task_path}'"
        command = f'powershell -command "Get-ScheduledTask -TaskPath {path} |start-ScheduledTask"'
        subprocess.call(command, shell=True)

    def stop_task(self,task_path:str):
        '''
        Stop task in task scheduler
        task_path = full path of the task
        '''
        path = f"'{task_path}'"
        command = f'powershell -command "Get-ScheduledTask -TaskPath {path} |stop-ScheduledTask"'
        subprocess.call(command, shell=True)

    def restart_task(self,task_path:str):
        '''
        Restart task in task scheduler
        task_path = full path of the task
        '''
        self.stop_task(task_path)
        self.start_task(task_path)