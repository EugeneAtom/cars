from selenium import webdriver
import time
import requests
import shutil
import os
import argparse


def save_img(inp, img, i, directory):
    try:
        filename = inp + '_' + str(i) + '.jpg'
        image_path = os.path.join(directory, filename)
        print(image_path)

        response = requests.get(img, stream=True, timeout=10)
        with open(image_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)

    except Exception as error:
        print(f"saving image error: {error}")
        pass


def find_urls(input_str: str, url, driver, directory):
    driver.get(url)

    for _ in range(3):
        driver.execute_script("window.scrollBy(0,100)")
        # try:
        #     driver.find_element_by_css_selector('.mye4qd').click()
        # except Exception as error:
        #     print(f"find element by css selector error: {error}")
        #     continue

    for j, img_url in enumerate(driver.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]')):
        try:
            img_url.click()

            # x_ = '//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img'
            xpath = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img'

            img = driver.find_element_by_xpath(xpath).get_attribute("src")
            print("ready to save some images!")
            save_img(input_str, img, j, directory)

            print("having nice deep sleep")
            time.sleep(1.5)
        except Exception as error:
            print(f"find element by xpath error: {error}")
            pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
    parser.add_argument('-d', '--directory', default='images/', type=str, help='save directory')
    args = parser.parse_args()

    driver = webdriver.Chrome("chromedriver")

    directory = args.directory
    input_str = args.search

    if not os.path.isdir(directory):
        os.makedirs(directory)

    url = 'https://www.google.com/search?q=' + str(
        input_str) + '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'

    find_urls(input_str, url, driver, directory)
