import pytest
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

screenshot_dir = r"C:\\Users\\menca\Documents\selenium"


edge_driver_path = r"C:\dEdge\msedgedriver.exe"


edge_options = Options()
options = webdriver.EdgeOptions()

@pytest.fixture
def driver():
   
    driver = webdriver.Edge(executable_path=edge_driver_path, options=options)
    yield driver
   
    driver.quit()

  
def save_screenshot(driver, name):
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    screenshot_dir_abs = os.path.abspath(screenshot_dir)  
    print(f"Guardando captura de pantalla en: {screenshot_dir_abs}")

    timestamp = time.strftime('%Y%m%d%H%M%S')
    screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path

def test_instagram_workflow(driver):
    
    driver.get("https://www.instagram.com")
    screenshot_path = save_screenshot(driver, "instagram_home")
    time.sleep(5)


driver = webdriver.Edge(options=edge_options)



driver.get("https://www.instagram.com")

time.sleep(5)
#save_screenshot(driver, "instagram")


driver.get("https://www.instagram.com/accounts/login/")


time.sleep(5)


usuario = driver.find_element(By.NAME, "username")
contraseña = driver.find_element(By.NAME, "password")
usuario.send_keys("misaelencarnacionjavier@hotmail.com")
contraseña.send_keys("tokioghoul1")
usuario.send_keys(Keys.ENTER)
#save_screenshot(driver, "instagram_login")



time.sleep(5)
save_screenshot(driver, "instagram_loginerer")


driver.get("https://www.instagram.com/accounts/edit/")


time.sleep(5)
#save_screenshot(driver, "instagram_account_settings")

driver.get("https://www.instagram.com/direct/inbox/")


time.sleep(5)
#save_screenshot(driver, "instagram_direct_messages")

driver.get("https://www.instagram.com/reels/C3ROC72uad4/")
#save_screenshot(driver, "instagram_direct_reels")





time.sleep(5)
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])

driver.close()