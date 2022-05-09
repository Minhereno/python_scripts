from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse

parser = argparse.ArgumentParser(description='Assembly References of organism. Enter in the binomial nomenclature of organism.') #Two arguments, Genus and Species
parser.add_argument('tax_name', type=str, help='Taxonomy (binomial nomenclature) name of organism(e.g. "Yersinia pestis"). Please place in quotations')
args = parser.parse_args()


#opening browser and going into assembly
browser = webdriver.Chrome('/Users/minhe/Desktop/chromedriver.exe')
browser.maximize_window()
browser.get("https://www.ncbi.nlm.nih.gov/assembly")

#Searching organism
searchorganism = browser.find_element_by_xpath('//*[@id="term"]')
searchorganism.send_keys(args.tax_name.lower())
searchorganism.send_keys(Keys.ENTER)

#Downloading references
browser.find_element_by_xpath('//*[@id="_level"]/li/ul/li[1]/a').click()
browser.find_element_by_xpath('//*[@id="_status"]/li/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="download-asm"]/a').click()
