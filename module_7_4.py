team1_num = input('Введите количество участников в команде "Мастера кода": ')
team2_num = input('Введите количество участников в команде "Волшебники данных": ')
score_1 = int(input('Введите, какое количество задач успела решить команда "Мастера кода": '))
score_2 = int(input('Введите, какое количество задач успела решить команда "Волшебники данных": '))
team1_time = float(input('Введите, сколько времени ушло на решиние задач у команды "Мастера кода" в секундах: '))
team2_time = float(input('Введите, сколько времени ушло на решиние задач у команды "Волшебники данных" в секундах: '))
tasks_total = score_1 + score_2
time_avg_1 = team1_time // score_1
time_avg_2 = team2_time // score_2
time_avg = (time_avg_1 + time_avg_2) / 2
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды "Мастера кода"!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды "Волшебники данных"!'
else:
    challenge_result = 'Ничья!'

print('В команде "Мастера кода" участников: %s' % team1_num)
print('В команде "Волшебники данных" участников: %s' % team2_num)
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print('Команда "Мастера кода" решила задач: {}'.format(score_1))
print('Команда "Волшебники данных" решила задач: {}'.format(score_2))
print('"Волшебники данных" решили задачи за {}'.format(team1_time))
print('"Мастера кода" решили задачи за {}'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')