from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import chromedriver_binary

# Google search list URL
def getLinks(driver, word):
    driver.get("https://www.google.co.jp/")
    search = driver.find_element_by_name('q')
    search.send_keys(word)
    search.send_keys(Keys.ENTER)

    elems = driver.find_elements_by_tag_name('a')
    links = [elem.get_attribute('href') for elem in elems]
    ret = []
    for link in links:
        try:
            if "www.google.co.jp/search" in link:
                ret.append(link)
        except:
            continue
    return ret
  

# click url in Google search result lists
def click(driver, links):
    for link in links:
        if ("cache" in link) or ("preferences" in link) or ("accounts" in link) or ("tbm=" in link):
            continue
        driver.get(link)
        results = driver.find_elements_by_tag_name('a')
        for result in results:
            try:
                article_link = result.get_attribute('href')
                if ("cache" in article_link) or ("preferences" in article_link) or ("accounts" in article_link):
                    continue
                if "YOUR HOMEPAGE URL" in article_link:
                    result.click()
                    driver.close()
                    driver.quit()
                    break
            except:
                continue
                

driver = webdriver.Chrome()
links = getLinks(driver, "SEARCH KEY WORD")
click(driver, links)
