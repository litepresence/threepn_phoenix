"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝

Tweet Extractor

WTFPL litepresence 2021
"""

from twitter_scraper_selenium import scrap_profile as scrape_profile
import json
import time
from datetime import datetime

def get_tweets(username, n_tweets):
    ret = json.loads(scrape_profile(twitter_username=username,output_format="json",browser="firefox",tweets_count=n_tweets)).values()
    tweets = []
    for tweet in ret:
        # if tweet["videos"] != []:
        #     print(json.dumps(tweet, indent=4))
        #     # "id__3z3r9co7hnn"
        #     from selenium import webdriver
        #     from selenium.common.exceptions import TimeoutException
        #     from selenium.webdriver.support.ui import WebDriverWait
        #     from selenium.webdriver.support import expected_conditions as EC
        #     from selenium.webdriver.common.by import By
        #     print(dir(By))
        #     timeout = 10
        #     driver = webdriver.Firefox() 
        #     driver.get(tweet["tweet_url"]) 
        #     driver.set_window_size(480, 320)

        #     try:
        #         element_present = EC.presence_of_element_located((By.ID, 'accessible-list-0'))
        #         WebDriverWait(driver, timeout).until(element_present)
        #         time.sleep(2)
        #     except TimeoutException:
        #         pass
        #     #Screenshot of an element 
        #     while True:
        #         try:

        #             driver.save_screenshot("screenshot.png")
        #             break
        #         except Exception as e:
        #             print(e)
 
        #     driver.quit()
        #     exit()
        n_tweet = {}
        n_tweet["id"] = tweet["tweet_id"]
        n_tweet["unix"] = int(
            time.mktime(datetime.strptime(tweet["posted_time"], "%Y-%m-%dT%H:%M:%S%z").timetuple())
        )
        n_tweet["images"] = tweet["images"]
        n_tweet["url"] = tweet["tweet_url"].replace("fxtwitter", "twitter")
        tweets.append(n_tweet)
    print(tweets)
    return tweets

def unit_test():
    """
    get ten latest tweets from a user with images
    """
    print("\033c")
    print(json.dumps(get_tweets("ffftechnology", 10), indent=4))

if __name__ == "__main__":

    unit_test()
