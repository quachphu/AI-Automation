# Email Leave Request Filter

Mini workflow program to automatically filter leave request emails from a CSV file.

## Overview

This program reads emails from `emails.csv`, identifies leave request emails based on keywords, and outputs filtered results to `leave_request.json`.

## Features

- Reads email data from CSV format
- Intelligent keyword detection for leave requests
- Outputs structured JSON format
- Available in both Python and Node.js

## Project Structure

```
.
├── email_filter.py          # Python implementation
├── emails.csv              # Input data (sample provided)
├── leave_request.json      # Output file (generated)
└── README.md               # This file
```

## 🐍 Python Version

### Requirements
- Python 3.6+
- No external dependencies (uses standard library)

### Usage

```bash
python email_filter.py
```

### How it works

1. Reads `emails.csv` using csv.DictReader
2. Checks each email for leave-related keywords
3. Filters emails containing: "leave"
4. Outputs filtered results to `leave_request.json`


## 📝 Input Format (emails.csv)

```csv
id,sender,subject,body
1,alice@company.com,Leave request,"I would like to take leave on 2025-09-28"
2,bob@company.com,IT issue,"My laptop cannot connect to wifi"
3,charlie@client.com,New leave request,"I would like to take day off on"
4,quachphuwork@gmail.com,Intern request ,"I love to applied to internship"
5,bob@company.com,Leave request,"I would like to take leave on 2026-09-28"
```

## 📤 Output Format (leave_request.json)

```json
[
  {
    "id": 1,
    "sender": "alice@company.com",
    "type": "leave_request"
  },
  {
    "id": 3,
    "sender": "charlie@client.com",
    "type": "leave_request"
  },
  {
    "id": 5,
    "sender": "bob@company.com",
    "type": "leave_request"
  }
]
```

## 🔍 Keyword Detection

The program detects leave requests by searching for these keywords in subject or body:
- `leave`


## 🛠️ Customization

To add more keywords, edit the `leave_keywords` list in either implementation:

**Python:**
```python
leave_keywords = ['leave','off', 'vacation', 'absence', 'day off', 'your_keyword']
```


## 📊 Example Output

```
Total : 3 leave requests
[
  {
    "id": 1,
    "sender": "alice@company.com",
    "type": "leave_request"
  },
  {
    "id": 3,
    "sender": "charlie@client.com",
    "type": "leave_request"
  },
  {
    "id": 5,
    "sender": "bob@company.com",
    "type": "leave_request"
  }
]
```

## 🧪 Testing with Your Own Data

1. Replace the contents of `emails.csv` with your data
2. Make sure the CSV has these columns: `id`, `sender`, `subject`, `body`
3. Run the program using Python

## 💡 Use Cases

- Automated HR email processing
- Leave request management systems
- Email categorization workflows
- Integration with automation platforms (n8n, Zapier, etc.)

## 📚 Technical Details

### Python Implementation
- Uses `csv.DictReader` for CSV parsing
- Uses `json.dump` for JSON output
- Case-insensitive keyword matching
- UTF-8 encoding support

## 🤝 Contributing

Feel free to customize and extend this program for your specific needs!

## 📄 License

MIT License - Feel free to use for your assignment or projects.
