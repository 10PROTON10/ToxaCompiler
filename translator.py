import json


class ThreeAddressCode:
    def __init__(self):
        self.code = []
        self.temp_counter = 0
        self.label_counter = 0

    def new_temp(self):
        temp_name = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp_name

    def new_label(self):
        label_name = f"L{self.label_counter}"
        self.label_counter += 1
        return label_name

    def add_code(self, instruction):
        self.code.append(instruction)

    def __str__(self):
        return "\n".join(self.code)

    def save_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write("\n".join(self.code))
            print(f"Промежуточный код сохранен в файл {file_path}")
        except Exception as e:
            print(f"Ошибка при сохранении промежуточного кода в файл {file_path}: {e}")


def load_ast_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            ast = json.load(file)
        return ast
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None


def process_expression(expr, tac):
    if "type" in expr:
        if expr["type"] == "INT":
            return str(expr["value"])
        elif expr["type"] == "FLOAT":
            return str(expr["value"])
        elif expr["type"] == "ID":
            return expr["value"]
        elif expr["type"] == "comparison":
            left = process_expression(expr["left"], tac)
            right = process_expression(expr["right"], tac)
            op = expr["operator"]
            temp = tac.new_temp()
            tac.add_code(f"{temp} = {left} {op} {right}")
            return temp
        elif expr["type"] == "logical":
            return process_logical_expression(expr, tac)
        elif expr["type"] == "functionCall":
            return process_function_call(expr, tac)
        elif expr["type"] == "expression":
            return process_expression(expr["expression"], tac)
        else:
            raise ValueError(f"Unknown expression type: {expr['type']}")
    elif "arithmetic" in expr:
        left = process_expression(expr["arithmetic"]["left"], tac)
        right = process_expression(expr["arithmetic"]["right"], tac)
        op = expr["arithmetic"]["operator"]
        if op == "PLUS":
            op = "+"
        elif op == "MINUS":
            op = "-"
        elif op == "MUL":
            op = "*"
        elif op == "DIV":
            op = "/"
        temp = tac.new_temp()
        tac.add_code(f"{temp} = {left} {op} {right}")
        return temp
    elif "comparison" in expr:
        left = process_expression(expr["left"], tac)
        right = process_expression(expr["right"], tac)
        op = expr["comparison"]
        temp = tac.new_temp()
        tac.add_code(f"{temp} = {left} {op} {right}")
        return temp
    elif "logical" in expr:
        return process_logical_expression(expr, tac)
    else:
        raise ValueError(f"Unknown expression structure: {expr}")

def process_logical_expression(expr, tac):
    if "logical" in expr:
        left = process_expression(expr["logical"]["left"], tac)
        right = process_expression(expr["logical"]["right"], tac)
        op = expr["logical"]["operator"]

        if op == "AND":
            temp = tac.new_temp()
            tac.add_code(f"{temp} = {left} and {right}")
        elif op == "OR":
            temp = tac.new_temp()
            tac.add_code(f"{temp} = {left} or {right}")
        else:
            raise ValueError(f"Unknown logical operator: {op}")

        return temp
    else:
        raise ValueError(f"Unknown logical expression structure: {expr}")


def process_assignment(node, tac):
    var_type = node["assignmentStatement"]["type"]
    var_name = node["assignmentStatement"]["ID"]
    expr = node["assignmentStatement"]["expression"]
    tac.add_code(f"{var_type.lower()} {var_name}")  # добавление типа переменной
    value = process_expression(expr, tac)
    tac.add_code(f"{var_name} = {value}")


def process_if(node, tac):
    condition = node["ifStatement"]["condition"]
    if_body = node["ifStatement"]["if_body"]

    condition_code = process_expression(condition, tac)
    label_if = tac.new_label()
    label_end = tac.new_label()

    tac.add_code(f"if {condition_code} goto {label_if}")
    tac.add_code(f"goto {label_end}")

    tac.add_code(f"{label_if}:")
    for stmt in if_body:
        process_node(stmt, tac)

    tac.add_code(f"{label_end}:")


def process_if_else(node, tac):
    condition = node["ifElseStatement"]["condition"]
    if_body = node["ifElseStatement"]["if_body"]
    else_body = node["ifElseStatement"]["else_body"]

    condition_code = process_expression(condition, tac)
    label_if = tac.new_label()
    label_else = tac.new_label()
    label_end = tac.new_label()

    tac.add_code(f"if {condition_code} goto {label_if}")
    tac.add_code(f"goto {label_else}")

    tac.add_code(f"{label_if}:")
    for stmt in if_body:
        process_node(stmt, tac)

    tac.add_code(f"goto {label_end}")

    tac.add_code(f"{label_else}:")
    for stmt in else_body:
        process_node(stmt, tac)

    tac.add_code(f"{label_end}:")



