import telnetlib

file = open('D:\configuration.txt','r')

comands = file.readlines() #команды
l = len(comands) #количество команд
tell = telnetlib.Telnet('172.17.9.151',4006) #подключение
i=0 #переменная для цикла
for i in range(l): #цикл
	tell.write((comands[i].replace('\n','') + '\n').encode('utf-8'))
	i+=1
tell.interact()
print("stop")
