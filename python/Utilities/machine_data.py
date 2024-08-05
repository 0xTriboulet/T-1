import psutil
from collections import Counter
import csv

def get_running_process_info():
    # List to hold the names and users of all running processes
    process_info = []
    
    # Iterate over all running processes
    for process in psutil.process_iter(['name', 'username']):
        try:
            # Get the name and username of the process
            name = process.info['name']
            username = process.info['username']
            # Append the name and username as a tuple to the list
            process_info.append((name, username))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # If the process has been terminated or access is denied, skip it
            continue

    return process_info

def analyze_processes(process_info):
    # Calculate the total number of processes
    total_processes = len(process_info)
    
    # Calculate the number of processes per user
    user_process_counts = Counter(user for _, user in process_info)
    
    # Calculate the total number of unique users
    total_users = len(user_process_counts)
    
    # Prepare data for CSV output
    data = [
        ["Process Count", total_processes],
        ["Process Count/Users", total_processes/total_users],
        ["User Count", total_users],
        ["Sandbox Score", 0]
    ]
    
    
    # Append user process counts to data
    # data.extend([["None" if not user else "SYSTEM" if "SYSTEM" in user else "User", count] for user, count in user_process_counts.items()])

    headers = []
    row = []
    
    # Print formatted results
    for item in data:
        headers.append(item[0])
        row.append(item[1])
        print(f"{item[0]}: {item[1]}")
    
    print(headers)
    print(row)
    
    # Write results to CSV
    with open('process_info.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(row)

if __name__ == "__main__":
    running_processes = get_running_process_info()
    analyze_processes(running_processes)

#run me pls
