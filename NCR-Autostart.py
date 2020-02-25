#NCR Counterpoint auto login

import subprocess
import win32api
import win32com.client

counterpoint = 'C:\Program Files (x86)\Radiant Systems\CounterPoint\CPSQL.1 - Station\Bin\CounterPoint.exe'
subprocess.Popen(counterpoint)
shell = win32com.client.Dispatch("WScript.shell")
win32api.Sleep(6000)
shell.SendKeys("laynes123")
shell.SendKeys("{ENTER}")
