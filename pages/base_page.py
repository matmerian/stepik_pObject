<<<<<<< HEAD
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
=======
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
>>>>>>> 17a66aff293163a5d57929d46876165dc62807e6
        self.browser.get(self.url)