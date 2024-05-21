# import llvmlite.ir as ir
# import llvmlite.binding as llvm
#
# class LLVMTranslator:
#     def __init__(self, tac_file):
#         self.module = ir.Module()
#         self.builder = None
#         self.current_function = None
#         self.symbol_table = {}  # Словарь для отслеживания переменных и их соответствующих LLVM IR значений
#         self.parse_tac(tac_file)
#
#     def parse_tac(self, tac_file):
#         # Здесь будет код для чтения промежуточного трёхадресного кода из файла и его обработки
#         pass
#
#     def translate_tac_to_llvm(self):
#         # Здесь будет код для перевода промежуточного трёхадресного кода в LLVM IR
#         pass
#
#     def save_ir_to_file(self, output_file):
#         # Здесь будет код для сохранения LLVM IR в файл
#         pass
#
# if __name__ == "__main__":
#     tac_file = "tac_code.txt"
#     llvm_translator = LLVMTranslator(tac_file)
#     llvm_translator.translate_tac_to_llvm()
#     llvm_translator.save_ir_to_file("output.ll")
#
#
# def parse_tac(self, tac_file):
#     with open(tac_file, "r") as f:
#         lines = f.readlines()
#
#     for line in lines:
#         line = line.strip()
#         if line:
#             self.parse_tac_line(line)
#
#
# def parse_tac_line(self, line):
#     parts = line.split()
#     if len(parts) < 3:
#         raise ValueError("Invalid TAC instruction: " + line)
#
#     instruction = parts[1]
#     if instruction == "=":
#         # Присваивание
#         dest = parts[0]
#         op = parts[2]
#         if op == "call":
#             # Вызов функции
#             self.parse_function_call(dest, parts[3:])
#         else:
#             # Арифметическая операция
#             self.parse_assignment(dest, parts[2:])
#     elif instruction == "goto":
#         # Безусловный переход
#         label = parts[2]
#         self.parse_goto(label)
#     elif instruction == "if":
#         # Условный переход
#         condition = parts[2]
#         label = parts[4]
#         self.parse_if(condition, label)
#     elif instruction == "print":
#         # Вывод на экран
#         value = parts[2]
#         self.parse_print(value)
#     else:
#         raise ValueError("Unknown TAC instruction: " + instruction)
#
# def parse_assignment(self, dest, parts):
#     if len(parts) < 3:
#         raise ValueError("Invalid assignment instruction")
#
#     value = parts[2]
#     if value.isdigit():
#         # Если значение - целое число
#         value_type = ir.IntType(32)
#         value_inst = ir.Constant(value_type, int(value))
#     elif value.replace('.', '', 1).isdigit():
#         # Если значение - число с плавающей точкой
#         value_type = ir.DoubleType()
#         value_inst = ir.Constant(value_type, float(value))
#     else:
#         # Иначе это переменная, создаем инструкцию загрузки
#         value_ptr = self.module.get_global(value)
#         if value_ptr is None:
#             raise ValueError("Unknown variable: " + value)
#         value_inst = self.builder.load(value_ptr)
#
#     dest_ptr = self.module.get_global(dest)
#     if dest_ptr is None:
#         raise ValueError("Unknown variable: " + dest)
#
#     self.builder.store(value_inst, dest_ptr)
#
# def parse_function_call(self, dest, parts):
#     if len(parts) < 2:
#         raise ValueError("Invalid function call instruction")
#
#     func_name = parts[0]
#     args = parts[1:]
#
#     # Получаем указатель на функцию
#     func_ptr = self.module.get_global(func_name)
#     if func_ptr is None:
#         raise ValueError("Unknown function: " + func_name)
#
#     # Создаем список аргументов
#     arg_insts = []
#     for arg in args:
#         if arg.isdigit():
#             # Если аргумент - целое число
#             arg_inst = ir.Constant(ir.IntType(32), int(arg))
#         elif arg.replace('.', '', 1).isdigit():
#             # Если аргумент - число с плавающей точкой
#             arg_inst = ir.Constant(ir.DoubleType(), float(arg))
#         else:
#             # Иначе это переменная, создаем инструкцию загрузки
#             arg_ptr = self.module.get_global(arg)
#             if arg_ptr is None:
#                 raise ValueError("Unknown variable: " + arg)
#             arg_inst = self.builder.load(arg_ptr)
#         arg_insts.append(arg_inst)
#
#     # Создаем инструкцию вызова функции
#     result = self.builder.call(func_ptr, arg_insts)
#
#     # Если есть переменная назначения, сохраняем результат вызова
#     if dest:
#         dest_ptr = self.module.get_global(dest)
#         if dest_ptr is None:
#             raise ValueError("Unknown variable: " + dest)
#         self.builder.store(result, dest_ptr)


