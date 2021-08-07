import subprocess
import time
from datetime import datetime
import pymysql

while (True):
    conexao = pymysql.connect(host='***', db='***', user='***', passwd='***', port=3306) #Conexão com o Banco
    i = 0
    count = 1000
    for i in range(0, 474): #474 Loops para passar por todo layout
        cursor = conexao.cursor()      
        maquina = 'sp0006pa' + str(count)        
        def ping(host): #Verifica o Staus da Maquina

            import subprocess, platform

            ping_str = "-n 1 -w 1" if  platform.system().lower()=="windows" else "-c 1"
            args = "ping " + " " + ping_str + " " + host
            need_sh = False if  platform.system().lower()=="windows" else True

            return subprocess.call(args, shell=need_sh) == 0

        if ping(maquina) == True:
            print ('Ok')
            cursor.execute("UPDATE `***` SET `status`='btn-success' WHERE pa = '"+maquina+"'") #Grava maquina Online
            conexao.commit()
        else:
            print ('falhou')
            cursor.execute("UPDATE `***` SET `status`='btn-danger' WHERE pa = '"+maquina+"'") #Grava maquina Offline
            conexao.commit()
        count += 1
        time.sleep(0.5)
        
    dataAtual = datetime.now() #Pega data e Hora 
    dataHora = dataAtual.strftime('%d/%m/%Y %H:%M') #Formata Data e Hora para padrão PT-BR
    print(dataHora)

    cursor.execute("UPDATE `relatorio` SET `data`='"+dataHora+"' WHERE 1") #Grava data e hora no Banco
    conexao.commit()
    conexao.close()
    
    time.sleep(900)
