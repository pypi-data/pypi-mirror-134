from antlr4 import *

from cwscript.lang.ast import *
from cwscript.lang.grammar.CWScriptLexer import CWScriptLexer
from cwscript.lang.grammar.CWScriptParser import CWScriptParser


def main():
    lexer = CWScriptLexer(FileStream("examples/cw20.cws"))
    stream = CommonTokenStream(lexer)
    parser = CWScriptParser(stream)
    tree = parser.sourceFile()
    ast_visitor = BuildASTVisitor()
    ast = ast_visitor.visitSourceFile(tree)
    print(ast)


if __name__ == "__main__":
    main()
