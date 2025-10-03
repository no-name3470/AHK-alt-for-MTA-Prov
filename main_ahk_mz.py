from time import *
import keyboard as kb
import customtkinter as ctk
import os
import json
import datetime

#!!!НЕ ЛЕЗТЬ В ВЕЩИ НИЖЕ НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ!!! а то всё сломается :(
def save_variables(filename, variables):
    if os.path.exists(filename):
        return
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(variables, file, ensure_ascii=False, indent=4)
        print(f"Данные успешно сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def load_variables(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            variables = json.load(file)
        print(f"Данные загружены из {filename}")
        return variables
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return {}
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        return {}

if __name__ == "__main__":
    my_variables = {
        "surname": "ВВЕДИТЕ ФАМИЛИЮ",
        "name": "ВВЕДИТЕ ИМЯ",
        "patronyme": "ВВЕДИТЕ ОТЧЕСТВО",
        "initials": "ВВЕДИТЕ ИНИЦИАЛЫ (Фамилия И.О.)",
        "rang": "ВВЕДИТЕ ДОЛЖНОСТЬ",
        "org": "ВВЕДИТЕ ОРГАНИЗАЦИЮ (ЦГБ-П/ЦГБ-Н/ОКБ-М)",
        "brigade": 0,
    }

    save_variables("data_ahk.txt", my_variables)

    loaded_vars = load_variables("data_ahk.txt")

    surname = loaded_vars.get("surname", "")
    name = loaded_vars.get("name", "")
    patronyme = loaded_vars.get("patronyme", "")
    initials = loaded_vars.get("initials", "")
    rang = loaded_vars.get("rang", "")
    org = loaded_vars.get("org", "")
    brigade = loaded_vars.get("brigade", "")

    print("\nДанные:")
    print(f"    Фамилия: {surname}")
    print(f"    Имя: {name}")
    print(f"    Отчество: {patronyme}")
    print(f"    Инициалы: {initials}")
    print(f"    Должность: {rang}")

yearC = datetime.datetime.now().year

checkwarn = 'Проверка...'
if org == 'ЦГБ-П':
    city = 'Приволжск'
    citygosp = 'ЦГБ города Приволжск'
elif org == 'ЦГБ-Н':
    city = 'Невский'
    citygosp = 'ЦГБ города Невский'
elif org == 'ОКБ-М':
    city = 'Мирный'
    citygosp = 'ОКБ города Мирный'
else:
    city = 'Ошибка!'
    checkwarn = '!!!ПРОВЕРЬТЕ СВОИ ДАННЫЕ В data_ahk.txt!!!'

errorbrig = None
if brigade <= 6 and city == 'Приволжск' :
    brigamb = 'АСМП'
elif brigade >= 7 and brigade <= 10  and city == 'Приволжск':
    brigamb = 'АСРП'
elif brigade <= 4 and city == 'Невский' :
    brigamb = 'АСМП'
elif brigade >= 5 and brigade <= 8 and city == 'Невский':
    brigamb = 'АСРП'
elif brigade <= 8 and city == 'Мирный' :
    brigamb = 'АСМП'
elif brigade >= 9 and brigade <= 12 and city == 'Мирный':
    brigamb = 'АСРП'
else:
    brigamb = 'Ошибка в определении типа кареты!'
    checkwarn = '!!!ПРОВЕРЬТЕ СВОИ ДАННЫЕ В data_ahk.txt!!!'
    errorbrig = 'Проверьте свои данные в файле "data_ahk.txt"!'

if checkwarn == 'Проверка...':
    checkwarn1 = 'Если хотите изменить эти данные, то изменяйте их через файл data_ahk.txt...'
else:
    checkwarn1 = 'Проверьте свои данные в файле "data_ahk.txt"!'

if errorbrig == 'Несуществующий номер бригады!':
    brigade = 'Несуществующий номер бригады!'
else:
    brigade = brigade

print(f"    Организация: {org}, город {city}")
print(f"    Бригада: {brigade}, {brigamb}")

if surname == 'Вавилов' and name == 'Александр' and org == 'ОКБ-М':
    pashalka = 'Ошибка! Вавилов не может быть в ОКБ-М!'
    checkwarn1 = pashalka
    print('\nХватит играться!')
else:
    checkwarn1 = checkwarn1

if surname == 'МакКартни' and name == 'Александр' and org == 'ЦГБ-П' and rang == 'Главный врач':
    pashalka = 'С возвращением, моя любовь❤️!'
    checkwarn1 = pashalka
    print('Я тебя люблю!')
else:
    checkwarn1 = checkwarn1

def hello():
    #Приветствие
    sleep(0.5)
    kb.send('f8')
    kb.write(f'say Здравствуйте! Я {rang}, {name} {patronyme}.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'do На форме сотрудника висит бейдж: {org}, {initials}, {rang}.')
    kb.send('enter + f8')

def datas():
    #Спросить данные
    sleep(0.5)
    kb.send('f8')
    kb.write('say Для начала надо заполнить данные. Назовите ваше имя, фамилию и повод обращения?')
    kb.send('enter + f8')

def form():
    #Заполнить данные
    sleep(1)
    kb.send('f8')
    kb.write('do Через плечо висит сумка.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Бланк обращения лежит в сумке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me достал бланк и заполнил данные обращения.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('say Всё готово, пройдемте за мной.')
    kb.send('enter + f8')

def questions():
    #Задать вопросы
    sleep(0.5)
    kb.send('f8')
    kb.write('say Как давно вы стали чувствовать боли?')
    kb.send('enter + f8')
    sleep(1.5)
    kb.send('f8')
    kb.write('say Алкоголь или табачные средства употребляете?')
    kb.send('enter + f8')
    sleep(1.5)
    kb.send('f8')
    kb.write('say Физической активностью занимаетесь?')
    kb.send('enter + f8')

def checkup_hosp():
    #Осмотр в больнице
    sleep(0.5)
    kb.send('f8')
    kb.write('say Сейчас я вас осмотрю, ожидайте')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Медицинские перчатки лежат на столе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял перчатки и надел их')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me начал проводить осмотр пациента')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Осмотр окончен.')
    kb.send('enter + f8')

def checkup_amb():
    #Осмотр в АСМП/АСРП
    sleep(0.5)
    kb.send('f8')
    kb.write('do Медицинские перчатки лежат на полке кареты.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял перчатки и надел их')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me начал проводить осмотр пациента')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Осмотр окончен.')
    kb.send('enter + f8')

def epicrisis_hosp():
    #Заполнение эпикриза в больнице
    sleep(0.5)
    kb.send('f8')
    kb.write('do Эпикриз и ручка лежат на столе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял ручку и заполнил результат обращения')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me поставил дату и подпись')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write("do Штамп стоит на столе.")
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'me взял штамп и поставил печать {org}')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Препарат стоит на полке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял препарат и передал пациенту')
    kb.send('enter + f8')
    sleep(0.1)
    kb.send('f8')
    sleep(0.1)
    kb.write('helpmed ')
    sleep(3)
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    sleep(0.25)
    kb.send('f8')
    kb.write('say Всего доброго, не болейте.')
    kb.send('enter + f8')
    
