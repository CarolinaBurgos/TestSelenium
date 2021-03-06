from selenium import webdriver
import csv
import page

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
            #writer.writerow(['career_name_en', 'code', 'complementary_subject_name', 'weekly_hours']) #Head of the file
            writer.writerow(['code', 'complementary_subject_name', 'weekly_hours'])  # Head of the file

            for i, f in enumerate(main.faculty, start=0):
                size = len(main.c_names[i])
                for j in range(0, size):
                    self.driver.get(main.c_curriculum[i][j])

                    current = page.MainPage(self.driver)
                    current.electives_subjects()

                    writer.writerow([])
                    writer.writerow(['      CAREER NAME: ' + main.c_names[i][j]])

                    size = len(current.s_name)
                    for k in range(0, size):
                        #writer.writerow([main.c_names[i][j], current.s_code[k], current.s_name[k], current.s_hours[k]])
                        writer.writerow([current.s_code[k], current.s_name[k], current.s_hours[k]])

        fd.close()
        self.driver.close()
        print("File " + self.file + " created successfully!")

if __name__ == "__main__":
    search = ComplementarySubjects()
    search.save()