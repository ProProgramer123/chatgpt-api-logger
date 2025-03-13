import requests

def get_working_ai_api():
    api_endpoints = [
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        "https://api.ai21.com/studio/v1/j1-jumbo/complete",
        "https://api.cohere.ai/generate",
        # Add more endpoints as needed
    ]
    
    for _ in range(10000):
        for endpoint in api_endpoints:
            try:
                response = requests.post(endpoint, json={"prompt": "Hello, world!", "max_tokens": 5})
                if response.status_code == 200:
                    return endpoint
            except requests.RequestException:
                continue
    
    return None

if __name__ == "__main__":
    working_api = get_working_ai_api()
    if working_api:
        print(f"Working API found: {working_api}")
    else:
        print("No working API found.")
