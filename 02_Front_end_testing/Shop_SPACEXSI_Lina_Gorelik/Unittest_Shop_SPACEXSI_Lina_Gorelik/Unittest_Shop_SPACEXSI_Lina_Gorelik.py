import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import Locator_SPACEXSI_Lina_Gorelik as ls
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import random
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import HtmlTestRunner
#import AllureReports


def delay():
    time.sleep(random.randint(2, 8))


class ChromePositiveSPACEXSI(unittest.TestCase):
    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_TC_P_001(self):
        ls.tc_p_001(self.driver)
        self.driver.quit()

    def test_TC_P_002(self):
        ls.tc_p_002(self.driver)
        self.driver.quit()

    def test_TC_P_003(self):
        ls.tc_p_003(self.driver)
        self.driver.quit()

    def test_TC_P_004(self):
        ls.tc_p_004(self.driver)
        self.driver.quit()

    def test_TC_P_005(self):
        ls.tc_p_005(self.driver)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()


class ChromeNegativeSPACEXSI(unittest.TestCase):
    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_TC_N_001(self):
        ls.tc_n_001(self.driver)
        self.driver.quit()

    def test_TC_N_002(self):
        ls.tc_n_002(self.driver)
        self.driver.quit()

    def test_TC_N_003(self):
        ls.tc_n_003(self.driver)
        self.driver.quit()

    def test_TC_N_004(self):
        ls.tc_n_004(self.driver)
        self.driver.quit()

    def test_TC_N_005(self):
        ls.tc_n_005(self.driver)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()


class FirefoxPositiveSPACEXSI(unittest.TestCase):
    def setUp(self):
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.set_preference("media.hardware-video-decoding.enabled", False)
        options.set_preference("layers.acceleration.disabled", True)
        options.set_preference("gfx.webrender.software", True)
        options.set_preference("browser.sessionstore.resume_from_crash", False)
        options.set_preference("browser.tabs.firefox-view", False)
        options.set_preference("dom.ipc.processCount", 1)
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        # Fallback: if GitHub API rate-limits geckodriver download, use PATH geckodriver
        try:
            service = FirefoxService(GeckoDriverManager().install())
        except Exception:
            print("GeckoDriverManager failed (likely GitHub rate limit), falling back to PATH geckodriver")
            service = FirefoxService()
        self.driver = webdriver.Firefox(service=service, options=options)

    def test_TC_P_001(self):
        ls.tc_p_001(self.driver)
        self.driver.quit()

    def test_TC_P_002(self):
        ls.tc_p_002(self.driver)
        self.driver.quit()

    def test_TC_P_003(self):
        ls.tc_p_003(self.driver)
        self.driver.quit()

    def test_TC_P_004(self):
        ls.tc_p_004(self.driver)
        self.driver.quit()

    def test_TC_P_005(self):
        ls.tc_p_005(self.driver)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()


class FirefoxNegativeSPACEXSI(unittest.TestCase):
    def setUp(self):
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.set_preference("media.hardware-video-decoding.enabled", False)
        options.set_preference("layers.acceleration.disabled", True)
        options.set_preference("gfx.webrender.software", True)
        options.set_preference("browser.sessionstore.resume_from_crash", False)
        options.set_preference("browser.tabs.firefox-view", False)
        options.set_preference("dom.ipc.processCount", 1)
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        # Fallback: if GitHub API rate-limits geckodriver download, use PATH geckodriver
        try:
            service = FirefoxService(GeckoDriverManager().install())
        except Exception:
            print("GeckoDriverManager failed (likely GitHub rate limit), falling back to PATH geckodriver")
            service = FirefoxService()
        self.driver = webdriver.Firefox(service=service, options=options)
        time.sleep(10)

    def test_TC_N_001(self):
        ls.tc_n_001(self.driver)
        self.driver.quit()

    def test_TC_N_002(self):
        ls.tc_n_002(self.driver)
        self.driver.quit()

    def test_TC_N_003(self):
        ls.tc_n_003(self.driver)
        self.driver.quit()

    def test_TC_N_004(self):
        ls.tc_n_004(self.driver)
        self.driver.quit()

    def test_TC_N_005(self):
        ls.tc_n_005(self.driver)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()


class EdgePositiveSPACEXSI(unittest.TestCase):
    def setUp(self):
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # Fallback: if Microsoft CDN is unreachable, use PATH edgedriver
        try:
            service = EdgeService(EdgeChromiumDriverManager().install())
        except Exception:
            print("EdgeChromiumDriverManager failed (network/DNS), falling back to PATH edgedriver")
            service = EdgeService()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.maximize_window()

    def test_TC_P_001(self):
        ls.tc_p_001(self.driver)
        self.driver.quit()

    def test_TC_P_002(self):
        ls.tc_p_002(self.driver)
        self.driver.quit()

    def test_TC_P_003(self):
        ls.tc_p_003(self.driver)
        self.driver.quit()

    def test_TC_P_004(self):
        ls.tc_p_004(self.driver)
        self.driver.quit()

    def test_TC_P_005(self):
        ls.tc_p_005(self.driver)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()


class EdgeNegativeSPACEXSI(unittest.TestCase):
    def setUp(self):
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # Fallback: if Microsoft CDN is unreachable, use PATH edgedriver
        try:
            service = EdgeService(EdgeChromiumDriverManager().install())
        except Exception:
            print("EdgeChromiumDriverManager failed (network/DNS), falling back to PATH edgedriver")
            service = EdgeService()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.maximize_window()
        time.sleep(8)

    def test_TC_N_001(self):
        ls.tc_n_001(self.driver)
        self.driver.quit()

    def test_TC_N_002(self):
        ls.tc_n_002(self.driver)
        self.driver.quit()

    def test_TC_N_003(self):
        ls.tc_n_003(self.driver)
        self.driver.quit()

    def test_TC_N_004(self):
        ls.tc_n_004(self.driver)
        self.driver.quit()

    def test_TC_N_005(self):
        ls.tc_n_005(self.driver)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

# if __name__ == "__main__":
#   unittest.main(AllureReports)