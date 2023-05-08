from selenium.webdriver.common.by import By


class Test_b():
    def test_4(self):
        a = 1000
        b = 20
        c = a - b
        if c == 980:
            assert True
        else:
            assert False

    # def test_google(self):
    #     from selenium import webdriver
    #     google = webdriver.Chrome()
    #     google.get("https://www.google.com/")
    #     logo =google.find_element(By.XPATH ,"//img[@alt='Google']").is_displayed()
    #     if logo == True:
    #        assert True
    #        print("yes i am on google home page")
    #     else :
    #         assert False