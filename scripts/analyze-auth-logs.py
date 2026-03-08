import json

log_file = "auth_logs.json"

try:
    with open(log_file) as file:
        logs = json.load(file)

    for entry in logs:
        if entry.get("status") == "failed":
            print("Failed login attempt:", entry)

except FileNotFoundError:
    print("No log file found for analysis.")
