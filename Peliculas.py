from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

def buscar_pelicula(titulo):
    # Inicializa el navegador (asegúrate de que la ruta a ChromeDriver sea correcta)
    service = Service(executable_path=r"C:\Users\falet\Desktop\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Navega a la página de inicio de repelis24
    driver.get('https://repelis24.online/')

    # Hacer clic en el icono de la lupa en dispositivos móviles
    lupa = driver.find_element(By.CLASS_NAME, "mobile-search")
    lupa.click()
    time.sleep(1)

    # Encuentra el cuadro de búsqueda e ingresa el título de la película
    cuadro_busqueda = driver.find_element(By.CSS_SELECTOR, 'input.form-control.search-input')
    cuadro_busqueda.send_keys(titulo)
    cuadro_busqueda.send_keys(Keys.RETURN)

    # Espera a que la página de resultados cargue
    time.sleep(3)

    # Extrae los resultados de la búsqueda
    resultados = driver.find_elements(By.CSS_SELECTOR, 'a.ml-mask.jt')

    if resultados:
        print(f'Se encontraron {len(resultados)} resultados para "{titulo}":\n')
        for resultado in resultados:
            pelicula_titulo = resultado.find_element(By.CSS_SELECTOR, 'h2').text
            pelicula_enlace = resultado.get_attribute('href')
            print(f'Título: {pelicula_titulo}')
            print(f'Enlace: {pelicula_enlace}\n')

        # Haz clic en el primer elemento con la clase 'ml-mask jt'
        primer_elemento = resultados[0]
        primer_elemento.click()

        # Espera a que la página de la película cargue
        time.sleep(3)

        # Realiza acciones adicionales aquí, si es necesario (por ejemplo, extraer información de la página de la película)
        pelicula = driver.find_element(By.XPATH, '//*[@id="mv-info"]/a')
        pelicula.click()

        # Espera a que la página cargue
        time.sleep(3)

        # Realiza un desplazamiento hacia abajo en la página
        driver.execute_script("window.scrollBy(0, 375);")

        frames = driver.find_elements(By.TAG_NAME, 'iframe')
        for frame in frames:
            driver.switch_to.frame(frame)
            frame_name = driver.execute_script("return window.name;")
            print("Nombre del marco:", frame_name)
            driver.switch_to.default_content()

        # Obtener el elemento iframe por su atributo src
        iframe = driver.find_element(By.CSS_SELECTOR,
                                     'iframe[src="https://stream.repelis24.online/embed/d0dBVUFQM2NONDlrYWV3WWVxUVhjOEtLWFhORTVYWlcvUWdlUU5ZNG5SOD0="]')

        # Cambiar al contexto del iframe
        driver.switch_to.frame(iframe)
        # Buscar el elemento dentro del iframe
        elemento_provideo = driver.find_element(By.CSS_SELECTOR, 'li.option.servers')

        # Hacer clic en el elemento
        elemento_provideo.click()
        # Volver al contexto predeterminado (fuera del iframe)
        driver.switch_to.default_content()

        time.sleep(8)

        # Esperar a que el elemento esté interactuable
        pelicula_interactuable = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tab1"]'))
        )

        # Hacer clic en el elemento
        pelicula_interactuable.click()

        time.sleep(10)

        # Esperar hasta que aparezca el reproductor de video
        reproductor = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'player')))

        # Cambiar al contexto del iframe del reproductor
        iframe = reproductor.find_element_by_tag_name('iframe')
        driver.switch_to.frame(iframe)

        # Esperar hasta que el tiempo de la película esté disponible (puedes adaptar el selector según la estructura real)
        tiempo_pelicula = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="movie-time"]')))

        # Obtener el texto del elemento que contiene el tiempo de la película
        tiempo = tiempo_pelicula.text

        # Imprimir el tiempo de la película
        print(tiempo)

    else:
        print(f'No se encontraron resultados para "{titulo}".')

    # Cierra el navegador
    driver.quit()

# Realizar búsqueda
buscar_pelicula("matrix")
