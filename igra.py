import random
import time
import os
lvl = 1   #первый уровень
n=3  #количество начальных слов и времени
verno = True
com = '.'  #точки во время загрузки
s=1     # для цикла for
stop = 'СТОП'
exit = 'выход'
zanovo = True


fs = open('data.txt', encoding='utf-8') #открываем файл, раскодируем русскоязычные символы
a = fs.readlines() #переводим в строки

print('Hello!')
print('Write your nickname and tap enter to start!')
nick = input()

for s in range(4):
    print('Loading', com*s)
    os.system('cls')
time.sleep(2)
for s in range(4):
    print('Wait', com*s)
    os.system('cls')
time.sleep(2)
print('\n')
print('Your stop-word is ', stop)
time.sleep(3)
print('\n')

q = []
for k in a:
    q.append(k[:-1])       #удаляет энтер
while verno == True:
    while zanovo == True:
        print('Start!')
        time.sleep(1)
        print('\n')
        while True:
            s = random.sample(q, n)     #выбирает несколько слов из списка
            for i in s:
                print (i, end = " ")
            print()
            time.sleep(n)
            os.system('cls')                        #очистка поля
            polz = input('Enter words\n').split()
            if polz == [stop]:              #стоп-слово
                verno = False
                print('Your level : ', lvl, 'See your soon :)')
                print('\n')
                print('Tap enter to return! Write выход if you want to exit\n')
                if input()== 'выход':
                    zanovo = False
                lvl=1
                n = 3
                break
                continue
            elif set(s) == set(polz):
                n=n+1
                lvl=lvl+1
                if lvl % 3 == 0 :
                    print('Good job , ', nick, ' !' )
                elif lvl % 4 == 0:
                    print('Keep it up!')
                else:
                    print('True!')
                    time.sleep(2)
                    os.system('cls')
            else:
                verno = False
                print('sorry ¯\_(ツ)_/¯ loser')
                print('Your level', lvl)
                print('\n')
                print('Tap double enter to return! Write выход if you want to exit \n')
                lvl = 1
                n = 3
                if input()== 'выход':
                    zanovo = False
                break
        input()