import json
from llvmlite import ir

class LLVMTranslator:
    def __init__(self):
        self.module = ir.Module(name="my_module")
        self.builder = None
        self.func = None
        self.block = None
        self.variables = {}

    def ensure_builder_initialized(self):
        if self.builder is None:
            func_type = ir.FunctionType(ir.VoidType(), [])
            self.func = ir.Function(self.module, func_type, name="main")
            block = self.func.append_basic_block('entry')
            self.builder = ir.IRBuilder(block)

    def translate(self, ast):
        self.ensure_builder_initialized()
        for statement in ast:
            print(f"Translating statement: {statement}")  # Debug: print each statement
            self.translate_statement(statement)
        return str(self.module)

    def translate_statement(self, statement):
        if 'assignmentStatement' in statement:
            self.translate_assignment(statement['assignmentStatement'])
        elif 'printStatement' in statement:
            self.translate_print(statement['printStatement'])
        elif 'ifStatement' in statement:
            self.translate_if(statement['ifStatement'])
        elif 'ifElseStatement' in statement:
            self.translate_if_else(statement['ifElseStatement'])
        elif 'forStatement' in statement:
            self.translate_for(statement['forStatement'])
        elif 'whileStatement' in statement:
            self.translate_while(statement['whileStatement'])
        elif 'functionStatement' in statement:
            self.translate_function(statement['functionStatement'])
        elif 'functionCall' in statement:
            self.translate_function_call(statement['functionCall'])
        elif 'returnStatement' in statement:
            self.translate_return(statement['returnStatement'])
        elif 'expression' in statement:
            self.translate_expression(statement['expression'])

    def translate_assignment(self, statement):
        self.ensure_builder_initialized()
        var_type = self.translate_type(statement['type'])
        var_name = statement['ID']
        var_value = self.translate_expression(statement['expression'])

        if var_name in self.variables:
            var_ptr = self.variables[var_name]
        else:
            var_ptr = ir.GlobalVariable(self.module, var_type, var_name)
            var_ptr.initializer = ir.Constant(var_type, None)  # Устанавливаем начальное значение
            self.variables[var_name] = var_ptr

        self.builder.store(var_value, var_ptr)

    def translate_print(self, statement):
        self.ensure_builder_initialized()
        if not hasattr(self, 'print_function'):
            self.print_function = ir.Function(self.module, ir.FunctionType(ir.VoidType(), [ir.IntType(32)]),
                                              name="my_print")
        value = self.translate_expression(statement['expression'])
        self.builder.call(self.print_function, [value])

    def translate_expression(self, expression):
        # Debug: print expression to understand its structure
        print(f"Translating expression: {expression}")

        if 'type' in expression:
            if expression['type'] == 'INT':
                return ir.Constant(ir.IntType(32), expression['value'])
            elif expression['type'] == 'FLOAT':
                return ir.Constant(ir.FloatType(), expression['value'])
            elif expression['type'] == 'ID':
                var_ptr = self.variables[expression['value']]
                return self.builder.load(var_ptr)
        elif 'arithmetic' in expression:
            left = self.translate_expression(expression['arithmetic']['left'])
            right = self.translate_expression(expression['arithmetic']['right'])
            operator = expression['arithmetic']['operator']
            if operator == 'PLUS':
                return self.builder.add(left, right)
            elif operator == 'MINUS':
                return self.builder.sub(left, right)
            elif operator == 'MUL':
                return self.builder.mul(left, right)
            elif operator == 'DIV':
                return self.builder.sdiv(left, right)
        elif 'comparison' in expression:
            left = self.translate_expression(expression['left'])
            right = self.translate_expression(expression['right'])
            operator = expression['comparison']
            if operator == '==':
                return self.builder.icmp_signed('==', left, right)
            elif operator == '!=':
                return self.builder.icmp_signed('!=', left, right)
            elif operator == '>':
                return self.builder.icmp_signed('>', left, right)
            elif operator == '<':
                return self.builder.icmp_signed('<', left, right)
            elif operator == '>=':
                return self.builder.icmp_signed('>=', left, right)
            elif operator == '<=':
                return self.builder.icmp_signed('<=', left, right)
        elif 'logical' in expression:
            left = self.translate_expression(expression['left'])
            right = self.translate_expression(expression['right'])
            operator = expression['logical']
            if operator == '&&':
                return self.builder.and_(left, right)
            elif operator == '||':
                return self.builder.or_(left, right)
        elif 'functionCall' in expression:
            return self.translate_function_call(expression['functionCall'])
        else:
            raise ValueError(f"Unsupported expression type: {expression}")

    def translate_type(self, type_str):
        if type_str == 'int':
            return ir.IntType(32)
        elif type_str == 'float':
            return ir.FloatType()
        else:
            raise Exception(f"Unknown type: {type_str}")

    def translate_if(self, statement):
        self.ensure_builder_initialized()
        condition = self.translate_expression(statement['condition'])
        with self.builder.if_then(condition):
            for stmt in statement['if_body']:
                self.translate_statement(stmt)

    def translate_if_else(self, statement):
        self.ensure_builder_initialized()
        print(f"Translating ifElseStatement: {statement}")  # Debug: print the ifElseStatement
        condition = self.translate_expression(statement['condition'])
        with self.builder.if_else(condition) as (then, otherwise):
            with then:
                for stmt in statement['if_body']:
                    self.translate_statement(stmt)
            with otherwise:
                for stmt in statement['else_body']:
                    self.translate_statement(stmt)

    def translate_for(self, statement):
        self.ensure_builder_initialized()
        # Создаем переменные и блоки
        self.translate_assignment(statement['initializer'])
        condition = self.translate_expression(statement['condition'])
        update = statement['update']
        body = statement['body']

        preheader_block = self.builder.block
        loop_block = self.builder.append_basic_block('loop')
        after_loop_block = self.builder.append_basic_block('after_loop')

        # Переходим в блок условия
        self.builder.branch(loop_block)
        self.builder.position_at_end(loop_block)

        # Проверяем условие
        with self.builder.if_then(condition):
            for stmt in body:
                self.translate_statement(stmt)
            # Обновляем переменную
            if update['operation'] == '++':
                self.builder.add(self.builder.load(self.variables[update['ID']]), ir.Constant(ir.IntType(32), 1))
            elif update['operation'] == '--':
                self.builder.sub(self.builder.load(self.variables[update['ID']]), ir.Constant(ir.IntType(32), 1))
            self.builder.branch(loop_block)

        # Переход в следующий блок после выхода из цикла
        self.builder.position_at_end(after_loop_block)

    def translate_while(self, statement):
        self.ensure_builder_initialized()
        # Создаем блоки для условия и тела цикла
        condition_block = self.builder.append_basic_block('condition')
        loop_block = self.builder.append_basic_block('loop')
        after_loop_block = self.builder.append_basic_block('after_loop')

        # Переход в блок условия
        self.builder.branch(condition_block)
        self.builder.position_at_end(condition_block)

        # Проверяем условие
        condition = self.translate_expression(statement['condition'])
        self.builder.cbranch(condition, loop_block, after_loop_block)

        # Тело цикла
        self.builder.position_at_end(loop_block)
        for stmt in statement['body']:
            self.translate_statement(stmt)
        self.builder.branch(condition_block)

        # Переход в следующий блок после выхода из цикла
        self.builder.position_at_end(after_loop_block)

    def translate_function(self, statement):
        self.ensure_builder_initialized()
        func_name = statement['name']
        params = [self.translate_type(param['type']) for param in statement['params']]
        func_type = ir.FunctionType(self.translate_type('void'), params)
        func = ir.Function(self.module, func_type, name=func_name)
        block = func.append_basic_block('entry')
        self.builder = ir.IRBuilder(block)

        # Создаем тело функции
        for stmt in statement['body']:
            self.translate_statement(stmt)

        self.builder.ret_void()

    def translate_function_call(self, statement):
        self.ensure_builder_initialized()
        func_name = statement['name']
        func = self.module.get_global(func_name)
        args = [self.translate_expression(arg) for arg in statement['params']]
        return self.builder.call(func, args)

    def translate_return(self, statement):
        self.ensure_builder_initialized()
        value = self.translate_expression(statement['expression'])
        self.builder.ret(value)

# Пример использования
def main():
    input_file = "ast.json"
    with open(input_file, "r") as f:
        ast = json.load(f)

    translator = LLVMTranslator()
    llvm_ir = translator.translate(ast)
    print(llvm_ir)

if __name__ == '__main__':
    main()


