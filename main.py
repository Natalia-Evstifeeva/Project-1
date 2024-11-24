#printing intro
import random
from colorama import init, Fore
import print_intro

init()#Инициализирую colorama
print(Fore.RED)# делаю весь текст красным

roles = ['Мафия', 'Доктор', 'Комиссар', 'Мирный житель', 'Мирный житель'] #лист ролей
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Немного о Докторе
can_heal_myself = True #переменная доктора(его способность 1 раз за игру вылечить самого себя
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------



def randomize_roles(dict):#рандомит роли всем игрокам, Игрок 1 - пользователь
    player_number = 1
    while len(roles) > 0:
        cur_player_role = random.choice(roles)
        dict[f'Игрок {player_number}'] = cur_player_role
        player_number += 1
        roles.remove(cur_player_role)

def print_players_for_choosing():# выводит игроков которых пользователь может выбрать для дальнейших манипуляций
    for i in range(0, len(list(players.keys()))):
        print(list(players.keys())[i])

def player_chooser(player_not_to_choose):# выбирает и возвращает из списка рандомного игрока не учитывая игрока переданного как аргумент
    tmp_dict_of_players = players.copy()
    if player_not_to_choose != '':
        del tmp_dict_of_players[player_not_to_choose]
    return random.choice(list(tmp_dict_of_players.keys()))

def who_not_to_choose(the_one_not_to_choose): # получение ключа словаря по значению
    player_not_to_choose = ''
    for i in players.keys():
        if players.get(i) == the_one_not_to_choose:
            player_not_to_choose = i
            break
    return player_not_to_choose

def komissar_check(player_to_check):# функция, которая обрабатывает проверку комиссаром игрока
    if players.get(player_to_check) == 'Мафия':
        text = 'Мафия.'
    else:
        text = 'не Мафия.'

    return f'{player_to_check} - {text}'

print_intro.print_intro(roles)

players = {}# создаю словарь формата {имя игрока: роль}
randomize_roles(players)
players_for_the_print_in_the_end = players.copy()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Немного о Комиссаре
komissar_players_to_check = list(players.keys()) # это список тех игроков, которых комиссар хочет проверить
komissar_players_to_check.remove(who_not_to_choose('Комиссар')) # из списка убираю самого комиссара
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
player_role = players['Игрок 1'] # записываю роль пользователя в переменную
print('\nВаша роль:', player_role)
print_intro.print_goal_based_on_the_role(player_role) # вывожу цель пользователя в зависимости от его роли
those_who_are_suspected_by_the_user = [i for i in list(players.keys())]  # создаю лист игроков, которых юзер подозревает
those_who_are_suspected_by_the_user.pop(0) # убираю из листа самого игрока
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Здесь начинается игра
#Text said by the narrator(program)
print('\nВнимание! Игрок 1 - это вы')
print('\nИгра начинается')

while 'Мафия' in players.values() and len(list(players.keys())) >= 3: #игра может продолжаться только если есть мафия и как минимум 2 мирных
    print('\nГород засыпает')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print('Просыпается Мафия, решает кого убить')

    if player_role == 'Мафия': # обрабатываю роль мафии
        print('Вот ваши варианты:')
        print_players_for_choosing()
        player_to_kill = input('Введите имя игрока, которого вы хотите убить: ')
    else:  # это рандомный выбор игрока для убийства, если роль юзера не Мафия
        player_to_kill = player_chooser(who_not_to_choose('Мафия'))

    print('Мафия сделала свой безжалостный выбор')
    print('Мафия засыпает\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if 'Доктор' in players.values():
        print('Просыпается Доктор, решает кого исцелить')
        if player_role == 'Доктор': # обрабатываю роль доктора
            print('Вот ваши варианты:')
            if can_heal_myself: #проверяю доступна ли доктору опция 'вылечить самого себя'
                print_players_for_choosing()
                can_heal_myself = False
                player_to_heal = input('Введите имя игрока, которого вы хотите исцелить, вы можете вылечить себя: ')
            else:
                print_players_for_choosing()
                player_to_heal = input('Введите имя игрока, которого вы хотите исцелить, помните, лечить самого себя вы не можете: ')
        else: # это рандомный выбор игрока для исцеления, если роль юзера не Доктор
            if can_heal_myself:
                player_to_heal = player_chooser(who_not_to_choose(''))
                can_heal_myself = False
            else:
                player_to_heal = player_chooser(who_not_to_choose('Доктор'))
        print('Доктор сделал свой выбор')
        print('Доктор засыпает\n')
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if 'Комиссар' in players.values():
        print('Просыпается Комиссар, решает кого проверить')
        if player_role == 'Комиссар': # обрабатываю роль комиссара
            print('Вот ваши варианты:')
            for i in komissar_players_to_check:
                print(i)
            komissar_player_to_check = input('Введите имя игрока, которого вы хотите проверить: ')
            print(komissar_check(komissar_player_to_check))
        else:  # это рандомный выбор игрока для проверки, если роль юзера не Комиссар
            komissar_player_to_check = random.choice(komissar_players_to_check)
        komissar_players_to_check.remove(komissar_player_to_check)
        komissar_text_to_say_after_the_round = komissar_check(komissar_player_to_check)

        print('Информация поступает Комиссару прямо в руки')
        print('Комиссар засыпает\n')
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print('Просыпается город\n')

    #Проверка после ночи
    if player_to_kill == player_to_heal:
        print('Этой ночью никого не убили')
    else:
        print(f'Этой ночью был убит {player_to_kill}, его роль: {players.get(player_to_kill)}')
        del players[player_to_kill]
        if 'Игрок 1' not in list(players.keys()):
            print('К сожалению для вас игра окончена, но вы можете продолжать наблюдать за развитием событий)')
    print('Также поступила информация о том, что ', komissar_text_to_say_after_the_round, 'Этой информации можно доверять.')

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    players_chosen_by_voting = []
    if 'Игрок 1'  in list(players.keys()):
        print('\nПроведем голосование')
        print('Вот ваши варианты:')
        print_players_for_choosing()

        player_chosen_by_voting_by_the_user = input('Введите имя игрока, который по вашему мнению является Мафией: ')
        players_chosen_by_voting.append(player_chosen_by_voting_by_the_user)

    #Осуществляю выбор игрока за которого голосуют все игроки(кроме юзера) по средствам рандома и записываю результаты в список
    for i in range(0,len(list(players.keys())) - 1):
        players_chosen_by_voting.append(random.choice(list(players.keys())))

    #нахожу наиболее часто упомянутого игрока, соответствующую ему роль и вывожу информацию на экран
    number_of_votes_for_each_player = []
    for i in players.keys():
        number_of_votes_for_each_player.append(players_chosen_by_voting.count(i))
    player_to_get_rid_of = list(players.keys())[number_of_votes_for_each_player.index(max(number_of_votes_for_each_player))]
    print(f'По результатам общего голосования, участник {player_to_get_rid_of} покидает игру. Его роль была: {players.get(player_to_get_rid_of)}.')
    del players[player_to_get_rid_of]

    if 'Игрок 1' not in list(players.keys()):
        print('К сожалению для вас игра окончена, но вы можете продолжать наблюдать за развитием событий)')

if 'Мафия' in players.values():
    print('В этой партии выйграла Мафия.')
else:
    print('В этой партии выйграли Мирные жители.')

print('Таковы были роли игроков:\n')
for i in range(0,len(list(players_for_the_print_in_the_end.keys()))):
    print(list(players_for_the_print_in_the_end.keys())[i], ' - ', list(players_for_the_print_in_the_end.values())[i])
print('Всем спасибо за игру!')

