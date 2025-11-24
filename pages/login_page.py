from playwright.sync_api import Page, Locator

class LoginPage:
    """
    Define el Page Object para la página de inicio de sesión de Sauce Demo.
    Contiene todo los localizadores (Modelo) y las acciones (Controlador).
    """
    def __init__(self, page: Page):
        self.page = page

        # Localizadores de la página de inicio de sesión
        self.username_input: Locator = page.locator("#user-name")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error_message: Locator = page.locator(".error-message-container")

    def navigate(self):
        """Navega a la URL base de la aplicación."""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """Realiza la acción de ingresar credenciales y hacer clic en el botón de login."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """Obtiene el texto del mensaje de error."""
        return self.error_message.inner_text()