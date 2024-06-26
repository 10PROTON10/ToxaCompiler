import json
import math


class ASTOptimizer:
    def __init__(self, ast_file):
        with open(ast_file, 'r') as file:
            self.ast = json.load(file)

    def fold_constants(self, ast):
        for statement in ast:
            if 'assignmentStatement' in statement:
                expression = statement['assignmentStatement']['expression']
                if 'arithmetic' in expression:
                    left = expression['arithmetic']['left']
                    right = expression['arithmetic']['right']
                    if 'value' in left and 'value' in right:
                        operator = expression['arithmetic']['operator']
                        if operator == 'PLUS':
                            value = left['value'] + right['value']
                        elif operator == 'MINUS':
                            value = left['value'] - right['value']
                        elif operator == 'MUL':
                            value = left['value'] * right['value']
                        elif operator == 'DIV':
                            value = left['value'] / right['value']
                        statement['assignmentStatement']['expression'] = {
                            'type': left['type'],
                            'value': value
                        }

    def check_for_var(self, expr):
        if expr['type'] == 'ID':
            return False
        elif expr['type'] in ['PLUS', 'MINUS', 'MUL', 'DIV']:
            return self.check_for_var(expr['left']) and self.check_for_var(expr['right'])
        return True

    def calculate(self, expr):
        if expr['type'] == 'INT':
            return expr['value']
        elif expr['type'] == 'FLOAT':
            return expr['value']
        elif expr['type'] == 'PLUS':
            return self.calculate(expr['left']) + self.calculate(expr['right'])
        elif expr['type'] == 'MINUS':
            return self.calculate(expr['left']) - self.calculate(expr['right'])
        elif expr['type'] == 'MUL':
            return self.calculate(expr['left']) * self.calculate(expr['right'])
        elif expr['type'] == 'DIV':
            return self.calculate(expr['left']) / self.calculate(expr['right'])

    def traverse(self, node):
        if isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, dict):
                    node[key] = self.traverse(value)
                elif isinstance(value, list):
                    node[key] = [self.traverse(item) for item in value]

            if node.get('type') in ['PLUS', 'MINUS', 'MUL', 'DIV']:
                if self.check_for_var(node):
                    value = self.calculate(node)
                    if value is not None:
                        if isinstance(value, int):
                            return {'type': 'INT', 'value': int(value)}
                        else:
                            return {'type': 'FLOAT', 'value': float(value)}
        return node

    def find_used_variables(self, node, used_vars):
        if isinstance(node, dict):
            if node.get('type') == 'ID':
                used_vars.add(node['value'])
            for key, value in node.items():
                self.find_used_variables(value, used_vars)
        elif isinstance(node, list):
            for item in node:
                self.find_used_variables(item, used_vars)

    def find_all_variables(self, node, all_vars):
        if isinstance(node, dict):
            if node.get('assignmentStatement'):
                var_name = node['assignmentStatement']['ID']
                all_vars.add(var_name)
            for key, value in node.items():
                self.find_all_variables(value, all_vars)
        elif isinstance(node, list):
            for item in node:
                self.find_all_variables(item, all_vars)

    def remove_dead_code(self, node, used_vars, all_vars):
        if isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, list):
                    node[key] = [self.remove_dead_code(item, used_vars, all_vars) for item in value if
                                 self.remove_dead_code(item, used_vars, all_vars) is not None]
                else:
                    node[key] = self.remove_dead_code(value, used_vars, all_vars)

            if node.get('assignmentStatement'):
                var_name = node['assignmentStatement']['ID']
                if var_name not in used_vars:
                    return None  # Удаляем мертвый код
        elif isinstance(node, list):
            new_node = []
            for child in node:
                result = self.remove_dead_code(child, used_vars, all_vars)
                if result is not None:
                    new_node.append(result)
            return new_node
        return node

    def remove_redundant_operations(self, node):
        if isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, dict):
                    node[key] = self.remove_redundant_operations(value)
                elif isinstance(value, list):
                    node[key] = [self.remove_redundant_operations(item) for item in value]

            if node.get('type') in ['PLUS', 'MINUS', 'MUL', 'DIV']:
                left = self.calculate(node['left'])
                right = self.calculate(node['right'])
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    result = eval(f"{left} {node['type']} {right}")
                    if isinstance(result, int):
                        return {'type': 'INT', 'value': int(result)}
                    else:
                        return {'type': 'FLOAT', 'value': float(result)}
        elif isinstance(node, list):
            new_node = []
            for child in node:
                new_node.append(self.remove_redundant_operations(child))
            return new_node
        return node

    def optimize(self):
        self.ast = self.traverse(self.ast)

        all_vars = set()
        self.find_all_variables(self.ast, all_vars)

        used_vars = set()
        self.find_used_variables(self.ast, used_vars)

        self.ast = self.remove_dead_code(self.ast, used_vars, all_vars)
        self.ast = self.remove_redundant_operations(self.ast)
        self.fold_constants(self.ast)

    def save_ast(self, output_file):
        with open(output_file, 'w') as file:
            json.dump(self.ast, file, indent=2)


def optimize_ast(ast_file, output_file):
    optimizer = ASTOptimizer(ast_file)
    optimizer.optimize()
    optimizer.save_ast(output_file)



if __name__ == "__main__":
    input_filename = 'ast.json'
    output_filename = 'upgrade.json'
    optimize_ast(input_filename, output_filename)