# Automated Security Scanning Utility

This is a command-line utility written in Python that performs automated security scanning using Nmap. It takes a list of target hosts or IP ranges, runs Nmap scans on each target, saves the scan results to CSV files, and optionally sends email notifications if potential security issues (open ports) are found.

## Features

- Scans multiple hosts or IP ranges automatically using Nmap.
- Saves scan results for each target to CSV files for further analysis.
- Provides optional email notifications for potential security issues (open ports).

## Requirements

- Python 3.x
- Nmap (Ensure it is installed on your system and accessible in the command-line.)

## Usage

1. Clone the repository to your local machine:

```bash
git clone git@github.com:n3xtChanc3/automated-security-scanner.git
cd automated-security-scanner

    Install the required Python libraries:

pip install python-nmap

    Open the automated_security_scanner.py file and customize the targets list with your desired target hosts or IP ranges.

    Run the Python script:

python3 automated_security_scanner.py

    The script will scan each target and save the results in CSV files. If any potential security issues (open ports) are found, it will print a message and, by default, send an email notification. To enable email notifications, provide your email server settings in the script.

Note: Make sure to have proper authorization before running security scans on any target. Unauthorized scanning may be illegal and unethical.
License

MIT License
Contributions

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.
Contact

If you have any questions or suggestions, you can contact me at starsonthesky@protonmail.com.


Of course, feel free to modify the content and structure of the `README.md` according to your project's specific details. The goal is to provide enough information to users so that they can understand what your utility does and how to use it effectively. Happy documenting
