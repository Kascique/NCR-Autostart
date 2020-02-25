#NCR Counterpoint auto login

import subprocess
import win32api
import win32com.client

#NCR Counterpoint exe location
counterpoint = 'C:\Program Files (x86)\Radiant Systems\CounterPoint\CPSQL.1 - Station\Bin\CounterPoint.exe'
subprocess.Popen(counterpoint)
#Dispatch shell
shell = win32com.client.Dispatch("WScript.shell")
#wait 6000ms
win32api.Sleep(6000)
#Enter Password
shell.SendKeys("laynes123")
#Press enter key
shell.SendKeys("{ENTER}")
