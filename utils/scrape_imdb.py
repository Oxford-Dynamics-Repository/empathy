# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - December 2022
#
# This script scrapes the website IMDB for written Harry Potter reviews.

import numpy as np
import pandas as pd
from scrapy.selector import Selector
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import warnings
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


def scrape_imdb():
    # Desired data types.
    rating_list = []
    review_date_list = []
    review_title_list = []
    review_list = []
    error_url_list = []
    error_msg_list = []

    # Setting up the URL which leads to the review page.
    driver = webdriver.Chrome('chromedriver.exe')
    url = 'https://www.imdb.com/title/tt0241527/reviews?ref_=tt_urv'
    driver.get(url)

    # Reading the number of reviews.
    sel = Selector(text = driver.page_source)
    review_counts = sel.css('.lister .header span::text').extract_first().replace(',','').split(' ')[0]
    more_review_pages = int(int(review_counts)/25)

    # Pressing all the "load more" buttons. 
    for i in tqdm(range(more_review_pages)):
        try:
            css_selector = 'load-more-trigger'
            driver.find_element(By.ID, css_selector).click()
            time.sleep(2)
        except:
            time.sleep(2)
            pass

    # Pulling out all the reviews.
    reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')

    for d in tqdm(reviews):
        try:
            selector = Selector(text = d.get_attribute('innerHTML'))

            # Pulling out the rating.
            try: rating = selector.css('.rating-other-user-rating span::text').extract_first()
            except: rating = np.NaN
            
            # Pulling out the review.
            try: 
                review = selector.css('.text.show-more__control::text').extract()

                # Removing whitespace. 
                for i in range(len(review)):
                    review[i] = ' '.join(review[i].split())

                review = ' '.join(review)
            except: 
                review = np.NaN
            
            # Pulling out the review date.
            try: review_date = selector.css('.review-date::text').extract_first()
            except: review_date = np.NaN
            
            # Pulling out the review title.
            try: review_title = selector.css('a.title::text').extract_first()
            except: review_title = np.NaN

            # Storing the data in the corresponding arrays. 
            rating_list.append(rating)
            review_date_list.append(review_date)
            review_title_list.append(review_title.strip())
            review_list.append(review.strip())
            
        except Exception as e:
            print("Exception called in the root try-except block.")
            error_url_list.append(url)
            error_msg_list.append(e)

    # Writing data into pandas-format.
    review_df = pd.DataFrame({
        'review': review_list})

    # Avoiding line-breaks.
    review_df['review'].replace(to_replace=r"\n", value=" ", regex=True, inplace=True)

    review_train_df, review_val_df = train_test_split(review_df, test_size = 0.25, random_state = 8)

    # Writing error messages into pandas-format.
    error_df = pd.DataFrame({
        'error_url': error_url_list,
        'error_msg': error_msg_list})

    # Saving to file.
    review_train_df.to_csv("harry_potter_1_reviews_train.csv", index = False)
    review_val_df.to_csv("harry_potter_1_reviews_val.csv", index = False)
    error_df.to_csv("error_messages.csv", index = False)

def main():
    scrape_imdb()
    print(pd.read_csv('harry_potter_1_reviews_train.csv'))
    

if __name__ == '__main__':
    main()