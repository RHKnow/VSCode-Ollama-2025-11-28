#Succesfully run 11/28/25

import requests
import json

resp = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": "Summarize Git in simple terms",
        "stream": True  # stream enabled
    },
    stream=True
)

# Iterate over the streamed lines
for line in resp.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        # Each chunk has a "response" key with partial text
        print(data.get("response", ""), end="", flush=True)

print("\n--- done ---")

# Note: This code handles streamed output from the API.
# Each line is a JSON object with partial response data.
