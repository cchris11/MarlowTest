# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

# define url
url = "https://www.amazon.com/"

# chrome full screen
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

# open browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chromeOptions)
driver.get(url)
time.sleep(2)

# select top left bar
driver.find_element(by=By.XPATH, value='//*[@id="nav-hamburger-menu"]').click()
time.sleep(1)
# select all electronics
driver.find_element(by=By.XPATH, value='//*[@id="hmenu-content"]/ul[1]/li[7]/a').click()
time.sleep(1)
# select category computers & accessories
driver.find_element(by=By.XPATH, value='//*[@id="hmenu-content"]/ul[5]/li[7]').click()
time.sleep(1)
# create a list of all products appeared in first page
product = driver.find_elements(by=By.XPATH, value="//span[@class='a-size-base-plus a-color-base a-text-normal']")
products = []
for p in product:
    products.append(p.text)
time.sleep(1)
# click the 4th product
driver.find_element(by=By.LINK_TEXT, value=products[3]).click()
time.sleep(1)
# get product's price
price = driver.find_element(by=By.CSS_SELECTOR, value=".a-price.a-text-price").text
time.sleep(3)
# add product to cart
driver.find_element(by=By.XPATH, value='//*[@id="add-to-cart-button"]').click()
time.sleep(5)
# get product's price in cart
priceInCart = driver.find_element(by=By.XPATH, value="//*[@id='attach-accessory-cart-subtotal']").text

# print(price)
# print (priceInCart)

if price == priceInCart:
    print('Test successful')
else:
    print('Test failed')
