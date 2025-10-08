from datetime import datetime
from unittest import result
from src.utils import get_status_emoji

def should_alert(result):
    """Determine if an alert should be sent based on the health check result."""
    critical_statuses = ['server_error', 'timeout', 'connection_error', 'error']
    return result['health_status'] in critical_statuses

def generate_alert_message(result):
    #Generate a formatted alert message based on the health check result.
    emoji = get_status_emoji(result['health_status'])
    timestamp = result['timestamp']
    url = result['url']
    status = result['health_status']
    error = result.get('error', 'No additional details')
    
    message = f"""
{emoji} ALERT: API Health Check Failed

Endpoint: {url}
Status: {status.upper()}
Time: {timestamp}
Error: {error}

Action Required: Investigate immediately
"""
    return message


def check_and_alert(results):
    #Check results and print alert messages for critical issues.
    alerts = []
    for result in results:
        if should_alert(result):
            alert_message = generate_alert_message(result)
            alerts.append(alert_message)
    return alerts   