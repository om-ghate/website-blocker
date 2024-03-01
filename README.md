# Python Website Blocker 🚫

## Description:
Python Website Blocker is a handy program designed to boost a programmer's productivity by blocking user-specified websites during a certain period of time in a day. This tool leverages the hosts file on Windows systems to control website accessibility, effectively redirecting specified URLs to the localhost address. By temporarily blocking distracting websites, programmers can focus more efficiently on their tasks.

## Language:
- Python 3.6 🐍

## Libraries:
- datetime ⏰
- tkinter 🖼️
- time ⌛

## Repository:
To clone the repository, use the following command:

```sh
git clone https://github.com/om-ghate/website-blocker.git
```

## How to Use:
To utilize Python Website Blocker:

1. Open the command prompt with Administrator privileges.
2. Navigate to the folder of the code.
3. Run the following command:

```sh
python website_blocker.py
```

## How it Works:
The program operates as follows:

1. **User Input:** The program prompts the user to input the website URL, start time, and end time for blocking.
2. **File Modification:** Once the user provides these parameters, the program updates the hosts file to block access to the specified website during the designated time frame.
3. **Restoration:** After the specified end time, the website becomes accessible again.

## Internal Working:
The internal functioning of the program involves the following steps:

- **Identifying Localhost:** The program identifies the localhost address of the system.
- **File Modification:** It writes entries to the hosts file to redirect specified website URLs to the localhost address.
- **File Handling:** Python's file handling capabilities are utilized to modify the hosts file.
- **User Interface:** Tkinter is employed to provide a user-friendly interface for inputting website URLs and time parameters.

## Example of Blocked Website Message:
When attempting to visit a blocked website, users will encounter a message similar to the following:

![Blocked Website Message](https://user-images.githubusercontent.com/19476654/33473547-baaee3a4-d62b-11e7-8b32-e90728aee3ea.png)

