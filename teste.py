from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxService

url = 'https://www.beecrowd.com.br/repository/UOJ_2023.html'

service = FirefoxService("/snap/bin/firefox.geckodriver")
driver = Firefox(service=service)
driver.get(url)

print(driver.page_source)

driver.close()
