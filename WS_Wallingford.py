from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import json

#EXTRACT HR WALLINGFORD DATA
def Extract_SC(lat,long):    
    driver = webdriver.Safari()
    # Navigate to Url
    driver.get("https://hydrology-uksuds.hrwallingford.com/site1/hydrology/?lat="+str(lat)+"&long="+str(long))
    #driver.implicitly_wait(2)
    # Get all the elements available with tag name 'body'
    elements = driver.find_elements(By.TAG_NAME, 'body')
    # Print elements & Assign to var X
    for e in elements:
        #print(e.text,"\n")
        SiteHydrologicalCharacteristic = e.text
    driver.quit
    return SiteHydrologicalCharacteristic

#SORT EXTRACTED INFORMATION FROM Extract_SC Function
def extract_strings(text):
    data = json.loads(text)
    soil = data['soil']
    saar = data['saar']
    m5_60 = data['m5_60']
    r_ratio = data['r_ratio']
    region = data['region']

    return soil, saar, m5_60, r_ratio, region








