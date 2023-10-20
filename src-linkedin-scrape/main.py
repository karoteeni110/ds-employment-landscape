from linkedin_scraper import JobSearch, actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
from pprint import pprint

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

def scrape_job_search(keyword):
    driver = webdriver.Chrome(options=set_chrome_options())
    actions.login(driver, os.environ["EMAIL"], os.environ["PWORD"]) # if email and password isnt given, it'll prompt in terminal
    print("... Logged in.")
    job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)

    job_listings = job_search.search(keyword) # returns the list of `Job` from the first page
    return job_listings

if __name__ == "__main__":
    import pickle 
    jl = scrape_job_search("data")
    print(jl)
    with open("10-20-kw=data-job-listings.pkl", "wb") as handle:
        pickle.dump(jl, handle, protocol=pickle.HIGHEST_PROTOCOL)