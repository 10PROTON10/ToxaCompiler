import re
from antlr4 import *
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from antlr4.error.ErrorListener import ErrorListener

# Класс MyErrorListener для обработки ошибок
class MyErrorListener(ErrorListener):
    def __init__(self):
        self.has_errors = False
        self.declared_functions = {}  # Словарь для хранения объявленных функций

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        raise Exception("Ошибка на строке " + str(line) + ":" + str(column) + " " + msg)


def add_declared_functions(input_file, declared_functions):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().startswith('function'):
                # Используем регулярное выражение для поиска названия функции
                match = re.search(r'function\s+(\w+)\s*\(', line)
                if match:
                    function_name = match.group(1)
                    declared_functions[function_name] = True

def check_indentation(input_file):
    correct_indentation = True
    errors = []
    indent_stack = [0]  # Стек для отслеживания уровня отступов

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            stripped_line = line.lstrip()
            if not stripped_line:  # Пропускаем пустые строки
                continue

            current_indent = len(line) - len(stripped_line)
            expected_indent = indent_stack[-1]

            if stripped_line.startswith(('if', 'while', 'for', 'function')):
                if current_indent != expected_indent:
                    errors.append(f"Ошибка отступа на строке {i + 1}: {line.strip()}")
                    correct_indentation = False
                indent_stack.append(current_indent + 4)
            elif stripped_line.startswith(('endif', 'endwhile', 'endfor', 'endfunction')):
                indent_stack.pop()
                expected_indent = indent_stack[-1]
                if current_indent != expected_indent:
                    errors.append(f"Ошибка отступа на строке {i + 1}: {line.strip()}")
                    correct_indentation = False
            elif stripped_line.startswith('else'):
                expected_indent = indent_stack[-1] - 4
                if current_indent != expected_indent:
                    errors.append(f"Ошибка отступа на строке {i + 1}: {line.strip()}")
                    correct_indentation = False
            else:
                if current_indent != expected_indent:
                    errors.append(f"Ошибка отступа на строке {i + 1}: {line.strip()}")
                    correct_indentation = False

    return correct_indentation, errors

def check_undefined_functions(input_file, declared_functions):
    undefined_function_calls = []

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            function_calls = re.findall(r'\bprint\s*\(\s*(\w+)\s*\(', line)
            for function_call in function_calls:
                if function_call not in declared_functions:
                    undefined_function_calls.append((i + 1, function_call))

    return undefined_function_calls


def check_syntax(input_file):
    # Проверка отступов
    correct_indentation, indentation_errors = check_indentation(input_file)
    if not correct_indentation:
        print("Обнаружены ошибки отступов:")
        for error in indentation_errors:
            print(error)
        return

    # Чтение входного файла
    input_stream = FileStream(input_file, encoding='utf-8')

    # Создание лексера
    lexer = ToxaLanguageLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Создание парсера
    parser = ToxaLanguageParser(token_stream)

    # Создание и добавление нашего обработчика ошибок
    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    try:
        # Начало разбора с начального правила 'program'
        parser.program()
        if not error_listener.has_errors:
            # Ручное добавление названий функций в declared_functions
            add_declared_functions(input_file, error_listener.declared_functions)

            # Получаем список необъявленных функций
            undefined_functions = check_undefined_functions(input_file, error_listener.declared_functions)
            if undefined_functions:
                error_messages = []
                for line, function_name in undefined_functions:
                    error_messages.append(f"Ошибка на строке {line}: вызов несуществующей функции '{function_name}'")
                return "\n".join(error_messages)
            else:
                return "Синтаксический анализ завершен успешно, ошибок не найдено."
    except Exception as e:
        return str(e)

# def main():
#     # Запрашиваем у пользователя путь к файлу
#     input_file = 'input_program.txt'
#
#     # Проверка отступов
#     correct_indentation, indentation_errors = check_indentation(input_file)
#     if not correct_indentation:
#         print("Обнаружены ошибки отступов:")
#         for error in indentation_errors:
#             print(error)
#         return
#
#     # Проверяем синтаксис файла
#     result = check_syntax(input_file)
#
#     # Выводим результат проверки
#     print(result)
#
# if __name__ == '__main__':
#     main()
