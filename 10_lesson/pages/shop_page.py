from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver, url):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = url

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу иагазина.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация на странице магазина")
    def login(self, username, password):
        """
        Авторизация на странице магазина.

        :param username: int — вводит логин,
        :param password: int — вводит пароль.
        """
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, product_name):
        """
        Добавление товара в корзину.

        :product_name: int — выбор товара по наименованию.

        """
        self.driver.find_element(
            By.XPATH, f"//button[text()='Add to cart' and '{product_name}']").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие на кнопку Checkout")
    def button_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step("Проверка товаров в корзине")
    def verify_cart_contents(self, expected_items):
        """
        Проверка товаров в корзине.

        :expected_items: int — товар, который должен быть в корзинне.

         """
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        actual_items = [item.text for item in cart_items]
        for item in expected_items:
            assert item in actual_items, f"Товар {item} отсутствует в корзине"


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver


@allure.step("Заполнение своих данных")
def fill_form(self, first_name, last_name, postal_code):
    """
    Заполнение своих данных.

    :first_name: int — ввод имени,
    :last_name: int — ввод фамилии,
    :postal_code: int — ввод индекса почтивой доставки.

     """
    self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
    self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
    self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
    self.driver.find_element(By.ID, 'continue').click()


@allure.step("Проверка итоговой суммы")
def verify_total(self, expected_total):
    """
    Проверка итоговой суммы.

    :expected_total: int — итоговая сумма, которая должна быть в корзине.

    """
    total_element = self.driver.find_element(
        By.CLASS_NAME, 'summary_total_label')
    actual_total = total_element.text.split("$")[-1]
    assert actual_total == expected_total, f"Итоговая стоимость{actual_total} не совпадает с ожидаемой {expected_total}"
