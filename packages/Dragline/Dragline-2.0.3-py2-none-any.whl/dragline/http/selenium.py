from __future__ import absolute_import
from Queue import Queue, Empty
from selenium import webdriver
from datetime import timedelta
from dragline import runtime
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


class Driver(object):
    def __len__(self):
        return 0

    @property
    def content(self):
        return self.page_source

    @property
    def url(self):
        return self.current_url

    @property
    def elapsed(self):
        return timedelta()


class Remote(webdriver.Remote, Driver):
    pass


class FirefoxDriver(webdriver.Firefox, Driver):
    pass


class ChromeDriver(webdriver.Chrome, Driver):
    pass


class PhantomJSDriver(webdriver.PhantomJS, Driver):
    pass


class Browser(object):
    def get_driver(self, **kwargs):
        return Remote(**kwargs)

    def __init__(self):
        self.browsers = Queue()

    def get_response(self, url, **kwargs):
        try:
            browser = self.browsers.get(block=False)
        except Empty:
            proxy = runtime.settings.SELENIUM_ARGS.get('proxy')
            if proxy:
                proxy = Proxy({
                    'proxyType': ProxyType.MANUAL,
                    'httpProxy': proxy,
                })
                browser = self.get_driver(proxy=proxy)
            else:
                browser = self.get_driver()
        browser.get(url)
        return browser

    def put_response(self, browser):
        self.browsers.put(browser)

    def clear(self):
        while True:
            try:
                browser = self.browsers.get(block=False)
                browser.close()
            except Empty:
                break


class Headless(Browser):
    def __init__(self):
        from xvfbwrapper import Xvfb
        self._vdisplay = Xvfb()
        self._vdisplay.start()
        super(Headless, self).__init__()

    def clear(self):
        super(Headless, self).clear()
        self._vdisplay.stop()


class Chrome(Browser):
    def get_driver(self, **kwargs):
        return ChromeDriver(**kwargs)


class ChromeX(Headless, Chrome):
    pass


class Firefox(Browser):
    def get_driver(self, **kwargs):
        firefoxProfile = FirefoxProfile()
        # Disable CSS
        firefoxProfile.set_preference('permissions.default.stylesheet', 2)
        # Disable images
        firefoxProfile.set_preference('permissions.default.image', 2)
        # Disable Flash
        firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        kwargs['firefox_profile'] = firefoxProfile
        return FirefoxDriver(**kwargs)


class FirefoxX(Headless, Firefox):
    pass


class PhantomJS(Browser):
    def get_driver(self, **kwargs):
        return PhantomJSDriver(**kwargs)
