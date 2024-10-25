import os
import time
import shutil
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(step_time=0.5, duration=20):
    print(Fore.CYAN + "Building", end="")
    for _ in range(duration):
        time.sleep(step_time)
        print(".", end="", flush=True)
    print(Style.RESET_ALL + "\n")

def ask_with_animation(question, options):
    print(Fore.YELLOW + question)
    for idx, option in enumerate(options, start=1):
        print(f"{Fore.GREEN}{idx}: {option}")
    choice = input(Fore.WHITE + "Select an option: ")
    return choice

def get_ip_and_port():
    choice = ask_with_animation("Are you hacking over the internet or locally?", ["Over the Internet", "At Local Network"])
    
    if choice == "1":
        public_ip = input("Enter a public IP: ")
        public_port = input("Enter a port for the public IP: ")
    elif choice == "2":
        private_ip = input("Enter a private IP: ")
        private_port = input("Enter a port for the private IP: ")
    else:
        print(Fore.RED + "Invalid option.")
        return None

    return choice

def merge_apk():
    choice = ask_with_animation("Do you want to merge an APK?", ["Yes", "No"])
    if choice == "1":
        apk_name = input("Enter the APK name (with extension): ")
        if os.path.exists(apk_name):
            print(Fore.GREEN + "APK found. Proceeding...")
            return apk_name
        else:
            print(Fore.RED + "No application found with that name.")
            return None
    elif choice == "2":
        print(Fore.YELLOW + "Skipping APK merge.")
        return None

def create_fake_apk(original_apk):
    time.sleep(2)
    print(Fore.CYAN + "Creating fake APK...")
    time.sleep(20)  # Simulate processing time
    new_apk_name = f"ready{os.path.splitext(original_apk)[1]}"
    
    shutil.move(original_apk, "deleted_apk_backup")  # Backup the deleted APK
    shutil.copy("example.apk", new_apk_name)  # Replace "example.apk" with the actual APK to copy
    print(Fore.GREEN + f"Application created: {new_apk_name}")
    
    return new_apk_name

def fake_listener_animation():
    print(Fore.CYAN + "Starting listener...")
    time.sleep(3)
    print(Fore.CYAN + "Checking for payload installation...")
    time.sleep(3)

def run_fake_application(apk_name):
    print(Fore.CYAN + "Launching application...")
    time.sleep(3)
    
    # Simulating opening in a new terminal tab
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'echo "Running {apk_name}"; sleep 10; echo "Finished running {apk_name}"; exec bash'])
    
    print(Fore.CYAN + "Connecting to server...")
    time.sleep(3)
    print(Fore.CYAN + "Client is running...")
    
    # Simulating fluctuating connection
    for _ in range(5):
        time.sleep(5)
        print(Fore.YELLOW + "Fluctuating connection...")
    
    print(Fore.RED + "Your network is weak. Sorry!")

if __name__ == "__main__":
    clear_screen()
    ip_and_port_choice = get_ip_and_port()
    if ip_and_port_choice:
        original_apk = merge_apk()
        new_apk = None
        
        if original_apk:
            loading_animation()
            new_apk = create_fake_apk(original_apk)
        
        time.sleep(3)  # Wait before asking to run
        run_app = ask_with_animation("Do you want to run the application?", ["Yes", "No"])
        
        if run_app == "1":
            fake_listener_animation()
            payload_installed = ask_with_animation("Have you installed or run the payload?", ["Yes", "No"])
            if payload_installed == "1":
                run_fake_application(new_apk)
            else:
                print(Fore.YELLOW + "Okay, please run the payload.")
                fake_listener_animation()
                payload_installed_again = ask_with_animation("Have you installed or run the payload?", ["Yes", "No"])
                if payload_installed_again == "1":
                    run_fake_application(new_apk)
