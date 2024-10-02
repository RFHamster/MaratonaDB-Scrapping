from selenium.webdriver import Firefox

url = ('https://codeforces.com/problemset/problem/2004/B')

driver = Firefox()
driver.get(url)

print(driver.page_source)

driver.close()