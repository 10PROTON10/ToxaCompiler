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
        self.func_symtab = {}

    def translate_program(self, ast):
        main_type = ir.FunctionType(ir.VoidType(), [])
        main_func = ir.Function(self.module, main_type, name="main")
        block = main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.create_global_fmt_str()
        self.func_symtab = {}

        for node in ast:
            if "assignmentStatement" in node:
                self.translate_assignment(node["assignmentStatement"])
            elif "whileStatement" in node:
                self.translate_while(node["whileStatement"])
            else:
                raise ValueError(f"Unknown node type in AST: {node.keys()}")

        self.builder.ret_void()

    def create_global_fmt_str(self):
        fmt_str = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len("%d\n")), name="fmt_str")
        fmt_str.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len("%d\n")), bytearray(b"%d\n"))
        self.fmt_str_ptr = self.builder.bitcast(fmt_str, ir.IntType(8).as_pointer())

    def translate_assignment(self, node):
        var_name = node["ID"]
        value = self.translate_expression(node["expression"])
        if var_name not in self.func_symtab:
            ptr = self.builder.alloca(value.type, name=var_name)
            self.func_symtab[var_name] = ptr
        else:
            ptr = self.func_symtab[var_name]
        self.builder.store(value, ptr)

    def translate_while(self, node):
        condition_node = node["condition"]
        body_node = node["body"]

        loop_condition_block = self.builder.append_basic_block(name="loop_condition")
        loop_body_block = self.builder.append_basic_block(name="loop_body")
        after_loop_block = self.builder.append_basic_block(name="after_loop")

        self.builder.branch(loop_condition_block)

        self.builder.position_at_end(loop_condition_block)
        cond_value = self.translate_expression(condition_node)
        self.builder.cbranch(cond_value, loop_body_block, after_loop_block)

        self.builder.position_at_end(loop_body_block)
        self.translate_statements(body_node)
        self.builder.branch(loop_condition_block)

        self.builder.position_at_end(after_loop_block)

    def translate_statements(self, statements):
        for statement in statements:
            if "printStatement" in statement:
                self.translate_print(statement["printStatement"])
            else:
                raise ValueError(f"Unknown statement type in AST: {statement.keys()}")

    def translate_print(self, node):
        value = self.translate_expression(node["expression"])
        print_func = self.module.globals.get("printf")
        if not print_func:
            voidptr_ty = ir.IntType(8).as_pointer()
            print_func_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
            print_func = ir.Function(self.module, print_func_ty, name="printf")
        self.builder.call(print_func, [self.fmt_str_ptr, value])

    def translate_expression(self, expression):
        if "type" in expression and expression["type"] == "INT":
            return ir.Constant(ir.IntType(32), expression["value"])
        elif "type" in expression and expression["type"] == "ID":
            var_ptr = self.func_symtab.get(expression["value"])
            if not var_ptr:
                raise ValueError(f"Variable '{expression['value']}' is not defined")
            return self.builder.load(var_ptr)
        elif "comparison" in expression:
            left = self.translate_expression(expression["left"])
            right = self.translate_expression(expression["right"])
            if expression["comparison"] == "<":
                return self.builder.icmp_signed("<", left, right)
            else:
                raise ValueError(f"Unknown comparison operator: {expression['comparison']}")
        else:
            raise ValueError("Unknown expression type in AST node.")

    def generate_code(self):
        return str(self.module)


def load_ast_from_file(filename):
    with open(filename, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    ast_filename = "ast.json"
    ast = load_ast_from_file(ast_filename)
    translator = LLVMTranslator()
    translator.translate_program(ast)
    llvm_code = translator.generate_code()
    with open("output.ll", "w") as output_file:
        output_file.write(llvm_code)


