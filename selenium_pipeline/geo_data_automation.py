import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.keys import Keys
import traceback
time.sleep(5)

def get_results(input_zip):
    input_zip = str(input_zip)
    assert len(input_zip) == 5

    # put the path of the downloaded chrome driver executable here"
    # driver_path = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Remote("http://selenium:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)
    # driver = webdriver.Chrome(driver_path)

    # put the url that you want to navigate to"
    driver.get(r"https://www.zip-codes.com/")

    # find the relevant element in the url that you want to search by"
    search_object = driver.find_element_by_id("side-zip")

    search_object.send_keys(f"{input_zip}")
    search_object.send_keys(Keys.RETURN)
    try:

        # The WebDriverWait method waits until it locates the presence of the element"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "statTable")))

        fetch_from_table = lambda row_index, data_index: (
            driver.find_element_by_xpath(f"//table[@class= 'statTable']//tbody//tr[{row_index}]/td[{data_index}]").text)

        cities_list = fetch_from_table(6, 2).split("\n")
        state = fetch_from_table(3, 2)
        result = {f"{input_zip}": {"cities": cities_list, "state": state}}
        time.sleep(2)

    except:
        result = {f"{input_zip}": None}
        traceback.print_exc()
        print(f"Error with zip code {input_zip}")
    driver.quit()
    return result

# Sample execution to test the fuction

# if __name__ == "__main__":
#     for i in [14701,23509,32120,53214,13583,32121]:
#         get_results(i)


# print(list(map(lambda x: table_data.text.replace("\n"," "))
# driver.quit()
