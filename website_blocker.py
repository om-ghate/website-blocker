import time
from datetime import datetime as dt
import tkinter as tk

def submit():
    global web_sites_list, start_time, end_time
    # Splitting by comma to handle multiple URLs
    web_sites_list = url_entry.get().split(",")  
    start_time = int(start_time_entry.get())
    end_time = int(end_time_entry.get())
    # Close the UI window after getting input
    root.destroy()  

root = tk.Tk()
root.title("Website URL and Time Range")

# URL Field
url_label = tk.Label(root, text="Website URLs (comma-separated):")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Start Time Field
start_time_label = tk.Label(root, text="Start Time (24-hour format):")
start_time_label.pack()
start_time_entry = tk.Entry(root)
start_time_entry.pack()

# End Time Field
end_time_label = tk.Label(root, text="End Time (24-hour format):")
end_time_label.pack()
end_time_entry = tk.Entry(root)
end_time_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()

# TODO : Add the path of hosts file located in your machine

hosts_path = r""

# ! Example for adding the path
# hosts_path = r"C:/Windows/System32/drivers/etc/hosts"

hosts_temp = "hosts"
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time):
        print("Working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in web_sites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_sites_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
