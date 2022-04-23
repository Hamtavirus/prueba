import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service as Cservice
from selenium.webdriver.common.by import By
from time import sleep

# El codigo tiene varios sleeps ya que la pagina no deja recorrer si no se hace una espera
# use firefox ya que es el navegador con el que he trabajado mas
# al dar click en buscar me bloquea los resultados, al yo copiar el mismo link en otra ventana 
# que no sea marioneta si me muestra los resultados de la busqueda

URL = "https://www.latamairlines.com"
CHROME_DRIVER = Cservice("C:\Drivers\chrome\chromedriver.exe")
FIREFOX_DRIVER =Service(r"C:\Drivers\firefox\geckodriver.exe")
def main():
    r_url = requests.get(URL)
    if r_url.status_code == 200:
        try:
            firefox = webdriver.Firefox(service=FIREFOX_DRIVER)
            firefox.get(URL)
            sleep(3)
            origen = firefox.find_element(By.XPATH, '//*[@id="txtInputOrigin_field"]')
            origen.send_keys("clo")
            sleep(0.5)
            boton_origen = firefox.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/ul/li/button/div[1]/span[1]')
            boton_origen.click()
            sleep(0.5)
            destino = firefox.find_element(By.XPATH, '//*[@id="txtInputDestination_field"]' )
            destino.send_keys("mia")
            sleep(0.5)
            boton_origen = firefox.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/ul/li[2]/button/div[1]/span[4]')
            boton_origen.click()
            sleep(0.5)
            ida = firefox.find_element(By.XPATH, '//*[@id="departureDate"]')
            ida.click()
            boton_ida = firefox.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[1]/span')
            boton_ida.click()
            sleep(0.5)
            boton_next = firefox.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div[2]')
            boton_next.click()
            sleep(0.5)
            boton_next.click()
            sleep(0.5)
            boton_next.click()
            sleep(0.5)
            boton_next.click()
            sleep(0.5)
            boton_next.click()
            sleep(0.5)
            boton_next.click()
            sleep(0.5)
            vuelta = firefox.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div[4]/div/table/tbody/tr[1]/td[5]/span')
            vuelta.click()
            buscar = firefox.find_element(By.XPATH, '//*[@id="btnSearchCTA"]')
            buscar.click()
        except Exception as error:
            print("Error en main: ", "\n", error)
  
 
if __name__ == "__main__":
    main()

# de igual modo si intento acceder al link de busqueda con chrome no me deja visualizar los resultados
# chrome = webdriver.Chrome(service=CHROME_DRIVER)
# chrome.get(r'https://www.latamairlines.com/co/es/ofertas-vuelos?dataFlight=%7B%22tripTypeSelected%22%3A%7B%22label%22%3A%22Ida+y+Vuelta%22%2C%22value%22%3A%22RT%22%7D%2C%22cabinSelected%22%3A%7B%22label%22%3A%22Economy%22%2C%22value%22%3A%22Economy%22%7D%2C%22passengerSelected%22%3A%7B%22adultQuantity%22%3A1%2C%22childrenQuantity%22%3A0%2C%22infantQuantity%22%3A0%7D%2C%22originSelected%22%3A%7B%22id%22%3A%22CLO_CO_AIRPORT%22%2C%22name%22%3A%22Alfonso+Bonilla+Aragon%22%2C%22city%22%3A%22Cali%22%2C%22cityIsoCode%22%3A%22CLO%22%2C%22country%22%3A%22Colombia%22%2C%22iata%22%3A%22CLO%22%2C%22latitude%22%3A3.54322%2C%22longitude%22%3A-76.3816%2C%22timezone%22%3A-5%2C%22tz%22%3A%22America%2FBogota%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22CO%22%2C%22allAirportsText%22%3Anull%2C%22airportIataCode%22%3A%22CLO%22%7D%2C%22destinationSelected%22%3A%7B%22id%22%3A%22MIA_US_AIRPORT%22%2C%22name%22%3A%22Miami+Intl.%22%2C%22city%22%3A%22Miami%22%2C%22cityIsoCode%22%3A%22MIA%22%2C%22country%22%3A%22Estados+Unidos%22%2C%22iata%22%3A%22MIA%22%2C%22latitude%22%3A25.79319953918457%2C%22longitude%22%3A-80.29060363769531%2C%22timezone%22%3A-4%2C%22tz%22%3A%22America%2FNew_York%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22US%22%2C%22allAirportsText%22%3Anull%2C%22airportIataCode%22%3A%22MIA%22%7D%2C%22dateGoSelected%22%3A%222022-05-02T17%3A00%3A00.000Z%22%2C%22dateReturnSelected%22%3A%222022-12-02T17%3A00%3A00.000Z%22%2C%22redemption%22%3Afalse%7D')