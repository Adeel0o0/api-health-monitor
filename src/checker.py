import requests
import time
from datetime import datetime


def check_endpoint(url, timeout=5):
    try:
        # record start time + make request with 5 second timeout, then return as a dictionary
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        duration = time.time() - start_time
        
        status_code = response.status_code
        
        if 200 <= status_code < 300:
            health_status = "healthy"
        elif 400 <= status_code < 500:
            health_status = "client_error"
        elif 500 <= status_code < 600:
            health_status = "server_error"
        else:
            health_status = "unknown"
        
        return {
            'url': url,
            'status_code': status_code,
            'response_time': round(duration, 2),
            'timestamp': datetime.now().isoformat(),
            'health_status': health_status,
            'error': None
        }
        
    except requests.exceptions.Timeout:
        return {
            'url': url,
            'status_code': None,
            'response_time': None,
            'timestamp': datetime.now().isoformat(),
            'health_status': 'timeout',
            'error': 'Request timed out after 5 seconds'
        }
        
    except requests.exceptions.ConnectionError as e:
        return {
            'url': url,
            'status_code': None,
            'response_time': None,
            'timestamp': datetime.now().isoformat(),
            'health_status': 'connection_error',
            'error': f'Connection failed: {str(e)[:100]}'
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'url': url,
            'status_code': None,
            'response_time': None,
            'timestamp': datetime.now().isoformat(),
            'health_status': 'error',
            'error': f'Request error: {str(e)[:100]}'
        }


def check_multiple_endpoints(endpoints, timeout=5):
    results = []
    for url in endpoints:
        result = check_endpoint(url, timeout)
        results.append(result)
    return results