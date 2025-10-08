# API health monitor

A python-based API health monitoring tool that checks endpoint availability, tracks response times and generates alerts for failures. Part of a wider project demo-ing monitoring, observability and automation

## Project Goals

- **Automate API health checks** across multiple endpoints
- **Track performance metrics** (response times, status codes)
- **Alert on critical failures** (server errors, timeouts, connection issues)
- **Demonstrate DevOps practices** (modular code, version control, production-ready patterns)

## Features 

- Multi-end point health checking
- Categorised health status (healthy, client_error, server_error timeout etc)
- Response time tracking
- JSON-based result persistence
- Alerting on critical issues, not client errors
- continous monitoring

## Tech Stack

- **Language:** Python 3.x
- **Libraries:** requests
- **Storage:** JSON (future: Azure Blob Storage)
- **Future Deployment:** Azure Functions, Docker

## Project Structure

- api-health-monitor/
- monitor.py              #Main entry point
- config.py               #Configuration settings
- requirements.txt        #Python dependencies
- src/
    - checker.py         #API health check logic
    - storage.py         #Result persistence
    - utils.py           #Display and formatting utilities
       - alerting.py        #Alert generation and filtering
- data/
- monitor_results.json  #Stored health check results

## Quick start

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/Adeel0o0/api-health-monitor.git
cd api-health-monitor

# Install dependencies
pip install -r requirements.txt