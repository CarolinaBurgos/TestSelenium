from selenium import webdriver
import csv
import page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators

class ComplementarySubjects():
    web_page = "http://www.espol.edu.ec/es/educacion/grado/catalogo"
    file = 'bonus.csv'

    def save(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.web_page)

        main = page.MainPage(self.driver)
        main.career_catalog_data()

        with open(self.file, mode='w', encoding='utf-8', newline='') as fd:
            writer = csv.writer(fd, delimiter=',', dialect='excel', lineterminator='\n')
            writer.writerow(['career_name_en', 'elective_code', 'elective_name', 'weekly_hours']) #Head of the file

            for i, f in enumerate(main.faculty, start=0):
                size = len(main.c_names[i])
                for j in range(0, size):
                    self.driver.get(main.c_curriculum[i][j])

                    current = page.MainPage(self.driver)
                    current.electives_subjects()

                    size = len(main.s_name[i])
                    for k in range(0, size):
                        writer.writerow([main.c_names[i][j], current.s_code[k], current.s_name[k], current.s_hours[k]])

        fd.close()
        self.driver.close()
        print("File " + self.file + " created successfully!")

if __name__ == "__main__":
    search = ComplementarySubjects()
    search.save()