# Generated from ./grammar/CWScriptParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3U")
        buf.write("\u03a9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\3\2\7\2\u00ae\n\2\f\2\16\2\u00b1\13\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u00b9\n\3\3\4\3\4\3\4\3\4\5\4\u00bf\n\4")
        buf.write("\3\4\3\4\5\4\u00c3\n\4\3\4\3\4\3\5\3\5\3\5\7\5\u00ca\n")
        buf.write("\5\f\5\16\5\u00cd\13\5\3\6\3\6\3\6\3\6\3\6\5\6\u00d4\n")
        buf.write("\6\3\7\3\7\3\7\3\7\5\7\u00da\n\7\3\7\3\7\5\7\u00de\n\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00e8\n\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00f3\n\t\3\n\3\n\7\n")
        buf.write("\u00f7\n\n\f\n\16\n\u00fa\13\n\3\n\3\n\3\13\3\13\7\13")
        buf.write("\u0100\n\13\f\13\16\13\u0103\13\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0115")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u011d\n\r\3\16\5\16\u0120")
        buf.write("\n\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u0128\n\17\3")
        buf.write("\17\3\17\3\20\5\20\u012d\n\20\3\20\6\20\u0130\n\20\r\20")
        buf.write("\16\20\u0131\3\21\5\21\u0135\n\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\5\22\u013d\n\22\3\22\3\22\3\23\5\23\u0142\n")
        buf.write("\23\3\23\6\23\u0145\n\23\r\23\16\23\u0146\3\24\5\24\u014a")
        buf.write("\n\24\3\24\3\24\3\24\5\24\u014f\n\24\3\25\3\25\3\25\5")
        buf.write("\25\u0154\n\25\3\25\3\25\3\26\5\26\u0159\n\26\3\26\3\26")
        buf.write("\5\26\u015d\n\26\6\26\u015f\n\26\r\26\16\26\u0160\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\6\31\u016d")
        buf.write("\n\31\r\31\16\31\u016e\3\32\3\32\3\32\3\32\5\32\u0175")
        buf.write("\n\32\3\32\3\32\3\32\3\33\5\33\u017b\n\33\3\33\3\33\3")
        buf.write("\33\5\33\u0180\n\33\3\33\3\33\3\34\5\34\u0185\n\34\3\34")
        buf.write("\3\34\3\34\5\34\u018a\n\34\3\35\5\35\u018d\n\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0194\n\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\7\36\u019b\n\36\f\36\16\36\u019e\13\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u01a6\n\37\3 \5 \u01a9\n \3")
        buf.write(" \3 \3 \3!\3!\3!\5!\u01b1\n!\3!\3!\3\"\5\"\u01b6\n\"\3")
        buf.write("\"\6\"\u01b9\n\"\r\"\16\"\u01ba\3#\5#\u01be\n#\3#\3#\3")
        buf.write("#\3$\3$\3$\5$\u01c6\n$\3$\3$\3%\5%\u01cb\n%\3%\6%\u01ce")
        buf.write("\n%\r%\16%\u01cf\3&\5&\u01d3\n&\3&\3&\3&\3\'\3\'\3\'\5")
        buf.write("\'\u01db\n\'\3\'\3\'\3(\5(\u01e0\n(\3(\3(\3(\3)\3)\3)")
        buf.write("\5)\u01e8\n)\3)\3)\3*\3*\3*\5*\u01ef\n*\3+\3+\5+\u01f3")
        buf.write("\n+\3+\3+\5+\u01f7\n+\3,\3,\3,\3-\3-\3.\3.\3.\3.\7.\u0202")
        buf.write("\n.\f.\16.\u0205\13.\3.\3.\3/\3/\3/\3/\7/\u020d\n/\f/")
        buf.write("\16/\u0210\13/\5/\u0212\n/\3/\3/\3\60\3\60\3\60\3\60\7")
        buf.write("\60\u021a\n\60\f\60\16\60\u021d\13\60\3\60\5\60\u0220")
        buf.write("\n\60\5\60\u0222\n\60\3\60\3\60\3\61\5\61\u0227\n\61\3")
        buf.write("\61\3\61\5\61\u022b\n\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\7\62\u0236\n\62\f\62\16\62\u0239\13\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0243\n")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\7\62\u024f\n\62\f\62\16\62\u0252\13\62\3\63\5\63\u0255")
        buf.write("\n\63\3\63\3\63\3\63\7\63\u025a\n\63\f\63\16\63\u025d")
        buf.write("\13\63\3\64\3\64\3\64\7\64\u0262\n\64\f\64\16\64\u0265")
        buf.write("\13\64\3\65\3\65\3\65\3\65\5\65\u026b\n\65\3\66\3\66\3")
        buf.write("\66\3\67\3\67\3\67\38\38\38\38\38\58\u0278\n8\38\78\u027b")
        buf.write("\n8\f8\168\u027e\138\38\58\u0281\n8\58\u0283\n8\38\38")
        buf.write("\39\39\39\39\39\3:\3:\3:\5:\u028f\n:\3;\3;\3;\5;\u0294")
        buf.write("\n;\3;\3;\3<\3<\3<\3=\3=\5=\u029d\n=\3=\3=\3>\3>\3>\7")
        buf.write(">\u02a4\n>\f>\16>\u02a7\13>\3?\3?\5?\u02ab\n?\3?\3?\3")
        buf.write("?\5?\u02b0\n?\3@\3@\3@\3@\3@\3@\5@\u02b8\n@\3@\3@\5@\u02bc")
        buf.write("\n@\6@\u02be\n@\r@\16@\u02bf\3A\3A\7A\u02c4\nA\fA\16A")
        buf.write("\u02c7\13A\3A\3A\3A\5A\u02cc\nA\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\5B\u02de\nB\3C\3C\3C\3C\3C\3")
        buf.write("D\3D\3D\5D\u02e8\nD\3D\3D\3D\3D\5D\u02ee\nD\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u02fd\nE\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u0320\nE\3E\7E\u0323")
        buf.write("\nE\fE\16E\u0326\13E\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F")
        buf.write("\3F\3F\3F\3F\3F\3F\5F\u0339\nF\3G\3G\5G\u033d\nG\3G\3")
        buf.write("G\5G\u0341\nG\3G\3G\3H\3H\3H\7H\u0348\nH\fH\16H\u034b")
        buf.write("\13H\3H\5H\u034e\nH\3I\3I\3I\3I\3J\3J\5J\u0356\nJ\3J\5")
        buf.write("J\u0359\nJ\3K\3K\3K\3K\3K\3K\3K\3K\5K\u0363\nK\3L\3L\6")
        buf.write("L\u0367\nL\rL\16L\u0368\3M\3M\3M\3N\3N\3N\3N\3N\3N\3N")
        buf.write("\3N\3N\3N\3N\5N\u0379\nN\3O\3O\3O\3O\3O\5O\u0380\nO\3")
        buf.write("P\3P\3P\7P\u0385\nP\fP\16P\u0388\13P\3Q\3Q\3Q\7Q\u038d")
        buf.write("\nQ\fQ\16Q\u0390\13Q\3R\3R\3R\7R\u0395\nR\fR\16R\u0398")
        buf.write("\13R\3S\3S\3S\3S\3T\3T\5T\u03a0\nT\3U\6U\u03a3\nU\rU\16")
        buf.write("U\u03a4\3V\3V\3V\2\4b\u0088W\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write("\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\2\t\b\2;;?")
        buf.write("?AACCEEGG\4\2>>@@\5\2BBDDFF\3\2HK\3\2<=\3\2QR\6\2\3\b")
        buf.write("\n\21\24\36 $\2\u03f6\2\u00af\3\2\2\2\4\u00b8\3\2\2\2")
        buf.write("\6\u00ba\3\2\2\2\b\u00c6\3\2\2\2\n\u00ce\3\2\2\2\f\u00d5")
        buf.write("\3\2\2\2\16\u00e1\3\2\2\2\20\u00f2\3\2\2\2\22\u00f4\3")
        buf.write("\2\2\2\24\u00fd\3\2\2\2\26\u0114\3\2\2\2\30\u011c\3\2")
        buf.write("\2\2\32\u011f\3\2\2\2\34\u0124\3\2\2\2\36\u012f\3\2\2")
        buf.write("\2 \u0134\3\2\2\2\"\u0139\3\2\2\2$\u0144\3\2\2\2&\u0149")
        buf.write("\3\2\2\2(\u0150\3\2\2\2*\u015e\3\2\2\2,\u0162\3\2\2\2")
        buf.write(".\u0166\3\2\2\2\60\u016c\3\2\2\2\62\u0170\3\2\2\2\64\u017a")
        buf.write("\3\2\2\2\66\u0184\3\2\2\28\u018c\3\2\2\2:\u0195\3\2\2")
        buf.write("\2<\u01a5\3\2\2\2>\u01a8\3\2\2\2@\u01ad\3\2\2\2B\u01b8")
        buf.write("\3\2\2\2D\u01bd\3\2\2\2F\u01c2\3\2\2\2H\u01cd\3\2\2\2")
        buf.write("J\u01d2\3\2\2\2L\u01d7\3\2\2\2N\u01df\3\2\2\2P\u01e4\3")
        buf.write("\2\2\2R\u01ee\3\2\2\2T\u01f2\3\2\2\2V\u01f8\3\2\2\2X\u01fb")
        buf.write("\3\2\2\2Z\u01fd\3\2\2\2\\\u0208\3\2\2\2^\u0215\3\2\2\2")
        buf.write("`\u0226\3\2\2\2b\u0242\3\2\2\2d\u0254\3\2\2\2f\u025e\3")
        buf.write("\2\2\2h\u026a\3\2\2\2j\u026c\3\2\2\2l\u026f\3\2\2\2n\u0272")
        buf.write("\3\2\2\2p\u0286\3\2\2\2r\u028b\3\2\2\2t\u0290\3\2\2\2")
        buf.write("v\u0297\3\2\2\2x\u029a\3\2\2\2z\u02a0\3\2\2\2|\u02a8\3")
        buf.write("\2\2\2~\u02bd\3\2\2\2\u0080\u02cb\3\2\2\2\u0082\u02dd")
        buf.write("\3\2\2\2\u0084\u02df\3\2\2\2\u0086\u02ed\3\2\2\2\u0088")
        buf.write("\u02fc\3\2\2\2\u008a\u0338\3\2\2\2\u008c\u033c\3\2\2\2")
        buf.write("\u008e\u0344\3\2\2\2\u0090\u034f\3\2\2\2\u0092\u0353\3")
        buf.write("\2\2\2\u0094\u0362\3\2\2\2\u0096\u0366\3\2\2\2\u0098\u036a")
        buf.write("\3\2\2\2\u009a\u0378\3\2\2\2\u009c\u037f\3\2\2\2\u009e")
        buf.write("\u0381\3\2\2\2\u00a0\u0389\3\2\2\2\u00a2\u0391\3\2\2\2")
        buf.write("\u00a4\u0399\3\2\2\2\u00a6\u039f\3\2\2\2\u00a8\u03a2\3")
        buf.write("\2\2\2\u00aa\u03a6\3\2\2\2\u00ac\u00ae\5\4\3\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00b3\7\2\2\3\u00b3\3\3\2\2\2\u00b4\u00b9\5\6\4")
        buf.write("\2\u00b5\u00b9\5\f\7\2\u00b6\u00b9\5\16\b\2\u00b7\u00b9")
        buf.write("\5\20\t\2\u00b8\u00b4\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\5\3\2\2\2\u00ba")
        buf.write("\u00bb\7\3\2\2\u00bb\u00be\5\u00a6T\2\u00bc\u00bd\7\n")
        buf.write("\2\2\u00bd\u00bf\5\u00a6T\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00c1\7\6\2\2")
        buf.write("\u00c1\u00c3\5\b\5\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3")
        buf.write("\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\5\22\n\2\u00c5")
        buf.write("\7\3\2\2\2\u00c6\u00cb\5\n\6\2\u00c7\u00c8\7,\2\2\u00c8")
        buf.write("\u00ca\5\n\6\2\u00c9\u00c7\3\2\2\2\u00ca\u00cd\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\t\3\2\2")
        buf.write("\2\u00cd\u00cb\3\2\2\2\u00ce\u00d3\5\u00a6T\2\u00cf\u00d0")
        buf.write("\7%\2\2\u00d0\u00d1\5\u009eP\2\u00d1\u00d2\7&\2\2\u00d2")
        buf.write("\u00d4\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\13\3\2\2\2\u00d5\u00d6\7\4\2\2\u00d6\u00d9\5\u00a6")
        buf.write("T\2\u00d7\u00d8\7\n\2\2\u00d8\u00da\5\u00a6T\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dd\3\2\2\2\u00db")
        buf.write("\u00dc\7\6\2\2\u00dc\u00de\5\b\5\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\5")
        buf.write("\24\13\2\u00e0\r\3\2\2\2\u00e1\u00e2\7\b\2\2\u00e2\u00e3")
        buf.write("\5\u00a6T\2\u00e3\u00e4\7\21\2\2\u00e4\u00e7\5\u00a6T")
        buf.write("\2\u00e5\u00e6\7\t\2\2\u00e6\u00e8\5\b\5\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00ea\5\24\13\2\u00ea\17\3\2\2\2\u00eb\u00ec\7\5\2\2")
        buf.write("\u00ec\u00f3\7N\2\2\u00ed\u00ee\7\5\2\2\u00ee\u00ef\5")
        buf.write("\u009eP\2\u00ef\u00f0\7\25\2\2\u00f0\u00f1\7N\2\2\u00f1")
        buf.write("\u00f3\3\2\2\2\u00f2\u00eb\3\2\2\2\u00f2\u00ed\3\2\2\2")
        buf.write("\u00f3\21\3\2\2\2\u00f4\u00f8\7)\2\2\u00f5\u00f7\5\26")
        buf.write("\f\2\u00f6\u00f5\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fb\u00fc\7*\2\2\u00fc\23\3\2\2\2\u00fd")
        buf.write("\u0101\7)\2\2\u00fe\u0100\5\30\r\2\u00ff\u00fe\3\2\2\2")
        buf.write("\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3")
        buf.write("\2\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105")
        buf.write("\7*\2\2\u0105\25\3\2\2\2\u0106\u0115\5h\65\2\u0107\u0115")
        buf.write("\5\32\16\2\u0108\u0115\5\34\17\2\u0109\u0115\5 \21\2\u010a")
        buf.write("\u0115\5\"\22\2\u010b\u0115\5&\24\2\u010c\u0115\5(\25")
        buf.write("\2\u010d\u0115\5\64\33\2\u010e\u0115\5> \2\u010f\u0115")
        buf.write("\5@!\2\u0110\u0115\5J&\2\u0111\u0115\5L\'\2\u0112\u0115")
        buf.write("\58\35\2\u0113\u0115\5:\36\2\u0114\u0106\3\2\2\2\u0114")
        buf.write("\u0107\3\2\2\2\u0114\u0108\3\2\2\2\u0114\u0109\3\2\2\2")
        buf.write("\u0114\u010a\3\2\2\2\u0114\u010b\3\2\2\2\u0114\u010c\3")
        buf.write("\2\2\2\u0114\u010d\3\2\2\2\u0114\u010e\3\2\2\2\u0114\u010f")
        buf.write("\3\2\2\2\u0114\u0110\3\2\2\2\u0114\u0111\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115\27\3\2\2\2\u0116")
        buf.write("\u011d\5h\65\2\u0117\u011d\5\66\34\2\u0118\u011d\5D#\2")
        buf.write("\u0119\u011d\5F$\2\u011a\u011d\5N(\2\u011b\u011d\5P)\2")
        buf.write("\u011c\u0116\3\2\2\2\u011c\u0117\3\2\2\2\u011c\u0118\3")
        buf.write("\2\2\2\u011c\u0119\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011b")
        buf.write("\3\2\2\2\u011d\31\3\2\2\2\u011e\u0120\5\u00a8U\2\u011f")
        buf.write("\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u0122\7\13\2\2\u0122\u0123\5R*\2\u0123\33\3\2\2")
        buf.write("\2\u0124\u0125\7\13\2\2\u0125\u0127\7)\2\2\u0126\u0128")
        buf.write("\5\36\20\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012a\7*\2\2\u012a\35\3\2\2\2\u012b")
        buf.write("\u012d\5\u00a8U\2\u012c\u012b\3\2\2\2\u012c\u012d\3\2")
        buf.write("\2\2\u012d\u012e\3\2\2\2\u012e\u0130\5R*\2\u012f\u012c")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\37\3\2\2\2\u0133\u0135\5\u00a8U\2")
        buf.write("\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u0137\7\f\2\2\u0137\u0138\5R*\2\u0138!\3")
        buf.write("\2\2\2\u0139\u013a\7\f\2\2\u013a\u013c\7)\2\2\u013b\u013d")
        buf.write("\5$\23\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u013f\7*\2\2\u013f#\3\2\2\2\u0140")
        buf.write("\u0142\5\u00a8U\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2")
        buf.write("\2\2\u0142\u0143\3\2\2\2\u0143\u0145\5R*\2\u0144\u0141")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147%\3\2\2\2\u0148\u014a\5\u00a8U\2\u0149")
        buf.write("\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b\u014e\7\26\2\2\u014c\u014f\5,\27\2\u014d\u014f")
        buf.write("\5.\30\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\'\3\2\2\2\u0150\u0151\7\26\2\2\u0151\u0153\7)\2\2\u0152")
        buf.write("\u0154\5*\26\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155\u0156\7*\2\2\u0156)\3\2\2\2")
        buf.write("\u0157\u0159\5\u00a8U\2\u0158\u0157\3\2\2\2\u0158\u0159")
        buf.write("\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u015d\5,\27\2\u015b")
        buf.write("\u015d\5.\30\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2")
        buf.write("\u015d\u015f\3\2\2\2\u015e\u0158\3\2\2\2\u015f\u0160\3")
        buf.write("\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161+")
        buf.write("\3\2\2\2\u0162\u0163\5\u00a6T\2\u0163\u0164\7/\2\2\u0164")
        buf.write("\u0165\5b\62\2\u0165-\3\2\2\2\u0166\u0167\5\u00a6T\2\u0167")
        buf.write("\u0168\5\60\31\2\u0168\u0169\7/\2\2\u0169\u016a\5b\62")
        buf.write("\2\u016a/\3\2\2\2\u016b\u016d\5\62\32\2\u016c\u016b\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f")
        buf.write("\3\2\2\2\u016f\61\3\2\2\2\u0170\u0174\7\'\2\2\u0171\u0172")
        buf.write("\5\u00a6T\2\u0172\u0173\7/\2\2\u0173\u0175\3\2\2\2\u0174")
        buf.write("\u0171\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\5b\62\2\u0177\u0178\7(\2\2\u0178\63\3\2\2")
        buf.write("\2\u0179\u017b\5\u00a8U\2\u017a\u0179\3\2\2\2\u017a\u017b")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\7\r\2\2\u017d")
        buf.write("\u017f\5x=\2\u017e\u0180\5v<\2\u017f\u017e\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\5\u0080")
        buf.write("A\2\u0182\65\3\2\2\2\u0183\u0185\5\u00a8U\2\u0184\u0183")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0187\7\r\2\2\u0187\u0189\5x=\2\u0188\u018a\5v<\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\67\3\2\2\2\u018b")
        buf.write("\u018d\5\u00a8U\2\u018c\u018b\3\2\2\2\u018c\u018d\3\2")
        buf.write("\2\2\u018d\u018e\3\2\2\2\u018e\u018f\7\7\2\2\u018f\u0190")
        buf.write("\5\b\5\2\u0190\u0193\3\2\2\2\u0191\u0194\5> \2\u0192\u0194")
        buf.write("\5J&\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u01949")
        buf.write("\3\2\2\2\u0195\u0196\7\7\2\2\u0196\u0197\5\b\5\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u019c\7)\2\2\u0199\u019b\5<\37\2")
        buf.write("\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019f\u01a0\7*\2\2\u01a0;\3\2\2\2\u01a1\u01a6")
        buf.write("\5> \2\u01a2\u01a6\5@!\2\u01a3\u01a6\5J&\2\u01a4\u01a6")
        buf.write("\5L\'\2\u01a5\u01a1\3\2\2\2\u01a5\u01a2\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6=\3\2\2\2\u01a7")
        buf.write("\u01a9\5\u00a8U\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2")
        buf.write("\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\7\16\2\2\u01ab\u01ac")
        buf.write("\5t;\2\u01ac?\3\2\2\2\u01ad\u01ae\7\16\2\2\u01ae\u01b0")
        buf.write("\7)\2\2\u01af\u01b1\5B\"\2\u01b0\u01af\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\7*\2\2\u01b3")
        buf.write("A\3\2\2\2\u01b4\u01b6\5\u00a8U\2\u01b5\u01b4\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b9\5t;\2\u01b8")
        buf.write("\u01b5\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01ba\u01bb\3\2\2\2\u01bbC\3\2\2\2\u01bc\u01be\5\u00a8")
        buf.write("U\2\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u01c0\7\16\2\2\u01c0\u01c1\5r:\2\u01c1")
        buf.write("E\3\2\2\2\u01c2\u01c3\7\16\2\2\u01c3\u01c5\7)\2\2\u01c4")
        buf.write("\u01c6\5H%\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c8\7*\2\2\u01c8G\3\2\2\2\u01c9")
        buf.write("\u01cb\5\u00a8U\2\u01ca\u01c9\3\2\2\2\u01ca\u01cb\3\2")
        buf.write("\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\5r:\2\u01cd\u01ca")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0I\3\2\2\2\u01d1\u01d3\5\u00a8U\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\3\2\2\2")
        buf.write("\u01d4\u01d5\7\17\2\2\u01d5\u01d6\5t;\2\u01d6K\3\2\2\2")
        buf.write("\u01d7\u01d8\7\17\2\2\u01d8\u01da\7)\2\2\u01d9\u01db\5")
        buf.write("B\"\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc")
        buf.write("\3\2\2\2\u01dc\u01dd\7*\2\2\u01ddM\3\2\2\2\u01de\u01e0")
        buf.write("\5\u00a8U\2\u01df\u01de\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01e2\7\17\2\2\u01e2\u01e3\5r:\2")
        buf.write("\u01e3O\3\2\2\2\u01e4\u01e5\7\17\2\2\u01e5\u01e7\7)\2")
        buf.write("\2\u01e6\u01e8\5H%\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8\3")
        buf.write("\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\7*\2\2\u01eaQ\3")
        buf.write("\2\2\2\u01eb\u01ef\5T+\2\u01ec\u01ef\5V,\2\u01ed\u01ef")
        buf.write("\5X-\2\u01ee\u01eb\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed")
        buf.write("\3\2\2\2\u01efS\3\2\2\2\u01f0\u01f3\5\u00a6T\2\u01f1\u01f3")
        buf.write("\7\62\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f6\3\2\2\2\u01f4\u01f7\5\\/\2\u01f5\u01f7\5^\60\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7U\3\2\2")
        buf.write("\2\u01f8\u01f9\5\u00a6T\2\u01f9\u01fa\5Z.\2\u01faW\3\2")
        buf.write("\2\2\u01fb\u01fc\5\u00a6T\2\u01fcY\3\2\2\2\u01fd\u01fe")
        buf.write("\7%\2\2\u01fe\u0203\5b\62\2\u01ff\u0200\7,\2\2\u0200\u0202")
        buf.write("\5b\62\2\u0201\u01ff\3\2\2\2\u0202\u0205\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2")
        buf.write("\u0205\u0203\3\2\2\2\u0206\u0207\7&\2\2\u0207[\3\2\2\2")
        buf.write("\u0208\u0211\7%\2\2\u0209\u020e\5`\61\2\u020a\u020b\7")
        buf.write(",\2\2\u020b\u020d\5`\61\2\u020c\u020a\3\2\2\2\u020d\u0210")
        buf.write("\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f")
        buf.write("\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0209\3\2\2\2")
        buf.write("\u0211\u0212\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0214\7")
        buf.write("&\2\2\u0214]\3\2\2\2\u0215\u0221\7)\2\2\u0216\u021b\5")
        buf.write("`\61\2\u0217\u0218\7,\2\2\u0218\u021a\5`\61\2\u0219\u0217")
        buf.write("\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b")
        buf.write("\u021c\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2")
        buf.write("\u021e\u0220\7,\2\2\u021f\u021e\3\2\2\2\u021f\u0220\3")
        buf.write("\2\2\2\u0220\u0222\3\2\2\2\u0221\u0216\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224\7*\2\2\u0224")
        buf.write("_\3\2\2\2\u0225\u0227\5\u00a8U\2\u0226\u0225\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u022a\5\u00a6")
        buf.write("T\2\u0229\u022b\7-\2\2\u022a\u0229\3\2\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022d\7/\2\2\u022d")
        buf.write("\u022e\5b\62\2\u022ea\3\2\2\2\u022f\u0230\b\62\1\2\u0230")
        buf.write("\u0243\5d\63\2\u0231\u0232\7%\2\2\u0232\u0237\5b\62\2")
        buf.write("\u0233\u0234\7,\2\2\u0234\u0236\5b\62\2\u0235\u0233\3")
        buf.write("\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238")
        buf.write("\3\2\2\2\u0238\u023a\3\2\2\2\u0239\u0237\3\2\2\2\u023a")
        buf.write("\u023b\7&\2\2\u023b\u0243\3\2\2\2\u023c\u023d\7\65\2\2")
        buf.write("\u023d\u0243\5b\62\6\u023e\u023f\7\63\2\2\u023f\u0243")
        buf.write("\5f\64\2\u0240\u0243\5h\65\2\u0241\u0243\7:\2\2\u0242")
        buf.write("\u022f\3\2\2\2\u0242\u0231\3\2\2\2\u0242\u023c\3\2\2\2")
        buf.write("\u0242\u023e\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0241\3")
        buf.write("\2\2\2\u0243\u0250\3\2\2\2\u0244\u0245\f\n\2\2\u0245\u0246")
        buf.write("\7H\2\2\u0246\u0247\5b\62\2\u0247\u0248\7J\2\2\u0248\u024f")
        buf.write("\3\2\2\2\u0249\u024a\f\b\2\2\u024a\u024f\7-\2\2\u024b")
        buf.write("\u024c\f\7\2\2\u024c\u024d\7\'\2\2\u024d\u024f\7(\2\2")
        buf.write("\u024e\u0244\3\2\2\2\u024e\u0249\3\2\2\2\u024e\u024b\3")
        buf.write("\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251c\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0255")
        buf.write("\7\60\2\2\u0254\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255")
        buf.write("\u0256\3\2\2\2\u0256\u025b\5\u00a6T\2\u0257\u0258\7\60")
        buf.write("\2\2\u0258\u025a\5\u00a6T\2\u0259\u0257\3\2\2\2\u025a")
        buf.write("\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2")
        buf.write("\u025ce\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u0263\5\n\6")
        buf.write("\2\u025f\u0260\7+\2\2\u0260\u0262\5\u00a6T\2\u0261\u025f")
        buf.write("\3\2\2\2\u0262\u0265\3\2\2\2\u0263\u0261\3\2\2\2\u0263")
        buf.write("\u0264\3\2\2\2\u0264g\3\2\2\2\u0265\u0263\3\2\2\2\u0266")
        buf.write("\u026b\5j\66\2\u0267\u026b\5l\67\2\u0268\u026b\5n8\2\u0269")
        buf.write("\u026b\5p9\2\u026a\u0266\3\2\2\2\u026a\u0267\3\2\2\2\u026a")
        buf.write("\u0268\3\2\2\2\u026a\u0269\3\2\2\2\u026bi\3\2\2\2\u026c")
        buf.write("\u026d\7\62\2\2\u026d\u026e\5^\60\2\u026ek\3\2\2\2\u026f")
        buf.write("\u0270\7!\2\2\u0270\u0271\5R*\2\u0271m\3\2\2\2\u0272\u0273")
        buf.write("\7\"\2\2\u0273\u0274\5\u00a6T\2\u0274\u0282\7)\2\2\u0275")
        buf.write("\u027c\5R*\2\u0276\u0278\7,\2\2\u0277\u0276\3\2\2\2\u0277")
        buf.write("\u0278\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027b\5R*\2\u027a")
        buf.write("\u0277\3\2\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2")
        buf.write("\u027c\u027d\3\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c\3")
        buf.write("\2\2\2\u027f\u0281\7,\2\2\u0280\u027f\3\2\2\2\u0280\u0281")
        buf.write("\3\2\2\2\u0281\u0283\3\2\2\2\u0282\u0275\3\2\2\2\u0282")
        buf.write("\u0283\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0285\7*\2\2")
        buf.write("\u0285o\3\2\2\2\u0286\u0287\7#\2\2\u0287\u0288\5\u00a6")
        buf.write("T\2\u0288\u0289\7;\2\2\u0289\u028a\5b\62\2\u028aq\3\2")
        buf.write("\2\2\u028b\u028c\5\u00a6T\2\u028c\u028e\5x=\2\u028d\u028f")
        buf.write("\5v<\2\u028e\u028d\3\2\2\2\u028e\u028f\3\2\2\2\u028fs")
        buf.write("\3\2\2\2\u0290\u0291\5\u00a6T\2\u0291\u0293\5x=\2\u0292")
        buf.write("\u0294\5v<\2\u0293\u0292\3\2\2\2\u0293\u0294\3\2\2\2\u0294")
        buf.write("\u0295\3\2\2\2\u0295\u0296\5\u0080A\2\u0296u\3\2\2\2\u0297")
        buf.write("\u0298\7\66\2\2\u0298\u0299\5b\62\2\u0299w\3\2\2\2\u029a")
        buf.write("\u029c\7%\2\2\u029b\u029d\5z>\2\u029c\u029b\3\2\2\2\u029c")
        buf.write("\u029d\3\2\2\2\u029d\u029e\3\2\2\2\u029e\u029f\7&\2\2")
        buf.write("\u029fy\3\2\2\2\u02a0\u02a5\5|?\2\u02a1\u02a2\7,\2\2\u02a2")
        buf.write("\u02a4\5|?\2\u02a3\u02a1\3\2\2\2\u02a4\u02a7\3\2\2\2\u02a5")
        buf.write("\u02a3\3\2\2\2\u02a5\u02a6\3\2\2\2\u02a6{\3\2\2\2\u02a7")
        buf.write("\u02a5\3\2\2\2\u02a8\u02aa\5\u00a6T\2\u02a9\u02ab\7-\2")
        buf.write("\2\u02aa\u02a9\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab\u02ac")
        buf.write("\3\2\2\2\u02ac\u02ad\7/\2\2\u02ad\u02af\5b\62\2\u02ae")
        buf.write("\u02b0\5~@\2\u02af\u02ae\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0")
        buf.write("}\3\2\2\2\u02b1\u02bb\7\61\2\2\u02b2\u02bc\5\u00a6T\2")
        buf.write("\u02b3\u02b4\5\u00a6T\2\u02b4\u02b7\7%\2\2\u02b5\u02b8")
        buf.write("\5\u00a0Q\2\u02b6\u02b8\5\u00a2R\2\u02b7\u02b5\3\2\2\2")
        buf.write("\u02b7\u02b6\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02ba\7")
        buf.write("&\2\2\u02ba\u02bc\3\2\2\2\u02bb\u02b2\3\2\2\2\u02bb\u02b3")
        buf.write("\3\2\2\2\u02bc\u02be\3\2\2\2\u02bd\u02b1\3\2\2\2\u02be")
        buf.write("\u02bf\3\2\2\2\u02bf\u02bd\3\2\2\2\u02bf\u02c0\3\2\2\2")
        buf.write("\u02c0\177\3\2\2\2\u02c1\u02c5\7)\2\2\u02c2\u02c4\5\u0082")
        buf.write("B\2\u02c3\u02c2\3\2\2\2\u02c4\u02c7\3\2\2\2\u02c5\u02c3")
        buf.write("\3\2\2\2\u02c5\u02c6\3\2\2\2\u02c6\u02c8\3\2\2\2\u02c7")
        buf.write("\u02c5\3\2\2\2\u02c8\u02cc\7*\2\2\u02c9\u02ca\7\67\2\2")
        buf.write("\u02ca\u02cc\5\u0082B\2\u02cb\u02c1\3\2\2\2\u02cb\u02c9")
        buf.write("\3\2\2\2\u02cc\u0081\3\2\2\2\u02cd\u02de\5\u0084C\2\u02ce")
        buf.write("\u02cf\5\u0088E\2\u02cf\u02d0\t\2\2\2\u02d0\u02d1\5\u0088")
        buf.write("E\2\u02d1\u02de\3\2\2\2\u02d2\u02de\5\u0092J\2\u02d3\u02de")
        buf.write("\5\u009aN\2\u02d4\u02d5\7\16\2\2\u02d5\u02de\5\u0088E")
        buf.write("\2\u02d6\u02d7\7$\2\2\u02d7\u02de\5\u0088E\2\u02d8\u02d9")
        buf.write("\7 \2\2\u02d9\u02de\5\u0088E\2\u02da\u02db\7\37\2\2\u02db")
        buf.write("\u02de\5\u0088E\2\u02dc\u02de\5\u0088E\2\u02dd\u02cd\3")
        buf.write("\2\2\2\u02dd\u02ce\3\2\2\2\u02dd\u02d2\3\2\2\2\u02dd\u02d3")
        buf.write("\3\2\2\2\u02dd\u02d4\3\2\2\2\u02dd\u02d6\3\2\2\2\u02dd")
        buf.write("\u02d8\3\2\2\2\u02dd\u02da\3\2\2\2\u02dd\u02dc\3\2\2\2")
        buf.write("\u02de\u0083\3\2\2\2\u02df\u02e0\7\36\2\2\u02e0\u02e1")
        buf.write("\5\u0086D\2\u02e1\u02e2\7;\2\2\u02e2\u02e3\5\u0088E\2")
        buf.write("\u02e3\u0085\3\2\2\2\u02e4\u02e7\5\u00a6T\2\u02e5\u02e6")
        buf.write("\7/\2\2\u02e6\u02e8\5b\62\2\u02e7\u02e5\3\2\2\2\u02e7")
        buf.write("\u02e8\3\2\2\2\u02e8\u02ee\3\2\2\2\u02e9\u02ea\7)\2\2")
        buf.write("\u02ea\u02eb\5\u009eP\2\u02eb\u02ec\7*\2\2\u02ec\u02ee")
        buf.write("\3\2\2\2\u02ed\u02e4\3\2\2\2\u02ed\u02e9\3\2\2\2\u02ee")
        buf.write("\u0087\3\2\2\2\u02ef\u02f0\bE\1\2\u02f0\u02f1\7%\2\2\u02f1")
        buf.write("\u02f2\5\u0088E\2\u02f2\u02f3\7&\2\2\u02f3\u02fd\3\2\2")
        buf.write("\2\u02f4\u02f5\t\3\2\2\u02f5\u02fd\5\u0088E\16\u02f6\u02f7")
        buf.write("\7.\2\2\u02f7\u02fd\5\u0088E\r\u02f8\u02fd\5\u0092J\2")
        buf.write("\u02f9\u02fa\7\17\2\2\u02fa\u02fd\5\u0088E\4\u02fb\u02fd")
        buf.write("\5\u008aF\2\u02fc\u02ef\3\2\2\2\u02fc\u02f4\3\2\2\2\u02fc")
        buf.write("\u02f6\3\2\2\2\u02fc\u02f8\3\2\2\2\u02fc\u02f9\3\2\2\2")
        buf.write("\u02fc\u02fb\3\2\2\2\u02fd\u0324\3\2\2\2\u02fe\u02ff\f")
        buf.write("\f\2\2\u02ff\u0300\7L\2\2\u0300\u0323\5\u0088E\r\u0301")
        buf.write("\u0302\f\13\2\2\u0302\u0303\t\4\2\2\u0303\u0323\5\u0088")
        buf.write("E\f\u0304\u0305\f\n\2\2\u0305\u0306\t\3\2\2\u0306\u0323")
        buf.write("\5\u0088E\13\u0307\u0308\f\t\2\2\u0308\u0309\t\5\2\2\u0309")
        buf.write("\u0323\5\u0088E\n\u030a\u030b\f\b\2\2\u030b\u030c\t\6")
        buf.write("\2\2\u030c\u0323\5\u0088E\t\u030d\u030e\f\7\2\2\u030e")
        buf.write("\u030f\7\32\2\2\u030f\u0323\5\u0088E\b\u0310\u0311\f\6")
        buf.write("\2\2\u0311\u0312\7\33\2\2\u0312\u0323\5\u0088E\7\u0313")
        buf.write("\u0314\f\21\2\2\u0314\u0315\7+\2\2\u0315\u0323\5\u00a6")
        buf.write("T\2\u0316\u0317\f\20\2\2\u0317\u0318\7\'\2\2\u0318\u0319")
        buf.write("\5\u0088E\2\u0319\u031a\7(\2\2\u031a\u0323\3\2\2\2\u031b")
        buf.write("\u031c\f\17\2\2\u031c\u031f\7%\2\2\u031d\u0320\5\u00a0")
        buf.write("Q\2\u031e\u0320\5\u00a2R\2\u031f\u031d\3\2\2\2\u031f\u031e")
        buf.write("\3\2\2\2\u031f\u0320\3\2\2\2\u0320\u0321\3\2\2\2\u0321")
        buf.write("\u0323\7&\2\2\u0322\u02fe\3\2\2\2\u0322\u0301\3\2\2\2")
        buf.write("\u0322\u0304\3\2\2\2\u0322\u0307\3\2\2\2\u0322\u030a\3")
        buf.write("\2\2\2\u0322\u030d\3\2\2\2\u0322\u0310\3\2\2\2\u0322\u0313")
        buf.write("\3\2\2\2\u0322\u0316\3\2\2\2\u0322\u031b\3\2\2\2\u0323")
        buf.write("\u0326\3\2\2\2\u0324\u0322\3\2\2\2\u0324\u0325\3\2\2\2")
        buf.write("\u0325\u0089\3\2\2\2\u0326\u0324\3\2\2\2\u0327\u0328\7")
        buf.write("%\2\2\u0328\u0339\7&\2\2\u0329\u0339\5\u008cG\2\u032a")
        buf.write("\u032b\7%\2\2\u032b\u032c\5\u00a0Q\2\u032c\u032d\7&\2")
        buf.write("\2\u032d\u0339\3\2\2\2\u032e\u032f\7\'\2\2\u032f\u0330")
        buf.write("\5\u00a0Q\2\u0330\u0331\7(\2\2\u0331\u0339\3\2\2\2\u0332")
        buf.write("\u0339\7N\2\2\u0333\u0339\7O\2\2\u0334\u0339\7P\2\2\u0335")
        buf.write("\u0339\7\34\2\2\u0336\u0339\7\35\2\2\u0337\u0339\5\u00a6")
        buf.write("T\2\u0338\u0327\3\2\2\2\u0338\u0329\3\2\2\2\u0338\u032a")
        buf.write("\3\2\2\2\u0338\u032e\3\2\2\2\u0338\u0332\3\2\2\2\u0338")
        buf.write("\u0333\3\2\2\2\u0338\u0334\3\2\2\2\u0338\u0335\3\2\2\2")
        buf.write("\u0338\u0336\3\2\2\2\u0338\u0337\3\2\2\2\u0339\u008b\3")
        buf.write("\2\2\2\u033a\u033d\5d\63\2\u033b\u033d\7\62\2\2\u033c")
        buf.write("\u033a\3\2\2\2\u033c\u033b\3\2\2\2\u033d\u033e\3\2\2\2")
        buf.write("\u033e\u0340\7)\2\2\u033f\u0341\5\u008eH\2\u0340\u033f")
        buf.write("\3\2\2\2\u0340\u0341\3\2\2\2\u0341\u0342\3\2\2\2\u0342")
        buf.write("\u0343\7*\2\2\u0343\u008d\3\2\2\2\u0344\u0349\5\u0090")
        buf.write("I\2\u0345\u0346\7,\2\2\u0346\u0348\5\u0090I\2\u0347\u0345")
        buf.write("\3\2\2\2\u0348\u034b\3\2\2\2\u0349\u0347\3\2\2\2\u0349")
        buf.write("\u034a\3\2\2\2\u034a\u034d\3\2\2\2\u034b\u0349\3\2\2\2")
        buf.write("\u034c\u034e\7,\2\2\u034d\u034c\3\2\2\2\u034d\u034e\3")
        buf.write("\2\2\2\u034e\u008f\3\2\2\2\u034f\u0350\5\u00a6T\2\u0350")
        buf.write("\u0351\7/\2\2\u0351\u0352\5\u0088E\2\u0352\u0091\3\2\2")
        buf.write("\2\u0353\u0355\5\u0094K\2\u0354\u0356\5\u0096L\2\u0355")
        buf.write("\u0354\3\2\2\2\u0355\u0356\3\2\2\2\u0356\u0358\3\2\2\2")
        buf.write("\u0357\u0359\5\u0098M\2\u0358\u0357\3\2\2\2\u0358\u0359")
        buf.write("\3\2\2\2\u0359\u0093\3\2\2\2\u035a\u035b\7\30\2\2\u035b")
        buf.write("\u035c\5\u0088E\2\u035c\u035d\5\u0080A\2\u035d\u0363\3")
        buf.write("\2\2\2\u035e\u035f\7\30\2\2\u035f\u0360\5\u0084C\2\u0360")
        buf.write("\u0361\5\u0080A\2\u0361\u0363\3\2\2\2\u0362\u035a\3\2")
        buf.write("\2\2\u0362\u035e\3\2\2\2\u0363\u0095\3\2\2\2\u0364\u0365")
        buf.write("\7\31\2\2\u0365\u0367\5\u0094K\2\u0366\u0364\3\2\2\2\u0367")
        buf.write("\u0368\3\2\2\2\u0368\u0366\3\2\2\2\u0368\u0369\3\2\2\2")
        buf.write("\u0369\u0097\3\2\2\2\u036a\u036b\7\31\2\2\u036b\u036c")
        buf.write("\5\u0080A\2\u036c\u0099\3\2\2\2\u036d\u036e\7\21\2\2\u036e")
        buf.write("\u036f\5\u009cO\2\u036f\u0370\7\24\2\2\u0370\u0371\5\u0088")
        buf.write("E\2\u0371\u0372\5\u0080A\2\u0372\u0379\3\2\2\2\u0373\u0374")
        buf.write("\7\21\2\2\u0374\u0375\5\u0088E\2\u0375\u0376\7\27\2\2")
        buf.write("\u0376\u0377\5\u0080A\2\u0377\u0379\3\2\2\2\u0378\u036d")
        buf.write("\3\2\2\2\u0378\u0373\3\2\2\2\u0379\u009b\3\2\2\2\u037a")
        buf.write("\u0380\5\u00a6T\2\u037b\u037c\7)\2\2\u037c\u037d\5\u009e")
        buf.write("P\2\u037d\u037e\7*\2\2\u037e\u0380\3\2\2\2\u037f\u037a")
        buf.write("\3\2\2\2\u037f\u037b\3\2\2\2\u0380\u009d\3\2\2\2\u0381")
        buf.write("\u0386\5\u00a6T\2\u0382\u0383\7,\2\2\u0383\u0385\5\u00a6")
        buf.write("T\2\u0384\u0382\3\2\2\2\u0385\u0388\3\2\2\2\u0386\u0384")
        buf.write("\3\2\2\2\u0386\u0387\3\2\2\2\u0387\u009f\3\2\2\2\u0388")
        buf.write("\u0386\3\2\2\2\u0389\u038e\5\u0088E\2\u038a\u038b\7,\2")
        buf.write("\2\u038b\u038d\5\u0088E\2\u038c\u038a\3\2\2\2\u038d\u0390")
        buf.write("\3\2\2\2\u038e\u038c\3\2\2\2\u038e\u038f\3\2\2\2\u038f")
        buf.write("\u00a1\3\2\2\2\u0390\u038e\3\2\2\2\u0391\u0396\5\u00a4")
        buf.write("S\2\u0392\u0393\7,\2\2\u0393\u0395\5\u00a4S\2\u0394\u0392")
        buf.write("\3\2\2\2\u0395\u0398\3\2\2\2\u0396\u0394\3\2\2\2\u0396")
        buf.write("\u0397\3\2\2\2\u0397\u00a3\3\2\2\2\u0398\u0396\3\2\2\2")
        buf.write("\u0399\u039a\5\u00a6T\2\u039a\u039b\7/\2\2\u039b\u039c")
        buf.write("\5\u0088E\2\u039c\u00a5\3\2\2\2\u039d\u03a0\7M\2\2\u039e")
        buf.write("\u03a0\5\u00aaV\2\u039f\u039d\3\2\2\2\u039f\u039e\3\2")
        buf.write("\2\2\u03a0\u00a7\3\2\2\2\u03a1\u03a3\t\7\2\2\u03a2\u03a1")
        buf.write("\3\2\2\2\u03a3\u03a4\3\2\2\2\u03a4\u03a2\3\2\2\2\u03a4")
        buf.write("\u03a5\3\2\2\2\u03a5\u00a9\3\2\2\2\u03a6\u03a7\t\b\2\2")
        buf.write("\u03a7\u00ab\3\2\2\2m\u00af\u00b8\u00be\u00c2\u00cb\u00d3")
        buf.write("\u00d9\u00dd\u00e7\u00f2\u00f8\u0101\u0114\u011c\u011f")
        buf.write("\u0127\u012c\u0131\u0134\u013c\u0141\u0146\u0149\u014e")
        buf.write("\u0153\u0158\u015c\u0160\u016e\u0174\u017a\u017f\u0184")
        buf.write("\u0189\u018c\u0193\u019c\u01a5\u01a8\u01b0\u01b5\u01ba")
        buf.write("\u01bd\u01c5\u01ca\u01cf\u01d2\u01da\u01df\u01e7\u01ee")
        buf.write("\u01f2\u01f6\u0203\u020e\u0211\u021b\u021f\u0221\u0226")
        buf.write("\u022a\u0237\u0242\u024e\u0250\u0254\u025b\u0263\u026a")
        buf.write("\u0277\u027c\u0280\u0282\u028e\u0293\u029c\u02a5\u02aa")
        buf.write("\u02af\u02b7\u02bb\u02bf\u02c5\u02cb\u02dd\u02e7\u02ed")
        buf.write("\u02fc\u031f\u0322\u0324\u0338\u033c\u0340\u0349\u034d")
        buf.write("\u0355\u0358\u0362\u0368\u0378\u037f\u0386\u038e\u0396")
        buf.write("\u039f\u03a4")
        return buf.getvalue()


class CWScriptParser ( Parser ):

    grammarFileName = "CWScriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'contract'", "'interface'", "'import'", 
                     "'implements'", "'impl'", "'extension'", "'requires'", 
                     "'extends'", "'error'", "'event'", "'instantiate'", 
                     "'exec'", "'query'", "'migrate'", "'for'", "'internal'", 
                     "'fn'", "'in'", "'from'", "'state'", "'times'", "'if'", 
                     "'else'", "'and'", "'or'", "'true'", "'false'", "'let'", 
                     "'fail'", "'return'", "'struct'", "'enum'", "'type'", 
                     "'emit'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'.'", "','", "'?'", "'!'", "':'", "'::'", "'#'", "'@'", 
                     "'$'", "'^'", "'&'", "'->'", "'=>'", "'''", "'\"'", 
                     "'_'", "'='", "'=='", "'!='", "'+'", "'+='", "'-'", 
                     "'-='", "'*'", "'*='", "'/'", "'/='", "'%'", "'%='", 
                     "'<'", "'<='", "'>'", "'>='", "'**'" ]

    symbolicNames = [ "<INVALID>", "CONTRACT", "INTERFACE", "IMPORT", "IMPLEMENTS", 
                      "IMPL", "EXTENSION", "REQUIRES", "EXTENDS", "ERROR", 
                      "EVENT", "INSTANTIATE", "EXEC", "QUERY", "MIGRATE", 
                      "FOR", "INTERNAL", "FN", "IN", "FROM", "STATE", "TIMES", 
                      "IF", "ELSE", "AND", "OR", "TRUE", "FALSE", "LET", 
                      "FAIL", "RETURN", "STRUCT", "ENUM", "TYPE", "EMIT", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
                      "RBRACE", "DOT", "COMMA", "QUEST", "EXCLAM", "COLON", 
                      "D_COLON", "HASH", "AT", "DOLLAR", "CARET", "AMP", 
                      "ARROW", "FAT_ARROW", "S_QUOTE", "D_QUOTE", "UNDERSCORE", 
                      "EQ", "EQEQ", "NEQ", "PLUS", "PLUS_EQ", "MINUS", "MINUS_EQ", 
                      "MUL", "MUL_EQ", "DIV", "DIV_EQ", "MOD", "MOD_EQ", 
                      "LT", "LT_EQ", "GT", "GT_EQ", "POW", "Ident", "StringLiteral", 
                      "IntegerLiteral", "DecimalLiteral", "CWSPEC_LINE_COMMENT", 
                      "CWSPEC_MULTI_COMMENT", "LINE_COMMENT", "MULTI_COMMENT", 
                      "WS" ]

    RULE_sourceFile = 0
    RULE_topLevelStmt = 1
    RULE_contractDefn = 2
    RULE_interfaceList = 3
    RULE_interfaceVal = 4
    RULE_interfaceDefn = 5
    RULE_interfaceExtDefn = 6
    RULE_importStmt = 7
    RULE_contractBody = 8
    RULE_interfaceBody = 9
    RULE_contractItem = 10
    RULE_interfaceItem = 11
    RULE_errorDefn = 12
    RULE_errorDefnBlock = 13
    RULE_errorDefnList = 14
    RULE_eventDefn = 15
    RULE_eventDefnBlock = 16
    RULE_eventDefnList = 17
    RULE_stateDefn = 18
    RULE_stateDefnBlock = 19
    RULE_stateDefnList = 20
    RULE_itemDefn = 21
    RULE_mapDefn = 22
    RULE_mapDefnKeys = 23
    RULE_mapDefnKey = 24
    RULE_instantiateDefn = 25
    RULE_instantiateDecl = 26
    RULE_implDefn = 27
    RULE_implDefnBlock = 28
    RULE_implDefnItem = 29
    RULE_execDefn = 30
    RULE_execDefnBlock = 31
    RULE_namedFnDefnList = 32
    RULE_execDecl = 33
    RULE_execDeclBlock = 34
    RULE_namedFnDeclList = 35
    RULE_queryDefn = 36
    RULE_queryDefnBlock = 37
    RULE_queryDecl = 38
    RULE_queryDeclBlock = 39
    RULE_enumVariant = 40
    RULE_enumVariant_struct = 41
    RULE_enumVariant_tuple = 42
    RULE_enumVariant_unit = 43
    RULE_tupleMembers = 44
    RULE_parenStructMembers = 45
    RULE_curlyStructMembers = 46
    RULE_structMember = 47
    RULE_typeExpr = 48
    RULE_typePath = 49
    RULE_reflectiveTypePath = 50
    RULE_typeDefn = 51
    RULE_autoStructDefn = 52
    RULE_structDefn = 53
    RULE_enumDefn = 54
    RULE_typeAliasDefn = 55
    RULE_namedFnDecl = 56
    RULE_namedFnDefn = 57
    RULE_fnType = 58
    RULE_fnArgs = 59
    RULE_fnArgList = 60
    RULE_fnArg = 61
    RULE_fnArgChecks = 62
    RULE_fnBody = 63
    RULE_stmt = 64
    RULE_letStmt_ = 65
    RULE_letLHS = 66
    RULE_expr = 67
    RULE_val = 68
    RULE_structVal_ = 69
    RULE_structValMembers = 70
    RULE_structValMember = 71
    RULE_ifExpr_ = 72
    RULE_ifClause_ = 73
    RULE_elseIfClauses = 74
    RULE_elseClause = 75
    RULE_forStmt_ = 76
    RULE_forItem = 77
    RULE_identList = 78
    RULE_exprList = 79
    RULE_namedExprList = 80
    RULE_namedExpr = 81
    RULE_ident = 82
    RULE_cwspec = 83
    RULE_reservedKeyword = 84

    ruleNames =  [ "sourceFile", "topLevelStmt", "contractDefn", "interfaceList", 
                   "interfaceVal", "interfaceDefn", "interfaceExtDefn", 
                   "importStmt", "contractBody", "interfaceBody", "contractItem", 
                   "interfaceItem", "errorDefn", "errorDefnBlock", "errorDefnList", 
                   "eventDefn", "eventDefnBlock", "eventDefnList", "stateDefn", 
                   "stateDefnBlock", "stateDefnList", "itemDefn", "mapDefn", 
                   "mapDefnKeys", "mapDefnKey", "instantiateDefn", "instantiateDecl", 
                   "implDefn", "implDefnBlock", "implDefnItem", "execDefn", 
                   "execDefnBlock", "namedFnDefnList", "execDecl", "execDeclBlock", 
                   "namedFnDeclList", "queryDefn", "queryDefnBlock", "queryDecl", 
                   "queryDeclBlock", "enumVariant", "enumVariant_struct", 
                   "enumVariant_tuple", "enumVariant_unit", "tupleMembers", 
                   "parenStructMembers", "curlyStructMembers", "structMember", 
                   "typeExpr", "typePath", "reflectiveTypePath", "typeDefn", 
                   "autoStructDefn", "structDefn", "enumDefn", "typeAliasDefn", 
                   "namedFnDecl", "namedFnDefn", "fnType", "fnArgs", "fnArgList", 
                   "fnArg", "fnArgChecks", "fnBody", "stmt", "letStmt_", 
                   "letLHS", "expr", "val", "structVal_", "structValMembers", 
                   "structValMember", "ifExpr_", "ifClause_", "elseIfClauses", 
                   "elseClause", "forStmt_", "forItem", "identList", "exprList", 
                   "namedExprList", "namedExpr", "ident", "cwspec", "reservedKeyword" ]

    EOF = Token.EOF
    CONTRACT=1
    INTERFACE=2
    IMPORT=3
    IMPLEMENTS=4
    IMPL=5
    EXTENSION=6
    REQUIRES=7
    EXTENDS=8
    ERROR=9
    EVENT=10
    INSTANTIATE=11
    EXEC=12
    QUERY=13
    MIGRATE=14
    FOR=15
    INTERNAL=16
    FN=17
    IN=18
    FROM=19
    STATE=20
    TIMES=21
    IF=22
    ELSE=23
    AND=24
    OR=25
    TRUE=26
    FALSE=27
    LET=28
    FAIL=29
    RETURN=30
    STRUCT=31
    ENUM=32
    TYPE=33
    EMIT=34
    LPAREN=35
    RPAREN=36
    LBRACK=37
    RBRACK=38
    LBRACE=39
    RBRACE=40
    DOT=41
    COMMA=42
    QUEST=43
    EXCLAM=44
    COLON=45
    D_COLON=46
    HASH=47
    AT=48
    DOLLAR=49
    CARET=50
    AMP=51
    ARROW=52
    FAT_ARROW=53
    S_QUOTE=54
    D_QUOTE=55
    UNDERSCORE=56
    EQ=57
    EQEQ=58
    NEQ=59
    PLUS=60
    PLUS_EQ=61
    MINUS=62
    MINUS_EQ=63
    MUL=64
    MUL_EQ=65
    DIV=66
    DIV_EQ=67
    MOD=68
    MOD_EQ=69
    LT=70
    LT_EQ=71
    GT=72
    GT_EQ=73
    POW=74
    Ident=75
    StringLiteral=76
    IntegerLiteral=77
    DecimalLiteral=78
    CWSPEC_LINE_COMMENT=79
    CWSPEC_MULTI_COMMENT=80
    LINE_COMMENT=81
    MULTI_COMMENT=82
    WS=83

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceFileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CWScriptParser.EOF, 0)

        def topLevelStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TopLevelStmtContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TopLevelStmtContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_sourceFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceFile" ):
                listener.enterSourceFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceFile" ):
                listener.exitSourceFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceFile" ):
                return visitor.visitSourceFile(self)
            else:
                return visitor.visitChildren(self)




    def sourceFile(self):

        localctx = CWScriptParser.SourceFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.EXTENSION))) != 0):
                self.state = 170
                self.topLevelStmt()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(CWScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def contractDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ContractDefnContext,0)


        def interfaceDefn(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceDefnContext,0)


        def interfaceExtDefn(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceExtDefnContext,0)


        def importStmt(self):
            return self.getTypedRuleContext(CWScriptParser.ImportStmtContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_topLevelStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelStmt" ):
                listener.enterTopLevelStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelStmt" ):
                listener.exitTopLevelStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelStmt" ):
                return visitor.visitTopLevelStmt(self)
            else:
                return visitor.visitChildren(self)




    def topLevelStmt(self):

        localctx = CWScriptParser.TopLevelStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelStmt)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.CONTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.contractDefn()
                pass
            elif token in [CWScriptParser.INTERFACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.interfaceDefn()
                pass
            elif token in [CWScriptParser.EXTENSION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.interfaceExtDefn()
                pass
            elif token in [CWScriptParser.IMPORT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.importStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContractDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext
            self.parent = None # IdentContext
            self.interfaces = None # InterfaceListContext

        def CONTRACT(self):
            return self.getToken(CWScriptParser.CONTRACT, 0)

        def contractBody(self):
            return self.getTypedRuleContext(CWScriptParser.ContractBodyContext,0)


        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def EXTENDS(self):
            return self.getToken(CWScriptParser.EXTENDS, 0)

        def IMPLEMENTS(self):
            return self.getToken(CWScriptParser.IMPLEMENTS, 0)

        def interfaceList(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_contractDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContractDefn" ):
                listener.enterContractDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContractDefn" ):
                listener.exitContractDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContractDefn" ):
                return visitor.visitContractDefn(self)
            else:
                return visitor.visitChildren(self)




    def contractDefn(self):

        localctx = CWScriptParser.ContractDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_contractDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(CWScriptParser.CONTRACT)

            self.state = 185
            localctx.name = self.ident()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.EXTENDS:
                self.state = 186
                self.match(CWScriptParser.EXTENDS)
                self.state = 187
                localctx.parent = self.ident()


            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.IMPLEMENTS:
                self.state = 190
                self.match(CWScriptParser.IMPLEMENTS)

                self.state = 191
                localctx.interfaces = self.interfaceList()


            self.state = 194
            self.contractBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceVal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.InterfaceValContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.InterfaceValContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_interfaceList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceList" ):
                listener.enterInterfaceList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceList" ):
                listener.exitInterfaceList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceList" ):
                return visitor.visitInterfaceList(self)
            else:
                return visitor.visitChildren(self)




    def interfaceList(self):

        localctx = CWScriptParser.InterfaceListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interfaceList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.interfaceVal()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CWScriptParser.COMMA:
                self.state = 197
                self.match(CWScriptParser.COMMA)
                self.state = 198
                self.interfaceVal()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.interfaceName = None # IdentContext
            self.interfaceExts = None # IdentListContext

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def identList(self):
            return self.getTypedRuleContext(CWScriptParser.IdentListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_interfaceVal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceVal" ):
                listener.enterInterfaceVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceVal" ):
                listener.exitInterfaceVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceVal" ):
                return visitor.visitInterfaceVal(self)
            else:
                return visitor.visitChildren(self)




    def interfaceVal(self):

        localctx = CWScriptParser.InterfaceValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interfaceVal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            localctx.interfaceName = self.ident()
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 205
                self.match(CWScriptParser.LPAREN)
                self.state = 206
                localctx.interfaceExts = self.identList()
                self.state = 207
                self.match(CWScriptParser.RPAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext
            self.parent = None # IdentContext
            self.interfaces = None # InterfaceListContext

        def INTERFACE(self):
            return self.getToken(CWScriptParser.INTERFACE, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceBodyContext,0)


        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def EXTENDS(self):
            return self.getToken(CWScriptParser.EXTENDS, 0)

        def IMPLEMENTS(self):
            return self.getToken(CWScriptParser.IMPLEMENTS, 0)

        def interfaceList(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_interfaceDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDefn" ):
                listener.enterInterfaceDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDefn" ):
                listener.exitInterfaceDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefn" ):
                return visitor.visitInterfaceDefn(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDefn(self):

        localctx = CWScriptParser.InterfaceDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_interfaceDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(CWScriptParser.INTERFACE)

            self.state = 212
            localctx.name = self.ident()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.EXTENDS:
                self.state = 213
                self.match(CWScriptParser.EXTENDS)
                self.state = 214
                localctx.parent = self.ident()


            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.IMPLEMENTS:
                self.state = 217
                self.match(CWScriptParser.IMPLEMENTS)

                self.state = 218
                localctx.interfaces = self.interfaceList()


            self.state = 221
            self.interfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceExtDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.extName = None # IdentContext
            self.interfaceName = None # IdentContext
            self.interfaceReqs = None # InterfaceListContext

        def EXTENSION(self):
            return self.getToken(CWScriptParser.EXTENSION, 0)

        def FOR(self):
            return self.getToken(CWScriptParser.FOR, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceBodyContext,0)


        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def REQUIRES(self):
            return self.getToken(CWScriptParser.REQUIRES, 0)

        def interfaceList(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_interfaceExtDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceExtDefn" ):
                listener.enterInterfaceExtDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceExtDefn" ):
                listener.exitInterfaceExtDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceExtDefn" ):
                return visitor.visitInterfaceExtDefn(self)
            else:
                return visitor.visitChildren(self)




    def interfaceExtDefn(self):

        localctx = CWScriptParser.InterfaceExtDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_interfaceExtDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(CWScriptParser.EXTENSION)

            self.state = 224
            localctx.extName = self.ident()
            self.state = 225
            self.match(CWScriptParser.FOR)

            self.state = 226
            localctx.interfaceName = self.ident()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.REQUIRES:
                self.state = 227
                self.match(CWScriptParser.REQUIRES)
                self.state = 228
                localctx.interfaceReqs = self.interfaceList()


            self.state = 231
            self.interfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fileName = None # Token
            self.symbols = None # IdentListContext

        def IMPORT(self):
            return self.getToken(CWScriptParser.IMPORT, 0)

        def StringLiteral(self):
            return self.getToken(CWScriptParser.StringLiteral, 0)

        def FROM(self):
            return self.getToken(CWScriptParser.FROM, 0)

        def identList(self):
            return self.getTypedRuleContext(CWScriptParser.IdentListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_importStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStmt" ):
                listener.enterImportStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStmt" ):
                listener.exitImportStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = CWScriptParser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_importStmt)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(CWScriptParser.IMPORT)

                self.state = 234
                localctx.fileName = self.match(CWScriptParser.StringLiteral)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(CWScriptParser.IMPORT)

                self.state = 236
                localctx.symbols = self.identList()
                self.state = 237
                self.match(CWScriptParser.FROM)

                self.state = 238
                localctx.fileName = self.match(CWScriptParser.StringLiteral)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContractBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.items = None # ContractItemContext

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def contractItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ContractItemContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ContractItemContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_contractBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContractBody" ):
                listener.enterContractBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContractBody" ):
                listener.exitContractBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContractBody" ):
                return visitor.visitContractBody(self)
            else:
                return visitor.visitChildren(self)




    def contractBody(self):

        localctx = CWScriptParser.ContractBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_contractBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(CWScriptParser.LBRACE)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.IMPL) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.AT))) != 0) or _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 243
                localctx.items = self.contractItem()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.items = None # InterfaceItemContext

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def interfaceItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.InterfaceItemContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.InterfaceItemContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_interfaceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceBody" ):
                listener.enterInterfaceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceBody" ):
                listener.exitInterfaceBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceBody" ):
                return visitor.visitInterfaceBody(self)
            else:
                return visitor.visitChildren(self)




    def interfaceBody(self):

        localctx = CWScriptParser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interfaceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(CWScriptParser.LBRACE)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.AT))) != 0) or _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 252
                localctx.items = self.interfaceItem()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContractItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDefn(self):
            return self.getTypedRuleContext(CWScriptParser.TypeDefnContext,0)


        def errorDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ErrorDefnContext,0)


        def errorDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.ErrorDefnBlockContext,0)


        def eventDefn(self):
            return self.getTypedRuleContext(CWScriptParser.EventDefnContext,0)


        def eventDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.EventDefnBlockContext,0)


        def stateDefn(self):
            return self.getTypedRuleContext(CWScriptParser.StateDefnContext,0)


        def stateDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.StateDefnBlockContext,0)


        def instantiateDefn(self):
            return self.getTypedRuleContext(CWScriptParser.InstantiateDefnContext,0)


        def execDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDefnContext,0)


        def execDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDefnBlockContext,0)


        def queryDefn(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDefnContext,0)


        def queryDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDefnBlockContext,0)


        def implDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ImplDefnContext,0)


        def implDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.ImplDefnBlockContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_contractItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContractItem" ):
                listener.enterContractItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContractItem" ):
                listener.exitContractItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContractItem" ):
                return visitor.visitContractItem(self)
            else:
                return visitor.visitChildren(self)




    def contractItem(self):

        localctx = CWScriptParser.ContractItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_contractItem)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.typeDefn()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.errorDefn()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.errorDefnBlock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.eventDefn()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.eventDefnBlock()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 265
                self.stateDefn()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 266
                self.stateDefnBlock()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 267
                self.instantiateDefn()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 268
                self.execDefn()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 269
                self.execDefnBlock()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 270
                self.queryDefn()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 271
                self.queryDefnBlock()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 272
                self.implDefn()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 273
                self.implDefnBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDefn(self):
            return self.getTypedRuleContext(CWScriptParser.TypeDefnContext,0)


        def instantiateDecl(self):
            return self.getTypedRuleContext(CWScriptParser.InstantiateDeclContext,0)


        def execDecl(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDeclContext,0)


        def execDeclBlock(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDeclBlockContext,0)


        def queryDecl(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDeclContext,0)


        def queryDeclBlock(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDeclBlockContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_interfaceItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceItem" ):
                listener.enterInterfaceItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceItem" ):
                listener.exitInterfaceItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceItem" ):
                return visitor.visitInterfaceItem(self)
            else:
                return visitor.visitChildren(self)




    def interfaceItem(self):

        localctx = CWScriptParser.InterfaceItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interfaceItem)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.typeDefn()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.instantiateDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.execDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 279
                self.execDeclBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 280
                self.queryDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 281
                self.queryDeclBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ErrorDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def ERROR(self):
            return self.getToken(CWScriptParser.ERROR, 0)

        def enumVariant(self):
            return self.getTypedRuleContext(CWScriptParser.EnumVariantContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_errorDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErrorDefn" ):
                listener.enterErrorDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErrorDefn" ):
                listener.exitErrorDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitErrorDefn" ):
                return visitor.visitErrorDefn(self)
            else:
                return visitor.visitChildren(self)




    def errorDefn(self):

        localctx = CWScriptParser.ErrorDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_errorDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 284
                localctx.spec = self.cwspec()


            self.state = 287
            self.match(CWScriptParser.ERROR)
            self.state = 288
            self.enumVariant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ErrorDefnBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.errorDefns = None # ErrorDefnListContext

        def ERROR(self):
            return self.getToken(CWScriptParser.ERROR, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def errorDefnList(self):
            return self.getTypedRuleContext(CWScriptParser.ErrorDefnListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_errorDefnBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErrorDefnBlock" ):
                listener.enterErrorDefnBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErrorDefnBlock" ):
                listener.exitErrorDefnBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitErrorDefnBlock" ):
                return visitor.visitErrorDefnBlock(self)
            else:
                return visitor.visitChildren(self)




    def errorDefnBlock(self):

        localctx = CWScriptParser.ErrorDefnBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_errorDefnBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(CWScriptParser.ERROR)
            self.state = 291
            self.match(CWScriptParser.LBRACE)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT) | (1 << CWScriptParser.AT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 292
                localctx.errorDefns = self.errorDefnList()


            self.state = 295
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ErrorDefnListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def enumVariant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.EnumVariantContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.EnumVariantContext,i)


        def cwspec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.CwspecContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.CwspecContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_errorDefnList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErrorDefnList" ):
                listener.enterErrorDefnList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErrorDefnList" ):
                listener.exitErrorDefnList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitErrorDefnList" ):
                return visitor.visitErrorDefnList(self)
            else:
                return visitor.visitChildren(self)




    def errorDefnList(self):

        localctx = CWScriptParser.ErrorDefnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_errorDefnList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                    self.state = 297
                    localctx.spec = self.cwspec()


                self.state = 300
                self.enumVariant()
                self.state = 303 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT) | (1 << CWScriptParser.AT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def EVENT(self):
            return self.getToken(CWScriptParser.EVENT, 0)

        def enumVariant(self):
            return self.getTypedRuleContext(CWScriptParser.EnumVariantContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_eventDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventDefn" ):
                listener.enterEventDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventDefn" ):
                listener.exitEventDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventDefn" ):
                return visitor.visitEventDefn(self)
            else:
                return visitor.visitChildren(self)




    def eventDefn(self):

        localctx = CWScriptParser.EventDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_eventDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 305
                localctx.spec = self.cwspec()


            self.state = 308
            self.match(CWScriptParser.EVENT)
            self.state = 309
            self.enumVariant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventDefnBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.eventDefns = None # EventDefnListContext

        def EVENT(self):
            return self.getToken(CWScriptParser.EVENT, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def eventDefnList(self):
            return self.getTypedRuleContext(CWScriptParser.EventDefnListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_eventDefnBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventDefnBlock" ):
                listener.enterEventDefnBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventDefnBlock" ):
                listener.exitEventDefnBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventDefnBlock" ):
                return visitor.visitEventDefnBlock(self)
            else:
                return visitor.visitChildren(self)




    def eventDefnBlock(self):

        localctx = CWScriptParser.EventDefnBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_eventDefnBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(CWScriptParser.EVENT)
            self.state = 312
            self.match(CWScriptParser.LBRACE)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT) | (1 << CWScriptParser.AT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 313
                localctx.eventDefns = self.eventDefnList()


            self.state = 316
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventDefnListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def enumVariant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.EnumVariantContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.EnumVariantContext,i)


        def cwspec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.CwspecContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.CwspecContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_eventDefnList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventDefnList" ):
                listener.enterEventDefnList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventDefnList" ):
                listener.exitEventDefnList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventDefnList" ):
                return visitor.visitEventDefnList(self)
            else:
                return visitor.visitChildren(self)




    def eventDefnList(self):

        localctx = CWScriptParser.EventDefnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_eventDefnList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                    self.state = 318
                    localctx.spec = self.cwspec()


                self.state = 321
                self.enumVariant()
                self.state = 324 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT) | (1 << CWScriptParser.AT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def STATE(self):
            return self.getToken(CWScriptParser.STATE, 0)

        def itemDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ItemDefnContext,0)


        def mapDefn(self):
            return self.getTypedRuleContext(CWScriptParser.MapDefnContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_stateDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateDefn" ):
                listener.enterStateDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateDefn" ):
                listener.exitStateDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateDefn" ):
                return visitor.visitStateDefn(self)
            else:
                return visitor.visitChildren(self)




    def stateDefn(self):

        localctx = CWScriptParser.StateDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stateDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 326
                localctx.spec = self.cwspec()


            self.state = 329
            self.match(CWScriptParser.STATE)
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 330
                self.itemDefn()
                pass

            elif la_ == 2:
                self.state = 331
                self.mapDefn()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateDefnBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.stateDefns = None # StateDefnListContext

        def STATE(self):
            return self.getToken(CWScriptParser.STATE, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def stateDefnList(self):
            return self.getTypedRuleContext(CWScriptParser.StateDefnListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_stateDefnBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateDefnBlock" ):
                listener.enterStateDefnBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateDefnBlock" ):
                listener.exitStateDefnBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateDefnBlock" ):
                return visitor.visitStateDefnBlock(self)
            else:
                return visitor.visitChildren(self)




    def stateDefnBlock(self):

        localctx = CWScriptParser.StateDefnBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stateDefnBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(CWScriptParser.STATE)
            self.state = 335
            self.match(CWScriptParser.LBRACE)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 336
                localctx.stateDefns = self.stateDefnList()


            self.state = 339
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateDefnListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def itemDefn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ItemDefnContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ItemDefnContext,i)


        def mapDefn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.MapDefnContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.MapDefnContext,i)


        def cwspec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.CwspecContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.CwspecContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_stateDefnList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateDefnList" ):
                listener.enterStateDefnList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateDefnList" ):
                listener.exitStateDefnList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateDefnList" ):
                return visitor.visitStateDefnList(self)
            else:
                return visitor.visitChildren(self)




    def stateDefnList(self):

        localctx = CWScriptParser.StateDefnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stateDefnList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                    self.state = 341
                    localctx.spec = self.cwspec()


                self.state = 346
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 344
                    self.itemDefn()
                    pass

                elif la_ == 2:
                    self.state = 345
                    self.mapDefn()
                    pass


                self.state = 350 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.itemName = None # IdentContext
            self.itemType = None # TypeExprContext

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_itemDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemDefn" ):
                listener.enterItemDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemDefn" ):
                listener.exitItemDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemDefn" ):
                return visitor.visitItemDefn(self)
            else:
                return visitor.visitChildren(self)




    def itemDefn(self):

        localctx = CWScriptParser.ItemDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_itemDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            localctx.itemName = self.ident()
            self.state = 353
            self.match(CWScriptParser.COLON)

            self.state = 354
            localctx.itemType = self.typeExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.mapName = None # IdentContext
            self.mapKeys = None # MapDefnKeysContext
            self.mapValType = None # TypeExprContext

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def mapDefnKeys(self):
            return self.getTypedRuleContext(CWScriptParser.MapDefnKeysContext,0)


        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_mapDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapDefn" ):
                listener.enterMapDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapDefn" ):
                listener.exitMapDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapDefn" ):
                return visitor.visitMapDefn(self)
            else:
                return visitor.visitChildren(self)




    def mapDefn(self):

        localctx = CWScriptParser.MapDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mapDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            localctx.mapName = self.ident()

            self.state = 357
            localctx.mapKeys = self.mapDefnKeys()
            self.state = 358
            self.match(CWScriptParser.COLON)

            self.state = 359
            localctx.mapValType = self.typeExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapDefnKeysContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapDefnKey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.MapDefnKeyContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.MapDefnKeyContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_mapDefnKeys

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapDefnKeys" ):
                listener.enterMapDefnKeys(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapDefnKeys" ):
                listener.exitMapDefnKeys(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapDefnKeys" ):
                return visitor.visitMapDefnKeys(self)
            else:
                return visitor.visitChildren(self)




    def mapDefnKeys(self):

        localctx = CWScriptParser.MapDefnKeysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_mapDefnKeys)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 361
                self.mapDefnKey()
                self.state = 364 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CWScriptParser.LBRACK):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapDefnKeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.keyName = None # IdentContext
            self.keyType = None # TypeExprContext

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_mapDefnKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapDefnKey" ):
                listener.enterMapDefnKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapDefnKey" ):
                listener.exitMapDefnKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapDefnKey" ):
                return visitor.visitMapDefnKey(self)
            else:
                return visitor.visitChildren(self)




    def mapDefnKey(self):

        localctx = CWScriptParser.MapDefnKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mapDefnKey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(CWScriptParser.LBRACK)
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 367
                localctx.keyName = self.ident()
                self.state = 368
                self.match(CWScriptParser.COLON)


            self.state = 372
            localctx.keyType = self.typeExpr(0)
            self.state = 373
            self.match(CWScriptParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstantiateDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def INSTANTIATE(self):
            return self.getToken(CWScriptParser.INSTANTIATE, 0)

        def fnArgs(self):
            return self.getTypedRuleContext(CWScriptParser.FnArgsContext,0)


        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def fnType(self):
            return self.getTypedRuleContext(CWScriptParser.FnTypeContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_instantiateDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstantiateDefn" ):
                listener.enterInstantiateDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstantiateDefn" ):
                listener.exitInstantiateDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstantiateDefn" ):
                return visitor.visitInstantiateDefn(self)
            else:
                return visitor.visitChildren(self)




    def instantiateDefn(self):

        localctx = CWScriptParser.InstantiateDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_instantiateDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 375
                localctx.spec = self.cwspec()


            self.state = 378
            self.match(CWScriptParser.INSTANTIATE)
            self.state = 379
            self.fnArgs()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.ARROW:
                self.state = 380
                self.fnType()


            self.state = 383
            self.fnBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstantiateDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def INSTANTIATE(self):
            return self.getToken(CWScriptParser.INSTANTIATE, 0)

        def fnArgs(self):
            return self.getTypedRuleContext(CWScriptParser.FnArgsContext,0)


        def fnType(self):
            return self.getTypedRuleContext(CWScriptParser.FnTypeContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_instantiateDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstantiateDecl" ):
                listener.enterInstantiateDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstantiateDecl" ):
                listener.exitInstantiateDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstantiateDecl" ):
                return visitor.visitInstantiateDecl(self)
            else:
                return visitor.visitChildren(self)




    def instantiateDecl(self):

        localctx = CWScriptParser.InstantiateDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_instantiateDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 385
                localctx.spec = self.cwspec()


            self.state = 388
            self.match(CWScriptParser.INSTANTIATE)
            self.state = 389
            self.fnArgs()
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.ARROW:
                self.state = 390
                self.fnType()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext
            self.interfaces = None # InterfaceListContext

        def IMPL(self):
            return self.getToken(CWScriptParser.IMPL, 0)

        def execDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDefnContext,0)


        def queryDefn(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDefnContext,0)


        def interfaceList(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceListContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_implDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplDefn" ):
                listener.enterImplDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplDefn" ):
                listener.exitImplDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplDefn" ):
                return visitor.visitImplDefn(self)
            else:
                return visitor.visitChildren(self)




    def implDefn(self):

        localctx = CWScriptParser.ImplDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_implDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 393
                localctx.spec = self.cwspec()


            self.state = 396
            self.match(CWScriptParser.IMPL)
            self.state = 397
            localctx.interfaces = self.interfaceList()
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 399
                self.execDefn()
                pass

            elif la_ == 2:
                self.state = 400
                self.queryDefn()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplDefnBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.interfaces = None # InterfaceListContext
            self.items = None # ImplDefnItemContext

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def IMPL(self):
            return self.getToken(CWScriptParser.IMPL, 0)

        def interfaceList(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceListContext,0)


        def implDefnItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ImplDefnItemContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ImplDefnItemContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_implDefnBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplDefnBlock" ):
                listener.enterImplDefnBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplDefnBlock" ):
                listener.exitImplDefnBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplDefnBlock" ):
                return visitor.visitImplDefnBlock(self)
            else:
                return visitor.visitChildren(self)




    def implDefnBlock(self):

        localctx = CWScriptParser.ImplDefnBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_implDefnBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(CWScriptParser.IMPL)
            self.state = 404
            localctx.interfaces = self.interfaceList()
            self.state = 406
            self.match(CWScriptParser.LBRACE)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CWScriptParser.EXEC or _la==CWScriptParser.QUERY or _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 407
                localctx.items = self.implDefnItem()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 413
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplDefnItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def execDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDefnContext,0)


        def execDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDefnBlockContext,0)


        def queryDefn(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDefnContext,0)


        def queryDefnBlock(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDefnBlockContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_implDefnItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplDefnItem" ):
                listener.enterImplDefnItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplDefnItem" ):
                listener.exitImplDefnItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplDefnItem" ):
                return visitor.visitImplDefnItem(self)
            else:
                return visitor.visitChildren(self)




    def implDefnItem(self):

        localctx = CWScriptParser.ImplDefnItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_implDefnItem)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.execDefn()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.execDefnBlock()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.queryDefn()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 418
                self.queryDefnBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)

        def namedFnDefn(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDefnContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_execDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecDefn" ):
                listener.enterExecDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecDefn" ):
                listener.exitExecDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecDefn" ):
                return visitor.visitExecDefn(self)
            else:
                return visitor.visitChildren(self)




    def execDefn(self):

        localctx = CWScriptParser.ExecDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_execDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 421
                localctx.spec = self.cwspec()


            self.state = 424
            self.match(CWScriptParser.EXEC)
            self.state = 425
            self.namedFnDefn()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecDefnBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.execDefns = None # NamedFnDefnListContext

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def namedFnDefnList(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDefnListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_execDefnBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecDefnBlock" ):
                listener.enterExecDefnBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecDefnBlock" ):
                listener.exitExecDefnBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecDefnBlock" ):
                return visitor.visitExecDefnBlock(self)
            else:
                return visitor.visitChildren(self)




    def execDefnBlock(self):

        localctx = CWScriptParser.ExecDefnBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_execDefnBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(CWScriptParser.EXEC)
            self.state = 428
            self.match(CWScriptParser.LBRACE)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 429
                localctx.execDefns = self.namedFnDefnList()


            self.state = 432
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedFnDefnListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def namedFnDefn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.NamedFnDefnContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.NamedFnDefnContext,i)


        def cwspec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.CwspecContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.CwspecContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_namedFnDefnList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedFnDefnList" ):
                listener.enterNamedFnDefnList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedFnDefnList" ):
                listener.exitNamedFnDefnList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedFnDefnList" ):
                return visitor.visitNamedFnDefnList(self)
            else:
                return visitor.visitChildren(self)




    def namedFnDefnList(self):

        localctx = CWScriptParser.NamedFnDefnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_namedFnDefnList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                    self.state = 434
                    localctx.spec = self.cwspec()


                self.state = 437
                self.namedFnDefn()
                self.state = 440 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)

        def namedFnDecl(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDeclContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_execDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecDecl" ):
                listener.enterExecDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecDecl" ):
                listener.exitExecDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecDecl" ):
                return visitor.visitExecDecl(self)
            else:
                return visitor.visitChildren(self)




    def execDecl(self):

        localctx = CWScriptParser.ExecDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_execDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 442
                localctx.spec = self.cwspec()


            self.state = 445
            self.match(CWScriptParser.EXEC)
            self.state = 446
            self.namedFnDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecDeclBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.execDecls = None # NamedFnDeclListContext

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def namedFnDeclList(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDeclListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_execDeclBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecDeclBlock" ):
                listener.enterExecDeclBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecDeclBlock" ):
                listener.exitExecDeclBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecDeclBlock" ):
                return visitor.visitExecDeclBlock(self)
            else:
                return visitor.visitChildren(self)




    def execDeclBlock(self):

        localctx = CWScriptParser.ExecDeclBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_execDeclBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(CWScriptParser.EXEC)
            self.state = 449
            self.match(CWScriptParser.LBRACE)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 450
                localctx.execDecls = self.namedFnDeclList()


            self.state = 453
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedFnDeclListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def namedFnDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.NamedFnDeclContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.NamedFnDeclContext,i)


        def cwspec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.CwspecContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.CwspecContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_namedFnDeclList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedFnDeclList" ):
                listener.enterNamedFnDeclList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedFnDeclList" ):
                listener.exitNamedFnDeclList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedFnDeclList" ):
                return visitor.visitNamedFnDeclList(self)
            else:
                return visitor.visitChildren(self)




    def namedFnDeclList(self):

        localctx = CWScriptParser.NamedFnDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_namedFnDeclList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                    self.state = 455
                    localctx.spec = self.cwspec()


                self.state = 458
                self.namedFnDecl()
                self.state = 461 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)

        def namedFnDefn(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDefnContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_queryDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDefn" ):
                listener.enterQueryDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDefn" ):
                listener.exitQueryDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryDefn" ):
                return visitor.visitQueryDefn(self)
            else:
                return visitor.visitChildren(self)




    def queryDefn(self):

        localctx = CWScriptParser.QueryDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_queryDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 463
                localctx.spec = self.cwspec()


            self.state = 466
            self.match(CWScriptParser.QUERY)
            self.state = 467
            self.namedFnDefn()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryDefnBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.queryDefns = None # NamedFnDefnListContext

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def namedFnDefnList(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDefnListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_queryDefnBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDefnBlock" ):
                listener.enterQueryDefnBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDefnBlock" ):
                listener.exitQueryDefnBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryDefnBlock" ):
                return visitor.visitQueryDefnBlock(self)
            else:
                return visitor.visitChildren(self)




    def queryDefnBlock(self):

        localctx = CWScriptParser.QueryDefnBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_queryDefnBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(CWScriptParser.QUERY)
            self.state = 470
            self.match(CWScriptParser.LBRACE)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 471
                localctx.queryDefns = self.namedFnDefnList()


            self.state = 474
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)

        def namedFnDecl(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDeclContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_queryDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDecl" ):
                listener.enterQueryDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDecl" ):
                listener.exitQueryDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryDecl" ):
                return visitor.visitQueryDecl(self)
            else:
                return visitor.visitChildren(self)




    def queryDecl(self):

        localctx = CWScriptParser.QueryDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_queryDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 476
                localctx.spec = self.cwspec()


            self.state = 479
            self.match(CWScriptParser.QUERY)
            self.state = 480
            self.namedFnDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryDeclBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.queryDecls = None # NamedFnDeclListContext

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def namedFnDeclList(self):
            return self.getTypedRuleContext(CWScriptParser.NamedFnDeclListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_queryDeclBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDeclBlock" ):
                listener.enterQueryDeclBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDeclBlock" ):
                listener.exitQueryDeclBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryDeclBlock" ):
                return visitor.visitQueryDeclBlock(self)
            else:
                return visitor.visitChildren(self)




    def queryDeclBlock(self):

        localctx = CWScriptParser.QueryDeclBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_queryDeclBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(CWScriptParser.QUERY)
            self.state = 483
            self.match(CWScriptParser.LBRACE)
            self.state = 485
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 484
                localctx.queryDecls = self.namedFnDeclList()


            self.state = 487
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumVariantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumVariant_struct(self):
            return self.getTypedRuleContext(CWScriptParser.EnumVariant_structContext,0)


        def enumVariant_tuple(self):
            return self.getTypedRuleContext(CWScriptParser.EnumVariant_tupleContext,0)


        def enumVariant_unit(self):
            return self.getTypedRuleContext(CWScriptParser.EnumVariant_unitContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_enumVariant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumVariant" ):
                listener.enterEnumVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumVariant" ):
                listener.exitEnumVariant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumVariant" ):
                return visitor.visitEnumVariant(self)
            else:
                return visitor.visitChildren(self)




    def enumVariant(self):

        localctx = CWScriptParser.EnumVariantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_enumVariant)
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.enumVariant_struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.enumVariant_tuple()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
                self.enumVariant_unit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumVariant_structContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext

        def AT(self):
            return self.getToken(CWScriptParser.AT, 0)

        def parenStructMembers(self):
            return self.getTypedRuleContext(CWScriptParser.ParenStructMembersContext,0)


        def curlyStructMembers(self):
            return self.getTypedRuleContext(CWScriptParser.CurlyStructMembersContext,0)


        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_enumVariant_struct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumVariant_struct" ):
                listener.enterEnumVariant_struct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumVariant_struct" ):
                listener.exitEnumVariant_struct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumVariant_struct" ):
                return visitor.visitEnumVariant_struct(self)
            else:
                return visitor.visitChildren(self)




    def enumVariant_struct(self):

        localctx = CWScriptParser.EnumVariant_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_enumVariant_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.CONTRACT, CWScriptParser.INTERFACE, CWScriptParser.IMPORT, CWScriptParser.IMPLEMENTS, CWScriptParser.IMPL, CWScriptParser.EXTENSION, CWScriptParser.EXTENDS, CWScriptParser.ERROR, CWScriptParser.EVENT, CWScriptParser.INSTANTIATE, CWScriptParser.EXEC, CWScriptParser.QUERY, CWScriptParser.MIGRATE, CWScriptParser.FOR, CWScriptParser.IN, CWScriptParser.FROM, CWScriptParser.STATE, CWScriptParser.TIMES, CWScriptParser.IF, CWScriptParser.ELSE, CWScriptParser.AND, CWScriptParser.OR, CWScriptParser.TRUE, CWScriptParser.FALSE, CWScriptParser.LET, CWScriptParser.RETURN, CWScriptParser.STRUCT, CWScriptParser.ENUM, CWScriptParser.TYPE, CWScriptParser.EMIT, CWScriptParser.Ident]:
                self.state = 494
                localctx.name = self.ident()
                pass
            elif token in [CWScriptParser.AT]:
                self.state = 495
                self.match(CWScriptParser.AT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.LPAREN]:
                self.state = 498
                self.parenStructMembers()
                pass
            elif token in [CWScriptParser.LBRACE]:
                self.state = 499
                self.curlyStructMembers()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumVariant_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext
            self.members = None # TupleMembersContext

        def tupleMembers(self):
            return self.getTypedRuleContext(CWScriptParser.TupleMembersContext,0)


        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_enumVariant_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumVariant_tuple" ):
                listener.enterEnumVariant_tuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumVariant_tuple" ):
                listener.exitEnumVariant_tuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumVariant_tuple" ):
                return visitor.visitEnumVariant_tuple(self)
            else:
                return visitor.visitChildren(self)




    def enumVariant_tuple(self):

        localctx = CWScriptParser.EnumVariant_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_enumVariant_tuple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            localctx.name = self.ident()
            self.state = 503
            localctx.members = self.tupleMembers()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumVariant_unitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_enumVariant_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumVariant_unit" ):
                listener.enterEnumVariant_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumVariant_unit" ):
                listener.exitEnumVariant_unit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumVariant_unit" ):
                return visitor.visitEnumVariant_unit(self)
            else:
                return visitor.visitChildren(self)




    def enumVariant_unit(self):

        localctx = CWScriptParser.EnumVariant_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_enumVariant_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            localctx.name = self.ident()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleMembersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)

        def typeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TypeExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TypeExprContext,i)


        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_tupleMembers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleMembers" ):
                listener.enterTupleMembers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleMembers" ):
                listener.exitTupleMembers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupleMembers" ):
                return visitor.visitTupleMembers(self)
            else:
                return visitor.visitChildren(self)




    def tupleMembers(self):

        localctx = CWScriptParser.TupleMembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_tupleMembers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(CWScriptParser.LPAREN)
            self.state = 508
            self.typeExpr(0)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CWScriptParser.COMMA:
                self.state = 509
                self.match(CWScriptParser.COMMA)
                self.state = 510
                self.typeExpr(0)
                self.state = 515
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 516
            self.match(CWScriptParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenStructMembersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StructMemberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_parenStructMembers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenStructMembers" ):
                listener.enterParenStructMembers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenStructMembers" ):
                listener.exitParenStructMembers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenStructMembers" ):
                return visitor.visitParenStructMembers(self)
            else:
                return visitor.visitChildren(self)




    def parenStructMembers(self):

        localctx = CWScriptParser.ParenStructMembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_parenStructMembers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(CWScriptParser.LPAREN)
            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 519
                self.structMember()
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CWScriptParser.COMMA:
                    self.state = 520
                    self.match(CWScriptParser.COMMA)
                    self.state = 521
                    self.structMember()
                    self.state = 526
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 529
            self.match(CWScriptParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CurlyStructMembersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StructMemberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_curlyStructMembers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCurlyStructMembers" ):
                listener.enterCurlyStructMembers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCurlyStructMembers" ):
                listener.exitCurlyStructMembers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCurlyStructMembers" ):
                return visitor.visitCurlyStructMembers(self)
            else:
                return visitor.visitChildren(self)




    def curlyStructMembers(self):

        localctx = CWScriptParser.CurlyStructMembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_curlyStructMembers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(CWScriptParser.LBRACE)
            self.state = 543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.CWSPEC_LINE_COMMENT - 75)) | (1 << (CWScriptParser.CWSPEC_MULTI_COMMENT - 75)))) != 0):
                self.state = 532
                self.structMember()
                self.state = 537
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 533
                        self.match(CWScriptParser.COMMA)
                        self.state = 534
                        self.structMember() 
                    self.state = 539
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

                self.state = 541
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.COMMA:
                    self.state = 540
                    self.match(CWScriptParser.COMMA)




            self.state = 545
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.spec = None # CwspecContext
            self.name = None # IdentContext
            self.option = None # Token
            self.value = None # TypeExprContext

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def cwspec(self):
            return self.getTypedRuleContext(CWScriptParser.CwspecContext,0)


        def QUEST(self):
            return self.getToken(CWScriptParser.QUEST, 0)

        def getRuleIndex(self):
            return CWScriptParser.RULE_structMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructMember" ):
                listener.enterStructMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructMember" ):
                listener.exitStructMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructMember" ):
                return visitor.visitStructMember(self)
            else:
                return visitor.visitChildren(self)




    def structMember(self):

        localctx = CWScriptParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_structMember)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT:
                self.state = 547
                localctx.spec = self.cwspec()


            self.state = 550
            localctx.name = self.ident()
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.QUEST:
                self.state = 551
                localctx.option = self.match(CWScriptParser.QUEST)


            self.state = 554
            self.match(CWScriptParser.COLON)

            self.state = 555
            localctx.value = self.typeExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_typeExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RefTypeExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AMP(self):
            return self.getToken(CWScriptParser.AMP, 0)
        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefTypeExpr" ):
                listener.enterRefTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefTypeExpr" ):
                listener.exitRefTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefTypeExpr" ):
                return visitor.visitRefTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParamzdTypeExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TypeExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TypeExprContext,i)

        def LT(self):
            return self.getToken(CWScriptParser.LT, 0)
        def GT(self):
            return self.getToken(CWScriptParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamzdTypeExpr" ):
                listener.enterParamzdTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamzdTypeExpr" ):
                listener.exitParamzdTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamzdTypeExpr" ):
                return visitor.visitParamzdTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class AutoTypeExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNDERSCORE(self):
            return self.getToken(CWScriptParser.UNDERSCORE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAutoTypeExpr" ):
                listener.enterAutoTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAutoTypeExpr" ):
                listener.exitAutoTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAutoTypeExpr" ):
                return visitor.visitAutoTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class TupleTypeExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)
        def typeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TypeExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TypeExprContext,i)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleTypeExpr" ):
                listener.enterTupleTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleTypeExpr" ):
                listener.exitTupleTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupleTypeExpr" ):
                return visitor.visitTupleTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class ShortOptionTypeExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)

        def QUEST(self):
            return self.getToken(CWScriptParser.QUEST, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShortOptionTypeExpr" ):
                listener.enterShortOptionTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShortOptionTypeExpr" ):
                listener.exitShortOptionTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortOptionTypeExpr" ):
                return visitor.visitShortOptionTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class ReflectiveTypeExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR(self):
            return self.getToken(CWScriptParser.DOLLAR, 0)
        def reflectiveTypePath(self):
            return self.getTypedRuleContext(CWScriptParser.ReflectiveTypePathContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReflectiveTypeExpr" ):
                listener.enterReflectiveTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReflectiveTypeExpr" ):
                listener.exitReflectiveTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReflectiveTypeExpr" ):
                return visitor.visitReflectiveTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class TypeDefnExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeDefn(self):
            return self.getTypedRuleContext(CWScriptParser.TypeDefnContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDefnExpr" ):
                listener.enterTypeDefnExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDefnExpr" ):
                listener.exitTypeDefnExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDefnExpr" ):
                return visitor.visitTypeDefnExpr(self)
            else:
                return visitor.visitChildren(self)


    class TypePathExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typePath(self):
            return self.getTypedRuleContext(CWScriptParser.TypePathContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypePathExpr" ):
                listener.enterTypePathExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypePathExpr" ):
                listener.exitTypePathExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypePathExpr" ):
                return visitor.visitTypePathExpr(self)
            else:
                return visitor.visitChildren(self)


    class ShortVecTypeExprContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShortVecTypeExpr" ):
                listener.enterShortVecTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShortVecTypeExpr" ):
                listener.exitShortVecTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortVecTypeExpr" ):
                return visitor.visitShortVecTypeExpr(self)
            else:
                return visitor.visitChildren(self)



    def typeExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CWScriptParser.TypeExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_typeExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = CWScriptParser.TypePathExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 558
                self.typePath()
                pass

            elif la_ == 2:
                localctx = CWScriptParser.TupleTypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 559
                self.match(CWScriptParser.LPAREN)
                self.state = 560
                self.typeExpr(0)
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CWScriptParser.COMMA:
                    self.state = 561
                    self.match(CWScriptParser.COMMA)
                    self.state = 562
                    self.typeExpr(0)
                    self.state = 567
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 568
                self.match(CWScriptParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = CWScriptParser.RefTypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 570
                self.match(CWScriptParser.AMP)
                self.state = 571
                self.typeExpr(4)
                pass

            elif la_ == 4:
                localctx = CWScriptParser.ReflectiveTypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 572
                self.match(CWScriptParser.DOLLAR)
                self.state = 573
                self.reflectiveTypePath()
                pass

            elif la_ == 5:
                localctx = CWScriptParser.TypeDefnExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 574
                self.typeDefn()
                pass

            elif la_ == 6:
                localctx = CWScriptParser.AutoTypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 575
                self.match(CWScriptParser.UNDERSCORE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 588
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        localctx = CWScriptParser.ParamzdTypeExprContext(self, CWScriptParser.TypeExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typeExpr)
                        self.state = 578
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 579
                        self.match(CWScriptParser.LT)
                        self.state = 580
                        self.typeExpr(0)
                        self.state = 581
                        self.match(CWScriptParser.GT)
                        pass

                    elif la_ == 2:
                        localctx = CWScriptParser.ShortOptionTypeExprContext(self, CWScriptParser.TypeExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typeExpr)
                        self.state = 583
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 584
                        self.match(CWScriptParser.QUEST)
                        pass

                    elif la_ == 3:
                        localctx = CWScriptParser.ShortVecTypeExprContext(self, CWScriptParser.TypeExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typeExpr)
                        self.state = 585
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 586
                        self.match(CWScriptParser.LBRACK)
                        self.state = 587
                        self.match(CWScriptParser.RBRACK)
                        pass

             
                self.state = 592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypePathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pathPath = None # IdentContext
            self.pathPart = None # IdentContext

        def D_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.D_COLON)
            else:
                return self.getToken(CWScriptParser.D_COLON, i)

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_typePath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypePath" ):
                listener.enterTypePath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypePath" ):
                listener.exitTypePath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypePath" ):
                return visitor.visitTypePath(self)
            else:
                return visitor.visitChildren(self)




    def typePath(self):

        localctx = CWScriptParser.TypePathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_typePath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.D_COLON:
                self.state = 593
                self.match(CWScriptParser.D_COLON)


            self.state = 596
            localctx.pathPath = self.ident()
            self.state = 601
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 597
                    self.match(CWScriptParser.D_COLON)
                    self.state = 598
                    localctx.pathPart = self.ident() 
                self.state = 603
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReflectiveTypePathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pathBase = None # InterfaceValContext
            self.pathPart = None # IdentContext

        def interfaceVal(self):
            return self.getTypedRuleContext(CWScriptParser.InterfaceValContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.DOT)
            else:
                return self.getToken(CWScriptParser.DOT, i)

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_reflectiveTypePath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReflectiveTypePath" ):
                listener.enterReflectiveTypePath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReflectiveTypePath" ):
                listener.exitReflectiveTypePath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReflectiveTypePath" ):
                return visitor.visitReflectiveTypePath(self)
            else:
                return visitor.visitChildren(self)




    def reflectiveTypePath(self):

        localctx = CWScriptParser.ReflectiveTypePathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_reflectiveTypePath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            localctx.pathBase = self.interfaceVal()
            self.state = 609
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 605
                    self.match(CWScriptParser.DOT)
                    self.state = 606
                    localctx.pathPart = self.ident() 
                self.state = 611
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def autoStructDefn(self):
            return self.getTypedRuleContext(CWScriptParser.AutoStructDefnContext,0)


        def structDefn(self):
            return self.getTypedRuleContext(CWScriptParser.StructDefnContext,0)


        def enumDefn(self):
            return self.getTypedRuleContext(CWScriptParser.EnumDefnContext,0)


        def typeAliasDefn(self):
            return self.getTypedRuleContext(CWScriptParser.TypeAliasDefnContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_typeDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDefn" ):
                listener.enterTypeDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDefn" ):
                listener.exitTypeDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDefn" ):
                return visitor.visitTypeDefn(self)
            else:
                return visitor.visitChildren(self)




    def typeDefn(self):

        localctx = CWScriptParser.TypeDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_typeDefn)
        try:
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 612
                self.autoStructDefn()
                pass
            elif token in [CWScriptParser.STRUCT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 613
                self.structDefn()
                pass
            elif token in [CWScriptParser.ENUM]:
                self.enterOuterAlt(localctx, 3)
                self.state = 614
                self.enumDefn()
                pass
            elif token in [CWScriptParser.TYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 615
                self.typeAliasDefn()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutoStructDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(CWScriptParser.AT, 0)

        def curlyStructMembers(self):
            return self.getTypedRuleContext(CWScriptParser.CurlyStructMembersContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_autoStructDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAutoStructDefn" ):
                listener.enterAutoStructDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAutoStructDefn" ):
                listener.exitAutoStructDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAutoStructDefn" ):
                return visitor.visitAutoStructDefn(self)
            else:
                return visitor.visitChildren(self)




    def autoStructDefn(self):

        localctx = CWScriptParser.AutoStructDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_autoStructDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.match(CWScriptParser.AT)
            self.state = 619
            self.curlyStructMembers()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(CWScriptParser.STRUCT, 0)

        def enumVariant(self):
            return self.getTypedRuleContext(CWScriptParser.EnumVariantContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_structDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDefn" ):
                listener.enterStructDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDefn" ):
                listener.exitStructDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefn" ):
                return visitor.visitStructDefn(self)
            else:
                return visitor.visitChildren(self)




    def structDefn(self):

        localctx = CWScriptParser.StructDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_structDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(CWScriptParser.STRUCT)
            self.state = 622
            self.enumVariant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(CWScriptParser.ENUM, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def enumVariant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.EnumVariantContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.EnumVariantContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_enumDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDefn" ):
                listener.enterEnumDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDefn" ):
                listener.exitEnumDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDefn" ):
                return visitor.visitEnumDefn(self)
            else:
                return visitor.visitChildren(self)




    def enumDefn(self):

        localctx = CWScriptParser.EnumDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_enumDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(CWScriptParser.ENUM)
            self.state = 625
            self.ident()
            self.state = 626
            self.match(CWScriptParser.LBRACE)
            self.state = 640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT) | (1 << CWScriptParser.AT))) != 0) or _la==CWScriptParser.Ident:
                self.state = 627
                self.enumVariant()
                self.state = 634
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 629
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CWScriptParser.COMMA:
                            self.state = 628
                            self.match(CWScriptParser.COMMA)


                        self.state = 631
                        self.enumVariant() 
                    self.state = 636
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

                self.state = 638
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.COMMA:
                    self.state = 637
                    self.match(CWScriptParser.COMMA)




            self.state = 642
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeAliasDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(CWScriptParser.TYPE, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def EQ(self):
            return self.getToken(CWScriptParser.EQ, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_typeAliasDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAliasDefn" ):
                listener.enterTypeAliasDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAliasDefn" ):
                listener.exitTypeAliasDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAliasDefn" ):
                return visitor.visitTypeAliasDefn(self)
            else:
                return visitor.visitChildren(self)




    def typeAliasDefn(self):

        localctx = CWScriptParser.TypeAliasDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_typeAliasDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self.match(CWScriptParser.TYPE)
            self.state = 645
            self.ident()
            self.state = 646
            self.match(CWScriptParser.EQ)
            self.state = 647
            self.typeExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedFnDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fnName = None # IdentContext

        def fnArgs(self):
            return self.getTypedRuleContext(CWScriptParser.FnArgsContext,0)


        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def fnType(self):
            return self.getTypedRuleContext(CWScriptParser.FnTypeContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_namedFnDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedFnDecl" ):
                listener.enterNamedFnDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedFnDecl" ):
                listener.exitNamedFnDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedFnDecl" ):
                return visitor.visitNamedFnDecl(self)
            else:
                return visitor.visitChildren(self)




    def namedFnDecl(self):

        localctx = CWScriptParser.NamedFnDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_namedFnDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            localctx.fnName = self.ident()
            self.state = 650
            self.fnArgs()
            self.state = 652
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.ARROW:
                self.state = 651
                self.fnType()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedFnDefnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fnName = None # IdentContext

        def fnArgs(self):
            return self.getTypedRuleContext(CWScriptParser.FnArgsContext,0)


        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def fnType(self):
            return self.getTypedRuleContext(CWScriptParser.FnTypeContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_namedFnDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedFnDefn" ):
                listener.enterNamedFnDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedFnDefn" ):
                listener.exitNamedFnDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedFnDefn" ):
                return visitor.visitNamedFnDefn(self)
            else:
                return visitor.visitChildren(self)




    def namedFnDefn(self):

        localctx = CWScriptParser.NamedFnDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_namedFnDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            localctx.fnName = self.ident()
            self.state = 655
            self.fnArgs()
            self.state = 657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.ARROW:
                self.state = 656
                self.fnType()


            self.state = 659
            self.fnBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.retType = None # TypeExprContext

        def ARROW(self):
            return self.getToken(CWScriptParser.ARROW, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_fnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnType" ):
                listener.enterFnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnType" ):
                listener.exitFnType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnType" ):
                return visitor.visitFnType(self)
            else:
                return visitor.visitChildren(self)




    def fnType(self):

        localctx = CWScriptParser.FnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_fnType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(CWScriptParser.ARROW)
            self.state = 662
            localctx.retType = self.typeExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def fnArgList(self):
            return self.getTypedRuleContext(CWScriptParser.FnArgListContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_fnArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnArgs" ):
                listener.enterFnArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnArgs" ):
                listener.exitFnArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnArgs" ):
                return visitor.visitFnArgs(self)
            else:
                return visitor.visitChildren(self)




    def fnArgs(self):

        localctx = CWScriptParser.FnArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_fnArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.match(CWScriptParser.LPAREN)
            self.state = 666
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or _la==CWScriptParser.Ident:
                self.state = 665
                self.fnArgList()


            self.state = 668
            self.match(CWScriptParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnArgListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fnArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.FnArgContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.FnArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_fnArgList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnArgList" ):
                listener.enterFnArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnArgList" ):
                listener.exitFnArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnArgList" ):
                return visitor.visitFnArgList(self)
            else:
                return visitor.visitChildren(self)




    def fnArgList(self):

        localctx = CWScriptParser.FnArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_fnArgList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self.fnArg()
            self.state = 675
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CWScriptParser.COMMA:
                self.state = 671
                self.match(CWScriptParser.COMMA)
                self.state = 672
                self.fnArg()
                self.state = 677
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def QUEST(self):
            return self.getToken(CWScriptParser.QUEST, 0)

        def fnArgChecks(self):
            return self.getTypedRuleContext(CWScriptParser.FnArgChecksContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_fnArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnArg" ):
                listener.enterFnArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnArg" ):
                listener.exitFnArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnArg" ):
                return visitor.visitFnArg(self)
            else:
                return visitor.visitChildren(self)




    def fnArg(self):

        localctx = CWScriptParser.FnArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_fnArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.ident()
            self.state = 680
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.QUEST:
                self.state = 679
                self.match(CWScriptParser.QUEST)


            self.state = 682
            self.match(CWScriptParser.COLON)
            self.state = 683
            self.typeExpr(0)
            self.state = 685
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.HASH:
                self.state = 684
                self.fnArgChecks()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnArgChecksContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.HASH)
            else:
                return self.getToken(CWScriptParser.HASH, i)

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.LPAREN)
            else:
                return self.getToken(CWScriptParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.RPAREN)
            else:
                return self.getToken(CWScriptParser.RPAREN, i)

        def exprList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprListContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprListContext,i)


        def namedExprList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.NamedExprListContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.NamedExprListContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_fnArgChecks

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnArgChecks" ):
                listener.enterFnArgChecks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnArgChecks" ):
                listener.exitFnArgChecks(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnArgChecks" ):
                return visitor.visitFnArgChecks(self)
            else:
                return visitor.visitChildren(self)




    def fnArgChecks(self):

        localctx = CWScriptParser.FnArgChecksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_fnArgChecks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 687
                self.match(CWScriptParser.HASH)
                self.state = 697
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
                if la_ == 1:
                    self.state = 688
                    self.ident()
                    pass

                elif la_ == 2:
                    self.state = 689
                    self.ident()
                    self.state = 690
                    self.match(CWScriptParser.LPAREN)
                    self.state = 693
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                    if la_ == 1:
                        self.state = 691
                        self.exprList()
                        pass

                    elif la_ == 2:
                        self.state = 692
                        self.namedExprList()
                        pass


                    self.state = 695
                    self.match(CWScriptParser.RPAREN)
                    pass


                self.state = 701 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CWScriptParser.HASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_fnBody

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NormalFnBodyContext(FnBodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.FnBodyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StmtContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalFnBody" ):
                listener.enterNormalFnBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalFnBody" ):
                listener.exitNormalFnBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalFnBody" ):
                return visitor.visitNormalFnBody(self)
            else:
                return visitor.visitChildren(self)


    class ArrowFnBodyContext(FnBodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.FnBodyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FAT_ARROW(self):
            return self.getToken(CWScriptParser.FAT_ARROW, 0)
        def stmt(self):
            return self.getTypedRuleContext(CWScriptParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrowFnBody" ):
                listener.enterArrowFnBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrowFnBody" ):
                listener.exitArrowFnBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrowFnBody" ):
                return visitor.visitArrowFnBody(self)
            else:
                return visitor.visitChildren(self)



    def fnBody(self):

        localctx = CWScriptParser.FnBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_fnBody)
        self._la = 0 # Token type
        try:
            self.state = 713
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.LBRACE]:
                localctx = CWScriptParser.NormalFnBodyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 703
                self.match(CWScriptParser.LBRACE)
                self.state = 707
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.FAIL) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT) | (1 << CWScriptParser.LPAREN) | (1 << CWScriptParser.LBRACK) | (1 << CWScriptParser.EXCLAM) | (1 << CWScriptParser.D_COLON) | (1 << CWScriptParser.AT) | (1 << CWScriptParser.PLUS) | (1 << CWScriptParser.MINUS))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CWScriptParser.Ident - 75)) | (1 << (CWScriptParser.StringLiteral - 75)) | (1 << (CWScriptParser.IntegerLiteral - 75)) | (1 << (CWScriptParser.DecimalLiteral - 75)))) != 0):
                    self.state = 704
                    self.stmt()
                    self.state = 709
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 710
                self.match(CWScriptParser.RBRACE)
                pass
            elif token in [CWScriptParser.FAT_ARROW]:
                localctx = CWScriptParser.ArrowFnBodyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 711
                self.match(CWScriptParser.FAT_ARROW)
                self.state = 712
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FailStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FAIL(self):
            return self.getToken(CWScriptParser.FAIL, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFailStmt" ):
                listener.enterFailStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFailStmt" ):
                listener.exitFailStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFailStmt" ):
                return visitor.visitFailStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifExpr_(self):
            return self.getTypedRuleContext(CWScriptParser.IfExpr_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class EmitStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EMIT(self):
            return self.getToken(CWScriptParser.EMIT, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmitStmt" ):
                listener.enterEmitStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmitStmt" ):
                listener.exitEmitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmitStmt" ):
                return visitor.visitEmitStmt(self)
            else:
                return visitor.visitChildren(self)


    class ExprStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def EQ(self):
            return self.getToken(CWScriptParser.EQ, 0)
        def PLUS_EQ(self):
            return self.getToken(CWScriptParser.PLUS_EQ, 0)
        def MINUS_EQ(self):
            return self.getToken(CWScriptParser.MINUS_EQ, 0)
        def MUL_EQ(self):
            return self.getToken(CWScriptParser.MUL_EQ, 0)
        def DIV_EQ(self):
            return self.getToken(CWScriptParser.DIV_EQ, 0)
        def MOD_EQ(self):
            return self.getToken(CWScriptParser.MOD_EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class ExecStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecStmt" ):
                listener.enterExecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecStmt" ):
                listener.exitExecStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecStmt" ):
                return visitor.visitExecStmt(self)
            else:
                return visitor.visitChildren(self)


    class ForStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def forStmt_(self):
            return self.getTypedRuleContext(CWScriptParser.ForStmt_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(CWScriptParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)


    class LetStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def letStmt_(self):
            return self.getTypedRuleContext(CWScriptParser.LetStmt_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStmt" ):
                listener.enterLetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStmt" ):
                listener.exitLetStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStmt" ):
                return visitor.visitLetStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = CWScriptParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 731
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                localctx = CWScriptParser.LetStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 715
                self.letStmt_()
                pass

            elif la_ == 2:
                localctx = CWScriptParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 716
                self.expr(0)
                self.state = 717
                _la = self._input.LA(1)
                if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (CWScriptParser.EQ - 57)) | (1 << (CWScriptParser.PLUS_EQ - 57)) | (1 << (CWScriptParser.MINUS_EQ - 57)) | (1 << (CWScriptParser.MUL_EQ - 57)) | (1 << (CWScriptParser.DIV_EQ - 57)) | (1 << (CWScriptParser.MOD_EQ - 57)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 718
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = CWScriptParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 720
                self.ifExpr_()
                pass

            elif la_ == 4:
                localctx = CWScriptParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 721
                self.forStmt_()
                pass

            elif la_ == 5:
                localctx = CWScriptParser.ExecStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 722
                self.match(CWScriptParser.EXEC)
                self.state = 723
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = CWScriptParser.EmitStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 724
                self.match(CWScriptParser.EMIT)
                self.state = 725
                self.expr(0)
                pass

            elif la_ == 7:
                localctx = CWScriptParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 726
                self.match(CWScriptParser.RETURN)
                self.state = 727
                self.expr(0)
                pass

            elif la_ == 8:
                localctx = CWScriptParser.FailStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 728
                self.match(CWScriptParser.FAIL)
                self.state = 729
                self.expr(0)
                pass

            elif la_ == 9:
                localctx = CWScriptParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 730
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStmt_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CWScriptParser.LET, 0)

        def letLHS(self):
            return self.getTypedRuleContext(CWScriptParser.LetLHSContext,0)


        def EQ(self):
            return self.getToken(CWScriptParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_letStmt_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStmt_" ):
                listener.enterLetStmt_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStmt_" ):
                listener.exitLetStmt_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStmt_" ):
                return visitor.visitLetStmt_(self)
            else:
                return visitor.visitChildren(self)




    def letStmt_(self):

        localctx = CWScriptParser.LetStmt_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_letStmt_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 733
            self.match(CWScriptParser.LET)
            self.state = 734
            self.letLHS()
            self.state = 735
            self.match(CWScriptParser.EQ)
            self.state = 736
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetLHSContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def identList(self):
            return self.getTypedRuleContext(CWScriptParser.IdentListContext,0)


        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def getRuleIndex(self):
            return CWScriptParser.RULE_letLHS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetLHS" ):
                listener.enterLetLHS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetLHS" ):
                listener.exitLetLHS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetLHS" ):
                return visitor.visitLetLHS(self)
            else:
                return visitor.visitChildren(self)




    def letLHS(self):

        localctx = CWScriptParser.LetLHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_letLHS)
        self._la = 0 # Token type
        try:
            self.state = 747
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.CONTRACT, CWScriptParser.INTERFACE, CWScriptParser.IMPORT, CWScriptParser.IMPLEMENTS, CWScriptParser.IMPL, CWScriptParser.EXTENSION, CWScriptParser.EXTENDS, CWScriptParser.ERROR, CWScriptParser.EVENT, CWScriptParser.INSTANTIATE, CWScriptParser.EXEC, CWScriptParser.QUERY, CWScriptParser.MIGRATE, CWScriptParser.FOR, CWScriptParser.IN, CWScriptParser.FROM, CWScriptParser.STATE, CWScriptParser.TIMES, CWScriptParser.IF, CWScriptParser.ELSE, CWScriptParser.AND, CWScriptParser.OR, CWScriptParser.TRUE, CWScriptParser.FALSE, CWScriptParser.LET, CWScriptParser.RETURN, CWScriptParser.STRUCT, CWScriptParser.ENUM, CWScriptParser.TYPE, CWScriptParser.EMIT, CWScriptParser.Ident]:
                self.enterOuterAlt(localctx, 1)
                self.state = 738
                self.ident()
                self.state = 741
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CWScriptParser.COLON:
                    self.state = 739
                    self.match(CWScriptParser.COLON)
                    self.state = 740
                    self.typeExpr(0)


                pass
            elif token in [CWScriptParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 743
                self.match(CWScriptParser.LBRACE)
                self.state = 744
                self.identList()
                self.state = 745
                self.match(CWScriptParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def AND(self):
            return self.getToken(CWScriptParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultDivModExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def MUL(self):
            return self.getToken(CWScriptParser.MUL, 0)
        def DIV(self):
            return self.getToken(CWScriptParser.DIV, 0)
        def MOD(self):
            return self.getToken(CWScriptParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDivModExpr" ):
                listener.enterMultDivModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDivModExpr" ):
                listener.exitMultDivModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDivModExpr" ):
                return visitor.visitMultDivModExpr(self)
            else:
                return visitor.visitChildren(self)


    class QueryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryExpr" ):
                listener.enterQueryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryExpr" ):
                listener.exitQueryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryExpr" ):
                return visitor.visitQueryExpr(self)
            else:
                return visitor.visitChildren(self)


    class ValExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def val(self):
            return self.getTypedRuleContext(CWScriptParser.ValContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValExpr" ):
                listener.enterValExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValExpr" ):
                listener.exitValExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValExpr" ):
                return visitor.visitValExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryNotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXCLAM(self):
            return self.getToken(CWScriptParser.EXCLAM, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryNotExpr" ):
                listener.enterUnaryNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryNotExpr" ):
                listener.exitUnaryNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryNotExpr" ):
                return visitor.visitUnaryNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def LT(self):
            return self.getToken(CWScriptParser.LT, 0)
        def GT(self):
            return self.getToken(CWScriptParser.GT, 0)
        def LT_EQ(self):
            return self.getToken(CWScriptParser.LT_EQ, 0)
        def GT_EQ(self):
            return self.getToken(CWScriptParser.GT_EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompExpr" ):
                listener.enterCompExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompExpr" ):
                listener.exitCompExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompExpr" ):
                return visitor.visitCompExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnarySignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def PLUS(self):
            return self.getToken(CWScriptParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CWScriptParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnarySignExpr" ):
                listener.enterUnarySignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnarySignExpr" ):
                listener.exitUnarySignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnarySignExpr" ):
                return visitor.visitUnarySignExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExpExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def POW(self):
            return self.getToken(CWScriptParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpExpr" ):
                listener.enterExpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpExpr" ):
                listener.exitExpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpExpr" ):
                return visitor.visitExpExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def OR(self):
            return self.getToken(CWScriptParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class IfExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifExpr_(self):
            return self.getTypedRuleContext(CWScriptParser.IfExpr_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExp" ):
                listener.enterIfExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExp" ):
                listener.exitIfExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExp" ):
                return visitor.visitIfExp(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def EQEQ(self):
            return self.getToken(CWScriptParser.EQEQ, 0)
        def NEQ(self):
            return self.getToken(CWScriptParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class TableLookupExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableLookupExpr" ):
                listener.enterTableLookupExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableLookupExpr" ):
                listener.exitTableLookupExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableLookupExpr" ):
                return visitor.visitTableLookupExpr(self)
            else:
                return visitor.visitChildren(self)


    class MemberAccessExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def DOT(self):
            return self.getToken(CWScriptParser.DOT, 0)
        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccessExpr" ):
                listener.enterMemberAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccessExpr" ):
                listener.exitMemberAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccessExpr" ):
                return visitor.visitMemberAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(CWScriptParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CWScriptParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class FnCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(CWScriptParser.ExprListContext,0)

        def namedExprList(self):
            return self.getTypedRuleContext(CWScriptParser.NamedExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnCallExpr" ):
                listener.enterFnCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnCallExpr" ):
                listener.exitFnCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnCallExpr" ):
                return visitor.visitFnCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class GroupedExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupedExpr" ):
                listener.enterGroupedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupedExpr" ):
                listener.exitGroupedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupedExpr" ):
                return visitor.visitGroupedExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CWScriptParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                localctx = CWScriptParser.GroupedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 750
                self.match(CWScriptParser.LPAREN)
                self.state = 751
                self.expr(0)
                self.state = 752
                self.match(CWScriptParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = CWScriptParser.UnarySignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 754
                _la = self._input.LA(1)
                if not(_la==CWScriptParser.PLUS or _la==CWScriptParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 755
                self.expr(12)
                pass

            elif la_ == 3:
                localctx = CWScriptParser.UnaryNotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 756
                self.match(CWScriptParser.EXCLAM)
                self.state = 757
                self.expr(11)
                pass

            elif la_ == 4:
                localctx = CWScriptParser.IfExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 758
                self.ifExpr_()
                pass

            elif la_ == 5:
                localctx = CWScriptParser.QueryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 759
                self.match(CWScriptParser.QUERY)
                self.state = 760
                self.expr(2)
                pass

            elif la_ == 6:
                localctx = CWScriptParser.ValExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 761
                self.val()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 802
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,90,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 800
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
                    if la_ == 1:
                        localctx = CWScriptParser.ExpExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 764
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 765
                        self.match(CWScriptParser.POW)
                        self.state = 766
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = CWScriptParser.MultDivModExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 767
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 768
                        _la = self._input.LA(1)
                        if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CWScriptParser.MUL - 64)) | (1 << (CWScriptParser.DIV - 64)) | (1 << (CWScriptParser.MOD - 64)))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 769
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = CWScriptParser.AddSubExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 770
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 771
                        _la = self._input.LA(1)
                        if not(_la==CWScriptParser.PLUS or _la==CWScriptParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 772
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = CWScriptParser.CompExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 773
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 774
                        _la = self._input.LA(1)
                        if not(((((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & ((1 << (CWScriptParser.LT - 70)) | (1 << (CWScriptParser.LT_EQ - 70)) | (1 << (CWScriptParser.GT - 70)) | (1 << (CWScriptParser.GT_EQ - 70)))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 775
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = CWScriptParser.EqExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 776
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 777
                        _la = self._input.LA(1)
                        if not(_la==CWScriptParser.EQEQ or _la==CWScriptParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 778
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = CWScriptParser.AndExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 779
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 780
                        self.match(CWScriptParser.AND)
                        self.state = 781
                        self.expr(6)
                        pass

                    elif la_ == 7:
                        localctx = CWScriptParser.OrExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 782
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 783
                        self.match(CWScriptParser.OR)
                        self.state = 784
                        self.expr(5)
                        pass

                    elif la_ == 8:
                        localctx = CWScriptParser.MemberAccessExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 785
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 786
                        self.match(CWScriptParser.DOT)
                        self.state = 787
                        self.ident()
                        pass

                    elif la_ == 9:
                        localctx = CWScriptParser.TableLookupExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 788
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 789
                        self.match(CWScriptParser.LBRACK)
                        self.state = 790
                        self.expr(0)
                        self.state = 791
                        self.match(CWScriptParser.RBRACK)
                        pass

                    elif la_ == 10:
                        localctx = CWScriptParser.FnCallExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 793
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 794
                        self.match(CWScriptParser.LPAREN)
                        self.state = 797
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
                        if la_ == 1:
                            self.state = 795
                            self.exprList()

                        elif la_ == 2:
                            self.state = 796
                            self.namedExprList()


                        self.state = 799
                        self.match(CWScriptParser.RPAREN)
                        pass

             
                self.state = 804
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,90,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_val

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TupleStructValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(CWScriptParser.ExprListContext,0)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleStructVal" ):
                listener.enterTupleStructVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleStructVal" ):
                listener.exitTupleStructVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupleStructVal" ):
                return visitor.visitTupleStructVal(self)
            else:
                return visitor.visitChildren(self)


    class TrueValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(CWScriptParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueVal" ):
                listener.enterTrueVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueVal" ):
                listener.exitTrueVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueVal" ):
                return visitor.visitTrueVal(self)
            else:
                return visitor.visitChildren(self)


    class StructValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def structVal_(self):
            return self.getTypedRuleContext(CWScriptParser.StructVal_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructVal" ):
                listener.enterStructVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructVal" ):
                listener.exitStructVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructVal" ):
                return visitor.visitStructVal(self)
            else:
                return visitor.visitChildren(self)


    class VecValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)
        def exprList(self):
            return self.getTypedRuleContext(CWScriptParser.ExprListContext,0)

        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVecVal" ):
                listener.enterVecVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVecVal" ):
                listener.exitVecVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVecVal" ):
                return visitor.visitVecVal(self)
            else:
                return visitor.visitChildren(self)


    class FalseValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(CWScriptParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseVal" ):
                listener.enterFalseVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseVal" ):
                listener.exitFalseVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseVal" ):
                return visitor.visitFalseVal(self)
            else:
                return visitor.visitChildren(self)


    class IdentValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentVal" ):
                listener.enterIdentVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentVal" ):
                listener.exitIdentVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentVal" ):
                return visitor.visitIdentVal(self)
            else:
                return visitor.visitChildren(self)


    class UnitValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnitVal" ):
                listener.enterUnitVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnitVal" ):
                listener.exitUnitVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitVal" ):
                return visitor.visitUnitVal(self)
            else:
                return visitor.visitChildren(self)


    class StringValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def StringLiteral(self):
            return self.getToken(CWScriptParser.StringLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringVal" ):
                listener.enterStringVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringVal" ):
                listener.exitStringVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringVal" ):
                return visitor.visitStringVal(self)
            else:
                return visitor.visitChildren(self)


    class IntegerValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IntegerLiteral(self):
            return self.getToken(CWScriptParser.IntegerLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerVal" ):
                listener.enterIntegerVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerVal" ):
                listener.exitIntegerVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerVal" ):
                return visitor.visitIntegerVal(self)
            else:
                return visitor.visitChildren(self)


    class DecimalValContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DecimalLiteral(self):
            return self.getToken(CWScriptParser.DecimalLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalVal" ):
                listener.enterDecimalVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalVal" ):
                listener.exitDecimalVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalVal" ):
                return visitor.visitDecimalVal(self)
            else:
                return visitor.visitChildren(self)



    def val(self):

        localctx = CWScriptParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_val)
        try:
            self.state = 822
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                localctx = CWScriptParser.UnitValContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 805
                self.match(CWScriptParser.LPAREN)
                self.state = 806
                self.match(CWScriptParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = CWScriptParser.StructValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 807
                self.structVal_()
                pass

            elif la_ == 3:
                localctx = CWScriptParser.TupleStructValContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 808
                self.match(CWScriptParser.LPAREN)
                self.state = 809
                self.exprList()
                self.state = 810
                self.match(CWScriptParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = CWScriptParser.VecValContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 812
                self.match(CWScriptParser.LBRACK)
                self.state = 813
                self.exprList()
                self.state = 814
                self.match(CWScriptParser.RBRACK)
                pass

            elif la_ == 5:
                localctx = CWScriptParser.StringValContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 816
                self.match(CWScriptParser.StringLiteral)
                pass

            elif la_ == 6:
                localctx = CWScriptParser.IntegerValContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 817
                self.match(CWScriptParser.IntegerLiteral)
                pass

            elif la_ == 7:
                localctx = CWScriptParser.DecimalValContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 818
                self.match(CWScriptParser.DecimalLiteral)
                pass

            elif la_ == 8:
                localctx = CWScriptParser.TrueValContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 819
                self.match(CWScriptParser.TRUE)
                pass

            elif la_ == 9:
                localctx = CWScriptParser.FalseValContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 820
                self.match(CWScriptParser.FALSE)
                pass

            elif la_ == 10:
                localctx = CWScriptParser.IdentValContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 821
                self.ident()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructVal_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.structType_ = None # TypePathContext
            self.members = None # StructValMembersContext

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def AT(self):
            return self.getToken(CWScriptParser.AT, 0)

        def structValMembers(self):
            return self.getTypedRuleContext(CWScriptParser.StructValMembersContext,0)


        def typePath(self):
            return self.getTypedRuleContext(CWScriptParser.TypePathContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_structVal_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructVal_" ):
                listener.enterStructVal_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructVal_" ):
                listener.exitStructVal_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructVal_" ):
                return visitor.visitStructVal_(self)
            else:
                return visitor.visitChildren(self)




    def structVal_(self):

        localctx = CWScriptParser.StructVal_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_structVal_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 826
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.CONTRACT, CWScriptParser.INTERFACE, CWScriptParser.IMPORT, CWScriptParser.IMPLEMENTS, CWScriptParser.IMPL, CWScriptParser.EXTENSION, CWScriptParser.EXTENDS, CWScriptParser.ERROR, CWScriptParser.EVENT, CWScriptParser.INSTANTIATE, CWScriptParser.EXEC, CWScriptParser.QUERY, CWScriptParser.MIGRATE, CWScriptParser.FOR, CWScriptParser.IN, CWScriptParser.FROM, CWScriptParser.STATE, CWScriptParser.TIMES, CWScriptParser.IF, CWScriptParser.ELSE, CWScriptParser.AND, CWScriptParser.OR, CWScriptParser.TRUE, CWScriptParser.FALSE, CWScriptParser.LET, CWScriptParser.RETURN, CWScriptParser.STRUCT, CWScriptParser.ENUM, CWScriptParser.TYPE, CWScriptParser.EMIT, CWScriptParser.D_COLON, CWScriptParser.Ident]:
                self.state = 824
                localctx.structType_ = self.typePath()
                pass
            elif token in [CWScriptParser.AT]:
                self.state = 825
                self.match(CWScriptParser.AT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 828
            self.match(CWScriptParser.LBRACE)
            self.state = 830
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0) or _la==CWScriptParser.Ident:
                self.state = 829
                localctx.members = self.structValMembers()


            self.state = 832
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructValMembersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structValMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StructValMemberContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StructValMemberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_structValMembers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructValMembers" ):
                listener.enterStructValMembers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructValMembers" ):
                listener.exitStructValMembers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructValMembers" ):
                return visitor.visitStructValMembers(self)
            else:
                return visitor.visitChildren(self)




    def structValMembers(self):

        localctx = CWScriptParser.StructValMembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_structValMembers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 834
            self.structValMember()
            self.state = 839
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 835
                    self.match(CWScriptParser.COMMA)
                    self.state = 836
                    self.structValMember() 
                self.state = 841
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

            self.state = 843
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CWScriptParser.COMMA:
                self.state = 842
                self.match(CWScriptParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructValMemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext
            self.value = None # ExprContext

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_structValMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructValMember" ):
                listener.enterStructValMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructValMember" ):
                listener.exitStructValMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructValMember" ):
                return visitor.visitStructValMember(self)
            else:
                return visitor.visitChildren(self)




    def structValMember(self):

        localctx = CWScriptParser.StructValMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_structValMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 845
            localctx.name = self.ident()
            self.state = 846
            self.match(CWScriptParser.COLON)
            self.state = 847
            localctx.value = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExpr_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifClause_(self):
            return self.getTypedRuleContext(CWScriptParser.IfClause_Context,0)


        def elseIfClauses(self):
            return self.getTypedRuleContext(CWScriptParser.ElseIfClausesContext,0)


        def elseClause(self):
            return self.getTypedRuleContext(CWScriptParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_ifExpr_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr_" ):
                listener.enterIfExpr_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr_" ):
                listener.exitIfExpr_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr_" ):
                return visitor.visitIfExpr_(self)
            else:
                return visitor.visitChildren(self)




    def ifExpr_(self):

        localctx = CWScriptParser.IfExpr_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_ifExpr_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 849
            self.ifClause_()
            self.state = 851
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.state = 850
                self.elseIfClauses()


            self.state = 854
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.state = 853
                self.elseClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfClause_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_ifClause_

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfLetClauseContext(IfClause_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.IfClause_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(CWScriptParser.IF, 0)
        def letStmt_(self):
            return self.getTypedRuleContext(CWScriptParser.LetStmt_Context,0)

        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfLetClause" ):
                listener.enterIfLetClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfLetClause" ):
                listener.exitIfLetClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfLetClause" ):
                return visitor.visitIfLetClause(self)
            else:
                return visitor.visitChildren(self)


    class IfClauseContext(IfClause_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.IfClause_Context
            super().__init__(parser)
            self.predicate = None # ExprContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(CWScriptParser.IF, 0)
        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfClause" ):
                listener.enterIfClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfClause" ):
                listener.exitIfClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfClause" ):
                return visitor.visitIfClause(self)
            else:
                return visitor.visitChildren(self)



    def ifClause_(self):

        localctx = CWScriptParser.IfClause_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_ifClause_)
        try:
            self.state = 864
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                localctx = CWScriptParser.IfClauseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 856
                self.match(CWScriptParser.IF)
                self.state = 857
                localctx.predicate = self.expr(0)
                self.state = 858
                self.fnBody()
                pass

            elif la_ == 2:
                localctx = CWScriptParser.IfLetClauseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 860
                self.match(CWScriptParser.IF)
                self.state = 861
                self.letStmt_()
                self.state = 862
                self.fnBody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfClausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.ELSE)
            else:
                return self.getToken(CWScriptParser.ELSE, i)

        def ifClause_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IfClause_Context)
            else:
                return self.getTypedRuleContext(CWScriptParser.IfClause_Context,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_elseIfClauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfClauses" ):
                listener.enterElseIfClauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfClauses" ):
                listener.exitElseIfClauses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfClauses" ):
                return visitor.visitElseIfClauses(self)
            else:
                return visitor.visitChildren(self)




    def elseIfClauses(self):

        localctx = CWScriptParser.ElseIfClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_elseIfClauses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 868 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 866
                    self.match(CWScriptParser.ELSE)
                    self.state = 867
                    self.ifClause_()

                else:
                    raise NoViableAltException(self)
                self.state = 870 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,99,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CWScriptParser.ELSE, 0)

        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_elseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseClause" ):
                listener.enterElseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseClause" ):
                listener.exitElseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseClause" ):
                return visitor.visitElseClause(self)
            else:
                return visitor.visitChildren(self)




    def elseClause(self):

        localctx = CWScriptParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 872
            self.match(CWScriptParser.ELSE)
            self.state = 873
            self.fnBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmt_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_forStmt_

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForInStmtContext(ForStmt_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ForStmt_Context
            super().__init__(parser)
            self.item = None # ForItemContext
            self.iterable = None # ExprContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(CWScriptParser.FOR, 0)
        def IN(self):
            return self.getToken(CWScriptParser.IN, 0)
        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)

        def forItem(self):
            return self.getTypedRuleContext(CWScriptParser.ForItemContext,0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInStmt" ):
                listener.enterForInStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInStmt" ):
                listener.exitForInStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInStmt" ):
                return visitor.visitForInStmt(self)
            else:
                return visitor.visitChildren(self)


    class ForTimesStmtContext(ForStmt_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ForStmt_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(CWScriptParser.FOR, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def TIMES(self):
            return self.getToken(CWScriptParser.TIMES, 0)
        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForTimesStmt" ):
                listener.enterForTimesStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForTimesStmt" ):
                listener.exitForTimesStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForTimesStmt" ):
                return visitor.visitForTimesStmt(self)
            else:
                return visitor.visitChildren(self)



    def forStmt_(self):

        localctx = CWScriptParser.ForStmt_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_forStmt_)
        try:
            self.state = 886
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                localctx = CWScriptParser.ForInStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 875
                self.match(CWScriptParser.FOR)
                self.state = 876
                localctx.item = self.forItem()
                self.state = 877
                self.match(CWScriptParser.IN)
                self.state = 878
                localctx.iterable = self.expr(0)
                self.state = 879
                self.fnBody()
                pass

            elif la_ == 2:
                localctx = CWScriptParser.ForTimesStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 881
                self.match(CWScriptParser.FOR)
                self.state = 882
                self.expr(0)
                self.state = 883
                self.match(CWScriptParser.TIMES)
                self.state = 884
                self.fnBody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def identList(self):
            return self.getTypedRuleContext(CWScriptParser.IdentListContext,0)


        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def getRuleIndex(self):
            return CWScriptParser.RULE_forItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForItem" ):
                listener.enterForItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForItem" ):
                listener.exitForItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForItem" ):
                return visitor.visitForItem(self)
            else:
                return visitor.visitChildren(self)




    def forItem(self):

        localctx = CWScriptParser.ForItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_forItem)
        try:
            self.state = 893
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.CONTRACT, CWScriptParser.INTERFACE, CWScriptParser.IMPORT, CWScriptParser.IMPLEMENTS, CWScriptParser.IMPL, CWScriptParser.EXTENSION, CWScriptParser.EXTENDS, CWScriptParser.ERROR, CWScriptParser.EVENT, CWScriptParser.INSTANTIATE, CWScriptParser.EXEC, CWScriptParser.QUERY, CWScriptParser.MIGRATE, CWScriptParser.FOR, CWScriptParser.IN, CWScriptParser.FROM, CWScriptParser.STATE, CWScriptParser.TIMES, CWScriptParser.IF, CWScriptParser.ELSE, CWScriptParser.AND, CWScriptParser.OR, CWScriptParser.TRUE, CWScriptParser.FALSE, CWScriptParser.LET, CWScriptParser.RETURN, CWScriptParser.STRUCT, CWScriptParser.ENUM, CWScriptParser.TYPE, CWScriptParser.EMIT, CWScriptParser.Ident]:
                self.enterOuterAlt(localctx, 1)
                self.state = 888
                self.ident()
                pass
            elif token in [CWScriptParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 889
                self.match(CWScriptParser.LBRACE)
                self.state = 890
                self.identList()
                self.state = 891
                self.match(CWScriptParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_identList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentList" ):
                listener.enterIdentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentList" ):
                listener.exitIdentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentList" ):
                return visitor.visitIdentList(self)
            else:
                return visitor.visitChildren(self)




    def identList(self):

        localctx = CWScriptParser.IdentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_identList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 895
            self.ident()
            self.state = 900
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CWScriptParser.COMMA:
                self.state = 896
                self.match(CWScriptParser.COMMA)
                self.state = 897
                self.ident()
                self.state = 902
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = CWScriptParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 903
            self.expr(0)
            self.state = 908
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CWScriptParser.COMMA:
                self.state = 904
                self.match(CWScriptParser.COMMA)
                self.state = 905
                self.expr(0)
                self.state = 910
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namedExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.NamedExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.NamedExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_namedExprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedExprList" ):
                listener.enterNamedExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedExprList" ):
                listener.exitNamedExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedExprList" ):
                return visitor.visitNamedExprList(self)
            else:
                return visitor.visitChildren(self)




    def namedExprList(self):

        localctx = CWScriptParser.NamedExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_namedExprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 911
            self.namedExpr()
            self.state = 916
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CWScriptParser.COMMA:
                self.state = 912
                self.match(CWScriptParser.COMMA)
                self.state = 913
                self.namedExpr()
                self.state = 918
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext
            self.value = None # ExprContext

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_namedExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedExpr" ):
                listener.enterNamedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedExpr" ):
                listener.exitNamedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedExpr" ):
                return visitor.visitNamedExpr(self)
            else:
                return visitor.visitChildren(self)




    def namedExpr(self):

        localctx = CWScriptParser.NamedExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_namedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 919
            localctx.name = self.ident()
            self.state = 920
            self.match(CWScriptParser.COLON)
            self.state = 921
            localctx.value = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ident(self):
            return self.getToken(CWScriptParser.Ident, 0)

        def reservedKeyword(self):
            return self.getTypedRuleContext(CWScriptParser.ReservedKeywordContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = CWScriptParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_ident)
        try:
            self.state = 925
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CWScriptParser.Ident]:
                self.enterOuterAlt(localctx, 1)
                self.state = 923
                self.match(CWScriptParser.Ident)
                pass
            elif token in [CWScriptParser.CONTRACT, CWScriptParser.INTERFACE, CWScriptParser.IMPORT, CWScriptParser.IMPLEMENTS, CWScriptParser.IMPL, CWScriptParser.EXTENSION, CWScriptParser.EXTENDS, CWScriptParser.ERROR, CWScriptParser.EVENT, CWScriptParser.INSTANTIATE, CWScriptParser.EXEC, CWScriptParser.QUERY, CWScriptParser.MIGRATE, CWScriptParser.FOR, CWScriptParser.IN, CWScriptParser.FROM, CWScriptParser.STATE, CWScriptParser.TIMES, CWScriptParser.IF, CWScriptParser.ELSE, CWScriptParser.AND, CWScriptParser.OR, CWScriptParser.TRUE, CWScriptParser.FALSE, CWScriptParser.LET, CWScriptParser.RETURN, CWScriptParser.STRUCT, CWScriptParser.ENUM, CWScriptParser.TYPE, CWScriptParser.EMIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 924
                self.reservedKeyword()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CwspecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CWSPEC_LINE_COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.CWSPEC_LINE_COMMENT)
            else:
                return self.getToken(CWScriptParser.CWSPEC_LINE_COMMENT, i)

        def CWSPEC_MULTI_COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.CWSPEC_MULTI_COMMENT)
            else:
                return self.getToken(CWScriptParser.CWSPEC_MULTI_COMMENT, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_cwspec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCwspec" ):
                listener.enterCwspec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCwspec" ):
                listener.exitCwspec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCwspec" ):
                return visitor.visitCwspec(self)
            else:
                return visitor.visitChildren(self)




    def cwspec(self):

        localctx = CWScriptParser.CwspecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_cwspec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 928 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 927
                _la = self._input.LA(1)
                if not(_la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 930 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CWScriptParser.CWSPEC_LINE_COMMENT or _la==CWScriptParser.CWSPEC_MULTI_COMMENT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReservedKeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTRACT(self):
            return self.getToken(CWScriptParser.CONTRACT, 0)

        def INTERFACE(self):
            return self.getToken(CWScriptParser.INTERFACE, 0)

        def IMPORT(self):
            return self.getToken(CWScriptParser.IMPORT, 0)

        def IMPLEMENTS(self):
            return self.getToken(CWScriptParser.IMPLEMENTS, 0)

        def IMPL(self):
            return self.getToken(CWScriptParser.IMPL, 0)

        def EXTENSION(self):
            return self.getToken(CWScriptParser.EXTENSION, 0)

        def EXTENDS(self):
            return self.getToken(CWScriptParser.EXTENDS, 0)

        def ERROR(self):
            return self.getToken(CWScriptParser.ERROR, 0)

        def EVENT(self):
            return self.getToken(CWScriptParser.EVENT, 0)

        def INSTANTIATE(self):
            return self.getToken(CWScriptParser.INSTANTIATE, 0)

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)

        def MIGRATE(self):
            return self.getToken(CWScriptParser.MIGRATE, 0)

        def FOR(self):
            return self.getToken(CWScriptParser.FOR, 0)

        def IN(self):
            return self.getToken(CWScriptParser.IN, 0)

        def FROM(self):
            return self.getToken(CWScriptParser.FROM, 0)

        def STATE(self):
            return self.getToken(CWScriptParser.STATE, 0)

        def TIMES(self):
            return self.getToken(CWScriptParser.TIMES, 0)

        def IF(self):
            return self.getToken(CWScriptParser.IF, 0)

        def ELSE(self):
            return self.getToken(CWScriptParser.ELSE, 0)

        def AND(self):
            return self.getToken(CWScriptParser.AND, 0)

        def OR(self):
            return self.getToken(CWScriptParser.OR, 0)

        def TRUE(self):
            return self.getToken(CWScriptParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CWScriptParser.FALSE, 0)

        def LET(self):
            return self.getToken(CWScriptParser.LET, 0)

        def RETURN(self):
            return self.getToken(CWScriptParser.RETURN, 0)

        def STRUCT(self):
            return self.getToken(CWScriptParser.STRUCT, 0)

        def ENUM(self):
            return self.getToken(CWScriptParser.ENUM, 0)

        def TYPE(self):
            return self.getToken(CWScriptParser.TYPE, 0)

        def EMIT(self):
            return self.getToken(CWScriptParser.EMIT, 0)

        def getRuleIndex(self):
            return CWScriptParser.RULE_reservedKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReservedKeyword" ):
                listener.enterReservedKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReservedKeyword" ):
                listener.exitReservedKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReservedKeyword" ):
                return visitor.visitReservedKeyword(self)
            else:
                return visitor.visitChildren(self)




    def reservedKeyword(self):

        localctx = CWScriptParser.ReservedKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_reservedKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 932
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CWScriptParser.CONTRACT) | (1 << CWScriptParser.INTERFACE) | (1 << CWScriptParser.IMPORT) | (1 << CWScriptParser.IMPLEMENTS) | (1 << CWScriptParser.IMPL) | (1 << CWScriptParser.EXTENSION) | (1 << CWScriptParser.EXTENDS) | (1 << CWScriptParser.ERROR) | (1 << CWScriptParser.EVENT) | (1 << CWScriptParser.INSTANTIATE) | (1 << CWScriptParser.EXEC) | (1 << CWScriptParser.QUERY) | (1 << CWScriptParser.MIGRATE) | (1 << CWScriptParser.FOR) | (1 << CWScriptParser.IN) | (1 << CWScriptParser.FROM) | (1 << CWScriptParser.STATE) | (1 << CWScriptParser.TIMES) | (1 << CWScriptParser.IF) | (1 << CWScriptParser.ELSE) | (1 << CWScriptParser.AND) | (1 << CWScriptParser.OR) | (1 << CWScriptParser.TRUE) | (1 << CWScriptParser.FALSE) | (1 << CWScriptParser.LET) | (1 << CWScriptParser.RETURN) | (1 << CWScriptParser.STRUCT) | (1 << CWScriptParser.ENUM) | (1 << CWScriptParser.TYPE) | (1 << CWScriptParser.EMIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[48] = self.typeExpr_sempred
        self._predicates[67] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def typeExpr_sempred(self, localctx:TypeExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 13)
         




