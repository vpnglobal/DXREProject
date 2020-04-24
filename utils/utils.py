# CONSTANTS
import inspect
URL = "http://localhost:8989/"
USERNAME = "admin"
PASSWORD = "password"

def whoami():
    return inspect.stack()[1][3]