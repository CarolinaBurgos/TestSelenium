from selenium import webdriver
import csv
import page

class CareersCatalog():
    web_page = "http://www.espol.edu.ec/es/educacion/grado/catalogo"
    file = 'career_catalog.csv'

    def save(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.web_page)

        main = page.MainPage(self.driver)
        main.career_catalog_data()

        with open(self.file, mode='w', encoding='utf-8', newline='') as fd:
            writer = csv.writer(fd, delimiter=',', dialect='excel', lineterminator='\n')
            writer.writerow(['career_name_en', 'career_code', 'faculty_name', 'link_to_career_curriculum']) #Head of the file

            for i, f in enumerate(main.faculty, start=0):
                size = len(main.c_names[i])
                for j in range(0, size):
                    writer.writerow([main.c_names[i][j], main.c_codes[i][j], f, main.c_curriculum[i][j]])

        fd.close()
        self.driver.close()
        print("File '"+ self.file + "' created successfully!")

if __name__ == "__main__":
    search = CareersCatalog()
    search.save()