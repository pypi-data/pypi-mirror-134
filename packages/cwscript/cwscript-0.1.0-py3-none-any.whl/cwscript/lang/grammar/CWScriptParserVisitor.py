# Generated from ./grammar/CWScriptParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CWScriptParser import CWScriptParser
else:
    from CWScriptParser import CWScriptParser

# This class defines a complete generic visitor for a parse tree produced by CWScriptParser.

class CWScriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CWScriptParser#sourceFile.
    def visitSourceFile(self, ctx:CWScriptParser.SourceFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#topLevelStmt.
    def visitTopLevelStmt(self, ctx:CWScriptParser.TopLevelStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#contractDefn.
    def visitContractDefn(self, ctx:CWScriptParser.ContractDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#interfaceList.
    def visitInterfaceList(self, ctx:CWScriptParser.InterfaceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#interfaceVal.
    def visitInterfaceVal(self, ctx:CWScriptParser.InterfaceValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#interfaceDefn.
    def visitInterfaceDefn(self, ctx:CWScriptParser.InterfaceDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#interfaceExtDefn.
    def visitInterfaceExtDefn(self, ctx:CWScriptParser.InterfaceExtDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#importStmt.
    def visitImportStmt(self, ctx:CWScriptParser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#contractBody.
    def visitContractBody(self, ctx:CWScriptParser.ContractBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#interfaceBody.
    def visitInterfaceBody(self, ctx:CWScriptParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#contractItem.
    def visitContractItem(self, ctx:CWScriptParser.ContractItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#interfaceItem.
    def visitInterfaceItem(self, ctx:CWScriptParser.InterfaceItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#errorDefn.
    def visitErrorDefn(self, ctx:CWScriptParser.ErrorDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#errorDefnBlock.
    def visitErrorDefnBlock(self, ctx:CWScriptParser.ErrorDefnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#errorDefnList.
    def visitErrorDefnList(self, ctx:CWScriptParser.ErrorDefnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#eventDefn.
    def visitEventDefn(self, ctx:CWScriptParser.EventDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#eventDefnBlock.
    def visitEventDefnBlock(self, ctx:CWScriptParser.EventDefnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#eventDefnList.
    def visitEventDefnList(self, ctx:CWScriptParser.EventDefnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#stateDefn.
    def visitStateDefn(self, ctx:CWScriptParser.StateDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#stateDefnBlock.
    def visitStateDefnBlock(self, ctx:CWScriptParser.StateDefnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#stateDefnList.
    def visitStateDefnList(self, ctx:CWScriptParser.StateDefnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#itemDefn.
    def visitItemDefn(self, ctx:CWScriptParser.ItemDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#mapDefn.
    def visitMapDefn(self, ctx:CWScriptParser.MapDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#mapDefnKeys.
    def visitMapDefnKeys(self, ctx:CWScriptParser.MapDefnKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#mapDefnKey.
    def visitMapDefnKey(self, ctx:CWScriptParser.MapDefnKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#instantiateDefn.
    def visitInstantiateDefn(self, ctx:CWScriptParser.InstantiateDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#instantiateDecl.
    def visitInstantiateDecl(self, ctx:CWScriptParser.InstantiateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#implDefn.
    def visitImplDefn(self, ctx:CWScriptParser.ImplDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#implDefnBlock.
    def visitImplDefnBlock(self, ctx:CWScriptParser.ImplDefnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#implDefnItem.
    def visitImplDefnItem(self, ctx:CWScriptParser.ImplDefnItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#execDefn.
    def visitExecDefn(self, ctx:CWScriptParser.ExecDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#execDefnBlock.
    def visitExecDefnBlock(self, ctx:CWScriptParser.ExecDefnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#namedFnDefnList.
    def visitNamedFnDefnList(self, ctx:CWScriptParser.NamedFnDefnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#execDecl.
    def visitExecDecl(self, ctx:CWScriptParser.ExecDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#execDeclBlock.
    def visitExecDeclBlock(self, ctx:CWScriptParser.ExecDeclBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#namedFnDeclList.
    def visitNamedFnDeclList(self, ctx:CWScriptParser.NamedFnDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#queryDefn.
    def visitQueryDefn(self, ctx:CWScriptParser.QueryDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#queryDefnBlock.
    def visitQueryDefnBlock(self, ctx:CWScriptParser.QueryDefnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#queryDecl.
    def visitQueryDecl(self, ctx:CWScriptParser.QueryDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#queryDeclBlock.
    def visitQueryDeclBlock(self, ctx:CWScriptParser.QueryDeclBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#enumVariant.
    def visitEnumVariant(self, ctx:CWScriptParser.EnumVariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#enumVariant_struct.
    def visitEnumVariant_struct(self, ctx:CWScriptParser.EnumVariant_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#enumVariant_tuple.
    def visitEnumVariant_tuple(self, ctx:CWScriptParser.EnumVariant_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#enumVariant_unit.
    def visitEnumVariant_unit(self, ctx:CWScriptParser.EnumVariant_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#tupleMembers.
    def visitTupleMembers(self, ctx:CWScriptParser.TupleMembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#parenStructMembers.
    def visitParenStructMembers(self, ctx:CWScriptParser.ParenStructMembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#curlyStructMembers.
    def visitCurlyStructMembers(self, ctx:CWScriptParser.CurlyStructMembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#structMember.
    def visitStructMember(self, ctx:CWScriptParser.StructMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#RefTypeExpr.
    def visitRefTypeExpr(self, ctx:CWScriptParser.RefTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ParamzdTypeExpr.
    def visitParamzdTypeExpr(self, ctx:CWScriptParser.ParamzdTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#AutoTypeExpr.
    def visitAutoTypeExpr(self, ctx:CWScriptParser.AutoTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TupleTypeExpr.
    def visitTupleTypeExpr(self, ctx:CWScriptParser.TupleTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ShortOptionTypeExpr.
    def visitShortOptionTypeExpr(self, ctx:CWScriptParser.ShortOptionTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ReflectiveTypeExpr.
    def visitReflectiveTypeExpr(self, ctx:CWScriptParser.ReflectiveTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TypeDefnExpr.
    def visitTypeDefnExpr(self, ctx:CWScriptParser.TypeDefnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TypePathExpr.
    def visitTypePathExpr(self, ctx:CWScriptParser.TypePathExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ShortVecTypeExpr.
    def visitShortVecTypeExpr(self, ctx:CWScriptParser.ShortVecTypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#typePath.
    def visitTypePath(self, ctx:CWScriptParser.TypePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#reflectiveTypePath.
    def visitReflectiveTypePath(self, ctx:CWScriptParser.ReflectiveTypePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#typeDefn.
    def visitTypeDefn(self, ctx:CWScriptParser.TypeDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#autoStructDefn.
    def visitAutoStructDefn(self, ctx:CWScriptParser.AutoStructDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#structDefn.
    def visitStructDefn(self, ctx:CWScriptParser.StructDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#enumDefn.
    def visitEnumDefn(self, ctx:CWScriptParser.EnumDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#typeAliasDefn.
    def visitTypeAliasDefn(self, ctx:CWScriptParser.TypeAliasDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#namedFnDecl.
    def visitNamedFnDecl(self, ctx:CWScriptParser.NamedFnDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#namedFnDefn.
    def visitNamedFnDefn(self, ctx:CWScriptParser.NamedFnDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnType.
    def visitFnType(self, ctx:CWScriptParser.FnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnArgs.
    def visitFnArgs(self, ctx:CWScriptParser.FnArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnArgList.
    def visitFnArgList(self, ctx:CWScriptParser.FnArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnArg.
    def visitFnArg(self, ctx:CWScriptParser.FnArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnArgChecks.
    def visitFnArgChecks(self, ctx:CWScriptParser.FnArgChecksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#NormalFnBody.
    def visitNormalFnBody(self, ctx:CWScriptParser.NormalFnBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ArrowFnBody.
    def visitArrowFnBody(self, ctx:CWScriptParser.ArrowFnBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#LetStmt.
    def visitLetStmt(self, ctx:CWScriptParser.LetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#AssignStmt.
    def visitAssignStmt(self, ctx:CWScriptParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IfStmt.
    def visitIfStmt(self, ctx:CWScriptParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ForStmt.
    def visitForStmt(self, ctx:CWScriptParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ExecStmt.
    def visitExecStmt(self, ctx:CWScriptParser.ExecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#EmitStmt.
    def visitEmitStmt(self, ctx:CWScriptParser.EmitStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ReturnStmt.
    def visitReturnStmt(self, ctx:CWScriptParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#FailStmt.
    def visitFailStmt(self, ctx:CWScriptParser.FailStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ExprStmt.
    def visitExprStmt(self, ctx:CWScriptParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#letStmt_.
    def visitLetStmt_(self, ctx:CWScriptParser.LetStmt_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#letLHS.
    def visitLetLHS(self, ctx:CWScriptParser.LetLHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#AndExpr.
    def visitAndExpr(self, ctx:CWScriptParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#MultDivModExpr.
    def visitMultDivModExpr(self, ctx:CWScriptParser.MultDivModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#QueryExpr.
    def visitQueryExpr(self, ctx:CWScriptParser.QueryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ValExpr.
    def visitValExpr(self, ctx:CWScriptParser.ValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#UnaryNotExpr.
    def visitUnaryNotExpr(self, ctx:CWScriptParser.UnaryNotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#CompExpr.
    def visitCompExpr(self, ctx:CWScriptParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#UnarySignExpr.
    def visitUnarySignExpr(self, ctx:CWScriptParser.UnarySignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ExpExpr.
    def visitExpExpr(self, ctx:CWScriptParser.ExpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#OrExpr.
    def visitOrExpr(self, ctx:CWScriptParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IfExp.
    def visitIfExp(self, ctx:CWScriptParser.IfExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#EqExpr.
    def visitEqExpr(self, ctx:CWScriptParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TableLookupExpr.
    def visitTableLookupExpr(self, ctx:CWScriptParser.TableLookupExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#MemberAccessExpr.
    def visitMemberAccessExpr(self, ctx:CWScriptParser.MemberAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:CWScriptParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#FnCallExpr.
    def visitFnCallExpr(self, ctx:CWScriptParser.FnCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#GroupedExpr.
    def visitGroupedExpr(self, ctx:CWScriptParser.GroupedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#UnitVal.
    def visitUnitVal(self, ctx:CWScriptParser.UnitValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#StructVal.
    def visitStructVal(self, ctx:CWScriptParser.StructValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TupleStructVal.
    def visitTupleStructVal(self, ctx:CWScriptParser.TupleStructValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#VecVal.
    def visitVecVal(self, ctx:CWScriptParser.VecValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#StringVal.
    def visitStringVal(self, ctx:CWScriptParser.StringValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IntegerVal.
    def visitIntegerVal(self, ctx:CWScriptParser.IntegerValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#DecimalVal.
    def visitDecimalVal(self, ctx:CWScriptParser.DecimalValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TrueVal.
    def visitTrueVal(self, ctx:CWScriptParser.TrueValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#FalseVal.
    def visitFalseVal(self, ctx:CWScriptParser.FalseValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IdentVal.
    def visitIdentVal(self, ctx:CWScriptParser.IdentValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#structVal_.
    def visitStructVal_(self, ctx:CWScriptParser.StructVal_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#structValMembers.
    def visitStructValMembers(self, ctx:CWScriptParser.StructValMembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#structValMember.
    def visitStructValMember(self, ctx:CWScriptParser.StructValMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ifExpr_.
    def visitIfExpr_(self, ctx:CWScriptParser.IfExpr_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IfClause.
    def visitIfClause(self, ctx:CWScriptParser.IfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IfLetClause.
    def visitIfLetClause(self, ctx:CWScriptParser.IfLetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#elseIfClauses.
    def visitElseIfClauses(self, ctx:CWScriptParser.ElseIfClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#elseClause.
    def visitElseClause(self, ctx:CWScriptParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ForInStmt.
    def visitForInStmt(self, ctx:CWScriptParser.ForInStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ForTimesStmt.
    def visitForTimesStmt(self, ctx:CWScriptParser.ForTimesStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#forItem.
    def visitForItem(self, ctx:CWScriptParser.ForItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#identList.
    def visitIdentList(self, ctx:CWScriptParser.IdentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#exprList.
    def visitExprList(self, ctx:CWScriptParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#namedExprList.
    def visitNamedExprList(self, ctx:CWScriptParser.NamedExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#namedExpr.
    def visitNamedExpr(self, ctx:CWScriptParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ident.
    def visitIdent(self, ctx:CWScriptParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#cwspec.
    def visitCwspec(self, ctx:CWScriptParser.CwspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#reservedKeyword.
    def visitReservedKeyword(self, ctx:CWScriptParser.ReservedKeywordContext):
        return self.visitChildren(ctx)



del CWScriptParser