def epicrisis_amb():
    #Заполнение эпикриза в АСМП/АСРП
    sleep(0.5)
    kb.send('f8')
    kb.write('do Через плечо висит мед.укладка.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Эпикриз и ручка лежат в мед.укладке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял ручку и заполнил результат обращения')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write("me поставил дату и подпись")
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Штамп лежит на полке кареты.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'me взял штамп и поставил печать {org}')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Препарат лежит в мед.укладке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял препарат и передал пациенту')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('say Всего доброго, не болейте.')
    kb.send('enter + f8')
    sleep(0.1)
    kb.send('f8')
    sleep(0.1)
    kb.write('helpmed ')
    sleep(0.1)
    kb.wait('Enter')
    kb.send('escape')
    sleep(0.5)
    kb.send('f8')
    kb.write('say Всего доброго, не болейте.')
    kb.send('enter + f8')

def checkup_pmp():
    #Осмотр (ПМП)
    sleep(0.5)
    kb.send('f8')
    kb.write('me начал осматривать тело пострадавшего')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Сотрудник осматривает всё тело пострадавшего.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Какие ранения и травмы имеются на теле?')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('b Чат открывается на клавишу T(англ) и туда прописываются эти команды.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('b Ответьте РП отыгровкой do в чат. Можете написать про ссадины, порезы, ушибы.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('b Пример: do На теле пострадавшего ножевое ранение; do На теле пострадавшего кровотечение.')
    kb.send('enter + f8')

def pulse():
    #Проверка пульса
    sleep(0.5)
    kb.send('f8')
    kb.write('me поднёс руку к сонной артерии пациента')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рука поднесена к сонной артерии пациента.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Пульс обнаружен?')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('b Ответьте РП отыгровкой в чат: do Да. или do Нет.')
    kb.send('enter + f8')

def spirt():
    #Приведение с сознание
    sleep(0.5)
    kb.send('f8')
    kb.write(f'do Медицинская укладка с пометкой {org} в руке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me поставив укладку на землю, открыл её')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Медицинская укладка открыта.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me достал спирт и вату из укладки')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Спирт и кусочек ваты в руках.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me смочив вату нашатырным спиртом, провёл ею около носа пострадавшего')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me откинув использованный кусочек ваты на землю, поставил спирт в укладку')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Нашатырный спирт в медицинской укладке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me закрыв медицинскую укладку, взял её в руку')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Пострадавший пришёл в сознание?')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('b Ответьте РП отыгровкой в чат: do Да. или do Нет.')
    kb.send('enter + f8')

