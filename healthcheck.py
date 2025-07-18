import sys
import urllib.error
import urllib.request

URL = "http://localhost:8000/health/"

try:
    with urllib.request.urlopen(URL, timeout=10) as response:
        if 200 <= response.getcode() < 300:
            sys.exit(0)
        else:
            sys.exit(1)  # fail, код не 2xx
except urllib.error.URLError:
    sys.exit(1)  # fail, запрос не удался
