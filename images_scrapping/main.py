import json
import os

from selenium import webdriver

from google_images_parser import find_urls

from webdriver_manager.chrome import ChromeDriverManager

images_folder = "images"
#driver = webdriver.Chrome("chromedriver")
driver = webdriver.Chrome(ChromeDriverManager().install())

with open("car_data.json", "r") as file:
    car_data = json.loads(file.read())

print(car_data['results'][0])

# 1932 done (from 4k)
# find element by xpath error: Message: unknown error: session deleted because of page crash
# find element by xpath error: Message: invalid session id
print(len(car_data['results']))
for i, data in enumerate(car_data["results"][4205:]):

    model = data["Model"]
    year = data["Year"]
    category = data['Category']
    make = data['Make']

    car_info = f"{make}_{model}_{year}_{category}"
    car_folder_path = os.path.join(images_folder, car_info)

    car_search_request = f"{make} {model} {year} {category}"

    if not os.path.isdir(car_folder_path):
        os.makedirs(car_folder_path)

    img_url_part = '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'
    url = 'https://www.google.com/search?q=' + car_search_request + img_url_part
    find_urls(car_search_request, url, driver, car_folder_path)

    print(i)
