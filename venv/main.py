import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
def generate_image(prompt):
    # Configuración del Service
    chrome_service = Service(executable_path=r"C:\Users\falet\Desktop\chromedriver.exe")

    # Configuración de las opciones del navegador
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--headless")  # Ejecutar en modo sin cabeza

    # Crear una instancia del navegador con el Service y las opciones
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = "https://deepai.org/machine-learning-model/text2img"
    driver.get(url)

    # Aceptar la política de cookies
    accept_cookies_button = driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv")
    accept_cookies_button.click()

    # Ingresar el prompt
    input_field = driver.find_element(By.CSS_SELECTOR, "textarea.model-input-text-input")
    input_field.send_keys(prompt)

    # Generar la imagen
    generate_button = driver.find_element(By.ID, "modelSubmitButton")
    driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, 100);", generate_button)
    time.sleep(1)
    generate_button.click()
    time.sleep(2) # Esperar a que la imagen se genere (puedes ajustar el tiempo si es necesario)

    # Cerrar la ventana emergente
    close_button = driver.find_element(By.ID, "close")
    close_button.click()

    # Volver a generar la imagen
    generate_button = driver.find_element(By.ID, "modelSubmitButton")
    driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, 100);", generate_button)
    time.sleep(1)
    generate_button.click()
    time.sleep(15) # Esperar a que la imagen se genere (puedes ajustar el tiempo si es necesario)

    # Guardar la imagen generada
    img_element = driver.find_element(By.CSS_SELECTOR, "#place_holder_picture_model > img")
    img_url = img_element.get_attribute("src")

    import urllib.request
    filename = f"generated_image.jpg"
    urllib.request.urlretrieve(img_url, filename)

    print(f"Imagen guardada como {filename}")

    # Cerrar el navegador
    driver.quit()

# Ejemplo de uso
prompt = "Un paisaje de montañas"
#generate_image(prompt)
