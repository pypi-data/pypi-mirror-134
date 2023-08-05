from sys import argv

from antlr4 import *

from cwscript.generated.grammar.CWScriptParser import CWScriptParser
from cwscript.generated.grammar.CWScriptLexer import CWScriptLexer
from cwscript.generated.grammar.CWScriptParserListener import CWScriptParserListener
from cwscript.generated.grammar.CWScriptParserVisitor import CWScriptParserVisitor
from cwscript.lang.ast import *

class CWSASTVisitor(CWScriptParserVisitor):
    """This visitor creates an AST out of the Parse Tree."""

    def visitSourceFile(self, ctx: CWScriptParser.SourceFileContext):
        return FileCode(body=ctx.children)

    def visitIdentList(self, ctx: CWScriptParser.IdentListContext):
        return ctx.children

class CWSContractModelListener(CWScriptParserListener):

    def __init__(self):
        self.models = []

    def enterContractDefn(self, ctx: CWScriptParser.ContractDefnContext):
        self.models.append({
            "name": ctx.name.text,
            "interfaces": ctx.interfaces and [x.text for x in ctx.interfaces.Ident()],
            "parent": ctx.parent and ctx.parent.text
        })

def parse_file(file_name: str):
    fs = FileStream(file_name)
    lexer = CWScriptLexer(fs)
    stream = CommonTokenStream(lexer)
    parser = CWScriptParser(stream)
    parse_tree = parser.sourceFile()
    ast = CWSASTVisitor().visit(parse_tree)
    get_contracts = CWSContractModelListener()
    walker = ParseTreeWalker()
    walker.walk(get_contracts, ast)

    print(get_contracts.models)
    
if __name__ == "__main__":
    parse_file(argv[1])