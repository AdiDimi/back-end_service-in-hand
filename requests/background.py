
from datetime import datetime

def audit_log_transaction(requestId: str, message=""):
    with open("audit_log.txt", mode="a") as logfile:
        content = f"-- Request -- requestId {requestId} executed {message} at {datetime.now()}"
        logfile.write(content)

def audit_log_error(status_code: str, message=""):
    with open("audit_log.txt", mode="a") as logfile:
        content = f"-- Error -- status_code {status_code} , exception msg: {message} at {datetime.now()}"
        logfile.write(content)
