from random import randint, choice
from os import system

class Item:
    def __init__(self, charcsTpl):
        self.Type = charcsTpl[0]
        self.Buff = charcsTpl[1]
        self.Debuff = charcsTpl[2]
        self.Compatibility = charcsTpl[3]
        self.isEqiupped = False
        self.Owner = None

CHARS = []
MOVE  = {}
TYPES = [
    #((миндмг, максдмг), оз, мтк, крит, додж, зщт, скр, имя)
    ((4, 9), 27, 75, 8, 0, 0, 3, 'Арбалетчица'),
    ((5, 10), 25, 66, 5, 5, 0, 5, 'Наёмник'),
    ((6, 12), 33, 80, 5, 5, 0, 1, 'Крестоносец'),
    ((5, 10), 22, 91, 6, 10, 1, 5, 'Разбойник'),
    ((5, 10), 31, 70, 4, 5, 0, 3, 'Воитель'),
    ((4, 7), 19, 78, 8, 10, 2, 6, 'Оккультист'),
    ((4, 7), 22, 88, 3, 5, 1, 7, 'Чумной доктор'),
    ((4, 7), 19, 77, 8, 5, 0, 7, 'Шут'),
]
ITEMS = [
    # (тип, бафф, дебафф, совместимость)
    ('chestplate', '3 DMG', '1 HP', '>7 DMG'),
    ('boots', '5 SPD', '3 DDG', '>2 CRT'),
    ('boots', '5 DDG', '3 SPD', '=5 CRT'),
]

INVENTORY = []

