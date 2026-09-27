import urllib.request
import json

WEBHOOK = "

try:
    data = json.dumps({"content": " Test"}).encode('utf-8')
    req = urllib.request.Request(
        WEBHOOK, 
        data=data, 
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )
    response = urllib.request.urlopen(req, timeout=10)
    print(f"Success: {response.getcode()}")
except Exception as e:
    print(f"Error: {e}")