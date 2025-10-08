def get_status_emoji(health_status):
    status_emoji ={
        'healthy': '✅',
        'client_error': '⚠️',
        'server_error': '❌',
        'timeout': '⏰',
        'connection_error': '🔌',
        'error': '❗',
        'unknown': '❓'
    }
    return status_emoji.get(health_status, '❓')

def print_result(result):
    emoji = get_status_emoji(result['health_status'])
    print(f"{emoji} {result['url']} - Status: {result['status_code']}, Response Time: {result['response_time']}s, Health: {result['health_status']}")
    if result['error']:
        print(f"   Error: {result['error']}")

def print_summary(results):
    status_counts = {}
    for result in results:
        status = result['health_status']
        status_counts[status] = status_counts.get(status, 0) + 1
    print("\nSummary of health check results:")
    for status, count in status_counts.items():
        print(f" - {status}: {count}")