class Person:
    global CHARS
    def __init__(self, charcsTpl : tuple, Enemy : bool):
        global CHARS
        self.Dmg = charcsTpl[0]
        self.Hp = charcsTpl[1]
        self.MaxHP = charcsTpl[1]
        self.Accuracy = charcsTpl[2]
        self.Crit = charcsTpl[3]
        self.Dodge = charcsTpl[4]
        self.Protection = charcsTpl[5]
        self.Speed = charcsTpl[6]
        self.Type = charcsTpl[7]
        self.Enemy = Enemy
        self.Equipped = []
        CHARS.append(self)

    @staticmethod
    def getobjbyname(name):
        global CHARS
        for i in CHARS:
            if (i.Name == name):
                return i
        else:
            return False

    @staticmethod
    def namethem():
        global CHARS
        for self in CHARS:
            self.Name = CHARS.index(self)

    @staticmethod
    def view(ctx = ctx):
        global CHARS
        await ctx.send('...................................................')
        sentence = ''
        for i in CHARS:
            if (i.Enemy == False):
                sentence += str(i.Name) + ' '
        sentence += '\/ '
        for i in CHARS:
            if (i.Enemy == True):
                sentence += str(i.Name) + ' '
        await ctx.send(sentence)
        await ctx.send('...................................................')

    @staticmethod
    def setmove():
        global CHARS
        global MOVE
        MOVE = {}
        temp = []
        for i in CHARS:
            temp.append(i)
        for i in range(1, len(CHARS) + 1):
            j = choice(temp)
            MOVE[i] = j
            temp.remove(j)

    @staticmethod
    def create_teams(these : int, those : int):
        global TYPES
        global CHARS
        CHARS = []
        for i in range(these):
            Person(choice(TYPES), False)
        for i in range(those):
            Person(choice(TYPES), True)

    def equip(self, ctx = ctx, item : Item):
        if (self.Enemy == False):
            if (item.isEqiupped != True):
                if not (item.Type in self.Equipped):
                    CharcsDict = {'HP' : self.MaxHP, 'DMG' : self.Dmg[1], 'DDG' : self.Dodge, 'PRT' : self.Protection, 'SPD' : self.Speed, 'CRT' : self.Crit}
                    CondList = ['<', '>', '=']
                    buffprr = item.Buff[item.Buff.index(' ') + 1:]
                    def buff(self, item, prm, CharcsDict = CharcsDict, buffprr = buffprr):
                        if (prm == '+'):
                            await ctx.send('...................................................')

                            await ctx.send(f'{str(self.Name)} получил бафф {buffprr} от экипировки.')
                            buffval = int(item.Buff[:item.Buff.index(' ')])
                            await ctx.send(f'Старый параметр: {str(CharcsDict[buffprr])} {buffprr}.')
                            CharcsDict[buffprr] += buffval
                            await ctx.send(f'Новый параметр: {str(CharcsDict[buffprr])} {buffprr}.')

                            await ctx.send('...................................................')
                        elif (prm == '-'):
                            buffprr = item.Debuff[item.Debuff.index(' ') + 1:]
                            await ctx.send(f'{str(self.Name)} подвергся негативному воздействию на {buffprr}.')
                            buffval = int(item.Debuff[:item.Debuff.index(' ')])
                            await ctx.send(f'Старый параметр: {str(CharcsDict[buffprr])} {buffprr}.')
                            CharcsDict[buffprr] -= buffval
                            await ctx.send(f'Новый параметр: {str(CharcsDict[buffprr])} {buffprr}.')

                            await ctx.send('...................................................')

                    if (item.Compatibility[0] == CondList[0]):
                        # if (self.Hp < compatible (fe <10))
                        if (CharcsDict[item.Compatibility[item.Compatibility.index(' ') + 1:]] < int(item.Compatibility[1:item.Compatibility.index(' ')])):
                            buff(self, item, '+')
                            if (item.Debuff):
                                buff(self, item, '-')

                            item.isEqiupped = True
                            item.Owner = self
                            self.Equipped.append(item.Type)
                        else:
                            await ctx.send(f'Похоже, {str(self.Name)} не совместим с данным предметом.')
                    elif (item.Compatibility[0] == CondList[1]):
                        if (CharcsDict[item.Compatibility[item.Compatibility.index(' ') + 1:]] > int(item.Compatibility[1:item.Compatibility.index(' ')])):
                            buff(self, item, '+')
                            if (item.Debuff):
                                buff(self, item, '-')

                            item.isEqiupped = True
                            item.Owner = self
                            self.Equipped.append(item.Type)
                            return True

                        else:
                            await ctx.send(f'Похоже, {str(self.Name)} не совместим с данным предметом.')
                    elif (item.Compatibility[0] == CondList[2]):
                        if (CharcsDict[item.Compatibility[item.Compatibility.index(' ') + 1:]] == int(item.Compatibility[1:item.Compatibility.index(' ')])):
                            buff(self, item, '+')
                            if (item.Debuff):
                                buff(self, item, '-')

                            item.isEqiupped = True
                            item.Owner = self
                            self.Equipped.append(item.Type)
                            return True

                        else:
                            await ctx.send(f'Похоже, {str(self.Name)} не совместим с данным предметом.')
                    else:
                        await ctx.send('[!] Недопустимый знак сравнения в условии совместмости предмета.')
                else:
                    await ctx.send('Предмет этого типа уже экипирован на персонаже.')
            else:
                await ctx.send(f'Предмет уже экипирован на {str(item.Owner.Name)}.')
        else:
            await ctx.send('Вы выбрали недопустимую цель для экипировки.')

    def attack(self, ctx = ctx, other):
        if (self.Enemy != other.Enemy):
            dmg = randint(self.Dmg[0], self.Dmg[1])
            await ctx.send(f'{str(self.Name)} атаковал {str(other.Name)}. ')
            misschance = randint(1, 100)
            for i in range(100 - self.Accuracy):
                if (i == misschance):
                    await ctx.send(f'{str(self.Name)} промахивается!\nЗдоровье {str(other.Name)} составляет {str(other.Hp)}/{str(other.MaxHP)} HP.')
                    await ctx.send('...................................................')
                    return

            dodgechance = randint(1, 100)
            for i in range(self.Dodge):
                if (i == dodgechance):
                    await ctx.send(f'{str(other.Name)} уклоняется от атаки.\nЕго здоровье составляет {str(other.Hp)}/{str(other.MaxHP)} HP.')
                    await ctx.send('...................................................')
                    Person.view()
                    return

            crit = False
            critchance = randint(1, 100)
            for i in range(self.Crit):
                if (i == critchance):
                    crit = True

            other.Hp -= dmg
            await ctx.send(f'У {str(other.Name)} осталось {str(other.Hp)}/{str(other.MaxHP)} HP.')

            if (crit):
                other.Hp -= dmg
                await ctx.send(f'КРИТ! У {other.Name} теперь {str(other.Hp)}/{str(other.MaxHP)} HP')
            if (other.Hp <= 0):
                await ctx.send(f'{str(other.Name)} погиб.')
                CHARS.remove(other)
            await ctx.send('...................................................')
            await ctx.send('___________________________________________________')

            Person.view()
        else:
            await ctx.send('Нельзя атаковать своих!')
            await ctx.send('Кого вы хотите атаковать?')
            channel = ctx.message.channel
            author = ctx.message.author
            def check(message):
                return (message.channel == channel and message.author == author)
            msg = await bot.wait_for('message', check = check)
            self.attack(gobn(int(msg.content)))
            # self.attack(gobn(int(input('Кого вы хотите атаковать?: '))))

    @staticmethod
    def round(ctx = ctx):
        global CHARS
        global MOVE
        Person.setmove()
        for i in range(1, len(MOVE) + 1):
            i = MOVE[i]
            if (i in CHARS):
                await ctx.send(f'{str(i.Name)} атакует!')
                if (i.Enemy == False):
                    ischoosed = False
                    while (ischoosed == False):
                        await ctx.send('Выбор: Просмотреть [И]нвентарь, [П]роинспектировать, [А]таковать\n:')
                        channel = ctx.message.channel
                        author = ctx.message.author
                        def check(message):
                            return (message.channel == channel and message.author == author)
                        choose = await bot.wait_for('message', check = check)
                        choose = choose.content
                        # choose = input('Выбор: Просмотреть [И]нвентарь, [П]роинспектировать, [А]таковать\n:')
                        await ctx.send('...................................................')
                        if (choose.lower().startswith('а')):
                            attacked = await bot.wait_for('message', check = check)
                            attacked = int(attacked.content)
                            # attacked = int(input('Кого вы хотите атаковать?: '))
                            if (gobn(attacked)):
                                i.attack(gobn(attacked))
                                ischoosed = True
                            else:
                                await ctx.send('Не существует такого персонажа, которого вы хотите атаковать.')
                        elif (choose.lower().startswith('и')):
                            if (INVENTORY != []):
                                for j in INVENTORY:
                                    await ctx.send(f'{str(INVENTORY.index(j))}: TYPE: {j.Type}, BUFF: {j.Buff}, DEBUFF: {j.Debuff}, CMPT: {j.Compatibility}')
                                iischoosed = False
                                while (iischoosed == False):
                                    chooose = input('Выбор: [И]спользовать предмет по индексу, [Н]азад\n:')
                                    await ctx.send('...................................................')
                                    if (chooose.lower().startswith('и')):
                                        if (INVENTORY != []):
                                            index = int(input('Введите индекс предмета: '))
                                            if (INVENTORY[index]):
                                                if (i.equip(INVENTORY[index])):
                                                    i.equip(INVENTORY[index])
                                                    iischoosed = True
                                                else:
                                                    pass
                                            else:
                                                await ctx.send('Вы выбрали некорректный предмет.')
                                        else:
                                            await ctx.send('Инвентарь пуст.')
                                    else:
                                        iischoosed = True
                            else:
                                await ctx.send('Инвентарь пуст.')
                        elif (choose.lower().startswith('п')):
                            iiischoosed = False
                            while (iiischoosed == False):
                                choooose = int(input('Введите имя персонажа, которого вы хотите проинспектировать: '))
                                if (gobn(choooose)):
                                    self = gobn(choooose)
                                    await ctx.send(f'TYPE: {self.Type}, avgDMG: {str((self.Dmg[0] + self.Dmg[1]) / 2)}, MaxHP: {str(self.MaxHP)}\nCRT: {str(self.Crit)}, SPD: {self.Speed}, PRT: {self.Protection}.')
                                    iiischoosed = True
                                else:
                                    await ctx.send('Выбран некорректный персонаж.')
                elif (i.Enemy == True):
                    attacked = None
                    enemy = None
                    while (enemy != False):
                        attacked = choice(CHARS)
                        enemy = attacked.Enemy
                    i.attack(attacked)
                if (won()):
                    return

def gobn(n):
    return Person.getobjbyname(n)

def won():
    global CHARS
    temp = []
    for i in CHARS:
        temp.append(i.Enemy)
    temp = set(temp)
    if (len(temp) == 1):
        INVENTORY.append(Item(choice(ITEMS)))
        return True
    else:
        return False

def startgame(ctx = ctx):
    gamech = ''
    while not (gamech.lower().startswith('з')):
        await ctx.send('Для продолжения после результатов атаки жмите Enter.')
        Person.create_teams(3, 3)
        Person.namethem()
        Person.view()
        while not (won()):
            Person.round()
        gamech = input('Вы хотите пойти в еще одну [И]гру или [З]акончить?\n:')

startgame()
