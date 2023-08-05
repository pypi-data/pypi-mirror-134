# Generated from ./grammar/CWScriptLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2U")
        buf.write("\u023e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)")
        buf.write("\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3<\3<")
        buf.write("\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3B\3C\3")
        buf.write("C\3D\3D\3D\3E\3E\3F\3F\3F\3G\3G\3H\3H\3H\3I\3I\3J\3J\3")
        buf.write("J\3K\3K\3K\3L\3L\7L\u01e1\nL\fL\16L\u01e4\13L\3M\3M\7")
        buf.write("M\u01e8\nM\fM\16M\u01eb\13M\3M\3M\3N\3N\3N\5N\u01f2\n")
        buf.write("N\3O\3O\3P\5P\u01f7\nP\3P\3P\3P\3Q\3Q\5Q\u01fe\nQ\3Q\7")
        buf.write("Q\u0201\nQ\fQ\16Q\u0204\13Q\3R\3R\3R\3R\3R\7R\u020b\n")
        buf.write("R\fR\16R\u020e\13R\3R\6R\u0211\nR\rR\16R\u0212\3S\3S\3")
        buf.write("S\3S\3S\7S\u021a\nS\fS\16S\u021d\13S\3S\3S\3S\3T\3T\3")
        buf.write("T\3T\7T\u0226\nT\fT\16T\u0229\13T\3T\3T\3U\3U\3U\3U\7")
        buf.write("U\u0231\nU\fU\16U\u0234\13U\3U\3U\3U\3U\3U\3V\3V\3V\3")
        buf.write("V\5\u020c\u021b\u0232\2W\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C")
        buf.write("\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093")
        buf.write("K\u0095L\u0097M\u0099N\u009b\2\u009dO\u009fP\u00a1\2\u00a3")
        buf.write("Q\u00a5R\u00a7S\u00a9T\u00abU\3\2\b\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\6\2\f\f\17\17$$^^\3\2\62;\4\2\f\f\17\17\5\2\13")
        buf.write("\f\17\17\"\"\2\u0246\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\3\u00ad\3\2\2")
        buf.write("\2\5\u00b6\3\2\2\2\7\u00c0\3\2\2\2\t\u00c7\3\2\2\2\13")
        buf.write("\u00d2\3\2\2\2\r\u00d7\3\2\2\2\17\u00e1\3\2\2\2\21\u00ea")
        buf.write("\3\2\2\2\23\u00f2\3\2\2\2\25\u00f8\3\2\2\2\27\u00fe\3")
        buf.write("\2\2\2\31\u010a\3\2\2\2\33\u010f\3\2\2\2\35\u0115\3\2")
        buf.write("\2\2\37\u011d\3\2\2\2!\u0121\3\2\2\2#\u012a\3\2\2\2%\u012d")
        buf.write("\3\2\2\2\'\u0130\3\2\2\2)\u0135\3\2\2\2+\u013b\3\2\2\2")
        buf.write("-\u0141\3\2\2\2/\u0144\3\2\2\2\61\u0149\3\2\2\2\63\u014d")
        buf.write("\3\2\2\2\65\u0150\3\2\2\2\67\u0155\3\2\2\29\u015b\3\2")
        buf.write("\2\2;\u015f\3\2\2\2=\u0164\3\2\2\2?\u016b\3\2\2\2A\u0172")
        buf.write("\3\2\2\2C\u0177\3\2\2\2E\u017c\3\2\2\2G\u0181\3\2\2\2")
        buf.write("I\u0183\3\2\2\2K\u0185\3\2\2\2M\u0187\3\2\2\2O\u0189\3")
        buf.write("\2\2\2Q\u018b\3\2\2\2S\u018d\3\2\2\2U\u018f\3\2\2\2W\u0191")
        buf.write("\3\2\2\2Y\u0193\3\2\2\2[\u0195\3\2\2\2]\u0197\3\2\2\2")
        buf.write("_\u019a\3\2\2\2a\u019c\3\2\2\2c\u019e\3\2\2\2e\u01a0\3")
        buf.write("\2\2\2g\u01a2\3\2\2\2i\u01a4\3\2\2\2k\u01a7\3\2\2\2m\u01aa")
        buf.write("\3\2\2\2o\u01ac\3\2\2\2q\u01ae\3\2\2\2s\u01b0\3\2\2\2")
        buf.write("u\u01b2\3\2\2\2w\u01b5\3\2\2\2y\u01b8\3\2\2\2{\u01ba\3")
        buf.write("\2\2\2}\u01bd\3\2\2\2\177\u01bf\3\2\2\2\u0081\u01c2\3")
        buf.write("\2\2\2\u0083\u01c4\3\2\2\2\u0085\u01c7\3\2\2\2\u0087\u01c9")
        buf.write("\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u01ce\3\2\2\2\u008d")
        buf.write("\u01d1\3\2\2\2\u008f\u01d3\3\2\2\2\u0091\u01d6\3\2\2\2")
        buf.write("\u0093\u01d8\3\2\2\2\u0095\u01db\3\2\2\2\u0097\u01de\3")
        buf.write("\2\2\2\u0099\u01e5\3\2\2\2\u009b\u01f1\3\2\2\2\u009d\u01f3")
        buf.write("\3\2\2\2\u009f\u01f6\3\2\2\2\u00a1\u01fb\3\2\2\2\u00a3")
        buf.write("\u0210\3\2\2\2\u00a5\u0214\3\2\2\2\u00a7\u0221\3\2\2\2")
        buf.write("\u00a9\u022c\3\2\2\2\u00ab\u023a\3\2\2\2\u00ad\u00ae\7")
        buf.write("e\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7e\2\2\u00b4\u00b5\7v\2\2\u00b5\4\3\2\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd")
        buf.write("\7c\2\2\u00bd\u00be\7e\2\2\u00be\u00bf\7g\2\2\u00bf\6")
        buf.write("\3\2\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7o\2\2\u00c2\u00c3")
        buf.write("\7r\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\b\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7o\2\2\u00c9\u00ca\7r\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7o\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7u\2\2\u00d1\n")
        buf.write("\3\2\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7o\2\2\u00d4\u00d5")
        buf.write("\7r\2\2\u00d5\u00d6\7n\2\2\u00d6\f\3\2\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\u00d9\7z\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de")
        buf.write("\7k\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7p\2\2\u00e0\16")
        buf.write("\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7s\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9\7u\2\2\u00e9\20")
        buf.write("\3\2\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7z\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7f\2\2\u00f0\u00f1\7u\2\2\u00f1\22\3\2\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7q\2\2\u00f6\u00f7\7t\2\2\u00f7\24\3\2\2\2\u00f8\u00f9")
        buf.write("\7g\2\2\u00f9\u00fa\7x\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\u00fd\7v\2\2\u00fd\26\3\2\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7u\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7c\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105\u0106\7k\2\2\u0106\u0107\7c\2\2\u0107\u0108")
        buf.write("\7v\2\2\u0108\u0109\7g\2\2\u0109\30\3\2\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b\u010c\7z\2\2\u010c\u010d\7g\2\2\u010d\u010e")
        buf.write("\7e\2\2\u010e\32\3\2\2\2\u010f\u0110\7s\2\2\u0110\u0111")
        buf.write("\7w\2\2\u0111\u0112\7g\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7{\2\2\u0114\34\3\2\2\2\u0115\u0116\7o\2\2\u0116\u0117")
        buf.write("\7k\2\2\u0117\u0118\7i\2\2\u0118\u0119\7t\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7v\2\2\u011b\u011c\7g\2\2\u011c\36")
        buf.write("\3\2\2\2\u011d\u011e\7h\2\2\u011e\u011f\7q\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120 \3\2\2\2\u0121\u0122\7k\2\2\u0122\u0123")
        buf.write("\7p\2\2\u0123\u0124\7v\2\2\u0124\u0125\7g\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7p\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129\"\3\2\2\2\u012a\u012b\7h\2\2\u012b\u012c")
        buf.write("\7p\2\2\u012c$\3\2\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7p\2\2\u012f&\3\2\2\2\u0130\u0131\7h\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7q\2\2\u0133\u0134\7o\2\2\u0134(\3")
        buf.write("\2\2\2\u0135\u0136\7u\2\2\u0136\u0137\7v\2\2\u0137\u0138")
        buf.write("\7c\2\2\u0138\u0139\7v\2\2\u0139\u013a\7g\2\2\u013a*\3")
        buf.write("\2\2\2\u013b\u013c\7v\2\2\u013c\u013d\7k\2\2\u013d\u013e")
        buf.write("\7o\2\2\u013e\u013f\7g\2\2\u013f\u0140\7u\2\2\u0140,\3")
        buf.write("\2\2\2\u0141\u0142\7k\2\2\u0142\u0143\7h\2\2\u0143.\3")
        buf.write("\2\2\2\u0144\u0145\7g\2\2\u0145\u0146\7n\2\2\u0146\u0147")
        buf.write("\7u\2\2\u0147\u0148\7g\2\2\u0148\60\3\2\2\2\u0149\u014a")
        buf.write("\7c\2\2\u014a\u014b\7p\2\2\u014b\u014c\7f\2\2\u014c\62")
        buf.write("\3\2\2\2\u014d\u014e\7q\2\2\u014e\u014f\7t\2\2\u014f\64")
        buf.write("\3\2\2\2\u0150\u0151\7v\2\2\u0151\u0152\7t\2\2\u0152\u0153")
        buf.write("\7w\2\2\u0153\u0154\7g\2\2\u0154\66\3\2\2\2\u0155\u0156")
        buf.write("\7h\2\2\u0156\u0157\7c\2\2\u0157\u0158\7n\2\2\u0158\u0159")
        buf.write("\7u\2\2\u0159\u015a\7g\2\2\u015a8\3\2\2\2\u015b\u015c")
        buf.write("\7n\2\2\u015c\u015d\7g\2\2\u015d\u015e\7v\2\2\u015e:\3")
        buf.write("\2\2\2\u015f\u0160\7h\2\2\u0160\u0161\7c\2\2\u0161\u0162")
        buf.write("\7k\2\2\u0162\u0163\7n\2\2\u0163<\3\2\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165\u0166\7g\2\2\u0166\u0167\7v\2\2\u0167\u0168")
        buf.write("\7w\2\2\u0168\u0169\7t\2\2\u0169\u016a\7p\2\2\u016a>\3")
        buf.write("\2\2\2\u016b\u016c\7u\2\2\u016c\u016d\7v\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e\u016f\7w\2\2\u016f\u0170\7e\2\2\u0170\u0171")
        buf.write("\7v\2\2\u0171@\3\2\2\2\u0172\u0173\7g\2\2\u0173\u0174")
        buf.write("\7p\2\2\u0174\u0175\7w\2\2\u0175\u0176\7o\2\2\u0176B\3")
        buf.write("\2\2\2\u0177\u0178\7v\2\2\u0178\u0179\7{\2\2\u0179\u017a")
        buf.write("\7r\2\2\u017a\u017b\7g\2\2\u017bD\3\2\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\u017e\7o\2\2\u017e\u017f\7k\2\2\u017f\u0180")
        buf.write("\7v\2\2\u0180F\3\2\2\2\u0181\u0182\7*\2\2\u0182H\3\2\2")
        buf.write("\2\u0183\u0184\7+\2\2\u0184J\3\2\2\2\u0185\u0186\7]\2")
        buf.write("\2\u0186L\3\2\2\2\u0187\u0188\7_\2\2\u0188N\3\2\2\2\u0189")
        buf.write("\u018a\7}\2\2\u018aP\3\2\2\2\u018b\u018c\7\177\2\2\u018c")
        buf.write("R\3\2\2\2\u018d\u018e\7\60\2\2\u018eT\3\2\2\2\u018f\u0190")
        buf.write("\7.\2\2\u0190V\3\2\2\2\u0191\u0192\7A\2\2\u0192X\3\2\2")
        buf.write("\2\u0193\u0194\7#\2\2\u0194Z\3\2\2\2\u0195\u0196\7<\2")
        buf.write("\2\u0196\\\3\2\2\2\u0197\u0198\7<\2\2\u0198\u0199\7<\2")
        buf.write("\2\u0199^\3\2\2\2\u019a\u019b\7%\2\2\u019b`\3\2\2\2\u019c")
        buf.write("\u019d\7B\2\2\u019db\3\2\2\2\u019e\u019f\7&\2\2\u019f")
        buf.write("d\3\2\2\2\u01a0\u01a1\7`\2\2\u01a1f\3\2\2\2\u01a2\u01a3")
        buf.write("\7(\2\2\u01a3h\3\2\2\2\u01a4\u01a5\7/\2\2\u01a5\u01a6")
        buf.write("\7@\2\2\u01a6j\3\2\2\2\u01a7\u01a8\7?\2\2\u01a8\u01a9")
        buf.write("\7@\2\2\u01a9l\3\2\2\2\u01aa\u01ab\7)\2\2\u01abn\3\2\2")
        buf.write("\2\u01ac\u01ad\7$\2\2\u01adp\3\2\2\2\u01ae\u01af\7a\2")
        buf.write("\2\u01afr\3\2\2\2\u01b0\u01b1\7?\2\2\u01b1t\3\2\2\2\u01b2")
        buf.write("\u01b3\7?\2\2\u01b3\u01b4\7?\2\2\u01b4v\3\2\2\2\u01b5")
        buf.write("\u01b6\7#\2\2\u01b6\u01b7\7?\2\2\u01b7x\3\2\2\2\u01b8")
        buf.write("\u01b9\7-\2\2\u01b9z\3\2\2\2\u01ba\u01bb\7-\2\2\u01bb")
        buf.write("\u01bc\7?\2\2\u01bc|\3\2\2\2\u01bd\u01be\7/\2\2\u01be")
        buf.write("~\3\2\2\2\u01bf\u01c0\7/\2\2\u01c0\u01c1\7?\2\2\u01c1")
        buf.write("\u0080\3\2\2\2\u01c2\u01c3\7,\2\2\u01c3\u0082\3\2\2\2")
        buf.write("\u01c4\u01c5\7,\2\2\u01c5\u01c6\7?\2\2\u01c6\u0084\3\2")
        buf.write("\2\2\u01c7\u01c8\7\61\2\2\u01c8\u0086\3\2\2\2\u01c9\u01ca")
        buf.write("\7\61\2\2\u01ca\u01cb\7?\2\2\u01cb\u0088\3\2\2\2\u01cc")
        buf.write("\u01cd\7\'\2\2\u01cd\u008a\3\2\2\2\u01ce\u01cf\7\'\2\2")
        buf.write("\u01cf\u01d0\7?\2\2\u01d0\u008c\3\2\2\2\u01d1\u01d2\7")
        buf.write(">\2\2\u01d2\u008e\3\2\2\2\u01d3\u01d4\7>\2\2\u01d4\u01d5")
        buf.write("\7?\2\2\u01d5\u0090\3\2\2\2\u01d6\u01d7\7@\2\2\u01d7\u0092")
        buf.write("\3\2\2\2\u01d8\u01d9\7@\2\2\u01d9\u01da\7?\2\2\u01da\u0094")
        buf.write("\3\2\2\2\u01db\u01dc\7,\2\2\u01dc\u01dd\7,\2\2\u01dd\u0096")
        buf.write("\3\2\2\2\u01de\u01e2\t\2\2\2\u01df\u01e1\t\3\2\2\u01e0")
        buf.write("\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e2\u01e3\3\2\2\2\u01e3\u0098\3\2\2\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e5\u01e9\5o8\2\u01e6\u01e8\5\u009bN\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01ec\u01ed\5o8\2\u01ed\u009a\3\2\2\2\u01ee\u01f2")
        buf.write("\n\4\2\2\u01ef\u01f0\7^\2\2\u01f0\u01f2\13\2\2\2\u01f1")
        buf.write("\u01ee\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u009c\3\2\2\2")
        buf.write("\u01f3\u01f4\5\u00a1Q\2\u01f4\u009e\3\2\2\2\u01f5\u01f7")
        buf.write("\5\u00a1Q\2\u01f6\u01f5\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01f9\5S*\2\u01f9\u01fa\5\u00a1Q")
        buf.write("\2\u01fa\u00a0\3\2\2\2\u01fb\u0202\t\5\2\2\u01fc\u01fe")
        buf.write("\7a\2\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0201\t\5\2\2\u0200\u01fd\3\2\2\2")
        buf.write("\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3")
        buf.write("\2\2\2\u0203\u00a2\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0206")
        buf.write("\7\61\2\2\u0206\u0207\7\61\2\2\u0207\u0208\7\61\2\2\u0208")
        buf.write("\u020c\3\2\2\2\u0209\u020b\13\2\2\2\u020a\u0209\3\2\2")
        buf.write("\2\u020b\u020e\3\2\2\2\u020c\u020d\3\2\2\2\u020c\u020a")
        buf.write("\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c\3\2\2\2\u020f")
        buf.write("\u0211\t\6\2\2\u0210\u0205\3\2\2\2\u0211\u0212\3\2\2\2")
        buf.write("\u0212\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u00a4\3")
        buf.write("\2\2\2\u0214\u0215\7\61\2\2\u0215\u0216\7,\2\2\u0216\u0217")
        buf.write("\7,\2\2\u0217\u021b\3\2\2\2\u0218\u021a\13\2\2\2\u0219")
        buf.write("\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021e\u021f\7,\2\2\u021f\u0220\7\61\2\2\u0220\u00a6")
        buf.write("\3\2\2\2\u0221\u0222\7\61\2\2\u0222\u0223\7\61\2\2\u0223")
        buf.write("\u0227\3\2\2\2\u0224\u0226\n\6\2\2\u0225\u0224\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022b")
        buf.write("\bT\2\2\u022b\u00a8\3\2\2\2\u022c\u022d\7\61\2\2\u022d")
        buf.write("\u022e\7,\2\2\u022e\u0232\3\2\2\2\u022f\u0231\13\2\2\2")
        buf.write("\u0230\u022f\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0233\3")
        buf.write("\2\2\2\u0232\u0230\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0232")
        buf.write("\3\2\2\2\u0235\u0236\7,\2\2\u0236\u0237\7\61\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u0239\bU\2\2\u0239\u00aa\3\2\2\2")
        buf.write("\u023a\u023b\t\7\2\2\u023b\u023c\3\2\2\2\u023c\u023d\b")
        buf.write("V\2\2\u023d\u00ac\3\2\2\2\16\2\u01e2\u01e9\u01f1\u01f6")
        buf.write("\u01fd\u0202\u020c\u0212\u021b\u0227\u0232\3\2\3\2")
        return buf.getvalue()


class CWScriptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CONTRACT = 1
    INTERFACE = 2
    IMPORT = 3
    IMPLEMENTS = 4
    IMPL = 5
    EXTENSION = 6
    REQUIRES = 7
    EXTENDS = 8
    ERROR = 9
    EVENT = 10
    INSTANTIATE = 11
    EXEC = 12
    QUERY = 13
    MIGRATE = 14
    FOR = 15
    INTERNAL = 16
    FN = 17
    IN = 18
    FROM = 19
    STATE = 20
    TIMES = 21
    IF = 22
    ELSE = 23
    AND = 24
    OR = 25
    TRUE = 26
    FALSE = 27
    LET = 28
    FAIL = 29
    RETURN = 30
    STRUCT = 31
    ENUM = 32
    TYPE = 33
    EMIT = 34
    LPAREN = 35
    RPAREN = 36
    LBRACK = 37
    RBRACK = 38
    LBRACE = 39
    RBRACE = 40
    DOT = 41
    COMMA = 42
    QUEST = 43
    EXCLAM = 44
    COLON = 45
    D_COLON = 46
    HASH = 47
    AT = 48
    DOLLAR = 49
    CARET = 50
    AMP = 51
    ARROW = 52
    FAT_ARROW = 53
    S_QUOTE = 54
    D_QUOTE = 55
    UNDERSCORE = 56
    EQ = 57
    EQEQ = 58
    NEQ = 59
    PLUS = 60
    PLUS_EQ = 61
    MINUS = 62
    MINUS_EQ = 63
    MUL = 64
    MUL_EQ = 65
    DIV = 66
    DIV_EQ = 67
    MOD = 68
    MOD_EQ = 69
    LT = 70
    LT_EQ = 71
    GT = 72
    GT_EQ = 73
    POW = 74
    Ident = 75
    StringLiteral = 76
    IntegerLiteral = 77
    DecimalLiteral = 78
    CWSPEC_LINE_COMMENT = 79
    CWSPEC_MULTI_COMMENT = 80
    LINE_COMMENT = 81
    MULTI_COMMENT = 82
    WS = 83

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'contract'", "'interface'", "'import'", "'implements'", "'impl'", 
            "'extension'", "'requires'", "'extends'", "'error'", "'event'", 
            "'instantiate'", "'exec'", "'query'", "'migrate'", "'for'", 
            "'internal'", "'fn'", "'in'", "'from'", "'state'", "'times'", 
            "'if'", "'else'", "'and'", "'or'", "'true'", "'false'", "'let'", 
            "'fail'", "'return'", "'struct'", "'enum'", "'type'", "'emit'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "'?'", 
            "'!'", "':'", "'::'", "'#'", "'@'", "'$'", "'^'", "'&'", "'->'", 
            "'=>'", "'''", "'\"'", "'_'", "'='", "'=='", "'!='", "'+'", 
            "'+='", "'-'", "'-='", "'*'", "'*='", "'/'", "'/='", "'%'", 
            "'%='", "'<'", "'<='", "'>'", "'>='", "'**'" ]

    symbolicNames = [ "<INVALID>",
            "CONTRACT", "INTERFACE", "IMPORT", "IMPLEMENTS", "IMPL", "EXTENSION", 
            "REQUIRES", "EXTENDS", "ERROR", "EVENT", "INSTANTIATE", "EXEC", 
            "QUERY", "MIGRATE", "FOR", "INTERNAL", "FN", "IN", "FROM", "STATE", 
            "TIMES", "IF", "ELSE", "AND", "OR", "TRUE", "FALSE", "LET", 
            "FAIL", "RETURN", "STRUCT", "ENUM", "TYPE", "EMIT", "LPAREN", 
            "RPAREN", "LBRACK", "RBRACK", "LBRACE", "RBRACE", "DOT", "COMMA", 
            "QUEST", "EXCLAM", "COLON", "D_COLON", "HASH", "AT", "DOLLAR", 
            "CARET", "AMP", "ARROW", "FAT_ARROW", "S_QUOTE", "D_QUOTE", 
            "UNDERSCORE", "EQ", "EQEQ", "NEQ", "PLUS", "PLUS_EQ", "MINUS", 
            "MINUS_EQ", "MUL", "MUL_EQ", "DIV", "DIV_EQ", "MOD", "MOD_EQ", 
            "LT", "LT_EQ", "GT", "GT_EQ", "POW", "Ident", "StringLiteral", 
            "IntegerLiteral", "DecimalLiteral", "CWSPEC_LINE_COMMENT", "CWSPEC_MULTI_COMMENT", 
            "LINE_COMMENT", "MULTI_COMMENT", "WS" ]

    ruleNames = [ "CONTRACT", "INTERFACE", "IMPORT", "IMPLEMENTS", "IMPL", 
                  "EXTENSION", "REQUIRES", "EXTENDS", "ERROR", "EVENT", 
                  "INSTANTIATE", "EXEC", "QUERY", "MIGRATE", "FOR", "INTERNAL", 
                  "FN", "IN", "FROM", "STATE", "TIMES", "IF", "ELSE", "AND", 
                  "OR", "TRUE", "FALSE", "LET", "FAIL", "RETURN", "STRUCT", 
                  "ENUM", "TYPE", "EMIT", "LPAREN", "RPAREN", "LBRACK", 
                  "RBRACK", "LBRACE", "RBRACE", "DOT", "COMMA", "QUEST", 
                  "EXCLAM", "COLON", "D_COLON", "HASH", "AT", "DOLLAR", 
                  "CARET", "AMP", "ARROW", "FAT_ARROW", "S_QUOTE", "D_QUOTE", 
                  "UNDERSCORE", "EQ", "EQEQ", "NEQ", "PLUS", "PLUS_EQ", 
                  "MINUS", "MINUS_EQ", "MUL", "MUL_EQ", "DIV", "DIV_EQ", 
                  "MOD", "MOD_EQ", "LT", "LT_EQ", "GT", "GT_EQ", "POW", 
                  "Ident", "StringLiteral", "DoubleQuotedStringCharacter", 
                  "IntegerLiteral", "DecimalLiteral", "DecimalDigits", "CWSPEC_LINE_COMMENT", 
                  "CWSPEC_MULTI_COMMENT", "LINE_COMMENT", "MULTI_COMMENT", 
                  "WS" ]

    grammarFileName = "CWScriptLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


