LESSONS = [
    {
        "index": 0,
        "title": "Привет, мир!",
        "theory": (
            "📚 <b>Урок 1: Вывод на экран</b>\n\n"
            "В Python есть функция print() — она выводит текст на экран.\n\n"
            "Пример:\n"
            "  print('Hello, World!')\n\n"
            "Текст нужно писать в кавычках — одинарных ' ' или двойных \" \".\n\n"
            "👇 <b>Задание:</b>\n"
            "Напиши код, который выведет на экран:\n"
            "  Привет, Python!"
        ),
        "expected_output": "Привет, Python!",
        "starter_code": "# Напиши свой код здесь\n",
        "hints": [
            "Используй print()",
            "print('Привет, Python!')",
        ],
    },
    {
        "index": 1,
        "title": "Переменные",
        "theory": (
            "📚 <b>Урок 2: Переменные</b>\n\n"
            "Переменная — это коробочка с именем, в которой хранится значение.\n\n"
            "Пример:\n"
            "  name = 'Артём'\n"
            "  age = 25\n"
            "  print(name)\n\n"
            "Правила имён:\n"
            "  • Только буквы, цифры, подчёркивание\n"
            "  • Не начинается с цифры\n"
            "  • Регистр важен: name и Name — разные переменные\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай переменную name = 'Python' и выведи её на экран."
        ),
        "expected_output": "Python",
        "starter_code": "# Создай переменную и выведи её\n",
        "hints": [
            "name = 'Python'",
            "print(name)",
        ],
    },
    {
        "index": 2,
        "title": "Числа и операции",
        "theory": (
            "📚 <b>Урок 3: Числа</b>\n\n"
            "Python умеет считать:\n\n"
            "  print(2 + 3)    # сложение → 5\n"
            "  print(10 - 4)   # вычитание → 6\n"
            "  print(3 * 4)    # умножение → 12\n"
            "  print(10 / 3)   # деление → 3.333...\n"
            "  print(10 // 3)  # целочисленное → 3\n"
            "  print(2 ** 3)   # степень → 8\n\n"
            "👇 <b>Задание:</b>\n"
            "Выведи результат: 7 * 8"
        ),
        "expected_output": "56",
        "starter_code": "# Вычисли и выведи 7 * 8\n",
        "hints": [
            "print(7 * 8)",
        ],
    },
    {
        "index": 3,
        "title": "Строки",
        "theory": (
            "📚 <b>Урок 4: Строки</b>\n\n"
            "Строки можно склеивать и умножать:\n\n"
            "  print('Hello' + ' ' + 'World')  # Hello World\n"
            "  print('Ha' * 3)                 # HaHaHa\n\n"
            "f-строки — вставляй значения прямо в текст:\n"
            "  name = 'Python'\n"
            "  print(f'Привет, {name}!')\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай переменную word = 'Python' и выведи f-строку: 'Я учу Python'"
        ),
        "expected_output": "Я учу Python",
        "starter_code": "# Создай переменную и выведи f-строку\n",
        "hints": [
            "word = 'Python'",
            "print(f'Я учу {word}')",
        ],
    },
    {
        "index": 4,
        "title": "Ввод данных",
        "theory": (
            "📚 <b>Урок 5: Ввод данных</b>\n\n"
            "Функция input() читает текст с клавиатуры:\n\n"
            "  name = input()\n"
            "  print('Привет, ' + name)\n\n"
            "input() всегда возвращает строку. Для чисел нужен int():\n"
            "  age = int(input())\n\n"
            "👇 <b>Задание:</b>\n"
            "Выведи текст 'Введи имя: ' и прочитай имя с input(). Потом выведи 'Привет, ' + имя.\n\n"
            "Подсказка: можно сделать в одну строку:\n"
            "  name = input('Введи имя: ')"
        ),
        "expected_output": "Привет, Артём",
        "starter_code": "# Прочитай имя и поздней\n# input() прочитает 'Артём'\n",
        "hints": [
            "name = input()",
            "print('Привет, ' + name)",
        ],
    },
    {
        "index": 5,
        "title": "Условия if/else",
        "theory": (
            "📚 <b>Урок 6: Условия</b>\n\n"
            "if проверяет условие:\n\n"
            "  age = 18\n"
            "  if age >= 18:\n"
            "      print('Взрослый')\n"
            "  else:\n"
            "      print('Ребёнок')\n\n"
            "Сравнение:\n"
            "  ==  равно\n"
            "  !=  не равно\n"
            "  >   больше\n"
            "  <   меньше\n"
            "  >=  больше или равно\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай x = 10 и напиши условие: если x > 5, выведи 'Большое число', иначе 'Малое число'"
        ),
        "expected_output": "Большое число",
        "starter_code": "x = 10\n# Напиши условие if/else\n",
        "hints": [
            "if x > 5:",
            "    print('Большое число')",
            "else:",
            "    print('Малое число')",
        ],
    },
    {
        "index": 6,
        "title": "Циклы for",
        "theory": (
            "📚 <b>Урок 7: Цикл for</b>\n\n"
            "for повторяет код N раз:\n\n"
            "  for i in range(5):\n"
            "      print(i)\n"
            "  # Выведет: 0 1 2 3 4\n\n"
            "range(5) → от 0 до 4\n"
            "range(1, 5) → от 1 до 4\n"
            "range(0, 10, 2) → 0, 2, 4, 6, 8\n\n"
            "👇 <b>Задание:</b>\n"
            "Выведи числа от 1 до 5 включительно через for"
        ),
        "expected_output": "1\n2\n3\n4\n5",
        "starter_code": "# Выведи числа от 1 до 5\nfor i in range(1, 6):\n",
        "hints": [
            "for i in range(1, 6):",
            "    print(i)",
        ],
    },
    {
        "index": 7,
        "title": "Списки",
        "theory": (
            "📚 <b>Урок 8: Списки</b>\n\n"
            "Список — упорядоченная коллекция:\n\n"
            "  fruits = ['яблоко', 'банан', 'вишня']\n"
            "  print(fruits[0])   # яблоко (нумерация с 0!)\n"
            "  fruits.append('апельсин')  # добавить\n"
            "  len(fruits)        # 4\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай список numbers = [1, 2, 3, 4, 5] и выведи его второй элемент (индекс 1)"
        ),
        "expected_output": "2",
        "starter_code": "# Создай список и выведи второй элемент\n",
        "hints": [
            "numbers = [1, 2, 3, 4, 5]",
            "print(numbers[1])",
        ],
    },
    {
        "index": 8,
        "title": "Словари",
        "theory": (
            "📚 <b>Урок 9: Словари</b>\n\n"
            "Словарь хранит пары ключ-значение:\n\n"
            "  person = {\n"
            "      'name': 'Артём',\n"
            "      'age': 25\n"
            "  }\n"
            "  print(person['name'])  # Артём\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай словарь car с ключами 'brand'='Tesla' и 'year'=2024, выведи brand"
        ),
        "expected_output": "Tesla",
        "starter_code": "# Создай словарь car и выведи brand\n",
        "hints": [
            "car = {'brand': 'Tesla', 'year': 2024}",
            "print(car['brand'])",
        ],
    },
    {
        "index": 9,
        "title": "Функции",
        "theory": (
            "📚 <b>Урок 10: Функции</b>\n\n"
            "Функция — переиспользуемый блок кода:\n\n"
            "  def greet(name):\n"
            "      return f'Привет, {name}!'\n"
            "  \n"
            "  print(greet('Мир'))\n\n"
            "def создаёт функцию, return возвращает результат.\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай функцию square(x), которая возвращает x * x. Вызови square(7) и выведи результат."
        ),
        "expected_output": "49",
        "starter_code": "# Создай функцию и выведи результат\n",
        "hints": [
            "def square(x):",
            "    return x * x",
            "print(square(7))",
        ],
    },
    {
        "index": 10,
        "title": "Цикл while",
        "theory": (
            "📚 <b>Урок 11: Цикл while</b>\n\n"
            "while повторяет, пока условие истинно:\n\n"
            "  count = 5\n"
            "  while count > 0:\n"
            "      print(count)\n"
            "      count -= 1\n"
            "  # Выведет: 5 4 3 2 1\n\n"
            "👇 <b>Задание:</b>\n"
            "Напиши while-цикл: начинай с n = 3, вывод n и уменьшай на 1. Пока n > 0."
        ),
        "expected_output": "3\n2\n1",
        "starter_code": "n = 3\n# Напиши while-цикл\n",
        "hints": [
            "while n > 0:",
            "    print(n)",
            "    n -= 1",
        ],
    },
    {
        "index": 11,
        "title": "Обработка ошибок",
        "theory": (
            "📚 <b>Урок 12: Обработка ошибок</b>\n\n"
            "try/except ловит ошибки:\n\n"
            "  try:\n"
            "      x = int('abc')\n"
            "  except ValueError:\n"
            "      print('Не число!')\n\n"
            "👇 <b>Задание:</b>\n"
            "Напиши try/except: попробуй int('hello'), если ValueError — выведи 'Ошибка: не число'"
        ),
        "expected_output": "Ошибка: не число",
        "starter_code": "# Обработай ошибку\n",
        "hints": [
            "try:",
            "    x = int('hello')",
            "except ValueError:",
            "    print('Ошибка: не число')",
        ],
    },
    {
        "index": 12,
        "title": "Методы строк",
        "theory": (
            "📚 <b>Урок 13: Методы строк</b>\n\n"
            "У строк есть методы:\n\n"
            "  text = 'hello world'\n"
            "  text.upper()      # HELLO WORLD\n"
            "  text.lower()      # hello world\n"
            "  text.replace('o', '0')  # hell0 w0rld\n"
            "  text.split(' ')   # ['hello', 'world']\n"
            "  len(text)         # 11\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай s = 'python', вызови upper() и выведи результат"
        ),
        "expected_output": "PYTHON",
        "starter_code": "# Создай строку и вызови upper()\ns = 'python'\n",
        "hints": [
            "s = 'python'",
            "print(s.upper())",
        ],
    },
    {
        "index": 13,
        "title": "Классы",
        "theory": (
            "📚 <b>Урок 14: Классы</b>\n\n"
            "Класс — шаблон для объектов:\n\n"
            "  class Cat:\n"
            "      def __init__(self, name):\n"
            "          self.name = name\n"
            "      \n"
            "      def say(self):\n"
            "          return f'{self.name} говорит Мяу'\n"
            "  \n"
            "  cat = Cat('Барсик')\n"
            "  print(cat.say())  # Барсик говорит Мяу\n\n"
            "👇 <b>Задание:</b>\n"
            "Создай класс Dog с __init__(self, name) и методом bark(self), который возвращает f'{self.name} говорит Гав'. Создай dog = Dog('Рекс') и выведи dog.bark()"
        ),
        "expected_output": "Рекс говорит Гав",
        "starter_code": "# Создай класс Dog\n\nclass Dog:\n    def __init__(self, name):\n        self.name = name\n",
        "hints": [
            "def bark(self):",
            "    return f'{self.name} говорит Гав'",
            "dog = Dog('Рекс')",
            "print(dog.bark())",
        ],
    },
]
