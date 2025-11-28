import requests

# Send request with stream disabled
resp = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral", 
        "prompt": "Summarize Git in simple terms", 
        "stream": False  # ensures one complete JSON response
    }
)

# Parse the JSON safely
data = resp.json()

if "error" in data:
    print("Error:", data["error"])
else:
    print(data["response"])
