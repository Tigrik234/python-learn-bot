"""The 200-lesson curriculum used by both the Telegram bot and its Mini App.

Run ``python lessons.py`` after editing the curriculum to regenerate the
published webapp/lessons.json file.
"""

import json
from pathlib import Path


# Each module has a short teaching note and ten focused, runnable exercises.
# Exercise rows contain: title, learning point, task, solution, expected output.
MODULES = [
    ("Python foundations", "Names, values, expressions and readable output are the building blocks of every Python program.",
     [
        ("Hello, Python", "A program is a sequence of instructions; print displays a value.", "Print the greeting exactly as shown.", "print('Привет, Python!')", "Привет, Python!"),
        ("Variables and assignment", "Assignment binds a descriptive name to an object; the name can be used again later.", "Store Python in language and print the value.", "language = 'Python'\nprint(language)", "Python"),
        ("Integers and arithmetic", "Integers support arithmetic operators; parentheses make the intended order explicit.", "Calculate and print seven times eight.", "answer = 7 * 8\nprint(answer)", "56"),
        ("Floating-point numbers", "Float values represent fractions approximately, so round when a fixed number of decimal places is needed.", "Round 1 divided by 3 to two decimal places.", "ratio = 1 / 3\nprint(f'{ratio:.2f}')", "0.33"),
        ("Strings and quoting", "Strings are immutable text values; single and double quotes both delimit them.", "Join two words with a space and print the result.", "word = 'Python'\nprint('Learn ' + word)", "Learn Python"),
        ("f-strings", "An f-string evaluates expressions inside braces and is a readable way to format values.", "Put the value 2026 into the sentence.", "year = 2026\nprint(f'Welcome to {year}')", "Welcome to 2026"),
        ("Booleans", "True and False represent truth values and are the result of comparisons.", "Check whether 10 is greater than 3.", "print(10 > 3)", "True"),
        ("None and absence", "None is the single value used to represent no result or an intentionally empty value.", "Print the value returned by a function with no return statement.", "def find_item():\n    pass\nprint(find_item())", "None"),
        ("Type inspection", "type reports an object's type; isinstance is often preferable when checking a type family.", "Print the type name of the integer 42.", "value = 42\nprint(type(value).__name__)", "int"),
        ("Comments and readable code", "Comments explain intent for people and are ignored by Python; names and spacing improve readability.", "Add a comment and print the result of 2 + 3.", "# A small arithmetic expression\nprint(2 + 3)", "5"),
     ]),
    ("Conditions and loops", "Control flow chooses which statements run and repeats work without copying the same code.",
     [
        ("Comparison operators", "Comparisons such as ==, !=, < and >= produce Boolean values.", "Test whether 8 is at least 8.", "print(8 >= 8)", "True"),
        ("if and else", "An if statement runs an indented block when its condition is true, otherwise else runs.", "Classify 17 as adult (18+) or child.", "age = 17\nif age >= 18:\n    print('adult')\nelse:\n    print('child')", "child"),
        ("elif branches", "elif adds mutually exclusive cases and keeps multi-way decisions easy to scan.", "Convert score 82 to the label pass.", "score = 82\nif score >= 90:\n    label = 'excellent'\nelif score >= 60:\n    label = 'pass'\nelse:\n    label = 'retry'\nprint(label)", "pass"),
        ("Boolean logic", "and, or and not combine conditions; short-circuit evaluation can avoid unnecessary work.", "Check that a value is inside the inclusive range 1 through 10.", "value = 7\nprint(1 <= value <= 10)", "True"),
        ("for and range", "for visits each item in an iterable; range(stop) produces integers up to, but not including, stop.", "Print each number from 1 through 4 on its own line.", "for number in range(1, 5):\n    print(number)", "1\n2\n3\n4"),
        ("Looping over text", "Strings are iterable, so a for loop can process each character in order.", "Print the letters of cat on separate lines.", "for letter in 'cat':\n    print(letter)", "c\na\nt"),
        ("while loops", "while repeats as long as a condition remains true; update loop state to guarantee progress.", "Count down from 3 to 1.", "count = 3\nwhile count:\n    print(count)\n    count -= 1", "3\n2\n1"),
        ("break and continue", "break exits the nearest loop; continue skips the rest of the current iteration.", "Print 1, 2 and 4, skipping 3.", "for number in range(1, 5):\n    if number == 3:\n        continue\n    print(number)", "1\n2\n4"),
        ("Loop else", "A loop's else block runs only when the loop finishes normally, not when it exits through break.", "Show that searching 1, 2, 3 completes without finding 9.", "for value in [1, 2, 3]:\n    if value == 9:\n        print('found')\n        break\nelse:\n    print('not found')", "not found"),
        ("Nested loops", "Nested loops model a product of two sequences; keep each loop's responsibility small.", "Print a 2-by-2 coordinate grid.", "for row in range(2):\n    for column in range(2):\n        print(f'{row},{column}')", "0,0\n0,1\n1,0\n1,1"),
     ]),
    ("Collections: lists and tuples", "Sequence collections preserve order; choose a mutable list or an immutable tuple to match the job.",
     [
        ("Creating lists", "Lists hold ordered, mutable values and use square brackets.", "Create a list of three colors and print its length.", "colors = ['red', 'green', 'blue']\nprint(len(colors))", "3"),
        ("Indexing and slicing", "Indexes start at zero; slices select a half-open range and do not include the stop index.", "Print the middle three items.", "values = [10, 20, 30, 40, 50]\nprint(values[1:4])", "[20, 30, 40]"),
        ("Appending and extending", "append adds one object, while extend adds each item from another iterable.", "Append 3 and then 4 to the list.", "values = [1, 2]\nvalues.append(3)\nvalues.extend([4])\nprint(values)", "[1, 2, 3, 4]"),
        ("Removing list values", "remove deletes the first matching value; pop removes and returns an item by index.", "Remove the final item and print what remains.", "items = ['a', 'b', 'c']\nitems.pop()\nprint(items)", "['a', 'b']"),
        ("List membership", "The in operator checks whether a value occurs in a collection.", "Check whether the list contains Python.", "languages = ['Ruby', 'Python', 'Go']\nprint('Python' in languages)", "True"),
        ("List comprehensions", "A comprehension builds a new list from an iterable with an optional filter.", "Create squares for 1, 2 and 3.", "squares = [n * n for n in range(1, 4)]\nprint(squares)", "[1, 4, 9]"),
        ("Sorting and key functions", "sorted returns a new sorted list; key can extract the value used for comparison.", "Sort words by their length.", "words = ['pear', 'fig', 'banana']\nprint(sorted(words, key=len))", "['fig', 'pear', 'banana']"),
        ("Tuples and unpacking", "Tuples are immutable sequences; unpacking assigns their elements to names in one operation.", "Unpack and print the coordinates.", "point = (4, 9)\nx, y = point\nprint(x, y)", "4 9"),
        ("Enumerate", "enumerate pairs each item with a counter and avoids manually maintaining an index.", "Print each fruit with a one-based number.", "for number, fruit in enumerate(['pear', 'plum'], start=1):\n    print(number, fruit)", "1 pear\n2 plum"),
        ("Zip", "zip iterates over several iterables together and stops when the shortest one ends.", "Pair each name with its score.", "for name, score in zip(['Ada', 'Lin'], [10, 9]):\n    print(f'{name}: {score}')", "Ada: 10\nLin: 9"),
     ]),
    ("Dictionaries and sets", "Mappings look up values by key; sets represent unique elements and support mathematical set operations.",
     [
        ("Dictionary creation", "A dict stores key-value pairs and retrieves values by key rather than position.", "Create and print a person's name.", "person = {'name': 'Ada', 'age': 36}\nprint(person['name'])", "Ada"),
        ("Safe dictionary lookup", "get returns a default when a key is absent instead of raising KeyError.", "Look up a missing city with the default unknown.", "profile = {'name': 'Sam'}\nprint(profile.get('city', 'unknown'))", "unknown"),
        ("Updating dictionaries", "Assignment inserts or replaces a key; update applies several key-value pairs at once.", "Add a language field and print the mapping.", "profile = {'name': 'Sam'}\nprofile.update({'language': 'Python'})\nprint(profile)", "{'name': 'Sam', 'language': 'Python'}"),
        ("Dictionary iteration", "items provides key-value pairs for readable dictionary iteration.", "Print each key and value.", "for key, value in {'x': 2, 'y': 5}.items():\n    print(key, value)", "x 2\ny 5"),
        ("Dictionary comprehensions", "A dictionary comprehension builds mappings from an iterable expression.", "Map each number from 1 to 3 to its square.", "squares = {n: n * n for n in range(1, 4)}\nprint(squares)", "{1: 1, 2: 4, 3: 9}"),
        ("Creating sets", "A set stores unique hashable values and does not promise positional order.", "Remove duplicates from the given values and count them.", "unique = set([2, 2, 3, 3, 3])\nprint(len(unique))", "2"),
        ("Set operations", "Union, intersection and difference express relationships between groups.", "Find the shared tags.", "first = {'python', 'web'}\nsecond = {'web', 'data'}\nprint(first & second)", "{'web'}"),
        ("Membership and fast lookup", "Set membership is usually constant-time on average and is useful for repeated lookups.", "Check whether the set includes 42.", "allowed = {7, 42, 99}\nprint(42 in allowed)", "True"),
        ("Counter", "collections.Counter counts hashable values and exposes the most common values.", "Count letters in banana and print the count for a.", "from collections import Counter\ncounts = Counter('banana')\nprint(counts['a'])", "3"),
        ("defaultdict", "defaultdict creates a missing value with a factory, which is convenient for grouping.", "Group two words by their first letter.", "from collections import defaultdict\ngroups = defaultdict(list)\nfor word in ['apple', 'apricot', 'berry']:\n    groups[word[0]].append(word)\nprint(groups['a'])", "['apple', 'apricot']"),
     ]),
    ("Functions and scope", "Functions name reusable behavior; parameters, return values and scope make that behavior composable.",
     [
        ("Defining a function", "def creates a function; its indented body runs when the function is called.", "Define greet and print its greeting for Ada.", "def greet(name):\n    return f'Hello, {name}!'\nprint(greet('Ada'))", "Hello, Ada!"),
        ("Return values", "return sends a value back to the caller and immediately exits the function.", "Return the square of 7.", "def square(number):\n    return number ** 2\nprint(square(7))", "49"),
        ("Default parameters", "A default parameter is used when the caller omits that argument.", "Use the default greeting for Lin.", "def greet(name, prefix='Hi'):\n    return f'{prefix}, {name}'\nprint(greet('Lin'))", "Hi, Lin"),
        ("Keyword arguments", "Keyword arguments make calls explicit and allow parameters to be supplied by name.", "Call the formatter with a custom separator.", "def join_words(left, right, separator=' '):\n    return left + separator + right\nprint(join_words('a', 'b', separator='-'))", "a-b"),
        ("Positional-only and keyword-only", "The / and * markers can constrain how callers provide arguments.", "Call a function using its keyword-only scale.", "def multiply(value, *, scale=2):\n    return value * scale\nprint(multiply(5, scale=3))", "15"),
        ("Variable positional arguments", "*args collects extra positional arguments into a tuple.", "Sum any supplied values.", "def total(*values):\n    return sum(values)\nprint(total(2, 3, 5))", "10"),
        ("Variable keyword arguments", "**kwargs collects extra named arguments into a dictionary.", "Read the theme passed as a keyword.", "def describe(**options):\n    return options['theme']\nprint(describe(theme='dark'))", "dark"),
        ("Local and global scope", "A function's local names are separate from names in the surrounding module scope.", "Return the local message without changing the outer variable.", "message = 'outer'\ndef get_message():\n    message = 'local'\n    return message\nprint(get_message(), message)", "local outer"),
        ("Lambda and sorting", "A lambda is a small anonymous function, often useful as a sort key or callback.", "Sort pairs by their second value.", "pairs = [('a', 3), ('b', 1)]\nprint(sorted(pairs, key=lambda pair: pair[1]))", "[('b', 1), ('a', 3)]"),
        ("Docstrings and annotations", "Docstrings document a function; annotations describe expected types without enforcing them.", "Annotate and call a function that doubles an integer.", "def double(value: int) -> int:\n    '''Return twice value.'''\n    return value * 2\nprint(double(6))", "12"),
     ]),
    ("String processing", "String methods, formatting and parsing make text transformations explicit and predictable.",
     [
        ("String immutability", "String methods return new strings because strings themselves cannot be changed in place.", "Uppercase the word and print both values.", "word = 'python'\nupper = word.upper()\nprint(word, upper)", "python PYTHON"),
        ("Whitespace and trimming", "strip removes surrounding whitespace; lstrip and rstrip handle one side.", "Trim the padded label.", "label = '  ready  '\nprint(label.strip())", "ready"),
        ("Splitting and joining", "split turns text into pieces; join combines strings with a chosen separator.", "Turn a comma-separated line into a spaced list.", "parts = 'red,green,blue'.split(',')\nprint(' | '.join(parts))", "red | green | blue"),
        ("Search and replace", "find returns a position or -1; replace returns text with matching pieces substituted.", "Replace the dash with a space.", "text = 'learn-python'\nprint(text.replace('-', ' '))", "learn python"),
        ("Prefix and suffix checks", "startswith and endswith test boundaries without creating slices.", "Check whether the filename is a Python source file.", "filename = 'lesson.py'\nprint(filename.endswith('.py'))", "True"),
        ("Character classification", "Methods such as isdigit and isalpha classify a string's characters.", "Check whether 2048 contains only digits.", "print('2048'.isdigit())", "True"),
        ("String formatting", "format specifications control alignment, width, precision and numeric representation.", "Show 3.14159 with three decimal places.", "value = 3.14159\nprint(f'{value:.3f}')", "3.142"),
        ("Unicode text", "Python strings are Unicode sequences; len counts code points, not encoded bytes.", "Print the number of characters in the word café.", "word = 'café'\nprint(len(word))", "4"),
        ("Regular expressions", "The re module describes text patterns; raw strings avoid double escaping backslashes.", "Find all two-digit numbers in the text.", "import re\nprint(re.findall(r'\\d{2}', 'A7 B42 C19'))", "['42', '19']"),
        ("Safe text construction", "Build output from values with formatting rather than manually mixing types.", "Format a name and a score into one line.", "name, score = 'Mira', 95\nprint(f'{name} scored {score} points')", "Mira scored 95 points"),
     ]),
    ("Comprehensions and functional tools", "Compact iteration tools can express transformations, filters and reductions without obscuring intent.",
     [
        ("Filtering with a comprehension", "An if clause in a comprehension keeps only values that satisfy a predicate.", "Select even numbers from 1 through 8.", "evens = [n for n in range(1, 9) if n % 2 == 0]\nprint(evens)", "[2, 4, 6, 8]"),
        ("Nested comprehensions", "Nested clauses express a small Cartesian product; use ordinary loops when nesting hurts clarity.", "Create coordinate pairs for a 2-by-2 grid.", "pairs = [(x, y) for x in range(2) for y in range(2)]\nprint(pairs)", "[(0, 0), (0, 1), (1, 0), (1, 1)]"),
        ("Generator expressions", "A generator expression yields values lazily instead of building the entire result list.", "Sum the squares of the first four integers.", "total = sum(n * n for n in range(1, 5))\nprint(total)", "30"),
        ("map", "map applies a function to each item and returns a lazy iterator.", "Convert three numeric strings to integers.", "values = list(map(int, ['2', '4', '6']))\nprint(values)", "[2, 4, 6]"),
        ("filter", "filter retains items for which a predicate returns true.", "Keep words longer than three characters.", "words = list(filter(lambda word: len(word) > 3, ['sun', 'moon', 'sky']))\nprint(words)", "['moon']"),
        ("any and all", "any checks whether at least one item is truthy; all checks whether every item is truthy.", "Check whether every value is positive.", "print(all(value > 0 for value in [2, 4, 1]))", "True"),
        ("sum, min and max", "Built-in reductions summarize an iterable without writing an accumulator loop.", "Print the minimum and maximum values.", "values = [8, 3, 11, 5]\nprint(min(values), max(values))", "3 11"),
        ("Reversed and sorted", "reversed iterates backwards without mutating; sorted creates a sorted list.", "Sort scores from highest to lowest.", "scores = [70, 95, 80]\nprint(sorted(scores, reverse=True))", "[95, 80, 70]"),
        ("itertools.count", "itertools provides composable iterator tools; count creates an unbounded arithmetic sequence.", "Take the first four even values from count.", "from itertools import count, islice\nprint(list(islice(count(0, 2), 4)))", "[0, 2, 4, 6]"),
        ("itertools.groupby", "groupby groups adjacent equal keys, so sort or prepare the input when global grouping is required.", "Count each adjacent run of equal letters.", "from itertools import groupby\nprint([(key, len(list(group))) for key, group in groupby('aaabbc')])", "[('a', 3), ('b', 2), ('c', 1)]"),
     ]),
    ("Object-oriented Python", "Classes combine data and behavior; instances carry their own state while methods describe operations.",
     [
        ("Defining a class", "A class is a blueprint; __init__ initializes each newly constructed instance.", "Create a Cat whose name is Luna and print it.", "class Cat:\n    def __init__(self, name):\n        self.name = name\ncat = Cat('Luna')\nprint(cat.name)", "Luna"),
        ("Instance methods", "Instance methods receive self and can read or update instance attributes.", "Make a dog return its bark.", "class Dog:\n    def bark(self):\n        return 'woof'\nprint(Dog().bark())", "woof"),
        ("Encapsulation", "Encapsulation keeps state changes behind methods that maintain an object's invariants.", "Deposit 25 into a small account.", "class Account:\n    def __init__(self):\n        self.balance = 0\n    def deposit(self, amount):\n        self.balance += amount\naccount = Account()\naccount.deposit(25)\nprint(account.balance)", "25"),
        ("Class and instance attributes", "Class attributes are shared defaults; instance attributes belong to a particular object.", "Show the shared species and one instance name.", "class Bird:\n    species = 'bird'\n    def __init__(self, name):\n        self.name = name\nbird = Bird('Pip')\nprint(bird.species, bird.name)", "bird Pip"),
        ("Inheritance", "Inheritance lets a specialized class reuse and extend a base class.", "Override speak in a child class.", "class Animal:\n    def speak(self):\n        return '...'\nclass Fox(Animal):\n    def speak(self):\n        return 'ring-ding'\nprint(Fox().speak())", "ring-ding"),
        ("super and initialization", "super delegates behavior to the next class in the method resolution order.", "Initialize a named child through its parent.", "class Person:\n    def __init__(self, name):\n        self.name = name\nclass Student(Person):\n    def __init__(self, name, course):\n        super().__init__(name)\n        self.course = course\nprint(Student('Ari', 'Python').name)", "Ari"),
        ("Properties", "A property exposes a method-backed attribute interface while validating assignments.", "Use a property to calculate a rectangle's area.", "class Rectangle:\n    def __init__(self, width, height):\n        self.width, self.height = width, height\n    @property\n    def area(self):\n        return self.width * self.height\nprint(Rectangle(3, 4).area)", "12"),
        ("Dunder methods", "Special methods let user-defined objects participate in built-in operations such as str and len.", "Make an object print as a friendly label.", "class Label:\n    def __str__(self):\n        return 'Python learner'\nprint(str(Label()))", "Python learner"),
        ("Dataclasses", "dataclass generates common methods such as __init__ and __repr__ for data-focused classes.", "Create a point and print its coordinates.", "from dataclasses import dataclass\n@dataclass\nclass Point:\n    x: int\n    y: int\npoint = Point(2, 5)\nprint(point.x, point.y)", "2 5"),
        ("Composition", "Composition builds a larger object from smaller collaborators instead of relying on deep inheritance.", "Give a car an engine and start it through delegation.", "class Engine:\n    def start(self):\n        return 'engine on'\nclass Car:\n    def __init__(self):\n        self.engine = Engine()\n    def start(self):\n        return self.engine.start()\nprint(Car().start())", "engine on"),
     ]),
    ("Advanced object model", "Python's object model supports protocols, controlled attributes, descriptors and deliberate interface design.",
     [
        ("Abstract base classes", "An abstract base class documents a required interface and prevents incomplete direct instances.", "Implement the required area method in a concrete shape.", "from abc import ABC, abstractmethod\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\nclass Square(Shape):\n    def __init__(self, side):\n        self.side = side\n    def area(self):\n        return self.side ** 2\nprint(Square(4).area())", "16"),
        ("Protocols by behavior", "Duck typing and Protocol-style design depend on supported operations rather than a concrete parent class.", "Use any object with a read method.", "class Source:\n    def read(self):\n        return 'data'\ndef load(source):\n    return source.read()\nprint(load(Source()))", "data"),
        ("Static methods", "A static method belongs in a class namespace when it is related to the type but needs no instance state.", "Call a unit conversion helper from the class.", "class Temperature:\n    @staticmethod\n    def celsius_to_fahrenheit(value):\n        return value * 9 / 5 + 32\nprint(Temperature.celsius_to_fahrenheit(0))", "32.0"),
        ("Class methods", "A class method receives the class and is useful for alternative constructors.", "Construct a user from a display label.", "class User:\n    def __init__(self, name):\n        self.name = name\n    @classmethod\n    def from_label(cls, label):\n        return cls(label.strip().title())\nprint(User.from_label('  ADA ').name)", "Ada"),
        ("Slots", "Slots restrict which per-instance attributes are stored and can reduce memory for many small objects.", "Create a slotted coordinate with x equal to 3.", "class Coordinate:\n    __slots__ = ('x', 'y')\n    def __init__(self, x, y):\n        self.x, self.y = x, y\nprint(Coordinate(3, 4).x)", "3"),
        ("Custom iteration", "An iterator implements __iter__ and __next__; StopIteration signals exhaustion.", "Iterate over a simple two-value sequence.", "class Pair:\n    def __init__(self):\n        self.values = iter([4, 5])\n    def __iter__(self):\n        return self\n    def __next__(self):\n        return next(self.values)\nprint(list(Pair()))", "[4, 5]"),
        ("Descriptors", "Descriptors customize attribute access with __get__, __set__ or __delete__ methods.", "Use a descriptor that returns a fixed label.", "class Constant:\n    def __get__(self, instance, owner):\n        return 'ready'\nclass Job:\n    state = Constant()\nprint(Job().state)", "ready"),
        ("Metaclasses: inspect classes", "A class is itself an object; type can inspect its name and bases without custom metaclasses.", "Print the class name of a list subclass.", "class TaggedList(list):\n    pass\nprint(type(TaggedList()).__name__)", "TaggedList"),
        ("MRO and cooperative methods", "The method resolution order determines where Python looks for an inherited method.", "Inspect the first two names in a class hierarchy.", "class Base:\n    pass\nclass Child(Base):\n    pass\nprint([cls.__name__ for cls in Child.__mro__[:2]])", "['Child', 'Base']"),
        ("Immutable value objects", "Immutable objects are easier to share safely; frozen dataclasses prevent field reassignment.", "Create a frozen point and read its x coordinate.", "from dataclasses import dataclass\n@dataclass(frozen=True)\nclass Point:\n    x: int\n    y: int\nprint(Point(1, 2).x)", "1"),
     ]),
    ("Errors and defensive programming", "Exceptions communicate failure; catch only errors you can handle and keep cleanup predictable.",
     [
        ("Catching a specific exception", "A try block covers risky work; except names the expected failure precisely.", "Handle converting invalid text to an integer.", "try:\n    int('nope')\nexcept ValueError:\n    print('invalid number')", "invalid number"),
        ("else and finally", "else runs when try succeeds, while finally runs regardless and is suited to cleanup.", "Show success and guaranteed cleanup.", "try:\n    value = int('12')\nexcept ValueError:\n    print('bad')\nelse:\n    print(value)\nfinally:\n    print('done')", "12\ndone"),
        ("Raising exceptions", "raise signals an invalid operation; use a clear exception type and message.", "Reject a negative age with a clear message.", "def validate_age(age):\n    if age < 0:\n        raise ValueError('age must be non-negative')\ntry:\n    validate_age(-1)\nexcept ValueError as error:\n    print(error)", "age must be non-negative"),
        ("Custom exception types", "A custom exception gives callers a meaningful way to distinguish a domain failure.", "Raise and catch an empty-inventory error.", "class OutOfStockError(Exception):\n    pass\ntry:\n    raise OutOfStockError('empty')\nexcept OutOfStockError as error:\n    print(error)", "empty"),
        ("Exception chaining", "raise ... from ... preserves the original cause while presenting a higher-level error.", "Translate a parsing problem into a domain message.", "try:\n    try:\n        int('x')\n    except ValueError as cause:\n        raise RuntimeError('invalid identifier') from cause\nexcept RuntimeError as error:\n    print(type(error.__cause__).__name__)", "ValueError"),
        ("Assertions and invariants", "Assertions document assumptions during development and are not a substitute for input validation.", "Assert that the normalized result is positive.", "result = 3 * 4\nassert result > 0\nprint(result)", "12"),
        ("EAFP and LBYL", "EAFP attempts an operation and handles its exception; LBYL checks first, but can introduce races.", "Use dict.get to handle an optional key safely.", "settings = {'theme': 'dark'}\nprint(settings.get('language', 'en'))", "en"),
        ("Exception groups of work", "Keep try blocks narrow so the handler does not accidentally hide unrelated programming errors.", "Catch a missing dictionary key only around the lookup.", "data = {}\ntry:\n    value = data['id']\nexcept KeyError:\n    value = 'unknown'\nprint(value)", "unknown"),
        ("Logging errors", "The logging module records events with levels and context instead of relying on scattered print calls.", "Format a warning message without configuring external logging.", "import logging\nrecord = logging.LogRecord('app', logging.WARNING, '', 0, 'retry %s', (2,), None)\nprint(record.getMessage())", "retry 2"),
        ("Resource cleanup", "Context managers guarantee cleanup even when an operation fails.", "Use a context manager to work with an in-memory stream.", "from io import StringIO\nwith StringIO() as stream:\n    stream.write('saved')\n    print(stream.closed)", "False"),
     ]),
    ("Files and serialization", "Files and serialized formats let programs persist information; choose an encoding and close resources reliably.",
     [
        ("Path objects", "pathlib.Path represents filesystem paths with portable methods and readable operators.", "Build a child path and print its filename.", "from pathlib import PurePosixPath\npath = PurePosixPath('data') / 'notes.txt'\nprint(path.name)", "notes.txt"),
        ("Reading text in memory", "Text streams expose read and write operations; explicit encoding prevents platform-default surprises.", "Read a line from an in-memory text stream.", "from io import StringIO\nwith StringIO('hello\\nworld') as stream:\n    print(stream.readline().strip())", "hello"),
        ("Writing text in memory", "A text stream accumulates characters; real file writes should use a with block.", "Write and then read back a short note.", "from io import StringIO\nstream = StringIO()\nstream.write('study')\nprint(stream.getvalue())", "study"),
        ("CSV reading", "csv.reader handles quoting and delimiters more safely than splitting rows by commas.", "Read the second column from a CSV row.", "import csv\nfrom io import StringIO\nrows = csv.reader(StringIO('name,score\\nAda,10'))\nnext(rows)\nprint(next(rows)[1])", "10"),
        ("CSV dictionaries", "DictReader maps each CSV row to field names, making columns self-documenting.", "Read the name from a CSV record.", "import csv\nfrom io import StringIO\nreader = csv.DictReader(StringIO('name,city\\nMira,Oslo\\n'))\nprint(next(reader)['city'])", "Oslo"),
        ("JSON encoding", "JSON converts basic Python data structures to a portable text representation.", "Encode a small object as compact JSON.", "import json\nprint(json.dumps({'ok': True, 'count': 2}, sort_keys=True))", '{"count": 2, "ok": true}'),
        ("JSON decoding", "json.loads parses JSON text into Python dictionaries, lists and scalar values.", "Read the count field from JSON.", "import json\npayload = json.loads('{\"count\": 7}')\nprint(payload['count'])", "7"),
        ("Binary data", "Binary streams handle bytes rather than decoded text; bytes literals use the b prefix.", "Print the length of a three-byte value.", "data = b'ABC'\nprint(len(data))", "3"),
        ("Temporary in-memory files", "In-memory streams are useful in tests and examples that should not touch the user's filesystem.", "Copy a value through BytesIO.", "from io import BytesIO\nstream = BytesIO()\nstream.write(b'OK')\nprint(stream.getvalue().decode())", "OK"),
        ("Serialization boundaries", "Validate decoded external data because successful parsing does not guarantee a valid application schema.", "Check that a decoded payload has the required name field.", "import json\npayload = json.loads('{\"name\":\"Ada\"}')\nprint('name' in payload)", "True"),
     ]),
    ("Useful standard library", "The standard library supplies dependable tools for dates, mathematics, randomness, statistics and structured data.",
     [
        ("math functions", "math provides precise named operations such as sqrt, ceil, floor and factorial.", "Calculate the square root of 81.", "import math\nprint(math.sqrt(81))", "9.0"),
        ("Decimal arithmetic", "Decimal represents decimal fractions exactly when initialized from strings, useful for financial calculations.", "Add two decimal prices exactly.", "from decimal import Decimal\nprint(Decimal('0.10') + Decimal('0.20'))", "0.30"),
        ("Fractions", "fractions.Fraction stores rational values in reduced form.", "Add one third and one sixth.", "from fractions import Fraction\nprint(Fraction(1, 3) + Fraction(1, 6))", "1/2"),
        ("Random choices", "random provides pseudorandom choices; use secrets instead for security-sensitive tokens.", "Choose deterministically after setting a seed.", "import random\nrandom.seed(4)\nprint(random.choice(['red', 'blue', 'green']))", "red"),
        ("Statistics", "statistics offers common descriptive summaries for numeric samples.", "Calculate the median of an odd-sized sample.", "import statistics\nprint(statistics.median([1, 9, 3]))", "3"),
        ("Dates", "date represents a calendar day; isoformat gives a stable, readable representation.", "Format a known date as ISO text.", "from datetime import date\nprint(date(2024, 2, 29).isoformat())", "2024-02-29"),
        ("Timedeltas", "timedelta represents a duration and can be added to or subtracted from a date.", "Find the date seven days after January 1.", "from datetime import date, timedelta\nprint((date(2024, 1, 1) + timedelta(days=7)).isoformat())", "2024-01-08"),
        ("Enum values", "Enum gives a fixed set of named values and makes state choices clearer than magic strings.", "Print the value of a named status.", "from enum import Enum\nclass Status(Enum):\n    READY = 'ready'\nprint(Status.READY.value)", "ready"),
        ("Deque", "collections.deque supports efficient appends and pops at either end.", "Remove the oldest value from a queue.", "from collections import deque\nqueue = deque([1, 2, 3])\nprint(queue.popleft())", "1"),
        ("Heap queues", "heapq maintains a min-heap so the smallest item can be retrieved efficiently.", "Pop the smallest priority.", "import heapq\nqueue = [7, 2, 5]\nheapq.heapify(queue)\nprint(heapq.heappop(queue))", "2"),
     ]),
    ("Iterators and generators", "Iterators produce values on demand; generators make lazy pipelines and resource-friendly processing easier.",
     [
        ("Iterable versus iterator", "An iterable can create an iterator; next advances an iterator one item at a time.", "Read two values from an iterator.", "iterator = iter(['first', 'second'])\nprint(next(iterator), next(iterator))", "first second"),
        ("Writing a generator", "yield produces one value and suspends the function until the next request.", "Yield the first three positive integers.", "def numbers():\n    yield 1\n    yield 2\n    yield 3\nprint(list(numbers()))", "[1, 2, 3]"),
        ("Generator expressions", "A generator expression avoids allocating an intermediate list for one-pass work.", "Compute the sum lazily.", "total = sum(n for n in range(5))\nprint(total)", "10"),
        ("yield from", "yield from delegates iteration to another iterable or generator.", "Delegate the two-item sequence.", "def values():\n    yield from [4, 5]\nprint(list(values()))", "[4, 5]"),
        ("Generator state", "A generator remembers local variables between yields, which makes incremental algorithms natural.", "Yield running totals.", "def running():\n    total = 0\n    for value in [2, 3, 4]:\n        total += value\n        yield total\nprint(list(running()))", "[2, 5, 9]"),
        ("Lazy pipelines", "Chaining generators avoids eagerly materializing every intermediate collection.", "Square only the even numbers.", "values = (n * n for n in range(1, 7) if n % 2 == 0)\nprint(list(values))", "[4, 16, 36]"),
        ("itertools chain", "chain presents several iterables as one continuous stream.", "Join two short sequences.", "from itertools import chain\nprint(list(chain([1, 2], [3])))", "[1, 2, 3]"),
        ("itertools islice", "islice selects a bounded window from an iterator without consuming the whole stream.", "Take three values starting at index two.", "from itertools import islice\nprint(list(islice(range(10), 2, 5)))", "[2, 3, 4]"),
        ("Generator cleanup", "A generator can use try/finally to release resources when iteration completes or closes.", "Observe a finalizer after exhausting the generator.", "def values():\n    try:\n        yield 'item'\n    finally:\n        print('closed')\nprint(list(values()))", "closed\n['item']"),
        ("Infinite iterators", "Infinite iterators require a consumer limit such as islice to avoid unbounded work.", "Take four values from an infinite repeat iterator.", "from itertools import repeat, islice\nprint(list(islice(repeat('go'), 4)))", "['go', 'go', 'go', 'go']"),
     ]),
    ("Decorators and context managers", "Decorators wrap callables to add reusable behavior; context managers pair setup with guaranteed cleanup.",
     [
        ("A first decorator", "A decorator receives a function and returns a replacement callable.", "Wrap a function and preserve its return value.", "def announce(function):\n    def wrapped():\n        return '-> ' + function()\n    return wrapped\n@announce\ndef message():\n    return 'hello'\nprint(message())", "-> hello"),
        ("functools.wraps", "wraps copies useful metadata from the wrapped function to the wrapper.", "Preserve the original function name.", "from functools import wraps\ndef decorate(function):\n    @wraps(function)\n    def wrapper(*args, **kwargs):\n        return function(*args, **kwargs)\n    return wrapper\n@decorate\ndef compute():\n    return 1\nprint(compute.__name__)", "compute"),
        ("Parameterized decorators", "A decorator factory accepts configuration and returns the actual decorator.", "Prefix a result with a selected label.", "def prefix(label):\n    def decorate(function):\n        def wrapper():\n            return label + function()\n        return wrapper\n    return decorate\n@prefix('OK: ')\ndef result():\n    return 'done'\nprint(result())", "OK: done"),
        ("Memoization", "lru_cache stores previous results for hashable arguments when repeated computation is safe.", "Cache and call a small pure function.", "from functools import lru_cache\n@lru_cache(maxsize=None)\ndef cube(n):\n    return n ** 3\nprint(cube(3), cube.cache_info().hits)", "27 0"),
        ("Context manager protocol", "A context manager's enter and exit methods define the with-statement lifecycle.", "Use a simple context manager to return a label.", "class LabelContext:\n    def __enter__(self):\n        return 'inside'\n    def __exit__(self, kind, value, traceback):\n        return False\nwith LabelContext() as label:\n    print(label)", "inside"),
        ("contextlib.contextmanager", "contextmanager turns a generator with one yield into a lightweight context manager.", "Yield a resource label inside a with statement.", "from contextlib import contextmanager\n@contextmanager\ndef resource():\n    yield 'open'\nwith resource() as value:\n    print(value)", "open"),
        ("Suppressing expected errors", "contextlib.suppress is concise for a known, intentionally ignored exception.", "Suppress a missing-key lookup and continue.", "from contextlib import suppress\nwith suppress(KeyError):\n    {}['missing']\nprint('continued')", "continued"),
        ("ExitStack", "ExitStack manages a dynamic number of context managers with one lexical scope.", "Register a callback that runs when the stack closes.", "from contextlib import ExitStack\nwith ExitStack() as stack:\n    stack.callback(print, 'released')\n    print('working')", "working\nreleased"),
        ("Timing a callable", "A decorator can measure elapsed time, but timing should not change the wrapped function's behavior.", "Use perf_counter to measure a tiny deterministic operation.", "from time import perf_counter\nstart = perf_counter()\nvalue = sum(range(10))\nelapsed = perf_counter() - start\nprint(value, elapsed >= 0)", "45 True"),
        ("Decorator composition", "Multiple decorators are applied from the function outward, so order changes the composition.", "Compose two simple transformations.", "def add_a(function):\n    return lambda: 'A' + function()\ndef add_b(function):\n    return lambda: 'B' + function()\n@add_a\n@add_b\ndef value():\n    return 'C'\nprint(value())", "ABC"),
     ]),
    ("Modules and environments", "Modules organize reusable code and dependencies; imports, entry points and environments keep projects maintainable.",
     [
        ("Importing standard modules", "import binds a module namespace; explicit qualified names make dependencies visible.", "Use the math module to calculate a circle's diameter.", "import math\nprint(math.tau)", "6.283185307179586"),
        ("from imports and aliases", "A from import binds a selected name; aliases can make long module names convenient.", "Import sqrt directly and calculate 144's root.", "from math import sqrt as root\nprint(root(144))", "12.0"),
        ("Module metadata", "__name__ identifies a module; an imported module is not named __main__.", "Show that the current interactive module has a name.", "print(bool(__name__))", "True"),
        ("Import cache", "Python caches imported modules in sys.modules to avoid loading the same module repeatedly.", "Check that math is registered after import.", "import math, sys\nprint('math' in sys.modules)", "True"),
        ("Environment variables", "Environment variables configure a process without hardcoding machine-specific values.", "Read a value with a safe default.", "import os\nprint(os.getenv('PYTHON_LESSON_MODE', 'practice'))", "practice"),
        ("Command-line arguments", "sys.argv carries command-line arguments; libraries should expose functions rather than parse arguments on import.", "Read the current script argument list length.", "import sys\nprint(len(sys.argv) >= 1)", "True"),
        ("Path composition", "pathlib composes paths using operators and exposes names and suffixes portably.", "Inspect the suffix of a Python filename.", "from pathlib import PurePath\nprint(PurePath('src/app.py').suffix)", ".py"),
        ("Virtual environment concepts", "Virtual environments isolate a project's installed packages from other Python projects.", "Display the active interpreter's major version.", "import sys\nprint(sys.version_info.major)", "3"),
        ("Package versions", "Package metadata can be queried through importlib.metadata when a distribution is installed.", "Read a known standard-library distribution-independent Python version.", "import platform\nprint(platform.python_version().split('.')[0])", "3"),
        ("Main guard", "The __main__ guard separates importable definitions from command-line startup behavior.", "Call a function only through an explicit main entry point.", "def main():\n    return 'started'\nif __name__ == '__main__':\n    print(main())", "started"),
     ]),
    ("Testing and quality", "Tests make expected behavior executable; small deterministic tests catch regressions and support safe refactoring.",
     [
        ("Assertions in tests", "An assertion compares actual behavior with an expected value and fails loudly on a mismatch.", "Assert the result and print a success label.", "assert 2 + 2 == 4\nprint('test passed')", "test passed"),
        ("unittest test cases", "unittest groups checks into TestCase methods and provides expressive assertion helpers.", "Run one small unittest case.", "import unittest\nclass MathTests(unittest.TestCase):\n    def test_double(self):\n        self.assertEqual(4 * 2, 8)\nsuite = unittest.TestLoader().loadTestsFromTestCase(MathTests)\nresult = unittest.TextTestRunner(stream=__import__('io').StringIO()).run(suite)\nprint(result.wasSuccessful())", "True"),
        ("Testing edge cases", "Boundary and empty-input tests often reveal bugs that ordinary examples miss.", "Check that an empty list has no maximum only after a guard.", "values = []\nprint('empty' if not values else max(values))", "empty"),
        ("Testing exceptions", "Tests should verify both that an error occurs and that the failure communicates the contract.", "Verify a conversion raises ValueError.", "try:\n    int('bad')\nexcept ValueError:\n    print('expected error')", "expected error"),
        ("Test fixtures", "Fixtures create repeatable input state and keep each test focused on its behavior.", "Build a reusable sample dictionary and assert its id.", "def make_user():\n    return {'id': 7, 'active': True}\nassert make_user()['id'] == 7\nprint('fixture ok')", "fixture ok"),
        ("Test doubles", "A stub or fake supplies a controlled dependency so a test does not rely on external services.", "Use a fake clock value in a function.", "class FakeClock:\n    def now(self):\n        return '2026-01-01'\ndef label(clock):\n    return clock.now()\nprint(label(FakeClock()))", "2026-01-01"),
        ("unittest.mock", "Mock objects record calls and provide controlled return values for isolated unit tests.", "Set a return value and call a mock.", "from unittest.mock import Mock\nsend = Mock(return_value='queued')\nprint(send('message'), send.call_count)", "queued 1"),
        ("Parameterized checks", "A table-driven test applies the same invariant to several representative inputs.", "Check a square function over several examples.", "def square(n):\n    return n * n\ncases = [(2, 4), (3, 9), (0, 0)]\nprint(all(square(n) == expected for n, expected in cases))", "True"),
        ("Test discovery naming", "Conventional test file and method names help test runners discover checks automatically.", "Check the conventional test method prefix.", "name = 'test_round_trip'\nprint(name.startswith('test_'))", "True"),
        ("Refactoring safely", "A passing behavior test gives a safety net when implementation details are improved.", "Check that a refactored helper preserves its public result.", "def normalize_name(name):\n    return ' '.join(name.split()).title()\nassert normalize_name('  ada   lovelace ') == 'Ada Lovelace'\nprint('behavior preserved')", "behavior preserved"),
     ]),
    ("Async Python fundamentals", "asyncio supports cooperative concurrency; coroutines yield control at await points and must be awaited.",
     [
        ("Coroutine functions", "async def defines a coroutine function; calling it creates a coroutine that must be awaited.", "Check that a function is recognized as asynchronous.", "import asyncio\nasync def fetch_label():\n    return 'ready'\nprint(asyncio.iscoroutinefunction(fetch_label))", "True"),
        ("Await expressions", "await suspends the current coroutine until the awaited operation produces a result.", "Define a coroutine with an awaitable sleep and inspect its type.", "import asyncio\nasync def pause():\n    await asyncio.sleep(0)\n    return 'resumed'\nprint(asyncio.iscoroutinefunction(pause))", "True"),
        ("Creating tasks", "create_task schedules a coroutine to run concurrently on the active event loop.", "Define a task-producing coroutine without blocking the lesson runner.", "import asyncio\nasync def work():\n    return 5\nprint(asyncio.iscoroutinefunction(work))", "True"),
        ("Gathering results", "gather waits for multiple awaitables and returns results in their input order.", "Prepare two coroutines and confirm both are coroutine functions.", "import asyncio\nasync def first():\n    return 1\nasync def second():\n    return 2\nprint(all(map(asyncio.iscoroutinefunction, [first, second])))", "True"),
        ("Async delays", "asyncio.sleep is a non-blocking delay that gives other scheduled tasks time to run.", "Create a coroutine that uses a zero-length cooperative delay.", "import asyncio\nasync def tick():\n    await asyncio.sleep(0)\n    return 'tick'\nprint(asyncio.iscoroutinefunction(tick))", "True"),
        ("Async iterators", "An async iterator implements __aiter__ and __anext__ and is consumed with async for.", "Recognize an async-generator function.", "import inspect\nasync def values():\n    yield 1\nprint(inspect.isasyncgenfunction(values))", "True"),
        ("Async context managers", "Async context managers provide __aenter__ and __aexit__ for asynchronous resource lifetimes.", "Check that a class defines async entry and exit methods.", "import inspect\nclass AsyncResource:\n    async def __aenter__(self):\n        return self\n    async def __aexit__(self, *exc):\n        return False\nprint(inspect.iscoroutinefunction(AsyncResource.__aenter__))", "True"),
        ("Cancellation", "Task cancellation is cooperative and should be handled with cleanup in finally blocks.", "Document the cancellation exception type used by asyncio.", "import asyncio\nprint(asyncio.CancelledError.__name__)", "CancelledError"),
        ("Timeouts", "Timeouts bound waiting and should be chosen according to the operation's expected latency.", "Check that asyncio offers a timeout mechanism in this Python version.", "import asyncio\nprint(hasattr(asyncio, 'timeout') or hasattr(asyncio, 'wait_for'))", "True"),
        ("Async entry points", "asyncio.run is a top-level entry point for scripts, but should not be nested in an active event loop.", "Inspect the standard runner without starting a nested event loop.", "import asyncio\nprint(callable(asyncio.run))", "True"),
     ]),
    ("Async patterns and concurrency", "Async applications need bounded concurrency, cancellation-aware cleanup and careful separation of blocking work.",
     [
        ("Concurrent gather pattern", "gather is appropriate when a group of independent coroutines can run together.", "Describe the expected gather return ordering with a small regular sequence.", "results = [value * 2 for value in (1, 2, 3)]\nprint(results)", "[2, 4, 6]"),
        ("Semaphore limits", "A semaphore caps how many tasks can enter a critical region concurrently.", "Create a semaphore with a maximum of three permits.", "import asyncio\nlimit = asyncio.Semaphore(3)\nprint(limit._value)", "3"),
        ("Queues and workers", "asyncio.Queue safely hands work between asynchronous producers and consumers.", "Create a queue and check its initial state.", "import asyncio\nqueue = asyncio.Queue()\nprint(queue.empty())", "True"),
        ("Async locks", "An asyncio.Lock coordinates coroutines that share mutable state across await points.", "Create an unlocked asynchronous lock.", "import asyncio\nlock = asyncio.Lock()\nprint(lock.locked())", "False"),
        ("Task groups", "TaskGroup scopes child task lifetimes so related work completes or fails as a unit.", "Check for structured task groups or the portable gather primitive.", "import asyncio\nprint(hasattr(asyncio, 'TaskGroup') or hasattr(asyncio, 'gather'))", "True"),
        ("Async generators", "Async generators stream values incrementally and can be consumed with async for.", "Declare a two-value async generator and inspect it.", "import inspect\nasync def stream():\n    yield 'a'\n    yield 'b'\nprint(inspect.isasyncgenfunction(stream))", "True"),
        ("Blocking work and threads", "Blocking calls stall the event loop; asyncio.to_thread can move suitable blocking work off-loop.", "Check that asyncio exposes a thread-related concurrency helper.", "import asyncio\nprint(hasattr(asyncio, 'to_thread') or hasattr(asyncio, 'run_coroutine_threadsafe'))", "True"),
        ("Async exception handling", "Exceptions raised by awaited work should be handled at a boundary where recovery is possible.", "Handle a regular exception and preserve a stable result.", "async def operation():\n    try:\n        raise ValueError('offline')\n    except ValueError:\n        return 'retry later'\nprint('coroutine defined')", "coroutine defined"),
        ("Backpressure", "Bounded queues apply backpressure so producers cannot create unlimited pending work.", "Create a queue with a capacity of two.", "import asyncio\nqueue = asyncio.Queue(maxsize=2)\nprint(queue.maxsize)", "2"),
        ("Async service design", "Separate I/O orchestration from pure transformation code to keep async services testable.", "Use a pure transform alongside an async function declaration.", "def normalize(value):\n    return value.strip().lower()\nasync def service(value):\n    return normalize(value)\nprint(normalize('  READY '))", "ready"),
     ]),
    ("Algorithms and complexity", "Algorithmic thinking starts with correct invariants and considers how runtime and memory grow with input size.",
     [
        ("Linear search", "A linear scan checks items in order and takes time proportional to the input length.", "Find the index of 7 in a short list.", "values = [3, 7, 9]\nprint(values.index(7))", "1"),
        ("Binary search invariant", "Binary search repeatedly halves a sorted search interval, giving logarithmic comparisons.", "Compute the midpoint of a search interval.", "low, high = 0, 9\nprint((low + high) // 2)", "4"),
        ("Counting frequencies", "A frequency table counts occurrences in one pass and supports fast later lookups.", "Count repeated letters.", "from collections import Counter\nprint(Counter('mississippi')['s'])", "4"),
        ("Two-pointer scan", "Two pointers can scan inward from both ends and avoid repeatedly building slices.", "Check whether the short sequence is a palindrome.", "values = [1, 2, 1]\nprint(values == values[::-1])", "True"),
        ("Stack behavior", "A stack is last-in, first-out and can be implemented with list append and pop.", "Pop the most recently added item.", "stack = ['first', 'last']\nprint(stack.pop())", "last"),
        ("Queue behavior", "A queue is first-in, first-out; deque avoids the shifting cost of removing a list's first item.", "Take the earliest queued item.", "from collections import deque\nqueue = deque(['first', 'next'])\nprint(queue.popleft())", "first"),
        ("Recursion and base cases", "A recursive function needs a base case and a step that moves toward it.", "Calculate 4! recursively.", "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n - 1)\nprint(factorial(4))", "24"),
        ("Memoized recursion", "Memoization saves repeated subproblem results and can turn exponential recursion into a tractable algorithm.", "Calculate a Fibonacci value with caching.", "from functools import lru_cache\n@lru_cache(None)\ndef fib(n):\n    return n if n < 2 else fib(n - 1) + fib(n - 2)\nprint(fib(10))", "55"),
        ("Stable sorting", "Python's sort is stable, so equal keys preserve their previous relative order.", "Sort records by score and retain ties in input order.", "records = [('A', 2), ('B', 1), ('C', 2)]\nprint([name for name, score in sorted(records, key=lambda row: row[1])])", "['B', 'A', 'C']"),
        ("Big-O intuition", "Big-O describes how growth scales, not exact elapsed time; nested full scans often yield quadratic work.", "Count pairs generated by a 3-by-3 nested loop.", "print(sum(1 for _ in range(3) for __ in range(3)))", "9"),
     ]),
    ("Architecture and design", "Good architecture separates responsibilities, limits coupling and makes behavior easy to test and evolve.",
     [
        ("Single responsibility", "A function with one clear responsibility is easier to name, test and change independently.", "Separate a pure total calculation from presentation.", "def total(prices):\n    return sum(prices)\nprint(total([2, 3, 5]))", "10"),
        ("Pure functions", "A pure function depends only on its inputs and returns a value without hidden side effects.", "Call a deterministic conversion twice.", "def to_celsius(fahrenheit):\n    return (fahrenheit - 32) * 5 / 9\nprint(to_celsius(32))", "0.0"),
        ("Dependency injection", "Passing a dependency explicitly makes a component easier to reuse and test.", "Inject a sender instead of constructing it inside the function.", "def notify(sender, text):\n    return sender(text)\nprint(notify(lambda value: 'sent: ' + value, 'hello'))", "sent: hello"),
        ("Layered design", "Separating input, domain logic and output prevents transport details from leaking into core rules.", "Keep the domain calculation independent of display formatting.", "def discount(price, rate):\n    return price * (1 - rate)\nprint(discount(100, 0.1))", "90.0"),
        ("Repository pattern", "A repository abstracts persistence behind a small interface so business logic can use a fake in tests.", "Use an in-memory repository to retrieve a record.", "class Repository:\n    def get(self, key):\n        return {'id': key}\nprint(Repository().get(7)['id'])", "7"),
        ("Configuration objects", "A configuration object groups related settings and makes defaults visible at application boundaries.", "Create a dataclass with a readable port default.", "from dataclasses import dataclass\n@dataclass\nclass Config:\n    port: int = 8000\nprint(Config().port)", "8000"),
        ("Domain validation", "Validate domain invariants at a clear boundary so invalid states do not spread through the application.", "Reject an empty username.", "def validate_username(name):\n    if not name.strip():\n        return 'required'\n    return 'ok'\nprint(validate_username('   '))", "required"),
        ("Event-driven design", "Events describe facts that already happened and let independent handlers react without direct coupling.", "Represent a completed event with a small immutable record.", "from dataclasses import dataclass\n@dataclass(frozen=True)\nclass LessonCompleted:\n    lesson_index: int\nprint(LessonCompleted(4).lesson_index)", "4"),
        ("Adapter pattern", "An adapter translates one interface into another while leaving the underlying collaborator unchanged.", "Adapt a legacy method to a new send interface.", "class Legacy:\n    def deliver(self, text):\n        return 'delivered ' + text\nclass Sender:\n    def __init__(self, legacy):\n        self.legacy = legacy\n    def send(self, text):\n        return self.legacy.deliver(text)\nprint(Sender(Legacy()).send('note'))", "delivered note"),
        ("Maintainable boundaries", "Stable boundaries keep implementation choices behind small public functions and types.", "Expose a tiny public function that delegates to a private helper.", "def _clean(text):\n    return text.strip()\ndef clean_text(text):\n    return _clean(text)\nprint(clean_text('  hello  '))", "hello"),
     ]),
    ("Project: CLI utilities", "A command-line project benefits from clear input parsing, reusable functions, stable output and deliberate error handling.",
     [
        ("CLI greeting", "A small CLI starts with a function that accepts values rather than reading global state.", "Build a greeting for the supplied name.", "def greet(name):\n    return f'Hello, {name}!'\nprint(greet('Python learner'))", "Hello, Python learner!"),
        ("CLI argument defaults", "Defaults make optional command-line inputs convenient while keeping behavior predictable.", "Use a default output format when no option is supplied.", "options = {'format': 'text'}\nprint(options.get('format', 'json'))", "text"),
        ("Input validation", "Validate and normalize user input before passing it into core logic.", "Normalize a padded command name.", "command = '  RUN  '.strip().lower()\nprint(command)", "run"),
        ("Exit codes", "A CLI uses zero for success and a nonzero status to signal failure to scripts.", "Choose a success status for a completed action.", "success = True\nstatus = 0 if success else 1\nprint(status)", "0"),
        ("Help text", "A helpful command-line interface documents its purpose and available options.", "Create a short usage line.", "program = 'study'\nprint(f'Usage: {program} [--help]')", "Usage: study [--help]"),
        ("Table output", "Column formatting makes command output easier to scan without changing the underlying values.", "Align two labels in a simple report.", "print(f'{\"NAME\":<8} SCORE')\nprint(f'{\"Ada\":<8} 10')", "NAME     SCORE\nAda      10"),
        ("Configuration precedence", "Explicit arguments commonly override environment configuration, which overrides defaults.", "Choose the command-line value when both are available.", "default, env, argument = 'text', 'json', 'csv'\nprint(argument or env or default)", "csv"),
        ("Retry policy", "Retries should be bounded and used only when repeating an operation is safe.", "Calculate the total attempts from two retries.", "retries = 2\nprint(retries + 1)", "3"),
        ("Command dispatch", "A dispatch table maps command names to handlers and avoids long nested conditionals.", "Select the handler for the list command.", "handlers = {'list': 'show_items', 'add': 'add_item'}\nprint(handlers['list'])", "show_items"),
        ("CLI project structure", "Keep the entry point thin and place reusable behavior in importable functions.", "Call a reusable main function.", "def main():\n    return 'CLI ready'\nprint(main())", "CLI ready"),
     ]),
    ("Project: data and web concepts", "Data-oriented applications transform validated input into useful results and isolate transport concerns from domain logic.",
     [
        ("Parse a record", "Parsing turns an external representation into values that the application can validate.", "Parse a key-value line.", "key, value = 'mode=study'.split('=', 1)\nprint(key, value)", "mode study"),
        ("Validate a payload", "Schema checks confirm required fields and types before processing data.", "Check that a payload contains an integer id.", "payload = {'id': 12}\nprint(isinstance(payload.get('id'), int))", "True"),
        ("Transform records", "A transformation should be a small deterministic function from one record shape to another.", "Normalize names from an input record.", "record = {'name': '  ADA  '}\nclean = {'name': record['name'].strip().title()}\nprint(clean)", "{'name': 'Ada'}"),
        ("Aggregate data", "Aggregation combines many records into a useful summary.", "Sum the totals from two records.", "orders = [{'total': 5}, {'total': 8}]\nprint(sum(order['total'] for order in orders))", "13"),
        ("Pagination math", "Offset pagination derives a start and end from a page number and page size.", "Compute the slice for page 2 with three items per page.", "page, size = 2, 3\nstart = (page - 1) * size\nprint(start, start + size)", "3 6"),
        ("Cache key design", "A cache key must include every input that can change the cached result.", "Build a stable key from user and locale.", "user_id, locale = 7, 'en'\nprint(f'user:{user_id}:{locale}')", "user:7:en"),
        ("Idempotent updates", "An idempotent operation can be repeated without changing the final result after the first application.", "Apply a set-based tag update twice and inspect unique tags.", "tags = set()\nfor _ in range(2):\n    tags.add('python')\nprint(len(tags))", "1"),
        ("HTTP status concepts", "Status codes communicate whether a request succeeded, failed validation or needs authentication.", "Classify a successful 200 response.", "status = 200\nprint('success' if 200 <= status < 300 else 'error')", "success"),
        ("JSON response shape", "A stable response envelope makes clients less dependent on incidental internal details.", "Create a successful response envelope.", "response = {'ok': True, 'data': [1, 2]}\nprint(response['ok'], len(response['data']))", "True 2"),
        ("Project integration", "An integration test exercises several layers together while keeping external services replaceable.", "Combine parsing and domain transformation in one check.", "raw = '  lesson  '\nresult = raw.strip().title()\nprint(result)", "Lesson"),
     ]),
    ("Project: capstone and professional practice", "A finished project combines clear requirements, modular implementation, tests, documentation and maintainable delivery.",
     [
        ("Define acceptance criteria", "Acceptance criteria turn a vague request into observable behaviors that can be implemented and tested.", "Express a passing score rule as a Boolean.", "score = 80\nprint(score >= 60)", "True"),
        ("Break work into functions", "Small functions create seams for independent tests and make a capstone easier to reason about.", "Compose two small steps to format a result.", "def add(a, b):\n    return a + b\ndef label(value):\n    return f'total={value}'\nprint(label(add(3, 4)))", "total=7"),
        ("Choose data structures", "Choosing a mapping for keyed lookup or a set for uniqueness clarifies intent and complexity.", "Count distinct tags using a set.", "tags = ['python', 'async', 'python']\nprint(len(set(tags)))", "2"),
        ("Document public behavior", "Documentation explains purpose, inputs and outputs so users can rely on a stable interface.", "Return the docstring of a documented public helper.", "def slugify(text):\n    '''Convert text to a simple lowercase slug.'''\n    return text.lower().replace(' ', '-')\nprint(slugify.__doc__)", "Convert text to a simple lowercase slug."),
        ("Review code safely", "Code review checks correctness, edge cases, readability and tests before implementation details are merged.", "Use a focused predicate for a simple reviewable rule.", "def is_even(value):\n    return value % 2 == 0\nprint(is_even(14))", "True"),
        ("Versioned interfaces", "Versioning lets a project evolve public contracts without surprising existing clients.", "Represent a simple semantic version.", "version = (1, 2, 0)\nprint('.'.join(map(str, version)))", "1.2.0"),
        ("Observability", "Useful logs and metrics describe system behavior without exposing secrets or sensitive user data.", "Create a sanitized event label.", "event = {'action': 'lesson_complete', 'user_id': 7}\nprint(event['action'])", "lesson_complete"),
        ("Security-minded configuration", "Keep credentials outside source code and avoid logging or publishing secret configuration values.", "Check whether a secret is configured without printing it.", "secret = ''\nprint(bool(secret))", "False"),
        ("Release checklist", "A release checklist verifies tests, documentation and artifact consistency before deployment.", "Combine three release checks into one result.", "checks = {'tests': True, 'docs': True, 'data': True}\nprint(all(checks.values()))", "True"),
        ("Capstone reflection", "Reflecting on tradeoffs turns a working program into a maintainable project and guides the next iteration.", "Print the next improvement as a concrete project note.", "next_step = 'add focused regression tests'\nprint(next_step)", "add focused regression tests"),
     ]),
]


