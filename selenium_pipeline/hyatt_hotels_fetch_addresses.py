import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import traceback
import itertools

from selenium.webdriver.common.keys import Keys

DRIVER_PATH = r"C:\Program Files (x86)\chromedriver.exe"


class Address_Scraping():

    def __init__(self):
        self.chrome_driver = webdriver.Chrome(DRIVER_PATH)

    def get_hyperlinks(self):

        self.chrome_driver.get("https://www.hyatt.com/explore-hotels")
        try:
            # The WebDriverWait method waits until it locates the presence of the element"
            WebDriverWait(self.chrome_driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "countries.b-ph0")))
            us_add = self.chrome_driver.find_element_by_xpath(
                "//ul[@class='countries b-ph0']//li[@data-js-country='United States']")
            links = us_add.find_elements_by_tag_name('a')
            hyperlinks = [link_field.get_attribute("href") for link_field in links]
            return hyperlinks


        except:
            print("error")
            traceback.print_exc()
        time.sleep(2)
        # chrome_driver.quit()

    def fetch_addresses_to_df(self):
        links_list = self.get_hyperlinks()
        # assert links_list != []
        results_list = []
        error_links_list = []

        for index, link in enumerate(links_list, start=1):
            if index == 5:
                break
            try:
                print("passing through link ------------>", link)
                self.chrome_driver.get(link)
                address_div = self.chrome_driver.find_elements_by_xpath(
                    "//div[@class='site-info-container b-mt2 b-mb2 b-mt0@sm b-mb0@sm']//a[@class='site-info-address b-d-inline-block b-d-flex@lg b-d-inline-block@xl b-mb2@sm b-mb1@md b-mr2']//span[@class='b-d-inline-block']")

                phone_num_div = self.chrome_driver.find_element_by_xpath(
                    "//div[@class='site-info-container b-mt2 b-mb2 b-mt0@sm b-mb0@sm']//a[@class='site-info-phone b-d-inline-block b-d-block@lg b-mb1@sm b-mr2']//span[@class='hover-border b-d-none b-d-inline@lg']")

                address = "".join(map(lambda x: x.text, address_div))
                phone_number = ", " + phone_num_div.text
                # self.chrome_driver.find_element_by_partial_link_text("Hoover, Alabama, United States, 35244").click()
                # time.sleep(3)
                # self.chrome_driver.close()
                # get_url = self.chrome_driver.current_url
                # print(get_url)
                # exit()
                combined_output = "".join([address, phone_number])
                results_list.append(combined_output.split(","))

            except:
                traceback.print_exc()
                error_links_list.append(link)

        final_df = pd.DataFrame(results_list, columns=["street", "city", "state", "country", "zip", "phone_number"],
                                index=None)
        final_df.to_excel("hyatt_hotels.xlsx", index=False)


if __name__ == "__main__":
    Address_Scraping().fetch_addresses_to_df()
