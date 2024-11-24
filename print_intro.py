
def print_roles(roles_list):#вывод ролей
    print('\nСреди игроков:')

    for i in roles_list:
        print(i)

def print_goal_based_on_the_role(role):#вывод цель игрока в зависимости от его роли
    goal_based_on_the_role = 'Ваша цель: '
    if role == 'Мафия':
        goal_based_on_the_role += 'убить всех, кроме себя'
    elif role == 'Доктор':
        goal_based_on_the_role += 'предугадывая ходы мафии, лечить мирных жителей, находящихся под угрозой убийства'
    elif role == 'Комиссар':
        goal_based_on_the_role += 'проверяя игроков, найти мафию и указать на нее остальным участникам, не выдав свою роль'
    else:
        goal_based_on_the_role += 'вычислить мафию, выжить'
    print(goal_based_on_the_role)

#Intro
def print_intro(roles):
    print('Поиграем в мафию!')
    print(f'Сегодня за столом собрались 5 игроков и ведущий.')
    print_roles(roles)
