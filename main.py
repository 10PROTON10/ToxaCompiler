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
    def __init__(self, input_file, output_file):
        self.input_file_path = input_file  # Save input file path
        self.output_file_path = output_file  # Save output file path
        self.llvm_code = None  # Initialize llvm_code attribute

        print(f"Processing file: {input_file}")

        # Lexer
        self.input_file_stream = FileStream(self.input_file_path)  # Create file stream
        self.lexer = ToxaLanguageLexer(self.input_file_stream)
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

        # Check syntax
        syntax_result = syntaxerror.check_syntax(self.input_file_path)
        if syntax_result != "Синтаксический анализ завершен успешно, ошибок не найдено.":
            print("Ошибка в синтаксисе файла:")
            print(syntax_result)
            return
        else:
            print("Parsing completed successfully")
            self.ast_builder = ASTBuilder()
            self.ast = self.ast_builder.visit(self.tree)
            self.save_ast()

    def save_ast(self):
        with open(self.output_file_path, "w") as f:  # Use output_file_path
            json.dump(self.ast, f, indent=4)
        print(f"AST saved to: {self.output_file_path}")

        # Close the file
        f.close()

        # Process AST
        translator = LLVMTranslator()
        translator.translate_program(self.ast)
        self.llvm_code = translator.generate_code()  # Assign llvm_code attribute

        # Define output file path based on optimization status
        output_ll_file = "output_opt.ll" if "upgrade" in self.output_file_path else "output_no_opt.ll"

        with open(output_ll_file, "w") as output_file:
            output_file.write(self.llvm_code)
        print(f"Created LLVM code: {output_ll_file}")


if __name__ == '__main__':
    input_file = "input_program.txt"
    output_file = "ast.json"
    upgrade_file = 'upgrade.json'
    # Measure time without optimization
    start_time_no_opt = time.time()
    compiler = Compiler(input_file, output_file)
    end_time_no_opt = time.time()
    llvm_code_no_opt_time = end_time_no_opt - start_time_no_opt

    print(f"LLVM code generation time without optimization: {llvm_code_no_opt_time:.4f} seconds")

    # Apply optimization to LLVM code
    optimize_ast(output_file, upgrade_file)

    # Measure time with optimization
    start_time_with_opt = time.time()
    compiler = Compiler(input_file, upgrade_file)
    end_time_with_opt = time.time()
    llvm_code_with_opt_time = end_time_with_opt - start_time_with_opt

    print(f"LLVM code generation time with optimization: {llvm_code_with_opt_time:.4f} seconds")

    # Output execution time
    print(f"Time without optimization: {llvm_code_no_opt_time:.4f} seconds")
    print(f"Time with optimization: {llvm_code_with_opt_time:.4f} seconds")