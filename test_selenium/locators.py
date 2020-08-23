from selenium.webdriver.common.by import By

class MainPageLocators(object):
    #Carrer Catalog
    FACULTY_HEAD = (By.XPATH, "//div[starts-with(@id,'headingF')]/h4")
    FACULTY_CAREERS = (By.XPATH, "//div[starts-with(@id,'collapseF')]")

    # Bonus
    TOTAL = (By.XPATH, "//select[@name='tbl_materias_complementarias_length']")
    ELECTIVES = (By.XPATH, "//a[@data-target='#myModalComplementaria']")
    COMPLEMENTARY_SUBJECTS = (By.XPATH, "//table[@id='tbl_materias_complementarias']/tbody/tr")


class SearchResultsPageLocators(object):
    # Carrer Catalog
    LIST = (By.XPATH, ".//p/strong[contains(text(),'Undergraduate Programs')]/following::ul[1]/li")
    LINK = (By.XPATH, ".//a")
    SPAN = (By.XPATH, ".//span")
    TITLE = (By.XPATH, ".//strong")

    # Bonus
    OPTION = (By.XPATH, "./option[4]")
    SUBJECT_CODE = (By.XPATH, "./td[1]")
    SUBJECT_NAME = (By.XPATH, "./td[2]")
    SUBJECT_HOURS = (By.XPATH, "./td[3]")
