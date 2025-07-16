from selenium.webdriver.common.by import By

class SearchCustomer:
    text_box_email_id = 'SearchEmail'
    text_box_first_name_id = 'SearchFirstName'
    text_box_last_name_id = 'SearchLastName'
    text_box_company_id = 'SearchCompany'

    search_button_id = 'search-customers'

    serach_results_table_xpath = "//table[@id='customers-grid']"
    search_result_table_rows = "//table[@id='customers-grid']/tbody/tr"
    search_result_table_columns = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.text_box_email_id).clear()
        self.driver.find_element(By.ID, self.text_box_email_id).send_keys(email)

    def setfirst_name(self, name):
        self.driver.find_element(By.ID, self.text_box_first_name_id).clear()
        self.driver.find_element(By.ID, self.text_box_first_name_id).send_keys(name)

    def set_last_name(self, name):
        self.driver.find_element(By.ID, self.text_box_last_name_id).clear()
        self.driver.find_element(By.ID, self.text_box_last_name_id).send_keys(name)

    def set_company(self, company):
        self.driver.find_element(By.ID, self.text_box_company_id).clear()
        self.driver.find_element(By.ID, self.text_box_company_id).send_keys(company)

    def click_search_button(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def getRowcnt(self):
        eles = self.driver.find_elements(By.XPATH, self.search_result_table_rows)
        return len(eles)

    def getColcnt(self):
        eles = self.driver.find_elements(By.XPATH, self.search_result_table_columns)
        return len(eles)

    def search_customer_by_email(self, email):
        flag=False
        for r in range(1, self.getRowcnt()+1):
            txt = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]")
            if txt.text == email:
                flag = True
                break
        return flag

    def search_customer_by_company(self, company_name):
        flag=False
        for r in range(1, self.getRowcnt()+1):
            txt = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[5]")
            if txt.text == company_name:
                flag = True
                break
        return flag



