import time
from datetime import datetime

from config import ENDPOINTS, CHECK_INTERVAL_SECONDS, RESULTS_FILE
from src.checker import check_multiple_endpoints
from src.storage import save_results
from src.utils import print_result, print_summary
from src.alerting import check_and_alert


def run_single_check():
    print("Starting single health check...")
    results = check_multiple_endpoints(ENDPOINTS)
    for result in results:
        print_result(result)
    print_summary(results)
    save_results(results, filename=RESULTS_FILE)

    print_summary(results)
    print (f"\n✅ Single health check complete at {datetime.now().isoformat()}")


def run_countious_monitoring(interval_seconds=CHECK_INTERVAL_SECONDS):
    print(f"Starting continuous monitoring every {interval_seconds} seconds...")
    try:
        while True:
            print(f"\n🔄 Running health check at {datetime.now().isoformat()}")
            results = check_multiple_endpoints(ENDPOINTS)
            for result in results:
                print_result(result)
            print_summary(results)
            save_results(results, filename=RESULTS_FILE)
            print(f"⏲️  Waiting for {interval_seconds} seconds before next check...")
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")


if __name__ == "__main__":
    # For demonstration, we'll run a single check. Change to run_continuous_monitoring() for continuous mode.
    run_single_check()
    # run_continuous_monitoring()