def slr():
    #СЛР (Сердечно-лёгочная реанимация)
    sleep(0.5)
    kb.send('f8')
    kb.write('me проводит непрямой массаж сердца пострадавшему, надавливая на грудную клетку')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Сотрудник выполняет непрямой массаж сердца.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me прислонил руку к сонной артерии пациента')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Пульс обнаружен?')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('b Ответьте РП отыгровкой в чат: do Да. или do Нет.')
    kb.send('enter + f8')

def hlorgeks():
    #Обработка ранений
    sleep(0.5)
    kb.send('f8')
    kb.write('do На плече висит сумка, в которой лежит спрей "Хлоргексидин".')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me открыв сумку, достал спрей')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Спрей "Хлоргексидин" в руке. ')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me нанес препарат на место ранения')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Место ранения продезинфицировано.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me убрал спрей в сумку')
    kb.send('enter + f8')

def bint():
    #Наложить бинт
    sleep(0.5)
    kb.send('f8')
    kb.write('do На плече висит сумка, в которой лежат бинты.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me открыв сумку, достал две упаковки бинтов')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Бинты в руке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me открыв бинты, отбросил упаковку на землю')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Два валика бинтов в руке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me приложил один валик к месту ранения')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Валик приложен к месту ранения.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me размотав второй валик бинта, наложил его на место ранения')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Давящая повязка наложена.')
    kb.send('enter + f8')

def viz1():
    sleep(0.5)
    kb.send('escape')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me сняв рацию с пояса начал что-то говорить')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 1')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'r [Бригада №{brigade}] Вызов №')
    sleep(3)
    kb.write(' принят в обработку.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me закончив говорить закрепил рацию на поясе')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 2')
    kb.send('enter + f8')

def viz2():
    sleep(0.5)
    kb.send('escape')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me сняв рацию с пояса начал что-то говорить')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 1')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'r [Бригада №{brigade}] Прибытие на место вызова №')
    sleep(3)
    kb.write('.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me закончив говорить закрепил рацию на поясе')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 2')
    kb.send('enter + f8')

def vizgosp():
    sleep(0.5)
    kb.send('escape')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me сняв рацию с пояса начал что-то говорить')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 1')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'r [Бригада №{brigade}] Проводится госпитализация в {citygosp} по вызову №')
    sleep(3)
    kb.write('. Повод: ')
    sleep(5)
    kb.write('.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me закончив говорить закрепил рацию на поясе')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 2')
    kb.send('enter + f8')

def vizcompl():
    sleep(0.5)
    kb.send('escape')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me сняв рацию с пояса начал что-то говорить')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 1')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'r [Бригада №{brigade}] Вызов №')
    sleep(3)
    kb.write(' обработан.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me закончив говорить закрепил рацию на поясе')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 2')
    kb.send('enter + f8')

def vizlozh():
    sleep(0.5)
    kb.send('escape')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me сняв рацию с пояса начал что-то говорить')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 1')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write(f'r [Бригада №{brigade}] Вызов №')
    sleep(3)
    kb.write(' ложный.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me закончив говорить закрепил рацию на поясе')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 2')
    kb.send('enter + f8')

