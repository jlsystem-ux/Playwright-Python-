import sys
import os

# --- INICIO DE LA SOLUCIÓN DE RUTA (NECESARIA POR CONFIGURACIÓN LOCAL) ---
# Esta sección fuerza al intérprete de Python a incluir la carpeta raíz del proyecto
# en el PATH de búsqueda, permitiendo la importación de 'pages.login_page'.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0, project_root)
# --- FIN DE LA SOLUCIÓN DE RUTA ---

from playwright.sync_api import Page
from pages.login_page import LoginPage  # Importamos la clase del otro archivo


def test_successful_login(page: Page):
    """
    Escenario de prueba: Verifica el inicio de sesión exitoso y la navegación
    a la página de inventario.
    """
    # 1. Inicializar el Page Object
    login_page = LoginPage(page)

    # 2. Definir los pasos del escenario usando los métodos del PO
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 3. Aserción y Generación de Evidencia
    # Verificamos que hemos sido redirigidos a la página de inventario
    assert "/inventory.html" in page.url

    # Genera la captura de pantalla como evidencia para el reclutador
    page.screenshot(path="artefactos/login_exitoso.png")
    print("\n✅ Prueba de inicio de sesión exitoso PASSED.")


def test_failed_login(page: Page):
    """
    Escenario de prueba: Verifica que el inicio de sesión falla con credenciales
    inválidas y que se muestra el mensaje de error correcto.
    """
    # 1. Inicializar el Page Object
    login_page = LoginPage(page)

    # 2. Definir los pasos del escenario
    login_page.navigate()
    login_page.login("usuario_invalido", "clave_incorrecta")

    # 3. Aserción
    expected_error = "Epic sadface: Username and password do not match any user in this service"

    # Verificamos que el mensaje de error del PO es el esperado
    assert login_page.get_error_message() == expected_error
    print("\n✅ Prueba de inicio de sesión fallido PASSED.")