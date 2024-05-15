import time

import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument(f"user-agent={UserAgent().random}")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--mute-audio")
driver = webdriver.Chrome(service=service, options=options)


# driver.implicitly_wait(10)

def get_stories(username):
    try:
        driver.get(f"https://insta-stories-viewer.com/ru/{username}/")

        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(10)
        parent_block = driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div[4]/div/div[1]/div[1]/ul')
        stories_count = parent_block.find_elements(By.TAG_NAME, 'li')
        stories_count = len(stories_count)
        print(stories_count)

        video_and_image_links = []

        for i in range(1, stories_count + 1):
            driver.find_element(by=By.XPATH,
                                value=f'/html/body/section/div[2]/div/div[4]/div/div[1]/div[1]/ul/li[{i}]/div/span[2]').click()
            if 4 < i < 8:
                driver.execute_script("window.scrollTo(0, 1000);")
                time.sleep(5)
            if 8 < i < 12:
                driver.execute_script("window.scrollTo(0, 1400);")
                time.sleep(5)
            if 12 < i < 16:
                driver.execute_script("window.scrollTo(0, 1800);")
                time.sleep(5)
            stories_modal = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[2]')
            images = stories_modal.find_elements(By.TAG_NAME, 'img')
            videos = stories_modal.find_elements(By.TAG_NAME, 'video')

            if images:
                video_and_image_links.append(images[0].get_attribute('src'))
            if videos:
                video_and_image_links.append(videos[0].get_attribute('src'))

            if i < stories_count:
                driver.find_element(by=By.XPATH, value='/html/body/div[6]/span').click()
                time.sleep(5)
        print(video_and_image_links)
        return video_and_image_links
    except (TimeoutException, NoSuchElementException, ElementNotInteractableException):
        return '❗️Сталася помилка❗️\nПеревірте юзернейм та спробуйте ще раз, або спробуйте пізніше'


def is_image(url):
    response = requests.get(url)
    content_type = response.headers.get('content-type')
    return content_type.startswith('image')


def is_video(url):
    response = requests.get(url)
    content_type = response.headers.get('content-type')
    return content_type.startswith('video')
