class presence_of_num_elements:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        # print(self.number)
        els = driver.find_elements(*self.locator)
        # print(len(els))
        if len(els) == self.number and els[0].is_displayed() and els[1].is_displayed():
            return els