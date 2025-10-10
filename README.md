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
- **Future Deployment:** Azure Functions

## Project Structure

- api-health-monitor/
- monitor.py              #Main entry point
- config.py               #Configuration settings
- requirements.txt        #Python dependencies
- dockerfile 
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

## 🐳 Docker Deployment

### Build the Docker Image
```bash
docker build -t api-health-monitor .

```

##  Example Output

```bash
🔍 Starting single health check...```
✅ https://api.github.com/status - Status: 200, Response Time: 0.13s, Health: healthy
❌ https://httpbin.org/status/500 - Status: 500, Response Time: 3.7s, Health: server_error
============================================================
❌ ALERT: API Health Check Failed
Endpoint: https://httpbin.org/status/500
Status: SERVER_ERROR
Action Required: Investigate immediately
```

## Next Steps

- [ ] Add Azure OpenAI integration for intelligent error analysis
- [ ] Deploy to Azure Functions (serverless)
- [ ] Integrate with Azure Monitor and Application Insights
- [ ] Add email/Slack notifications for alerts
- [ ] Web dashboard for visualization