def fracvoice1():
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me сняв рацию с пояса начал что-то говорить')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 1')
    kb.send('enter + f8')

def fracvoice2():
    sleep(0.5)
    kb.send('f8')
    kb.write('me закончив говорить закрепил рацию на поясе')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Рация закреплена на поясе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('fracvoice 2')
    kb.send('enter + f8')

def dfb1():
    sleep(0.5)
    kb.send('f8')
    kb.write(f'do Дефибриллятор и резиновые перчатки находятся в {brigamb}.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял дефибриллятор и надел перчатки')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me снял с пострадавшего верхнюю одежду и украшения, висящие на груди')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Пострадавший готов к началу процедуры.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Гель находится в медицинской укладке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me взял гель и намазал его на электроды')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Электроды намазаны гелем.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me убрал гель в медицинскую укладку')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Гель в мед. укладке.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me установил первый электрод на грудной клетке, слева, чуть выше области верхушки сердца')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me установил второй электрод под правой ключицей')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Электроды установлены.')
    kb.send('enter + f8')

def dfb2():
    kb.send('f8')
    kb.write('me включил дефибриллятор и выставил необходимую мощность')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Дефибриллятор готов к работе.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me убедившись в безопасности, подал разряд')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Разряд подан.')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('me проверил пульс пострадавшего')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('do Пульс стал стабильным?')
    kb.send('enter + f8')
    sleep(0.5)
    kb.send('f8')
    kb.write('n Ответьте РП отыгровкой do Да. или do Нет.')
    kb.send('enter + f8')







