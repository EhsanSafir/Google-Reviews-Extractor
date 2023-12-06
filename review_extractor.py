import time

from openpyxl import Workbook
from selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import clean_rated_value, extract_url_from_style, generate_file_name_base_on_url


class SelectorRepo:
    REVIEW_FORM = (By.CLASS_NAME, 'AVvGRc')
    REVIEW_TAB = (By.LINK_TEXT, 'Reviews')
    REVIEW_CARD = (By.CLASS_NAME, 'gws-localreviews__google-review')
    REVIEW_CARD_REVIEWER = (By.CSS_SELECTOR, '.TSUbDb a')
    REVIEW_CARD_RATE = (By.CSS_SELECTOR, '[aria-label^="Rated "]')
    REVIEW_CARD_TEXT = (By.CSS_SELECTOR, 'span[data-expandable-section]')
    REVIEW_DATA_FETCHER = (By.CSS_SELECTOR, 'div[data-async-context][data-async-trigger]')
    REVIEW_PHOTOS = (By.CSS_SELECTOR, 'div[aria-label="Photos"]')


class GoogleReviewExtractor:
    def __init__(self, review_full_url, pagination_request_count=130, timeout=120):
        self._timeout = timeout
        self._pagination_request_count = pagination_request_count
        self._review_full_url = review_full_url
        self._selector_repo = SelectorRepo
        self._extracted_reviews = []
        self._excel_header = ['reviewer', 'reviewer_rate', 'review_text', 'review_images']

    def _show_full_review_text(self):
        js_script = ("document.querySelectorAll('.review-full-text, .k8MTF').forEach(element => { "
                     "element.style.display = 'block' });")
        self._driver.execute_script(js_script)

    def start_scrapping(self):
        try:
            self._start_web_driver()
            self._driver.get(self._review_full_url)
            self._select_review_tab()
            self._data_trigger()
            self._show_full_review_text()
            all_reviews = self._get_reviews()
            self._create_data_structure(all_reviews)
            self._export_as_excel_file()
        finally:
            if self._driver:
                self._driver.quit()

    def _setup_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

    def _start_web_driver(self):
        self._driver = self._setup_driver()
        self._web_driver_wait = WebDriverWait(self._driver, self._timeout)
        print("[x] Driver is started")

    def _select_review_tab(self):
        print("[x] Web page is  loading ...")
        self._web_driver_wait.until(
            EC.element_to_be_clickable(self._selector_repo.REVIEW_FORM)
        )
        review_form = self._driver.find_element(*self._selector_repo.REVIEW_FORM)
        print("[x] Review popup is found")
        # select review tab
        self._web_driver_wait.until(
            EC.element_to_be_clickable(self._selector_repo.REVIEW_TAB)
        )
        review_tabs = review_form.find_element(*self._selector_repo.REVIEW_TAB)
        review_tabs.click()
        print("[x] Reviews tab  is selected")

    def _data_trigger(self):

        try:
            element = self._web_driver_wait.until(
                EC.element_to_be_clickable(self._selector_repo.REVIEW_DATA_FETCHER)
            )
            print("[x] Data trigger found")
            for _ in range(self._pagination_request_count):
                element.click()
                time.sleep(2)
                print(f"\t[x] Data triggered for page {_}")
        except (ElementNotInteractableException, ElementClickInterceptedException):
            pass
        finally:
            print(f"[x] All data triggered ")

    def _get_reviews(self):
        self._web_driver_wait.until(
            EC.presence_of_element_located(self._selector_repo.REVIEW_CARD)
        )

        reviews_elements = self._driver.find_elements(*self._selector_repo.REVIEW_CARD)
        print(f"[x] Reviews Elements selected ")
        return reviews_elements

    def _create_data_structure(self, all_reviews):
        for review in all_reviews:
            reviewer = review.find_element(*self._selector_repo.REVIEW_CARD_REVIEWER).text
            review_rate = review.find_element(*self._selector_repo.REVIEW_CARD_RATE).get_attribute('aria-label')
            try:
                review_text = review.find_element(*self._selector_repo.REVIEW_CARD_TEXT).text
            except NoSuchElementException:
                review_text = ''
            review_rate = clean_rated_value(review_rate)
            review_images = [extract_url_from_style(item.get_attribute('style')) for item in
                             review.find_elements(*self._selector_repo.REVIEW_PHOTOS)]
            review_images = ' || '.join(review_images)
            self._extracted_reviews.append(
                {'reviewer': reviewer, 'reviewer_rate': review_rate, 'review_text': review_text,
                 'review_images': review_images})
        print(f"[x] Data Structure Created")

    def _export_as_excel_file(self):
        wb = Workbook()
        ws = wb.active
        ws.append(self._excel_header)

        for row_data in self._extracted_reviews:
            row_values = [row_data[field] for field in self._excel_header]
            ws.append(row_values)

        excel_file_path = f"{generate_file_name_base_on_url(self._review_full_url)}.xlsx"
        wb.save(excel_file_path)
        print(f"[x] Excel File created")

    def get_extracted_reviews(self):
        return self._extracted_reviews
