import csv
import nmap
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to run Nmap scan on a target
def run_nmap_scan(target):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=target, arguments='-T4 -F')
    return result

# Function to save scan results to a CSV file
def save_to_csv(target, scan_results):
    csv_file = f'{target}_scan_results.csv'
    with open(csv_file, 'w', newline='') as file:
        fieldnames = ['Port', 'State', 'Service']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for port, port_info in scan_results.items():
            writer.writerow({'Port': port, 'State': port_info['state'], 'Service': port_info['name']})

# Function to send email notification
def send_email_notification(target, scan_results):
    # Replace the following with your email settings
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    receiver_email = 'receiver_email@example.com'
    password = 'your_email_password'
    
    # Prepare email content
    subject = f'Security Scan Results for {target}'
    body = f"Security scan results for {target}:\n{scan_results}"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Main function
def main():
    # Replace the following with your list of target hosts or IP ranges
    targets = ['scanme.nmap.org', '192.168.0.1', '10.0.0.0/24']

    for target in targets:
        print(f"Scanning target: {target}")
        scan_results = run_nmap_scan(target)
        save_to_csv(target, scan_results['scan'][target]['tcp'])
        print(f"Scan results saved to {target}_scan_results.csv")
        security_issues = [port for port, port_info in scan_results['scan'][target]['tcp'].items() if port_info['state'] == 'open']
        
        if security_issues:
            print(f"Potential security issues found for {target} on ports: {security_issues}")
            # Uncomment the line below to send email notification
            # send_email_notification(target, scan_results)
        else:
            print(f"No security issues found for {target}")

if __name__ == "__main__":
    main()
