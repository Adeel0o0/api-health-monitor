# Endpoints to monitor
ENDPOINTS = [
    "https://api.github.com/status",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://api.github.com/this-does-not-exist",  # 404 test
    "https://httpbin.org/status/500",  # 500 error - SHOULD alert
    "https://this-definitely-does-not-exist-12345.com",  # Connection error - SHOULD alert
]

# monitoring settings
CHECK_INTERVAL_SECONDS = 300  # seconds
REQUEST_TIMEOUT_SECONDS = 5  # seconds

# storage settings
RESULTS_FILE = "data/monitor_results.json"

