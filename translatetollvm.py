import llvmlite.ir as ir
import llvmlite.binding as llvm

class LLVMTranslator:
    def __init__(self, tac_file):
        self.module = ir.Module()
        self.builder = None
        self.current_function = None
        self.symbol_table = {}  # Словарь для отслеживания переменных и их соответствующих LLVM IR значений
        self.parse_tac(tac_file)

    def parse_tac(self, tac_file):
        # Здесь будет код для чтения промежуточного трёхадресного кода из файла и его обработки
        pass

    def translate_tac_to_llvm(self):
        # Здесь будет код для перевода промежуточного трёхадресного кода в LLVM IR
        pass

    def save_ir_to_file(self, output_file):
        # Здесь будет код для сохранения LLVM IR в файл
        pass

if __name__ == "__main__":
    tac_file = "tac_code.txt"
    llvm_translator = LLVMTranslator(tac_file)
    llvm_translator.translate_tac_to_llvm()
    llvm_translator.save_ir_to_file("output.ll")


def parse_tac(self, tac_file):
    with open(tac_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line:
            self.parse_tac_line(line)


def parse_tac_line(self, line):
    parts = line.split()
    if len(parts) < 3:
        raise ValueError("Invalid TAC instruction: " + line)

    instruction = parts[1]
    if instruction == "=":
        # Присваивание
        dest = parts[0]
        op = parts[2]
        if op == "call":
            # Вызов функции
            self.parse_function_call(dest, parts[3:])
        else:
            # Арифметическая операция
            self.parse_assignment(dest, parts[2:])
    elif instruction == "goto":
        # Безусловный переход
        label = parts[2]
        self.parse_goto(label)
    elif instruction == "if":
        # Условный переход
        condition = parts[2]
        label = parts[4]
        self.parse_if(condition, label)
    elif instruction == "print":
        # Вывод на экран
        value = parts[2]
        self.parse_print(value)
    else:
        raise ValueError("Unknown TAC instruction: " + instruction)

def parse_assignment(self, dest, parts):
    if len(parts) < 3:
        raise ValueError("Invalid assignment instruction")

    value = parts[2]
    if value.isdigit():
        # Если значение - целое число
        value_type = ir.IntType(32)
        value_inst = ir.Constant(value_type, int(value))
    elif value.replace('.', '', 1).isdigit():
        # Если значение - число с плавающей точкой
        value_type = ir.DoubleType()
        value_inst = ir.Constant(value_type, float(value))
    else:
        # Иначе это переменная, создаем инструкцию загрузки
        value_ptr = self.module.get_global(value)
        if value_ptr is None:
            raise ValueError("Unknown variable: " + value)
        value_inst = self.builder.load(value_ptr)

    dest_ptr = self.module.get_global(dest)
    if dest_ptr is None:
        raise ValueError("Unknown variable: " + dest)

    self.builder.store(value_inst, dest_ptr)

def parse_function_call(self, dest, parts):
    if len(parts) < 2:
        raise ValueError("Invalid function call instruction")

    func_name = parts[0]
    args = parts[1:]

    # Получаем указатель на функцию
    func_ptr = self.module.get_global(func_name)
    if func_ptr is None:
        raise ValueError("Unknown function: " + func_name)

    # Создаем список аргументов
    arg_insts = []
    for arg in args:
        if arg.isdigit():
            # Если аргумент - целое число
            arg_inst = ir.Constant(ir.IntType(32), int(arg))
        elif arg.replace('.', '', 1).isdigit():
            # Если аргумент - число с плавающей точкой
            arg_inst = ir.Constant(ir.DoubleType(), float(arg))
        else:
            # Иначе это переменная, создаем инструкцию загрузки
            arg_ptr = self.module.get_global(arg)
            if arg_ptr is None:
                raise ValueError("Unknown variable: " + arg)
            arg_inst = self.builder.load(arg_ptr)
        arg_insts.append(arg_inst)

    # Создаем инструкцию вызова функции
    result = self.builder.call(func_ptr, arg_insts)

    # Если есть переменная назначения, сохраняем результат вызова
    if dest:
        dest_ptr = self.module.get_global(dest)
        if dest_ptr is None:
            raise ValueError("Unknown variable: " + dest)
        self.builder.store(result, dest_ptr)