kb.add_hotkey('alt + 1', hello)
kb.add_hotkey('alt + 2', datas)
kb.add_hotkey('alt + 3', form)
kb.add_hotkey('alt + 4', questions)
kb.add_hotkey('alt + 5', checkup_hosp)
kb.add_hotkey('alt + ctrl + 5', checkup_amb)
kb.add_hotkey('alt + 7', epicrisis_hosp)
kb.add_hotkey('alt + ctrl + 7', epicrisis_amb)
kb.add_hotkey('ctrl + num_1', checkup_pmp)
kb.add_hotkey('ctrl + num_2', pulse)
kb.add_hotkey('ctrl + num_3', spirt)
kb.add_hotkey('ctrl + num_4', slr)
kb.add_hotkey('ctrl + num_5', hlorgeks)
kb.add_hotkey('ctrl + num_6', bint)
kb.add_hotkey('alt + ctrl + shift + 1', viz1)
kb.add_hotkey('alt + ctrl + shift + 2', viz2)
kb.add_hotkey('alt + ctrl + shift + 3', vizgosp)
kb.add_hotkey('alt + ctrl + shift + =', vizcompl)
kb.add_hotkey('alt + ctrl + shift + -', vizlozh)
kb.add_hotkey('alt + backspace', fracvoice1)
kb.add_hotkey('alt + enter', fracvoice2)
kb.add_hotkey('alt + num_/', dfb1)
kb.add_hotkey('alt + num_*', dfb2)
kb.add_abbreviation('/голова', 'say Я выпишу Вам Нурофен. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/ушиб', 'say Я выпишу Вам Финалгон. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/тошнота', 'say Я выпишу Вам Лоразепам. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/отравление', 'say Я выпишу Вам Смекта. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/обезбол', 'say Я выпишу Вам Дексалгин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/запор', 'say Я выпишу Вам Гутталакс. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/понос', 'say Я выпишу Вам Лоперамид. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/геморрой', 'say Я выпишу Вам Релиф. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/сустав', 'say Я выпишу Вам Ибупрофен. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/судороги', 'say Я выпишу Вам Панангин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/витамины', 'say Я выпишу Вам Центрум. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/аллергия', 'say Я выпишу Вам Супрастин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/простуда', 'say Я выпишу Вам Колдрекс. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/горло', 'say Я выпишу Вам Амбробене. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/насморк', 'say Я выпишу Вам Отривин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/бессонница', 'say Я выпишу Вам Мелатонин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/печень', 'say Я выпишу Вам Овесол. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/половыеорганы', 'say Я выпишу Вам Тридерм. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/сердце', 'say Я выпишу Вам Валидол. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/зубы', 'say Я выпишу Вам Баралгин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/глаза', 'say Я выпишу Вам Алкаин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/ожог', 'say Я выпишу Вам Фенистил. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/уши', 'say Я выпишу Вам Отипакс. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/почки', 'say Я выпишу Вам Нефротин. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/давление', 'say Я выпишу Вам Небилет. Стоимость 500 рублей. Согласны?')
kb.add_abbreviation('/мочевой', 'say Я выпишу Вам Цистерол. Стоимость 500 рублей. Согласны?')

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AutoHotKey для сотрудников Министерства Здравоохранения | ver. 0.1")
        self.geometry("800x750")

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)

        tab_names = ["Лечение", "Мед. карта", "ПМП/Вызов", "Операции", "Доклады", "Личные данные", "Разное"]

        for tab_name in tab_names:
            self.tabview.add(tab_name)
        
        texts = {
            "Лечение": '\nЛЕЧЕНИЕ ПАЦИЕНТОВ\n\nAlt + 1 | Приветствие\nAlt + 2 | Спросить данные\nAlt + 3 | Заполнить бланк\nAlt + 4 | Задать вопросы\nAlt + 5 | Осмотр в больнице\nAlt + Ctrl + 5 | Осмотр в АСМП/АСРП\nAlt + 7 | Выписка эпикриза в больнице\nAlt + Ctrl + 7 | Выписка эпикриза в АСМП/АСРП\n\n\nОСНОВНЫЕ ТАБЛЕТКИ\n\n/голова, /ушиб\n/тошнота, /отравление, /обезбол\n/запор, /понос, /геморрой\n/суставы, /судороги, /витамины\n/аллергия, /простуда, /горло\n/насморк, /бессонница, /печень\n/половыеорганы, /сердце, /зубы\n/глаза, /ожог, /уши\n/почки, /давление, /мочевой\n\nP.S. Прописывать в консоли.\nНажимайте на пробел, а не на энтер.\n',
            "Мед. карта": '\nВ разработке...\n',
            "ПМП/Вызов": "\nБАЗОВОЕ ПМП\n\nCtrl + 1 | Осмотр\nCtrl + 2 | Проверка пульса\nCtrl + 3 | Приведение в сознание\nCtrl + 4 | Массаж сердца\nCtrl + 5 | Обработка ранений\nCtrl + 6 | Бинт\n\n\n!!!НИЖЕ ПОКА-ЧТО НЕ РАБОТАЕТ!!!\nПМП ПРИ ПЕРЕЛОМЕ\n\nAlt + Ctrl +  7 | Пальпация\n/шина1 | Достать шину\n/шина2 | Наложить шину\n/шина3 | Убрать шину\n\n\nПМП ПРИ ОСТАНОВКЕ СЕРДЦА\n\nAlt + Numpad . | АМБУ\nAlt + Numpad / | Достать дефибриллятор\nAlt + Numpad * | Разряд 1\nAlt + Numpad - | Разряд 2\nAlt + Numpad + | Убрать дефибриллятор\n Alt+ Numpad Enter | Пациент мёртв\n",
            "Операции": "\nВ разработке...\n",
            "Доклады": "\nРАЦИЯ\n\nAlt + Backspace | Рация доклад\nAlt + Enter | Рация прослушка\n\n\nОБРАБОТКА ВЫЗОВА\n\nAlt + Ctrl + Shift + 1 | Принятие вызова\nAlt + Ctrl + Shift + 2 | Прибытие на место вызова\nAlt + Ctrl + Shift + 3 | Госпитализация в больницу\nAlt + Ctrl + Shift + = | Вызов обработан\nAlt + Ctrl + Shift + - | Вызов ложный\n",
            "Личные данные": f"\nФИО: {surname} {name} {patronyme}\nДолжность: {rang}\nГород трудоустройства: {city}\nНомер бригады : {brigade}\n\n{checkwarn1}\n",
            "Разное": f"\nВ разработке...\nСкоро здесь что-то будет...\n(Лекций тут не будет.)\n\n\n©Alexander_Vavilov {yearC}\nПожалуйста, не публикуйте в открытом доступе без моего разрешения.\n"
        }

        for tab_name in tab_names:
            label = ctk.CTkLabel(
                master=self.tabview.tab(tab_name),
                text=texts[tab_name],
                font=("Rubik Medium", 14),
                wraplength=500,
                justify="center",
                fg_color='#494d4e',
                corner_radius=10
            )
            label.pack(padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()