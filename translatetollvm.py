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
        fmt_str = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len("%.3f\n")), name="fmt_str")
        fmt_str.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len("%.3f\n")), bytearray(b"%.3f\n"))
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
            elif "assignmentStatement" in statement:
                self.translate_assignment(statement["assignmentStatement"])
            else:
                raise ValueError(f"Unknown statement type in AST: {statement.keys()}")

    def translate_print(self, node):
        value = self.translate_expression(node["expression"])
        double_value = self.builder.fpext(value, ir.DoubleType())  # Расширяем float до double
        print_func = self.module.globals.get("printf")
        if not print_func:
            voidptr_ty = ir.IntType(8).as_pointer()
            print_func_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
            print_func = ir.Function(self.module, print_func_ty, name="printf")
        self.builder.call(print_func, [self.fmt_str_ptr, double_value])

    def translate_expression(self, expression):
        if "type" in expression:
            if expression["type"] == "INT":
                return ir.Constant(ir.IntType(32), expression["value"])
            elif expression["type"] == "FLOAT":
                return ir.Constant(ir.FloatType(), expression["value"])
            elif expression["type"] == "ID":
                var_ptr = self.func_symtab.get(expression["value"])
                if not var_ptr:
                    raise ValueError(f"Variable '{expression['value']}' is not defined")
                return self.builder.load(var_ptr)
        elif "arithmetic" in expression:
            left = self.translate_expression(expression["arithmetic"]["left"])
            right = self.translate_expression(expression["arithmetic"]["right"])
            left, right = self.auto_convert_types(left, right)
            operator = expression["arithmetic"]["operator"]
            if operator == "PLUS":
                return self.builder.fadd(left, right) if left.type == ir.FloatType() else self.builder.add(left, right)
            elif operator == "MINUS":
                return self.builder.fsub(left, right) if left.type == ir.FloatType() else self.builder.sub(left, right)
            elif operator == "MUL":
                return self.builder.fmul(left, right) if left.type == ir.FloatType() else self.builder.mul(left, right)
            elif operator == "DIV":
                return self.builder.fdiv(left, right) if left.type == ir.FloatType() else self.builder.sdiv(left, right)
            else:
                raise ValueError(f"Unknown arithmetic operator: {operator}")
        elif "comparison" in expression:
            left = self.translate_expression(expression["left"])
            right = self.translate_expression(expression["right"])
            left, right = self.auto_convert_types(left, right)
            operator = expression["comparison"]
            if left.type == ir.FloatType():
                if operator == "<":
                    return self.builder.fcmp_ordered("<", left, right)
                elif operator == ">":
                    return self.builder.fcmp_ordered(">", left, right)
                elif operator == "<=":
                    return self.builder.fcmp_ordered("<=", left, right)
                elif operator == ">=":
                    return self.builder.fcmp_ordered(">=", left, right)
                elif operator == "==":
                    return self.builder.fcmp_ordered("==", left, right)
                elif operator == "!=":
                    return self.builder.fcmp_ordered("!=", left, right)
                else:
                    raise ValueError(f"Unknown comparison operator: {operator}")
            else:
                if operator == "<":
                    return self.builder.icmp_signed("<", left, right)
                elif operator == ">":
                    return self.builder.icmp_signed(">", left, right)
                elif operator == "<=":
                    return self.builder.icmp_signed("<=", left, right)
                elif operator == ">=":
                    return self.builder.icmp_signed(">=", left, right)
                elif operator == "==":
                    return self.builder.icmp_signed("==", left, right)
                elif operator == "!=":
                    return self.builder.icmp_signed("!=", left, right)
                else:
                    raise ValueError(f"Unknown comparison operator: {operator}")
        else:
            raise ValueError("Unknown expression type in AST node.")

    def auto_convert_types(self, left, right):
        if left.type == ir.IntType(32) and right.type == ir.FloatType():
            left = self.builder.sitofp(left, ir.FloatType())
        elif left.type == ir.FloatType() and right.type == ir.IntType(32):
            right = self.builder.sitofp(right, ir.FloatType())
        return left, right

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
