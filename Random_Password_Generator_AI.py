import time

i = 0

while i <= 100:
    print('Загрузка... ', i, '%')
    time.sleep(0.21) 
    i = i + 5
print("Привет, я (Петя) ИИ по созданию паролей. Чем могу быть полезен? ")   
choice = input(" 1 - Сгенерировать пароль, 2 - Завершить: ")
if choice == '1':
    import string
    import random
    import itertools
    for item in itertools.repeat("бесконечно"):
        if item == "бесконечно":
            def generate_password(length):
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for _ in range(length))
                return password

            password_length = int(input("Введите желаемую длину пароля: "))
            generated_password = generate_password(password_length)
            print("Ваш сгенерированный пароль:", generated_password)
            print("ВНИМАНИЕ: не советуется вводить длину пароля больше 1000!!!! На более слабых компьютерах не советуется больше 100! ")
            print("Советуется проверить данный пароль на наличие в базах, ну и все сгенерированные тоже. И не советуется делать пароли короче 10.")
            print("                                                         ")
elif choice == '2':
    print("...")
else:
    print("Неверный выбор.") 

