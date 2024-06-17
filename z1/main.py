import subprocess
import json

def send_request(url):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout, result.stderr

# Funkcja do sprawdzania statusu odpowiedzi HTTP
def check_status(response):
    try:
        data = json.loads(response)
        if isinstance(data, dict):
            return 'status' in data
        elif isinstance(data, list):
            return len(data) > 0 and 'id' in data[0]
    except json.JSONDecodeError:
        return False

def test_endpoint(url):
    response, error = send_request(url)
    if error:
        print(f"Error: {error.decode('utf-8')}")
        return False

    if check_status(response):
        return True
    else:
        return False

def run_tests():
    endpoints = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/users"
    ]

    for i, endpoint in enumerate(endpoints, 1):
        result = test_endpoint(endpoint)
        if result:
            print(f"Test {i}: PASSED")
        else:
            print(f"Test {i}: FAILED")

if __name__ == "__main__":
    run_tests()
