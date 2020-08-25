# TestSelenium

### Instructions
Install the libraries:
* selenium
* csv

**IMPORTANT:** Install [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to the enviroment variables.

### ESPOL Career Catalog
Inside test_selenium folder, run the program usign:
```sh
$ python career_catalog.py
```

For this program, the *page.py* file uses the XPATH expressions from the *locators.py* file, which are necessary to obtain the desired information about the careers.
On the other hand, the *career_catalog.py* file will allow obtaining the information saved in lists from the *page.py* file in order to save it in a CSV file (*career_catalog.csv*) following the established format.

### Bonus Exercise
Inside test_selenium folder, run the program usign:
```sh
$ python bonus.py
```

This program also uses the XPATH expressions from the *locators.py* file in the *page.py* file to save in lists the information about complementary subjects of each career.
The *bonus.py* file, obtain the information save in the *page.py* file about de subjects, but also gets the information about the careers (similar to previous exercise) because we have to know the link of their curriculums to get and save the information of the complementary subjects in the *bonus.csv* file with the next format (separating the subjects according to each career).

'code', 'complementary_subject_name', 'weekly_hours'