def _starter_code(solution, task):
    """Keep useful setup when possible and leave the final action for the learner."""
    lines = solution.splitlines()
    if len(lines) > 1 and not lines[-1].startswith(("    ", "\t")):
        return "\n".join(lines[:-1]) + "\n"
    return f"# Практика: {task}\n"


def build_lessons():
    lessons = []
    for module_number, (module_name, module_intro, exercises) in enumerate(MODULES, start=1):
        # Keep every learning area represented while selecting exactly 200
        # focused exercises from the broader curriculum outline.
        selected_exercises = exercises[:8 if module_number <= 7 else 9]
        for title, focus, task, solution, expected in selected_exercises:
            index = len(lessons)
            lesson_number = index + 1
            theory = (
                f"📚 <b>Модуль: {module_name}</b>\n\n"
                f"<b>{title}</b>\n"
                f"{module_intro}\n\n"
                f"<b>Ключевая идея.</b> {focus}\n\n"
                f"<b>Пример решения:</b>\n<pre>{solution}</pre>\n\n"
                f"👇 <b>Практика:</b>\n{task}\n"
                f"Проверь, что программа выводит:\n<pre>{expected}</pre>"
            )
            lessons.append({
                "index": index,
                "title": title,
                "theory": theory,
                "expected_output": expected,
                "starter_code": _starter_code(solution, task),
                "hints": solution.splitlines(),
            })
    return lessons


LESSONS = build_lessons()


def export_webapp_lessons(path=None):
    """Write the browser's data file using the exact same curriculum records."""
    destination = Path(path) if path else Path(__file__).parent / "webapp" / "lessons.json"
    browser_lessons = [
        {
            "index": lesson["index"],
            "title": lesson["title"],
            "theory": lesson["theory"],
            "expectedOutput": lesson["expected_output"],
            "starterCode": lesson["starter_code"],
            "hints": lesson["hints"],
        }
        for lesson in LESSONS
    ]
    destination.write_text(
        json.dumps(browser_lessons, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    export_webapp_lessons()
    print(f"Exported {len(LESSONS)} lessons.")
