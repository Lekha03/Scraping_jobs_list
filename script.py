from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

website="https://in.indeed.com/"
path='C:/Program Files/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)  # selenium 4
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()


button=driver.find_element(by="xpath", value='//button[@type="submit"]')
button.click()

Job_name=[]
Job_location=[]
Company_name=[]

#PAGINATION

pagination=driver.find_elements(by="xpath", value='//nav[@aria-label="pagination"]')
pages=driver.find_elements(by="xpath", value='//nav[@aria-label="pagination"]/ul/li')



required_jobs=1000

while len(Job_name)<required_jobs:
    time.sleep(5)
    #jobs_names=driver.find_elements(by="xpath", value="//h2[@class='jobTitle css-1psdjh5 eu4oa1w0']/a/span")
    #jobs=driver.find_elements(by="xpath", value='//table[@role="presentation"]')
    #time.sleep(100)
    #print(len(jobs_names))


    jobs_names=driver.find_elements(by="xpath", value="//h2[(@class='jobTitle css-1psdjh5 eu4oa1w0') or (@class='jobTitle jobTitle-newJob css-1psdjh5 eu4oa1w0')]/a/span")
    company_names=driver.find_elements(by="xpath", value='//table[@role="presentation"]/tbody/tr/td/div[@class="company_location css-i375s1 e37uo190"]/div/div/span[@data-testid="company-name"]')
    jobs_location=driver.find_elements(by="xpath", value='//table[@role="presentation"]/tbody/tr/td/div[@class="company_location css-i375s1 e37uo190"]/div/div[@data-testid="text-location"]')
    print(jobs_names)

    for x in range(len(jobs_names)):
        print(x)
        Job_name.append(jobs_names[x].text)
        Job_location.append(jobs_location[x].text)
        Company_name.append(company_names[x].text)

    try:
        next_page = driver.find_elements(by="xpath", value='//a[@data-testid="pagination-page-next"]')
        next_page.click()
    except:
        pass


df=pd.DataFrame({"Job Name":Job_name, "Job Location":Job_location, "Company Name":Company_name})
print(df)
df.to_csv('jobs_indeed_1000.csv', index=False)
time.sleep(10)
driver.quit()
