import selenium

driver = selenium.webdriver.Chrome() # Abre o Browser
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScRAp5R3y4k7vVsHvdGWSXQNn-jC3Ub_ShfMVfxAhFbcgs8yA/viewform') # Página mae

elemento = driver.find_element_by_xpath('//*[@id="i5"]/div[3]/div') # elemento xpah alvo (//*[@id="i8"]/div[3]/div)
elemento.click() # clique no alvo
botao = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span/span')
botao.click()
list()