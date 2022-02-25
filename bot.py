import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox import service
import os
import time
import re


class WppBot:
    dir_path = os.getcwd()
    path=r'C:\Users\Transanches\Desktop\Robozap\geckodriver.exe'
    nome_bot="tiago"
    def __init__(self):
       #contruct
       dir_path = os.getcwd()
       self.profile = os.path.join(dir_path, "profile", "wpp")
       self.nome_bot=self.nome_bot
       self.firefox =r'C:\ProgramData\Mozilla-1de4eec8-1241-4177-a864-e594e8d1fb38\updates\308046B0AF4A39CB'
       self.mozila = self.dir_path  +self.path
       self.options = webdriver.FirefoxOptions()
    def conect(self):
        #Conect
        self.driver = webdriver.Firefox()
        self.options.add_argument(r"user-data-dir=" + self.profile)
        self.driver.get("https://web.whatsapp.com/")
        self.driver.implicitly_wait(10)
    def FindContact(self,contact):
        #find contact and send mensage
        self.phaser="oi tiago"
        self.FindBox=self.driver.findElement(By.CLASS_NAME('_13NKt'))
        time.sleep(20)
        self.FindBox.send_keys(contact)
        time.sleep(5)
        self.ClickBox=self.driver.findElement(By.CLASS_NAME('_3vPI2'))
        self.ClickBox.click()
        time.sleep(1)
        self.message=self.driver.findElement(By.XPATH('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'))
        self.message.send_keys(self.phaser)
        self.SendMensage=self.driver.findElement(By.XPATH('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'))
        self.SendMensage.click()
    def greeting(self):
        "first messagem"
        phaser_start="Escolha uma opção:\n"
        option="1-Carga\n2-Pagamento\n"
        time.sleep(5)
        best_wishes=["Bom Dia","Boa Tarde","Boa Noite"]
        i=1
        while True:
            try:
              hour = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div['+str(i)+']/div/div/div/div[2]/div[1]/div[2]')
              hour.click()

              if str(hour.text) > str(5) or str(hour.text) <= str(13):
                  self.gretting = "Olá" + "," + best_wishes[0]

              elif str(hour.text) > str(13) or str(hour.text) <= str(18):
                  self.gretting = "Olá" + "," + best_wishes[1]
              else:
                  self.gretting = "Olá" + "," + best_wishes[2]


              #self.message = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
              #self.message.send_keys(self.gretting + " " + phaser_start + "" + option)
              print(self.gretting + " " + phaser_start + "" + option)
              #self.SendMensage = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
              #self.SendMensage.click()
              print(i)
              i += 1
            except:break

    def Response(self):
        "Response Msg"
        option="3-Adiantamento\n4-Saldo\n"
        data="Digite uma da opções:\nT-Truck\nC-Carreta\nO-outros"
        debit="Para receber o saldo você deve primeiro enviar os comprovantes digitalizado em pdf para o" \
              "E-mail comprovantes@transanches.com.br\nPoderá entrar em contato com\n"
        QuestionType="Digite Qual o Tipo de Carroceria:\nS-Sider\nB-Bau\nA-Aberto\nG-Graneleiro\n"
        SingleAswer="No momento Não Temos Carga:\nDeixe seu Nome\nTipo de Veiculo\nTipo de Carroceria\n" \
                    "Telefone neste formato(xx)xxxxx-xxxx"
        DataDriver=None
        charge="Get database"
        database={}
        BodyType="Para este tipo de caminhão não temos carga\nTemos as seguntes cargas\n",str(database).strip()
        i=1
        hour = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div['+ str(i)+']/div/div/div/div[2]/div[1]/div[2]')
        hour.click()
        post=self.driver.find_element_by_xpath('_22Msk')
        ultimo=len(post)-1
        ReceiverMsg=str(post[ultimo].find_element_by_css('span.selectable-text').text)
        ReceiverMsg2=str(post[ultimo].find_element_by_css('span.selectable-text').text)
        button_clip = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div')
        if ReceiverMsg==str(1) and charge==0:
             "get msg "
             self.message.send_keys(SingleAswer)
             self.SendMensage.click()
             time.sleep(10)
             if ReceiverMsg2!=str(1):
                DataDriver=str(ReceiverMsg2)
        elif ReceiverMsg==str(1) and charge>0:
             self.message.send_keys(data)
             self.SendMensage.click()
        elif ReceiverMsg=="T" or ReceiverMsg=="C" or ReceiverMsg=="O":
            self.message.send_keys(QuestionType)
            self.SendMensage.click()
        elif ReceiverMsg=="S" or ReceiverMsg=="B" or ReceiverMsg=="G":
                 if ReceiverMsg not in database:
                     self.message.send_keys(BodyType)
                     self.SendMensage.click()
                 else:
                     self.message.send_keys(database.get(ReceiverMsg))
                     self.SendMensage.click()
        elif  ReceiverMsg==str(2):
              self.message.send_keys(option)
              self.SendMensage.click()
        elif ReceiverMsg==str(3):
             self.message.send_keys()
             self.SendMensage.click()
        elif ReceiverMsg==str(4):
             self.message.send_keys(debit)
             self.SendMensage.click()
             button_clip.click()
             contact=self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[5]/button/span')
             contact.click()
             FindContat=self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[1]/div/label/div/div[2]')
             FindContat.send_keys("Comprovantes")
             Checklist=self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div')
             Checklist.click()
        i=+1








