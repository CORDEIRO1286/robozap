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
    def ChargeCarga(self):
        self.qtd=int(input("Quantidade de carga para contratação de caminhoneiro digite [0]-Para nenhuma : "))
        self.DataBase={}
        charge=[]
        TypeTruck=None
        star=None
        end=None

        if self.qtd>0:

            for i in range(self.qtd):
                TypeTruck=str.upper(input("Tipo de caminhão:\n[T]-Truck\n[BT]-Bitruck\n[C]-Carreta\n"
                                                 "[CT]-CARRETA TRUCADA\n"
                                                  "[O]-outros\n\n"))
                BodyWork=str.upper(input("Tipo de Carroceria:\n"
                                         "[S]-Sider\n"
                                         "[A]-Aberta\n"
                                         "[B]-Báu\n"
                                         "[G]-Graneleiro"
                                         "[T]-Para Qualquer tipo de Carroceria:\n\n "))

                city=str.upper(input(("Cidade de Embarque:\n")))
                uf=str.upper(input("Estado de Embarque [UF]:\n"))
                star=city+"/"+uf
                city = str.upper(input("Cidade de Desembarque:\n"))
                uf = str.upper(input("Estado de  Dsembarque [UF]:\n\n"))
                end=city+"/"+uf
                weight=float(int(input("Qual o peso:\n\n")))
                size=int(input("Qual o Volume Caso não precisar colocar 0 "))
                if TypeTruck=="T" or TypeTruck=="BT":
                    size_Truck=8.5

                self.DataBase[i]={"out":star,"end":end,"TypeTruck":TypeTruck,"BodyWork":BodyWork,"weight":weight,"size_charge"
                                  :size,"size_min":size_Truck}
        return self.DataBase

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
        data="Digite uma da opções:\n[T]-Truck\n" \
             "[BT]-Bitruck\n[C]-Carreta\n" \
              "[CT]-CARRETA TRUCADA\n"\
              "[O]-outros\n\n"
        debit="Para receber o saldo você deve primeiro enviar os comprovantes digitalizado em pdf para o" \
              "E-mail comprovantes@transanches.com.br\nPoderá entrar em contato com\n"
        QuestionType="Digite Qual o Tipo de Carroceria:\n[S]-Sider\n[B]-Bau\n[A]-Aberto\n[G]-Graneleiro\n"
        SingleAswer="No momento Não Temos Carga:\nDeixe seu Nome\nTipo de Veiculo\nTipo de Carroceria\n" \
                    "Cidade que gostaria de ir\nTelefone neste formato(xx)xxxxx-xxxx use a virgula(,) para separar "

        DataDriver=[]
        DataBase=[] # get Database
        charge=self.qtd
        BodyType="Para este tipo de caminhão não temos carga"
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
                DataDriver.append(str(ReceiverMsg2))
                i+=1
        elif ReceiverMsg==str(1) and charge>0:
             self.message.send_keys(data)
             self.SendMensage.click()
             time.sleep(10)
             if ReceiverMsg2!=str(i):
                for v in self.DataBase.keys():
                    if ReceiverMsg2 in self.DataBase[v]["TypeTruck"]:
                        self.message.send_keys(str(self.DataBase[v]).strip())
                        time.sleep(10)
                        self.message.send_keys("Deseja de ir?\n Para Sim digite [S]\n Para Não digite[N]\n\n")
                        self.SendMensage.click()
                        time.sleep(10)
                        if ReceiverMsg2=="S":
                            self.message.send_keys("Ok\n""Um atendente vai entrar em contato contigo")
                            self.SendMensage.click()
                            i+=1
                        elif ReceiverMsg2=="N":
                            self.message.send_keys(SingleAswer.strip())
                            self.SendMensage.click()
                            time.sleep(10)
                        else:
                            self.message.send_keys("Digite uma opção valida")
                            self.SendMensage.click()
                            i+=1
        i=+1








