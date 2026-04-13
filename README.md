![Tests](https://github.com/brovkinas/playwright-python-autotest/actions/workflows/tests.yml/badge.svg)

# UI Test Automation (Playwright + Pytest)

## 📌 Описание проекта
Демонстрационный проект автоматизации UI тестирования веб-приложения.

---

## 💡 Что демонстрирует проект

- построение UI automation framework на базе Playwright + Pytest
- реализацию Page Object Model с разделением ответственности
- использование pytest fixtures для управления состоянием тестов
- интеграцию CI/CD (GitHub Actions + Allure reporting)

---

## 🔍 Тестируемое приложение

Демо-сайт: https://the-internet.herokuapp.com  

---

## 🧰 Стек

- Python  
- Playwright  
- Pytest  
- Allure (reporting)  
- Page Object Model  

---

## 🧠 Почему Playwright

- встроенные auto-wait механизмы
- стабильность UI тестов
- поддержка нескольких браузеров из коробки

---

## 🏗 Архитектура проекта

- `pages/` — Page Objects (инкапсуляция UI-логики)
- `tests/` — тестовые сценарии (без UI-деталей, только бизнес-логика)
- `conftest.py` — фикстуры:
  - browser/page lifecycle
  - setup/teardown
- `utils/` — вспомогательные функции
- `test_data/` — тестовые данные

---

## 🌿 Branches

- `main` — стабильная версия проекта  
- `allure-report` — публикация отчётов тестирования (GitHub Pages)  

Используется упрощённый workflow, приближенный к реальному процессу разработки (разделение стабильной версии и артефактов тестирования).

---

## 📊 Test Report (Allure)

Проект включает генерацию Allure-отчётов с результатами выполнения автотестов.

🔗 https://brovkinas.github.io/playwright-python-autotest/

---

## ▶️ Запуск проекта

```bash```
pip install -r requirements.txt

### запуск всех тестов
pytest

### запуск в headed режиме
pytest --headed

### запуск в конкретном браузере
pytest --browser=chromium

---

## ⚙️ CI/CD

GitHub Actions pipeline:
- запуск тестов в CI окружении
- генерация Allure отчёта
- публикация отчёта через GitHub Pages

---

## ✅ Тестовое покрытие

### Авторизация
- позитивный сценарий (валидные креды)
- негативные сценарии:
  - неверные данные
  - пустые поля
- проверка сообщений об ошибках

### UI проверки
- наличие ключевых элементов
- корректность отображения

### Негативные сценарии
- валидация форм
- обработка некорректных данных

---

## 🧪 Пример теста

Тесты используют фабрику страниц для централизованного создания Page Objects.

@pytest.mark.regression

@allure.epic("Authentication")

@allure.feature("Login by username and password")

@allure.story("Login error: username")

def test_invalid_username_login(pages):

    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.user_login(get_user(UserRole.USER_WRONG_NAME))
    login_page.should_have_invalid_username_error()

---

## 📄 Пример Page Object

Используются обёртки над элементами (Input, Button) для переиспользования логики и улучшения читаемости тестов.

@register_page(PageType.LOGIN)
class LoginPage(BasePage):

    URL = "/login"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

        self.username_input = Input(page.locator("#username"), "Username input")
        self.password_input = Input(
            page.locator("#password"), "Password input", is_secret=True
        )
        self.login_button = Button(
            page.locator("button[type='submit']"), "Login button"
        )
        self.login_flash_message = BaseElement(page.locator("#flash"), "Flash message")

    @allure.step(f"Open login page")
    def open(self):
        super().open(self.URL)

---

## ⚠️ Ограничения

- проект использует демо-сайт (не production)
- ограниченное покрытие (фокус на демонстрации подхода)
- отсутствуют API тесты
