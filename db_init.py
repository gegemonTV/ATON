import sqlite3, random
from uuid import uuid4

MALE_NAMES = ["Алексей", "Арсений", "Антон", "Александр", "Аркадий", "Анатолий", "Вадим", "Виктор", "Виталий", "Валентин", "Григорий", "Геннадий", "Глеб", "Даниил", "Данил", "Евгений"]
LAST_NAMES = ["Кузнецов", "Попов", "Смирнов", "Мосин", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков", "Федоров", "Волков", "Морозов", "Алексеев", "Лебедев", "Семенов", "Егоров"]
MALE_MIDDLE_NAMES = ["Владимирович", "Александрович", "Николаевич", "Сергеевич", "Викторович", "Анатольевич", "Иванович", "Юрьевич", "Михайлович"]

FEMALE_NAMES = ["София", "Анастасия", "Дарья", "Мария", "Анна", "Виктория", "Полина", "Елизавета", "Екатерина", "Ксения", "Валерия", "Вероника"]
FEMALE_MIDDLE_NAMES = ["Владимировна", "Александровна", "Николаевна", "Сергеевна", "Викторовна", "Анатольевна", "Ивановна", "Юрьевна", "Михайловна"]


def login_generator():
    vowel_letter = ['a', 'e', 'i', 'o', 'u', 'y']
    alphabet = []
    for i in range(97, 123):
        alphabet.append(chr(i))
    login = ''
    login += vowel_letter[random.randint(0, len(vowel_letter) - 1)]
    for j in range(5):
        login += alphabet[random.randint(0, len(alphabet) - 1)]
    return login

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

responsible_usernames = []

for _ in range(20):
    full_name = MALE_NAMES[random.randint(0, len(MALE_NAMES)-1)] + " " \
        + LAST_NAMES[random.randint(0, len(LAST_NAMES)-1)] + " " \
        + MALE_MIDDLE_NAMES[random.randint(0, len(MALE_MIDDLE_NAMES)-1)]
    
    login = login_generator()
    password = uuid4().hex[:10]
    responsible_usernames.append(full_name)
    cursor.execute("INSERT INTO db_connector_user (full_name, login, password) VALUES (?, ?, ?)", (full_name, login, password))

for _ in range(55):
    is_male = random.randint(0, 1)
    first_name = None
    last_name = None
    middle_name = None

    if is_male:
        first_name = random.choice(MALE_NAMES)
        last_name = random.choice(LAST_NAMES)
        middle_name = random.choice(MALE_MIDDLE_NAMES)
    else:
        first_name = random.choice(FEMALE_NAMES)
        last_name = random.choice(LAST_NAMES) + 'а'
        middle_name = random.choice(FEMALE_MIDDLE_NAMES)
    account_number = random.randint(10000000000, 99999999999)
    date_of_birth = sqlite3.Date(random.randint(1970, 2024), random.randint(1, 12), random.randint(1, 28))
    tin = random.randint(1000000000, 9999999999)
    status = "Не в работе"
    cursor.execute("INSERT INTO db_connector_client (account_number, last_name, first_name, middle_name, date_of_birth, tin, status, responsible_user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (account_number, last_name, first_name, middle_name, date_of_birth, tin, status, random.choice(responsible_usernames)))

connection.commit()
connection.close()
