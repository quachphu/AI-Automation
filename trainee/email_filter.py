import csv
import json
import re

def is_leave_request(subject, body):
    leave_keywords = ['leave'] # use keywords to identify leave requests
    text = (subject + " " + body).lower()  
    
    for i in leave_keywords:
        if i in text:
            return True
    return False

def process_emails(input_file='emails.csv', output_file='leave_request.json'):
    """
    Read emails from CSV and filter leave requests to JSON
    """
    leave_requests = [] # create empty list to store all leave requests 
    
    try:
        # Read the CSV file
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                email_id = int(row['id'])
                sender = row['sender']
                subject = row['subject']
                body = row['body']
                
                if is_leave_request(subject, body):
                    leave_requests.append({
                        "id": email_id,
                        "sender": sender,
                        "type": "leave_request"
                    })
        
        # Write to JSON file
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(leave_requests, jsonfile)
        
        print(f"Total : {len(leave_requests)} leave requests")
        
        print(json.dumps(leave_requests, indent=2, ensure_ascii=False))
        
    except Exception as e:
        print(f"Error: {str(e)}")

process_emails()

