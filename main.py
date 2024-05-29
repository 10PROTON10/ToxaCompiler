import json
import time
from antlr4 import *
import syntaxerror
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ast_create import ASTBuilder, MyErrorListener
from translatetollvm import LLVMTranslator
from optimizer import optimize_ast

class Compiler:
    first_run = True  # Класс-атрибут для отслеживания первого запуска

    def __init__(self, input_file, output_file):
        self.input_file_path = input_file  # Сохраняем путь к входному файлу
        self.output_file_path = output_file  # Сохраняем путь к выходному файлу
        self.llvm_code = None  # Инициализируем атрибут llvm_code

        # Лексер
        self.input_file_stream = FileStream(self.input_file_path)  # Создаем файловый поток
        self.lexer = ToxaLanguageLexer(self.input_file_stream)
        self.lexer.removeErrorListeners()
        self.error_listener = MyErrorListener()
        self.lexer.addErrorListener(self.error_listener)

        # Поток токенов
        self.stream = CommonTokenStream(self.lexer)

        # Парсер
        self.parser = ToxaLanguageParser(self.stream)
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(self.error_listener)

        # Дерево разбора
        self.tree = self.parser.program()

        # Проверка синтаксиса
        syntax_result = syntaxerror.check_syntax(self.input_file_path)
        if syntax_result != "Синтаксический анализ завершен успешно, ошибок не найдено.":
            print("Ошибка в синтаксисе файла:")
            print(syntax_result)
            return
        else:
            self.ast_builder = ASTBuilder()
            self.ast = self.ast_builder.visit(self.tree)
            if Compiler.first_run:  # Сохраняем AST только при первом запуске
                self.save_ast()
                Compiler.first_run = False

    def save_ast(self):
        with open(self.output_file_path, "w") as f:  # Используем output_file_path
            json.dump(self.ast, f, indent=4)
        print(f"AST сохранён в: {self.output_file_path}")

        # Закрываем файл
        f.close()

        # Обработка AST
        translator = LLVMTranslator()
        translator.translate_program(self.ast)
        self.llvm_code = translator.generate_code()  # Присваиваем атрибут llvm_code

        # Определяем путь к выходному файлу на основе статуса оптимизации
        output_ll_file = "output_opt.ll" if "upgrade" in self.output_file_path else "output_no_opt.ll"

        with open(output_ll_file, "w") as output_file:
            output_file.write(self.llvm_code)
        print(f"Код LLVM создан: {output_ll_file}")

if __name__ == '__main__':
    input_file = "input_program.txt"
    syntax_result = syntaxerror.check_syntax(input_file)
    if syntax_result != "Синтаксический анализ завершен успешно, ошибок не найдено.":
        print("Исправьте ошибку")
        print(syntax_result)
    else:
        print("Синтаксический анализ завершен успешно")
        print("Семантический анализ завершен успешно")
        output_file = "ast.json"
        upgrade_file = 'upgrade.json'
        # Измеряем время без оптимизации
        start_time_no_opt = time.time()
        compiler = Compiler(input_file, output_file)
        end_time_no_opt = time.time()
        llvm_code_no_opt_time = end_time_no_opt - start_time_no_opt

        print(f"Время генерации кода LLVM без оптимизации: {llvm_code_no_opt_time:.4f} секунд")

        # Применяем оптимизацию к коду LLVM
        optimize_ast(output_file, upgrade_file)

        # Измеряем время с оптимизацией
        start_time_with_opt = time.time()
        compiler = Compiler(input_file, upgrade_file)
        end_time_with_opt = time.time()
        llvm_code_with_opt_time = end_time_with_opt - start_time_with_opt

        print(f"Время генерации кода LLVM с оптимизацией: {llvm_code_with_opt_time:.4f} секунд")