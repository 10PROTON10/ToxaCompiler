import json
from antlr4 import *
from ToxaLanguageLexer import ToxaLanguageLexer
from ToxaLanguageParser import ToxaLanguageParser
from ast_create import ASTBuilder, MyErrorListener
import llvmlite.ir as ir
import llvmlite.binding as llvm

from translatetollvm import LLVMTranslator


class Compiler:
    def __init__(self, input_file, output_file):
        self.input_file = FileStream(input_file)
        self.output_file = output_file

        print(f"Processing file: {input_file}")

        # Lexer
        self.lexer = ToxaLanguageLexer(self.input_file)
        self.lexer.removeErrorListeners()
        self.error_listener = MyErrorListener()
        self.lexer.addErrorListener(self.error_listener)

        # Token Stream
        self.stream = CommonTokenStream(self.lexer)

        # Parser
        self.parser = ToxaLanguageParser(self.stream)
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(self.error_listener)

        # Parse Tree
        self.tree = self.parser.program()

        # If no syntax errors
        if not self.error_listener.has_errors:
            print("Parsing completed successfully")
            self.ast_builder = ASTBuilder()
            self.ast = self.ast_builder.visit(self.tree)
            self.save_ast()
            #         # Create LLVM module and builder
            #         self.module = ir.Module(name="main")
            #         self.builder = ir.IRBuilder()
            #
            #         # Create and walk CustomToxaListener
            #         printer = CustomToxaListener(self.builder, self.module, self.ast)
            #         walker = ParseTreeWalker()
            #         walker.walk(printer, self.tree)
            #
            #         # Compile the LLVM module
            #         self.compile(printer)
            #     else:
            #         print("Parsing failed with syntax errors")
            #
            # def compile(self, gen_module):
            #     llvm.initialize()
            #     llvm.initialize_native_target()
            #     llvm.initialize_native_asmprinter()
            #
            #     target = llvm.Target.from_default_triple()
            #     target_machine = target.create_target_machine(codemodel="small")
            #
            #     gen_module.module.triple = llvm.get_default_triple()
            #     gen_module.module.data_layout = target_machine.target_data
            #
            #     module_ref = llvm.parse_assembly(str(gen_module.module))
            #     module_ref.verify()
            #
            #     with open("output.l", "w") as f:
            #         f.write(str(gen_module.module))
            #
            #     print(str(gen_module.module))

    def save_ast(self):
        with open(self.output_file, "w") as f:
            json.dump(self.ast, f, indent=4)
        print(f"AST saved to: {self.output_file}")

        # Process AST
        translator = LLVMTranslator()
        translator.translate_program(self.ast)
        llvm_code = translator.generate_code()
        with open("output.ll", "w") as output_file:
            output_file.write(llvm_code)


if __name__ == '__main__':
    input_file = "input_program.txt"
    output_file = "ast.json"
    compiler = Compiler(input_file, output_file)