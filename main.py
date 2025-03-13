import requests
import random
import string
import signal
import sys
import time

def generate_api_key():
    return 'sk-' + ''.join(random.choices(string.ascii_letters + string.digits + '-_', k=48))

def fetch_openai_models(api_key):
    url = "https://api.openai.com/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [model["id"] for model in response.json()["data"]]
    else:
        print(f"Failed to fetch models: {response.status_code}")
        return []

def get_working_ai_api():
    while True:
        api_key = generate_api_key()
        models = fetch_openai_models(api_key)
        
        if not models:
            # Fallback to old APIs if fetching models fails
            api_endpoints = [
                {"url": "https://api.openai.com/v1/engines/davinci-codex/completions", "api_key": generate_api_key(), "model": "davinci-codex"},
                {"url": "https://api.openai.com/v1/engines/text-davinci-002/completions", "api_key": generate_api_key(), "model": "text-davinci-002"},
                {"url": "https://api.openai.com/v1/engines/gpt-3.5/completions", "api_key": generate_api_key(), "model": "gpt-3.5"},
                {"url": "https://api.openai.com/v1/engines/gpt-4o-mini/completions", "api_key": generate_api_key(), "model": "gpt-4o-mini"},
                {"url": "https://api.openai.com/v1/engines/dall-e/completions", "api_key": generate_api_key(), "model": "dall-e"},
                {"url": "https://api.openai.com/v1/engines/whisper/completions", "api_key": generate_api_key(), "model": "whisper"},
                {"url": "https://api.openai.com/v1/engines/jukebox/completions", "api_key": generate_api_key(), "model": "jukebox"},
                {"url": "https://api.openai.com/v1/engines/o1-mini/completions", "api_key": generate_api_key(), "model": "o1-mini"},
            ]
        else:
            api_endpoints = [{"url": f"https://api.openai.com/v1/engines/{model}/completions", "api_key": api_key, "model": model} for model in models]
        
        for endpoint in api_endpoints:
            try:
                headers = {"Authorization": f"Bearer {endpoint['api_key']}"}
                response = requests.post(endpoint["url"], headers=headers, json={"prompt": "How are you?", "max_tokens": 5})
                if response.status_code == 200:
                    print(f"[SUCCESS] {endpoint['api_key']} with model {endpoint['model']}")
                    return endpoint["url"]
                elif response.status_code == 429:  # Rate limit exceeded
                    print(f"[RATE LIMIT] {endpoint['api_key']} with model {endpoint['model']}")
                    time.sleep(1)  # Wait for 1 second before retrying
                else:
                    print(f"[FAILURE] {endpoint['api_key']} with model {endpoint['model']}")
            except requests.RequestException:
                print(f"[FAILURE] {endpoint['api_key']} with model {endpoint['model']}")
                continue

def signal_handler(sig, frame):
    print("\nProcess interrupted. Exiting...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    working_api = get_working_ai_api()
    if working_api:
        print(f"Working API found: {working_api}")
        sys.exit(0)
    else:
        print("No working API found.")