def process_print(node, tac):
    expr = node["printStatement"]["expression"]
    value = process_expression(expr, tac)
    tac.add_code(f"print {value}")


def process_while(node, tac):
    condition = node["whileStatement"]["condition"]
    while_body = node["whileStatement"]["body"]  # Изменено на "body"

    tac.add_code(f"Begin while")
    label_start = tac.new_label()
    label_body = tac.new_label()
    label_end = tac.new_label()

    condition_code = process_expression(condition, tac)

    tac.add_code(f"{label_start}:")
    tac.add_code(f"if {condition_code} goto {label_body}")
    tac.add_code(f"goto {label_end}")

    tac.add_code(f"{label_body}:")
    for stmt in while_body:
        process_node(stmt, tac)

    tac.add_code(f"goto {label_start}")
    tac.add_code(f"{label_end}:")
    tac.add_code(f"End while")

def process_for(node, tac):
    initializer = node["forStatement"]["initializer"]
    condition = node["forStatement"]["condition"]
    update = node["forStatement"]["update"]
    for_body = node["forStatement"]["body"]

    tac.add_code(f"Begin for")  # Метка начала цикла for

    label_start = tac.new_label()
    label_body = tac.new_label()
    label_end = tac.new_label()

    # Извлечение типа и имени переменной из инициализатора
    var_type = initializer["type"]
    var_name = initializer["ID"]

    # Обработка выражения инициализации
    init_value = process_expression(initializer["value"], tac)
    tac.add_code(f"{var_type.lower()} {var_name}")
    tac.add_code(f"{var_name} = {init_value}")

    condition_code = process_expression(condition, tac)

    tac.add_code(f"{label_start}:")
    tac.add_code(f"if {condition_code} goto {label_body}")
    tac.add_code(f"goto {label_end}")

    tac.add_code(f"{label_body}:")

    for stmt in for_body:
        process_node(stmt, tac)



    if update["operation"] == "++":
        tac.add_code(f"{update['ID']} = {update['ID']} + 1")
    elif update["operation"] == "--":
        tac.add_code(f"{update['ID']} = {update['ID']} - 1")

    tac.add_code(f"goto {label_start}")
    tac.add_code(f"{label_end}:")
    tac.add_code(f"End for")  # Метка конца цикла for

def process_function(node, tac):
    func_name = node["functionStatement"]["name"]
    params = node["functionStatement"]["params"]
    function_body = node["functionStatement"]["body"]

    tac.add_code(f"function {func_name}")

    if params:
        for param in params:
            tac.add_code(f"param {param['type'].lower()} {param['value']}")  # добавление типа параметра

    for stmt in function_body:
        process_node(stmt, tac)

    tac.add_code(f"endfunction {func_name}")


def process_function_call(node, tac):
    func_name = node["functionCall"]["name"]
    params = node["functionCall"]["params"]
    param_str = ", ".join([process_expression(param, tac) for param in params])
    temp = tac.new_temp()
    tac.add_code(f"{temp} = call {func_name}({param_str})")
    return temp



def process_return(node, tac):
    expr = node["returnStatement"]["expression"]
    value = process_expression(expr, tac)
    tac.add_code(f"return {value}")


def process_node(node, tac):
    if "assignmentStatement" in node:
        process_assignment(node, tac)
    elif "ifStatement" in node:
        process_if(node, tac)
    elif "ifElseStatement" in node:
        process_if_else(node, tac)
    elif "printStatement" in node:
        process_print(node, tac)
    elif "whileStatement" in node:
        process_while(node, tac)
    elif "forStatement" in node:
        process_for(node, tac)
    elif "functionCall" in node:
        process_function_call(node, tac)
    elif "functionStatement" in node:
        process_function(node, tac)
    elif "returnStatement" in node:
        process_return(node, tac)
    elif "expression" in node:
        process_expression(node["expression"], tac)
    # Добавьте обработку других типов узлов


def generate_three_address_code(ast):
    tac = ThreeAddressCode()
    for node in ast:
        process_node(node, tac)
    return tac

# # Пример использования
# ast = load_ast_from_file("ast.json")
# if ast:
#     tac = generate_three_address_code(ast)
#     print("Промежуточный трёхадресный код:")
#     print(tac)
#     tac.save_to_file("tac_code.txt")