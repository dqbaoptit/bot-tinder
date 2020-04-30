from selenium import webdriver
from time import sleep
class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = ''
        self.password = ''
    def open(self):
        self.driver.get('https://tinder.com')
        try:
            acp_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            acp_btn.click()
        except: 
            pass
        sleep(3)

    def log_fb(self):
        # if self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button') :
        #     more_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        #     more_btn.click()
        #     sleep(2)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        number_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        number_in.send_keys(self.username)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(self.password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(5)

    def cancel_pop(self):
        # handle pop-up
        popup_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        sleep(5)
    def cancel_set_loca(self):

        popup_3 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
        popup_3.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()
        
    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()



if __name__ == "__main__": 
    bot = Bot()
    bot.open()
    bot.log_fb()
    sleep(5)
    bot.cancel_pop()
    sleep(5)
    bot.cancel_set_loca()
    bot.auto_swipe()