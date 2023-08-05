# Generated from ./grammar/CWScriptParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CWScriptParser import CWScriptParser
else:
    from CWScriptParser import CWScriptParser

# This class defines a complete listener for a parse tree produced by CWScriptParser.
class CWScriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by CWScriptParser#sourceFile.
    def enterSourceFile(self, ctx:CWScriptParser.SourceFileContext):
        pass

    # Exit a parse tree produced by CWScriptParser#sourceFile.
    def exitSourceFile(self, ctx:CWScriptParser.SourceFileContext):
        pass


    # Enter a parse tree produced by CWScriptParser#topLevelStmt.
    def enterTopLevelStmt(self, ctx:CWScriptParser.TopLevelStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#topLevelStmt.
    def exitTopLevelStmt(self, ctx:CWScriptParser.TopLevelStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#contractDefn.
    def enterContractDefn(self, ctx:CWScriptParser.ContractDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#contractDefn.
    def exitContractDefn(self, ctx:CWScriptParser.ContractDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#interfaceList.
    def enterInterfaceList(self, ctx:CWScriptParser.InterfaceListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#interfaceList.
    def exitInterfaceList(self, ctx:CWScriptParser.InterfaceListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#interfaceVal.
    def enterInterfaceVal(self, ctx:CWScriptParser.InterfaceValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#interfaceVal.
    def exitInterfaceVal(self, ctx:CWScriptParser.InterfaceValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#interfaceDefn.
    def enterInterfaceDefn(self, ctx:CWScriptParser.InterfaceDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#interfaceDefn.
    def exitInterfaceDefn(self, ctx:CWScriptParser.InterfaceDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#interfaceExtDefn.
    def enterInterfaceExtDefn(self, ctx:CWScriptParser.InterfaceExtDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#interfaceExtDefn.
    def exitInterfaceExtDefn(self, ctx:CWScriptParser.InterfaceExtDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#importStmt.
    def enterImportStmt(self, ctx:CWScriptParser.ImportStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#importStmt.
    def exitImportStmt(self, ctx:CWScriptParser.ImportStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#contractBody.
    def enterContractBody(self, ctx:CWScriptParser.ContractBodyContext):
        pass

    # Exit a parse tree produced by CWScriptParser#contractBody.
    def exitContractBody(self, ctx:CWScriptParser.ContractBodyContext):
        pass


    # Enter a parse tree produced by CWScriptParser#interfaceBody.
    def enterInterfaceBody(self, ctx:CWScriptParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by CWScriptParser#interfaceBody.
    def exitInterfaceBody(self, ctx:CWScriptParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by CWScriptParser#contractItem.
    def enterContractItem(self, ctx:CWScriptParser.ContractItemContext):
        pass

    # Exit a parse tree produced by CWScriptParser#contractItem.
    def exitContractItem(self, ctx:CWScriptParser.ContractItemContext):
        pass


    # Enter a parse tree produced by CWScriptParser#interfaceItem.
    def enterInterfaceItem(self, ctx:CWScriptParser.InterfaceItemContext):
        pass

    # Exit a parse tree produced by CWScriptParser#interfaceItem.
    def exitInterfaceItem(self, ctx:CWScriptParser.InterfaceItemContext):
        pass


    # Enter a parse tree produced by CWScriptParser#errorDefn.
    def enterErrorDefn(self, ctx:CWScriptParser.ErrorDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#errorDefn.
    def exitErrorDefn(self, ctx:CWScriptParser.ErrorDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#errorDefnBlock.
    def enterErrorDefnBlock(self, ctx:CWScriptParser.ErrorDefnBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#errorDefnBlock.
    def exitErrorDefnBlock(self, ctx:CWScriptParser.ErrorDefnBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#errorDefnList.
    def enterErrorDefnList(self, ctx:CWScriptParser.ErrorDefnListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#errorDefnList.
    def exitErrorDefnList(self, ctx:CWScriptParser.ErrorDefnListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#eventDefn.
    def enterEventDefn(self, ctx:CWScriptParser.EventDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#eventDefn.
    def exitEventDefn(self, ctx:CWScriptParser.EventDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#eventDefnBlock.
    def enterEventDefnBlock(self, ctx:CWScriptParser.EventDefnBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#eventDefnBlock.
    def exitEventDefnBlock(self, ctx:CWScriptParser.EventDefnBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#eventDefnList.
    def enterEventDefnList(self, ctx:CWScriptParser.EventDefnListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#eventDefnList.
    def exitEventDefnList(self, ctx:CWScriptParser.EventDefnListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#stateDefn.
    def enterStateDefn(self, ctx:CWScriptParser.StateDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#stateDefn.
    def exitStateDefn(self, ctx:CWScriptParser.StateDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#stateDefnBlock.
    def enterStateDefnBlock(self, ctx:CWScriptParser.StateDefnBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#stateDefnBlock.
    def exitStateDefnBlock(self, ctx:CWScriptParser.StateDefnBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#stateDefnList.
    def enterStateDefnList(self, ctx:CWScriptParser.StateDefnListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#stateDefnList.
    def exitStateDefnList(self, ctx:CWScriptParser.StateDefnListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#itemDefn.
    def enterItemDefn(self, ctx:CWScriptParser.ItemDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#itemDefn.
    def exitItemDefn(self, ctx:CWScriptParser.ItemDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#mapDefn.
    def enterMapDefn(self, ctx:CWScriptParser.MapDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#mapDefn.
    def exitMapDefn(self, ctx:CWScriptParser.MapDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#mapDefnKeys.
    def enterMapDefnKeys(self, ctx:CWScriptParser.MapDefnKeysContext):
        pass

    # Exit a parse tree produced by CWScriptParser#mapDefnKeys.
    def exitMapDefnKeys(self, ctx:CWScriptParser.MapDefnKeysContext):
        pass


    # Enter a parse tree produced by CWScriptParser#mapDefnKey.
    def enterMapDefnKey(self, ctx:CWScriptParser.MapDefnKeyContext):
        pass

    # Exit a parse tree produced by CWScriptParser#mapDefnKey.
    def exitMapDefnKey(self, ctx:CWScriptParser.MapDefnKeyContext):
        pass


    # Enter a parse tree produced by CWScriptParser#instantiateDefn.
    def enterInstantiateDefn(self, ctx:CWScriptParser.InstantiateDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#instantiateDefn.
    def exitInstantiateDefn(self, ctx:CWScriptParser.InstantiateDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#instantiateDecl.
    def enterInstantiateDecl(self, ctx:CWScriptParser.InstantiateDeclContext):
        pass

    # Exit a parse tree produced by CWScriptParser#instantiateDecl.
    def exitInstantiateDecl(self, ctx:CWScriptParser.InstantiateDeclContext):
        pass


    # Enter a parse tree produced by CWScriptParser#implDefn.
    def enterImplDefn(self, ctx:CWScriptParser.ImplDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#implDefn.
    def exitImplDefn(self, ctx:CWScriptParser.ImplDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#implDefnBlock.
    def enterImplDefnBlock(self, ctx:CWScriptParser.ImplDefnBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#implDefnBlock.
    def exitImplDefnBlock(self, ctx:CWScriptParser.ImplDefnBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#implDefnItem.
    def enterImplDefnItem(self, ctx:CWScriptParser.ImplDefnItemContext):
        pass

    # Exit a parse tree produced by CWScriptParser#implDefnItem.
    def exitImplDefnItem(self, ctx:CWScriptParser.ImplDefnItemContext):
        pass


    # Enter a parse tree produced by CWScriptParser#execDefn.
    def enterExecDefn(self, ctx:CWScriptParser.ExecDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#execDefn.
    def exitExecDefn(self, ctx:CWScriptParser.ExecDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#execDefnBlock.
    def enterExecDefnBlock(self, ctx:CWScriptParser.ExecDefnBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#execDefnBlock.
    def exitExecDefnBlock(self, ctx:CWScriptParser.ExecDefnBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#namedFnDefnList.
    def enterNamedFnDefnList(self, ctx:CWScriptParser.NamedFnDefnListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#namedFnDefnList.
    def exitNamedFnDefnList(self, ctx:CWScriptParser.NamedFnDefnListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#execDecl.
    def enterExecDecl(self, ctx:CWScriptParser.ExecDeclContext):
        pass

    # Exit a parse tree produced by CWScriptParser#execDecl.
    def exitExecDecl(self, ctx:CWScriptParser.ExecDeclContext):
        pass


    # Enter a parse tree produced by CWScriptParser#execDeclBlock.
    def enterExecDeclBlock(self, ctx:CWScriptParser.ExecDeclBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#execDeclBlock.
    def exitExecDeclBlock(self, ctx:CWScriptParser.ExecDeclBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#namedFnDeclList.
    def enterNamedFnDeclList(self, ctx:CWScriptParser.NamedFnDeclListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#namedFnDeclList.
    def exitNamedFnDeclList(self, ctx:CWScriptParser.NamedFnDeclListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#queryDefn.
    def enterQueryDefn(self, ctx:CWScriptParser.QueryDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#queryDefn.
    def exitQueryDefn(self, ctx:CWScriptParser.QueryDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#queryDefnBlock.
    def enterQueryDefnBlock(self, ctx:CWScriptParser.QueryDefnBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#queryDefnBlock.
    def exitQueryDefnBlock(self, ctx:CWScriptParser.QueryDefnBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#queryDecl.
    def enterQueryDecl(self, ctx:CWScriptParser.QueryDeclContext):
        pass

    # Exit a parse tree produced by CWScriptParser#queryDecl.
    def exitQueryDecl(self, ctx:CWScriptParser.QueryDeclContext):
        pass


    # Enter a parse tree produced by CWScriptParser#queryDeclBlock.
    def enterQueryDeclBlock(self, ctx:CWScriptParser.QueryDeclBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#queryDeclBlock.
    def exitQueryDeclBlock(self, ctx:CWScriptParser.QueryDeclBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#enumVariant.
    def enterEnumVariant(self, ctx:CWScriptParser.EnumVariantContext):
        pass

    # Exit a parse tree produced by CWScriptParser#enumVariant.
    def exitEnumVariant(self, ctx:CWScriptParser.EnumVariantContext):
        pass


    # Enter a parse tree produced by CWScriptParser#enumVariant_struct.
    def enterEnumVariant_struct(self, ctx:CWScriptParser.EnumVariant_structContext):
        pass

    # Exit a parse tree produced by CWScriptParser#enumVariant_struct.
    def exitEnumVariant_struct(self, ctx:CWScriptParser.EnumVariant_structContext):
        pass


    # Enter a parse tree produced by CWScriptParser#enumVariant_tuple.
    def enterEnumVariant_tuple(self, ctx:CWScriptParser.EnumVariant_tupleContext):
        pass

    # Exit a parse tree produced by CWScriptParser#enumVariant_tuple.
    def exitEnumVariant_tuple(self, ctx:CWScriptParser.EnumVariant_tupleContext):
        pass


    # Enter a parse tree produced by CWScriptParser#enumVariant_unit.
    def enterEnumVariant_unit(self, ctx:CWScriptParser.EnumVariant_unitContext):
        pass

    # Exit a parse tree produced by CWScriptParser#enumVariant_unit.
    def exitEnumVariant_unit(self, ctx:CWScriptParser.EnumVariant_unitContext):
        pass


    # Enter a parse tree produced by CWScriptParser#tupleMembers.
    def enterTupleMembers(self, ctx:CWScriptParser.TupleMembersContext):
        pass

    # Exit a parse tree produced by CWScriptParser#tupleMembers.
    def exitTupleMembers(self, ctx:CWScriptParser.TupleMembersContext):
        pass


    # Enter a parse tree produced by CWScriptParser#parenStructMembers.
    def enterParenStructMembers(self, ctx:CWScriptParser.ParenStructMembersContext):
        pass

    # Exit a parse tree produced by CWScriptParser#parenStructMembers.
    def exitParenStructMembers(self, ctx:CWScriptParser.ParenStructMembersContext):
        pass


    # Enter a parse tree produced by CWScriptParser#curlyStructMembers.
    def enterCurlyStructMembers(self, ctx:CWScriptParser.CurlyStructMembersContext):
        pass

    # Exit a parse tree produced by CWScriptParser#curlyStructMembers.
    def exitCurlyStructMembers(self, ctx:CWScriptParser.CurlyStructMembersContext):
        pass


    # Enter a parse tree produced by CWScriptParser#structMember.
    def enterStructMember(self, ctx:CWScriptParser.StructMemberContext):
        pass

    # Exit a parse tree produced by CWScriptParser#structMember.
    def exitStructMember(self, ctx:CWScriptParser.StructMemberContext):
        pass


    # Enter a parse tree produced by CWScriptParser#RefTypeExpr.
    def enterRefTypeExpr(self, ctx:CWScriptParser.RefTypeExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#RefTypeExpr.
    def exitRefTypeExpr(self, ctx:CWScriptParser.RefTypeExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ParamzdTypeExpr.
    def enterParamzdTypeExpr(self, ctx:CWScriptParser.ParamzdTypeExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ParamzdTypeExpr.
    def exitParamzdTypeExpr(self, ctx:CWScriptParser.ParamzdTypeExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#AutoTypeExpr.
    def enterAutoTypeExpr(self, ctx:CWScriptParser.AutoTypeExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#AutoTypeExpr.
    def exitAutoTypeExpr(self, ctx:CWScriptParser.AutoTypeExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TupleTypeExpr.
    def enterTupleTypeExpr(self, ctx:CWScriptParser.TupleTypeExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TupleTypeExpr.
    def exitTupleTypeExpr(self, ctx:CWScriptParser.TupleTypeExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ShortOptionTypeExpr.
    def enterShortOptionTypeExpr(self, ctx:CWScriptParser.ShortOptionTypeExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ShortOptionTypeExpr.
    def exitShortOptionTypeExpr(self, ctx:CWScriptParser.ShortOptionTypeExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ReflectiveTypeExpr.
    def enterReflectiveTypeExpr(self, ctx:CWScriptParser.ReflectiveTypeExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ReflectiveTypeExpr.
    def exitReflectiveTypeExpr(self, ctx:CWScriptParser.ReflectiveTypeExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TypeDefnExpr.
    def enterTypeDefnExpr(self, ctx:CWScriptParser.TypeDefnExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TypeDefnExpr.
    def exitTypeDefnExpr(self, ctx:CWScriptParser.TypeDefnExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TypePathExpr.
    def enterTypePathExpr(self, ctx:CWScriptParser.TypePathExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TypePathExpr.
    def exitTypePathExpr(self, ctx:CWScriptParser.TypePathExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ShortVecTypeExpr.
    def enterShortVecTypeExpr(self, ctx:CWScriptParser.ShortVecTypeExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ShortVecTypeExpr.
    def exitShortVecTypeExpr(self, ctx:CWScriptParser.ShortVecTypeExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#typePath.
    def enterTypePath(self, ctx:CWScriptParser.TypePathContext):
        pass

    # Exit a parse tree produced by CWScriptParser#typePath.
    def exitTypePath(self, ctx:CWScriptParser.TypePathContext):
        pass


    # Enter a parse tree produced by CWScriptParser#reflectiveTypePath.
    def enterReflectiveTypePath(self, ctx:CWScriptParser.ReflectiveTypePathContext):
        pass

    # Exit a parse tree produced by CWScriptParser#reflectiveTypePath.
    def exitReflectiveTypePath(self, ctx:CWScriptParser.ReflectiveTypePathContext):
        pass


    # Enter a parse tree produced by CWScriptParser#typeDefn.
    def enterTypeDefn(self, ctx:CWScriptParser.TypeDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#typeDefn.
    def exitTypeDefn(self, ctx:CWScriptParser.TypeDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#autoStructDefn.
    def enterAutoStructDefn(self, ctx:CWScriptParser.AutoStructDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#autoStructDefn.
    def exitAutoStructDefn(self, ctx:CWScriptParser.AutoStructDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#structDefn.
    def enterStructDefn(self, ctx:CWScriptParser.StructDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#structDefn.
    def exitStructDefn(self, ctx:CWScriptParser.StructDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#enumDefn.
    def enterEnumDefn(self, ctx:CWScriptParser.EnumDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#enumDefn.
    def exitEnumDefn(self, ctx:CWScriptParser.EnumDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#typeAliasDefn.
    def enterTypeAliasDefn(self, ctx:CWScriptParser.TypeAliasDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#typeAliasDefn.
    def exitTypeAliasDefn(self, ctx:CWScriptParser.TypeAliasDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#namedFnDecl.
    def enterNamedFnDecl(self, ctx:CWScriptParser.NamedFnDeclContext):
        pass

    # Exit a parse tree produced by CWScriptParser#namedFnDecl.
    def exitNamedFnDecl(self, ctx:CWScriptParser.NamedFnDeclContext):
        pass


    # Enter a parse tree produced by CWScriptParser#namedFnDefn.
    def enterNamedFnDefn(self, ctx:CWScriptParser.NamedFnDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#namedFnDefn.
    def exitNamedFnDefn(self, ctx:CWScriptParser.NamedFnDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnType.
    def enterFnType(self, ctx:CWScriptParser.FnTypeContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnType.
    def exitFnType(self, ctx:CWScriptParser.FnTypeContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnArgs.
    def enterFnArgs(self, ctx:CWScriptParser.FnArgsContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnArgs.
    def exitFnArgs(self, ctx:CWScriptParser.FnArgsContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnArgList.
    def enterFnArgList(self, ctx:CWScriptParser.FnArgListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnArgList.
    def exitFnArgList(self, ctx:CWScriptParser.FnArgListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnArg.
    def enterFnArg(self, ctx:CWScriptParser.FnArgContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnArg.
    def exitFnArg(self, ctx:CWScriptParser.FnArgContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnArgChecks.
    def enterFnArgChecks(self, ctx:CWScriptParser.FnArgChecksContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnArgChecks.
    def exitFnArgChecks(self, ctx:CWScriptParser.FnArgChecksContext):
        pass


    # Enter a parse tree produced by CWScriptParser#NormalFnBody.
    def enterNormalFnBody(self, ctx:CWScriptParser.NormalFnBodyContext):
        pass

    # Exit a parse tree produced by CWScriptParser#NormalFnBody.
    def exitNormalFnBody(self, ctx:CWScriptParser.NormalFnBodyContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ArrowFnBody.
    def enterArrowFnBody(self, ctx:CWScriptParser.ArrowFnBodyContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ArrowFnBody.
    def exitArrowFnBody(self, ctx:CWScriptParser.ArrowFnBodyContext):
        pass


    # Enter a parse tree produced by CWScriptParser#LetStmt.
    def enterLetStmt(self, ctx:CWScriptParser.LetStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#LetStmt.
    def exitLetStmt(self, ctx:CWScriptParser.LetStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#AssignStmt.
    def enterAssignStmt(self, ctx:CWScriptParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#AssignStmt.
    def exitAssignStmt(self, ctx:CWScriptParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IfStmt.
    def enterIfStmt(self, ctx:CWScriptParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IfStmt.
    def exitIfStmt(self, ctx:CWScriptParser.IfStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ForStmt.
    def enterForStmt(self, ctx:CWScriptParser.ForStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ForStmt.
    def exitForStmt(self, ctx:CWScriptParser.ForStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ExecStmt.
    def enterExecStmt(self, ctx:CWScriptParser.ExecStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ExecStmt.
    def exitExecStmt(self, ctx:CWScriptParser.ExecStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#EmitStmt.
    def enterEmitStmt(self, ctx:CWScriptParser.EmitStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#EmitStmt.
    def exitEmitStmt(self, ctx:CWScriptParser.EmitStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ReturnStmt.
    def enterReturnStmt(self, ctx:CWScriptParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ReturnStmt.
    def exitReturnStmt(self, ctx:CWScriptParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#FailStmt.
    def enterFailStmt(self, ctx:CWScriptParser.FailStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#FailStmt.
    def exitFailStmt(self, ctx:CWScriptParser.FailStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ExprStmt.
    def enterExprStmt(self, ctx:CWScriptParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ExprStmt.
    def exitExprStmt(self, ctx:CWScriptParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#letStmt_.
    def enterLetStmt_(self, ctx:CWScriptParser.LetStmt_Context):
        pass

    # Exit a parse tree produced by CWScriptParser#letStmt_.
    def exitLetStmt_(self, ctx:CWScriptParser.LetStmt_Context):
        pass


    # Enter a parse tree produced by CWScriptParser#letLHS.
    def enterLetLHS(self, ctx:CWScriptParser.LetLHSContext):
        pass

    # Exit a parse tree produced by CWScriptParser#letLHS.
    def exitLetLHS(self, ctx:CWScriptParser.LetLHSContext):
        pass


    # Enter a parse tree produced by CWScriptParser#AndExpr.
    def enterAndExpr(self, ctx:CWScriptParser.AndExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#AndExpr.
    def exitAndExpr(self, ctx:CWScriptParser.AndExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#MultDivModExpr.
    def enterMultDivModExpr(self, ctx:CWScriptParser.MultDivModExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#MultDivModExpr.
    def exitMultDivModExpr(self, ctx:CWScriptParser.MultDivModExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#QueryExpr.
    def enterQueryExpr(self, ctx:CWScriptParser.QueryExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#QueryExpr.
    def exitQueryExpr(self, ctx:CWScriptParser.QueryExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ValExpr.
    def enterValExpr(self, ctx:CWScriptParser.ValExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ValExpr.
    def exitValExpr(self, ctx:CWScriptParser.ValExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#UnaryNotExpr.
    def enterUnaryNotExpr(self, ctx:CWScriptParser.UnaryNotExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#UnaryNotExpr.
    def exitUnaryNotExpr(self, ctx:CWScriptParser.UnaryNotExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#CompExpr.
    def enterCompExpr(self, ctx:CWScriptParser.CompExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#CompExpr.
    def exitCompExpr(self, ctx:CWScriptParser.CompExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#UnarySignExpr.
    def enterUnarySignExpr(self, ctx:CWScriptParser.UnarySignExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#UnarySignExpr.
    def exitUnarySignExpr(self, ctx:CWScriptParser.UnarySignExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ExpExpr.
    def enterExpExpr(self, ctx:CWScriptParser.ExpExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ExpExpr.
    def exitExpExpr(self, ctx:CWScriptParser.ExpExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#OrExpr.
    def enterOrExpr(self, ctx:CWScriptParser.OrExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#OrExpr.
    def exitOrExpr(self, ctx:CWScriptParser.OrExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IfExp.
    def enterIfExp(self, ctx:CWScriptParser.IfExpContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IfExp.
    def exitIfExp(self, ctx:CWScriptParser.IfExpContext):
        pass


    # Enter a parse tree produced by CWScriptParser#EqExpr.
    def enterEqExpr(self, ctx:CWScriptParser.EqExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#EqExpr.
    def exitEqExpr(self, ctx:CWScriptParser.EqExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TableLookupExpr.
    def enterTableLookupExpr(self, ctx:CWScriptParser.TableLookupExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TableLookupExpr.
    def exitTableLookupExpr(self, ctx:CWScriptParser.TableLookupExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#MemberAccessExpr.
    def enterMemberAccessExpr(self, ctx:CWScriptParser.MemberAccessExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#MemberAccessExpr.
    def exitMemberAccessExpr(self, ctx:CWScriptParser.MemberAccessExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:CWScriptParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:CWScriptParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#FnCallExpr.
    def enterFnCallExpr(self, ctx:CWScriptParser.FnCallExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#FnCallExpr.
    def exitFnCallExpr(self, ctx:CWScriptParser.FnCallExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#GroupedExpr.
    def enterGroupedExpr(self, ctx:CWScriptParser.GroupedExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#GroupedExpr.
    def exitGroupedExpr(self, ctx:CWScriptParser.GroupedExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#UnitVal.
    def enterUnitVal(self, ctx:CWScriptParser.UnitValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#UnitVal.
    def exitUnitVal(self, ctx:CWScriptParser.UnitValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#StructVal.
    def enterStructVal(self, ctx:CWScriptParser.StructValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#StructVal.
    def exitStructVal(self, ctx:CWScriptParser.StructValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TupleStructVal.
    def enterTupleStructVal(self, ctx:CWScriptParser.TupleStructValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TupleStructVal.
    def exitTupleStructVal(self, ctx:CWScriptParser.TupleStructValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#VecVal.
    def enterVecVal(self, ctx:CWScriptParser.VecValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#VecVal.
    def exitVecVal(self, ctx:CWScriptParser.VecValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#StringVal.
    def enterStringVal(self, ctx:CWScriptParser.StringValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#StringVal.
    def exitStringVal(self, ctx:CWScriptParser.StringValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IntegerVal.
    def enterIntegerVal(self, ctx:CWScriptParser.IntegerValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IntegerVal.
    def exitIntegerVal(self, ctx:CWScriptParser.IntegerValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#DecimalVal.
    def enterDecimalVal(self, ctx:CWScriptParser.DecimalValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#DecimalVal.
    def exitDecimalVal(self, ctx:CWScriptParser.DecimalValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TrueVal.
    def enterTrueVal(self, ctx:CWScriptParser.TrueValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TrueVal.
    def exitTrueVal(self, ctx:CWScriptParser.TrueValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#FalseVal.
    def enterFalseVal(self, ctx:CWScriptParser.FalseValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#FalseVal.
    def exitFalseVal(self, ctx:CWScriptParser.FalseValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IdentVal.
    def enterIdentVal(self, ctx:CWScriptParser.IdentValContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IdentVal.
    def exitIdentVal(self, ctx:CWScriptParser.IdentValContext):
        pass


    # Enter a parse tree produced by CWScriptParser#structVal_.
    def enterStructVal_(self, ctx:CWScriptParser.StructVal_Context):
        pass

    # Exit a parse tree produced by CWScriptParser#structVal_.
    def exitStructVal_(self, ctx:CWScriptParser.StructVal_Context):
        pass


    # Enter a parse tree produced by CWScriptParser#structValMembers.
    def enterStructValMembers(self, ctx:CWScriptParser.StructValMembersContext):
        pass

    # Exit a parse tree produced by CWScriptParser#structValMembers.
    def exitStructValMembers(self, ctx:CWScriptParser.StructValMembersContext):
        pass


    # Enter a parse tree produced by CWScriptParser#structValMember.
    def enterStructValMember(self, ctx:CWScriptParser.StructValMemberContext):
        pass

    # Exit a parse tree produced by CWScriptParser#structValMember.
    def exitStructValMember(self, ctx:CWScriptParser.StructValMemberContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ifExpr_.
    def enterIfExpr_(self, ctx:CWScriptParser.IfExpr_Context):
        pass

    # Exit a parse tree produced by CWScriptParser#ifExpr_.
    def exitIfExpr_(self, ctx:CWScriptParser.IfExpr_Context):
        pass


    # Enter a parse tree produced by CWScriptParser#IfClause.
    def enterIfClause(self, ctx:CWScriptParser.IfClauseContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IfClause.
    def exitIfClause(self, ctx:CWScriptParser.IfClauseContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IfLetClause.
    def enterIfLetClause(self, ctx:CWScriptParser.IfLetClauseContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IfLetClause.
    def exitIfLetClause(self, ctx:CWScriptParser.IfLetClauseContext):
        pass


    # Enter a parse tree produced by CWScriptParser#elseIfClauses.
    def enterElseIfClauses(self, ctx:CWScriptParser.ElseIfClausesContext):
        pass

    # Exit a parse tree produced by CWScriptParser#elseIfClauses.
    def exitElseIfClauses(self, ctx:CWScriptParser.ElseIfClausesContext):
        pass


    # Enter a parse tree produced by CWScriptParser#elseClause.
    def enterElseClause(self, ctx:CWScriptParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by CWScriptParser#elseClause.
    def exitElseClause(self, ctx:CWScriptParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ForInStmt.
    def enterForInStmt(self, ctx:CWScriptParser.ForInStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ForInStmt.
    def exitForInStmt(self, ctx:CWScriptParser.ForInStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ForTimesStmt.
    def enterForTimesStmt(self, ctx:CWScriptParser.ForTimesStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ForTimesStmt.
    def exitForTimesStmt(self, ctx:CWScriptParser.ForTimesStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#forItem.
    def enterForItem(self, ctx:CWScriptParser.ForItemContext):
        pass

    # Exit a parse tree produced by CWScriptParser#forItem.
    def exitForItem(self, ctx:CWScriptParser.ForItemContext):
        pass


    # Enter a parse tree produced by CWScriptParser#identList.
    def enterIdentList(self, ctx:CWScriptParser.IdentListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#identList.
    def exitIdentList(self, ctx:CWScriptParser.IdentListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#exprList.
    def enterExprList(self, ctx:CWScriptParser.ExprListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#exprList.
    def exitExprList(self, ctx:CWScriptParser.ExprListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#namedExprList.
    def enterNamedExprList(self, ctx:CWScriptParser.NamedExprListContext):
        pass

    # Exit a parse tree produced by CWScriptParser#namedExprList.
    def exitNamedExprList(self, ctx:CWScriptParser.NamedExprListContext):
        pass


    # Enter a parse tree produced by CWScriptParser#namedExpr.
    def enterNamedExpr(self, ctx:CWScriptParser.NamedExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#namedExpr.
    def exitNamedExpr(self, ctx:CWScriptParser.NamedExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ident.
    def enterIdent(self, ctx:CWScriptParser.IdentContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ident.
    def exitIdent(self, ctx:CWScriptParser.IdentContext):
        pass


    # Enter a parse tree produced by CWScriptParser#cwspec.
    def enterCwspec(self, ctx:CWScriptParser.CwspecContext):
        pass

    # Exit a parse tree produced by CWScriptParser#cwspec.
    def exitCwspec(self, ctx:CWScriptParser.CwspecContext):
        pass


    # Enter a parse tree produced by CWScriptParser#reservedKeyword.
    def enterReservedKeyword(self, ctx:CWScriptParser.ReservedKeywordContext):
        pass

    # Exit a parse tree produced by CWScriptParser#reservedKeyword.
    def exitReservedKeyword(self, ctx:CWScriptParser.ReservedKeywordContext):
        pass


