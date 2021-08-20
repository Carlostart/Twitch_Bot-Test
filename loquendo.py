from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# from playsound import playsound
import winsound
import time
import os


class LoquendoBot:
    def __init__(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": os.getcwd() + r'\Temp',
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self.bot = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=options)
        self.bot.get('http://nuancevocalizerexpressive.sodels.com/')

    def decirT(self, text):
        bot = self.bot
        textarea = bot.find_element_by_id('tbTexto')
        textarea.clear()
        textarea.send_keys(text)
        boton = bot.find_element_by_name('bEscuchar')
        boton.click()
        filename = []
        cont = 0
        while not filename and cont <= 5:
            cont += 1
            time.sleep(1)
            filename = os.listdir(os.getcwd()+'/Temp/')

        if filename:
            f = filename.pop()
            print(f)
            # playsound(os.getcwd()+'/Temp/' + f)
            winsound.PlaySound(os.getcwd()+'/Temp/' + f, winsound.SND_FILENAME)
            os.remove(os.getcwd()+'/Temp/' + f)
        else:
            print("Error: Audio LOQUENDO no descargado.")


# b = LoquendoBot()
# b.decirT('hola, esto es un texto de prueba')
# time.sleep(5)
# b.decirT('mariquita el ultimo')
