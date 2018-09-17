import time
from splinter import Browser
from selenium import webdriver

def splinter(url):
    #executable_path = {'executable_path': '~/Downloads/phantomjs-2.1.1-macosx/bin (master)'}
    #executable_path = {'executable_path': '/Applications'}
    #browser = Browser('chrome', **executable_path)
    #browser = Browser('chrome')
    browser = webdriver.Chrome('/Users/liujinjian/Downloads/phantomjs-2.1.1-macosx/bin/node_modules/chromedriver/bin/')
    browser.visit(url)
    #wait web element loading
    time.sleep(5)
    #fill in account and password
    #browser.find_by_id('getIdPLink').click()#fill('d347wang')
    browser.click_link_by_href('javascript:getIdPLink()')
    time.sleep(2)
    browser.find_by_id('saml-username').fill('d347wang')

    browser.find_by_id('saml-password').fill('Ding707296/')
    #click the button of login
    browser.find_by_id('saml-submit').click()
    time.sleep(8)
    browser.click_link_by_href("javascript:submitAction_win0(document.win0,'DERIVED_SSS_SCR_SSS_LINK_ANCHOR3');").click()
    time.sleep(1)
    # button_shopcart = browser.find_by_xpath('//*[@id="win0divDERIVED_SSTSNAV_SSTS_NAV_SUBTABS"]/div/table/tbody/tr/td[8]/a')
    # button_shopcart.click()
    # btn_sel_cm762 = browser.find_by_xpath('//*[@id="P_SELECT$0"]')
    # btn_sel_cm762.click()
    # btn_sel_ece606 = browser.find_by_xpath('//*[@id="P_SELECT$9"]')
    # btn_sel_ece606.click()
    # btn_enroll = browser.find_by_xpath('//*[@id="DERIVED_REGFRM1_LINK_ADD_ENRL$291$"]')
    # btn_enroll.click()
    btn_add = browser.find_by_xpath('//*[@id="win0divDERIVED_SSTSNAV_SSTS_NAV_SUBTABS"]/div/table/tbody/tr/td[14]/a')
    btn_add.click()
    btn_ad_search = browser.find_by_xpath('//*[@id="DERIVED_REGFRM1_SSR_PB_SRCH"]')
    btn_ad_search.click()
    tx_subject = browser.find_by_xpath('//*[@id="SSR_CLSRCH_WRK_SUBJECT$0"]')
    tx_subject.fill('ECE')
    tx_crs_num = browser.find_by_xpath('//*[@id="SSR_CLSRCH_WRK_CATALOG_NBR$1"]')
    tx_crs_num.fill('651')
    btn_srch_search = browser.find_by_xpath('//*[@id="CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH"]')
    btn_srch_search.click()
    btn_select_ece651 = browser.find_by_xpath('//*[@id="SSR_PB_SELECT$0"]')
    btn_select_ece651.click()
    browser.find_by_xpath('//*[@id="DERIVED_CLS_DTL_NEXT_PB$280$"]').click()
    #close the window of brower
    browser.quit()

if __name__ == '__main__':
    websize ='https://quest.pecs.uwaterloo.ca/psp/SS/ACADEMIC/SA/?cmd=login&languageCd=ENG'
    splinter(websize)