import math
from .. import loader, utils

def calculator(command):
    # Функция калькулятора для Telegram User Bot
    # Умеет выполнять простые и более сложные математические операции
    
    if command.startswith(".к "):
        command = command[3:]  # Удаляем первые три символа (".к ")
        
        if command == ".пи":
            return "🤓 π ≈ 3.14159265358979323846264338327950288419716939937510"
        
        if "+" in command:
            x, y = map(int, command.split("+"))
            return f"🤓 Ответ: {x} + {y} = {x + y}"
        elif "-" in command:
            x, y = map(int, command.split("-"))
            return f"🤓 Ответ: {x} - {y} = {x - y}"
        elif "*" in command:
            x, y = map(int, command.split("*"))
            return f"🤓 Ответ: {x} * {y} = {x * y}"
        elif "/" in command:
            x, y = map(int, command.split("/"))
            if y != 0:
                return f"🤓 Ответ: {x} / {y} = {x / y}"
            else:
                return "🤓 Ошибка: Деление на ноль"
        elif "√" in command:
            base_index = command.index("√")
            number = int(command[:base_index])
            base = int(command[base_index + 1:])
            if base > 0:
                return f"🤓 Ответ: Квадратный корень из {number} = {number ** (1/base)}"
            else:
                return "🤓 Ошибка: Корень должен быть положительным числом"
        elif "^" in command:
            x, y = map(int, command.split("**")
            return f"🤓 Ответ: {x} в степени {y} = {x ** y}"
        elif "!" in command:
            x = int(command[1:])
            return f"🤓 Ответ: Факториал от {x} = {math.factorial(x)}"
        elif "-!" in command:
            x = int(command[1:])
            return f"🤓 Ответ: Субфакториал от {x} = {(math.factorial(x - 1) / (x - 1))}" if x > 1 else "🤓 Ошибка: Субфакториал определен только для x > 1"
        else:
            return "🤓 Ошибка: Неверный формат команды"
    else:
        return "🤓 Ошибка: Команда должна начинаться с '.к '"

# Информация об авторе и описание модуля
author = "@lainux"
module_description = "Модуль калькулятора для Telegram User Bot на Python. Выполняет различные математические операции, включая сложение, вычитание, умножение, деление, квадратный корень, степень, факториал и субфакториал."

# Пример использования
command_1 = ".к 10+5"
print("😎 Пример:", command_1)
result_1 = calculator(command_1)
print(result_1)

command_2 = ".к 25-10"
print("\n😎 Пример:", command_2)
result_2 = calculator(command_2)
print(result_2)

command_3 = ".к 5*8"
print("\n😎 Пример:", command_3)
result_3 = calculator(command_3)

# Автоматический вывод результата и возможность скачать модуль
if result_1 and result_2 and result_3:
    message = f"👀 Примеры использования:\n    1. {command_1}\n        🔍 Результат: {result_1}\n    2. {command_2}\n        🔍 Результат: {result_2}\n    3. {command_3}\n        🔍 Результат: {result_3}\nСоздатель: {author}\nОписание: {module_description}"
    print(message)
    
    download_link = "https://github.com/Hugensy/calculain/blob/main/cacl.py"
    print(f"💾 Скачать модуль: {download_link}")
