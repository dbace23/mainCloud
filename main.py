import logging
import schedule
import time
from concurrent.futures import ThreadPoolExecutor
from scraper import tennis  # Import your tennis scraper function

# Create a ThreadPoolExecutor to run multiple tasks concurrently
executor = ThreadPoolExecutor(max_workers=5)  # Adjust as needed

def run_task_concurrently(scraper_func, *args):
    """Run the scraper function concurrently"""
    try:
        logging.info(f"Running scraper with args: {args}")
        return scraper_func(*args)  # Call the scraper with arguments
    except Exception as exc:
        logging.error(f"Error in scraper: {exc}")
        return None

# Schedule the jobs at the same time but run them concurrently
schedule.every().day.at("05:57").do(lambda: executor.submit(run_task_concurrently, tennis, 
    '["17:00 - 18:00"]', '%5B%2217%3A00+-+18%3A00%22%5D', 
    '["12:00 - 13:00"]', '%5B%2212%3A00+-+13%3A00%22%5D', 
    'geraldi.eka@gmail.com', 'jembut888'))

schedule.every().day.at("05:57").do(lambda: executor.submit(run_task_concurrently, tennis, 
    '["18:00 - 19:00"]', '%5B%2218%3A00+-+19%3A00%22%5D', 
    '["13:00 - 14:00"]', '%5B%2213%3A00+-+14%3A00%22%5D', 
    'p_hilips@yahoo.com', 'Raket123!'))

schedule.every().day.at("05:57").do(lambda: executor.submit(run_task_concurrently, tennis, 
    '["19:00 - 20:00"]', '%5B%2219%3A00+-+20%3A00%22%5D', 
    '["14:00 - 15:00"]', '%5B%2214%3A00+-+15%3A00%22%5D', 
    'Chris.wijaya9@gmail.com', 'sayangayahibu1'))

schedule.every().day.at("05:57").do(lambda: executor.submit(run_task_concurrently, tennis, 
    '["20:00 - 21:00"]', '%5B%2220%3A00+-+21%3A00%22%5D', 
    '["15:00 - 16:00"]', '%5B%2215%3A00+-+16%3A00%22%5D', 
    'yosua.wasita@gmail.com', 'Astro123!'))

schedule.every().day.at("05:57").do(lambda: executor.submit(run_task_concurrently, tennis, 
    '["21:00 - 22:00"]', '%5B%2221%3A00+-+22%3A00%22%5D', 
    '["16:00 - 17:00"]', '%5B%2216%3A00+-+17%3A00%22%5D', 
    'cecilialukardi@gmail.com', 'Tomat1234!'))

def run_scheduler():
    """Run the scheduled tasks continuously"""
    while True:
        schedule.run_pending()
        time.sleep(30)  # Wait before checking again

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_scheduler()
