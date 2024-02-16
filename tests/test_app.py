from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

# Usei o nome correto "webdriver.Chrome()"
driver = webdriver.Chrome()

driver.set_page_load_timeout(5)

try:
    driver.get("http://localhost:8501")
    sleep(5)
    print("Acessou a página com sucesso")
except TimeoutException:
    print("Não acessou!")
finally:
    # Certifique-se de fechar o driver, independentemente do resultado
    driver.quit()
