from selenium.webdriver.common.by import By

class MainPageLocators(object):
    #Carrer Catalog
    FACULTY_HEAD = (By.XPATH, "//div[starts-with(@id,'headingF')]")
    FACULTY_CAREERS = (By.XPATH, "//div[starts-with(@id,'collapseF')]")

class SearchResultsPageLocators(object):
    # Carrer Catalog
    LIST = (By.XPATH, ".//p/strong[contains(text(),'Undergraduate Programs')]/following::ul[1]/li")
    LINK = (By.XPATH, ".//a")
    SPAN = (By.XPATH, ".//span")
    TITLE = (By.XPATH, ".//strong")
