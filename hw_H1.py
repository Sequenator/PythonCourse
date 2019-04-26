class Zombie:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
    def __str__(self):
        return f'{self.name} имеет {self.HP} HP'

class Survivor(Zombie):
    pass

from time import sleep
from random import randint

surv = Survivor(name= 'Выживший ' + input('Введите имя выжившего: '), HP= 100)
zomb = Zombie(name= 'Зомби', HP= 100)

print('')

print('Выживший столкнулся с зомби, сражение началось!', end= '\n\n')

while True:
    dmg1 = int(randint(10, 25))
    surv.HP = surv.HP - dmg1
    if dmg1 >= 20:
        print(f'Критическое попадание! {zomb.name} откусывает от выжившего кусок плоти и наносит ему {dmg1} урона!')
    else:
        print(f'{zomb.name} кусается и отнимает у выжившего {dmg1} HP')
    print(surv, end= '\n\n')
    sleep(1)
    if surv.HP <= 0:
        print(f'{surv.name} был съеден заживо, сражение завершено!')
        break

    dmg2 = int(randint(10, 25))
    zomb.HP = zomb.HP - dmg2
    if dmg2 >= 20:
        print(f'Критическое попадание! {surv.name} ломает зомби несколько костей арматурой и наносит ему {dmg2} урона!')
    else:
        print(f'{surv.name} отбивается арматурой и отнимает у зомби {dmg2} HP')
    print(zomb, end= '\n\n')
    sleep(1)
    if zomb.HP <= 0:
        print(f'{zomb.name} был забит насмерть (снова), сражение завершено!')
        break
    
    
    
