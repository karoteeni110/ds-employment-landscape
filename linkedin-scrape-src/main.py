from linkedin_scraper import JobSearch, actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def scrape_job_search():
    driver = webdriver.Chrome(options=set_chrome_options())
    actions.login(driver) # if email and password isnt given, it'll prompt in terminal
    input("Press Enter")
    job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)

    job_listings = job_search.search("Machine Learning Engineer") # returns the list of `Job` from the first page
    return job_listings

if __name__ == "__main__":
    print(scrape_job_search())