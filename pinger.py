import os

os.system("clear")
adress = input("IP/Host Girin  : ")
i = 1

for count in range(100):
    os.system("clear")
    print((i) , ". Ping Başladı")
    os.system("ping " + (adress))
    sleep(0)
    i+=1

