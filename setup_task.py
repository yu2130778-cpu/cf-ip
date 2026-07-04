import win32com.client
import datetime
import os

python_exe = "C:\Program Files\Python312\pythonw.exe"
script_path = "D:\cfnb\main.py"
work_dir = "D:\cfnb"

svc = win32com.client.Dispatch("Schedule.Service")
svc.Connect()
root = svc.GetFolder("\\")

try:
    root.DeleteTask("CloudflareIPPreferred", 0)
except:
    pass

task_def = svc.NewTask(0)
reg_info = task_def.RegistrationInfo
reg_info.Description = "Cloudflare IP Preferred Tool"

principal = task_def.Principal
principal.LogonType = 5
principal.RunLevel = 1

settings = task_def.Settings
settings.Enabled = True
settings.StartWhenAvailable = False
settings.AllowHardTerminate = True
settings.ExecutionTimeLimit = "PT72H"
settings.MultipleInstances = 3
settings.Priority = 0
settings.DisallowStartIfOnBatteries = False
settings.StopIfGoingOnBatteries = False

trigger = task_def.Triggers.Create(1)
trigger.StartBoundary = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
trigger.Repetition.Interval = "PT5M"
trigger.Repetition.StopAtDurationEnd = False
trigger.Enabled = True

action = task_def.Actions.Create(0)
action.Path = python_exe
action.Arguments = script_path
action.WorkingDirectory = work_dir

root.RegisterTaskDefinition(
    "CloudflareIPPreferred",
    task_def,
    6,
    "SYSTEM",
    None,
    5
)

print("SUCCESS: Task 'CloudflareIPPreferred' created!")
print(f"Python: {python_exe}")
print(f"Script: {script_path}")
print(f"WorkingDir: {work_dir}")
print(f"Interval: Every 5 minutes")
