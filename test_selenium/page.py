from locators import MainPageLocators, SearchResultsPageLocators
from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    faculty, c_names, c_codes, c_curriculum = [], [], [], []
    s_name, s_code, s_hours = [], [], []

    def career_catalog_data(self):
        f_locator = self.driver.find_elements(*MainPageLocators.FACULTY_HEAD)
        for fl in f_locator:
            f_name = fl.find_element(*SearchResultsPageLocators.TITLE)
            f_name = f_name.text.split("\n")[1] #We are going to have spanish [0] and english [1] faculty name
            self.faculty.append(f_name)

        f_locator = self.driver.find_elements(*MainPageLocators.FACULTY_CAREERS)
        for fl in f_locator:
            c_name, c_code, c_link = [], [], []

            f_carreers = fl.find_elements(*SearchResultsPageLocators.LIST)
            for fcl in f_carreers:
                c_information = fcl.get_attribute("textContent")
                c_information = c_information.split(" (see program flowchart)")

                c_name.append(c_information[0]) #Career name
                c_code.append(c_information[1]) #Career code

                #Another way to get the career code
                '''
                c = fcl.find_element(*SearchResultsPageLocators.SPAN)
                code = c.get_attribute("textContent")
                c_code.append(code)
                '''

                l = fcl.find_element(*SearchResultsPageLocators.LINK)
                link = l.get_attribute("href")
                c_link.append(link) #Career curriculum link

            self.c_names.append(c_name)
            self.c_codes.append(c_code)
            self.c_curriculum.append(c_link)

    def electives_subjects(self):
        # We need to clear them before looking in another career
        self.s_name.clear()
        self.s_code.clear()
        self.s_hours.clear()

        try:
            self.driver.find_element(*MainPageLocators.ELECTIVES).click()
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(MainPageLocators.TOTAL))
            total = self.driver.find_element(*MainPageLocators.TOTAL)
            total.click()
            total.find_element(*SearchResultsPageLocators.OPTION).click()
            WebDriverWait(self.driver, 120).until(EC.presence_of_element_located(MainPageLocators.COMPLEMENTARY_SUBJECTS))

            for c_data in self.driver.find_elements(*MainPageLocators.COMPLEMENTARY_SUBJECTS):
                code = c_data.find_element(*SearchResultsPageLocators.SUBJECT_CODE).get_attribute("textContent")
                name = c_data.find_element(*SearchResultsPageLocators.SUBJECT_NAME).get_attribute("textContent")
                hours = c_data.find_element(*SearchResultsPageLocators.SUBJECT_HOURS).get_attribute("textContent")
                self.s_code.append(code.strip())
                self.s_name.append(name)
                self.s_hours.append(hours)
        except:
            print("ERROR: An error occurred when trying to obtain the information of the complementary subjects.")

class SearchResultsPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
