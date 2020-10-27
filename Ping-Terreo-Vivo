import subprocess
import time
from datetime import datetime
import pymysql

while (True):
    conexao = pymysql.connect(host='10.35.18.40', db='almavivalayout', user='root', passwd='xcpo10tg', port=3306)
    i = 0
    count = 1000
    for i in range(0, 474):
        cursor = conexao.cursor()
        print (count)
        maquina = 'sp0006pa' + str(count)
        print (maquina)
        def ping(host):

            import subprocess, platform

            ping_str = "-n 1 -w 1" if  platform.system().lower()=="windows" else "-c 1"
            args = "ping " + " " + ping_str + " " + host
            need_sh = False if  platform.system().lower()=="windows" else True

            return subprocess.call(args, shell=need_sh) == 0

        if ping(maquina) == True:
            print ('Ok')
            cursor.execute("UPDATE `layout` SET `status`='btn-success' WHERE pa = '"+maquina+"'")
            conexao.commit()
        else:
            print ('falhou')
            cursor.execute("UPDATE `layout` SET `status`='btn-danger' WHERE pa = '"+maquina+"'")
            conexao.commit()
        count += 1
        time.sleep(0.5)
        
    dataAtual = datetime.now()
    dataHora = dataAtual.strftime('%d/%m/%Y %H:%M')
    print(dataHora)

    cursor.execute("UPDATE `relatorio` SET `data`='"+dataHora+"' WHERE 1")
    conexao.commit()
    conexao.close()
    
    time.sleep(900)
