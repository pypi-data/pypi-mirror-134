from dataclasses import dataclass
from itertools import *
from typing import Any, Callable, Iterator, List, Optional, Type, TypeVar, Union

from antlr4 import *

from cwscript.lang.grammar.CWScriptParser import CWScriptParser
from cwscript.lang.grammar.CWScriptParserListener import CWScriptParserListener
from cwscript.lang.grammar.CWScriptParserVisitor import CWScriptParserVisitor
from cwscript.util.strings import pascal_to_snake, snake_to_pascal

T = TypeVar("T")

def iis(test, *types: list) -> bool:
    """Returns `True` if `isinstance(test, t)` works for ANY `t` in `types`"""
    return any(isinstance(test, t) for t in types)


def _collect(item, predicate: Callable[[Any], bool], *, dfs: bool = True):
    nodes = []
    if dfs:
        # depth-first
        if predicate(item):
            nodes.append(item)
        if iis(item, _Ast):
            for child in item.__dict__.values():
                nodes.extend(_collect(child, predicate))
        elif iis(item, list, tuple):
            for elem in item:
                nodes.extend(_collect(elem, predicate))
        else:
            return nodes
    else:
        # breadth-first
        if predicate(item):
            nodes.append(item)
        if _Ast.is_ast(item):
            for child in item.__dict__.values():
                if predicate(child):
                    nodes.append(child)
        elif iis(item, list, tuple):
            for elem in item:
                if predicate(elem):
                    nodes.append(elem)
        else:
            return nodes
        nodes.extend(_collect(elem, predicate, dfs=False))
    return nodes

@dataclass
class ASTNode:
    ctx: ParserRuleContext

    def collect(self, predicate: Callable[[Any], bool], *, dfs: bool = True) -> list:
        """Gets children for which the provided predicate returns True."""
        return _collect(self, predicate)

    def collect_type(self, _type: T, **kwargs) -> List[T]:
        return self.collect(lambda x: iis(x, _type), **kwargs)

    def contains_type(self, _type, **kwargs):
        return len(self.collect_type(_type, **kwargs)) > 0

    def __contains__(self, _type) -> bool:
        """Alias for the 'in' operator."""
        if iis(_type, list, tuple):
            return self.contains_type(_type)
        return self.contains_type(_type)

    
@dataclass
class SourceFile(ASTNode):
    stmts: any

@dataclass
class ContractDefn(ASTNode):
    name: "Ident"
    parent: "Ident"
    interfaces: list

@dataclass
class Ident(ASTNode):
    symbol: any

    def to_pascal(self) -> "Ident":
        return Ident(snake_to_pascal(str(self.symbol)))

    def to_snake(self) -> "Ident":
        return Ident(pascal_to_snake(str(self.symbol)))

    def __str__(self) -> str:
        return str(self.symbol)


class BuildASTVisitor(CWScriptParserVisitor):
    def visitSourceFile(self, ctx: CWScriptParser.SourceFileContext):
        stmts = ctx.topLevelStmt()
        return SourceFile(ctx, stmts=[self.visitTopLevelStmt(stmt) for stmt in stmts])

    def visitContractDefn(self, ctx: CWScriptParser.ContractDefnContext):
        return ContractDefn(
             ctx,
             name=self.visitIdent(ctx.name),
             parent=self.visitIdent(ctx.parent),
             interfaces=self.visitIdentList(ctx.interfaces),
        )
    
    def visitIdent(self, ctx: CWScriptParser.IdentContext):
        return ctx and Ident(ctx, ctx.getText())
    
    def visitIdentList(self, ctx: CWScriptParser.IdentListContext):
        return ctx and [self.visitIdent(x) for x in ctx.ident()]
