import pygments
from pygments.lexer import RegexLexer, include, bygroups, words, default
from pygments.token import (
    Text,
    Comment,
    Operator,
    Keyword,
    Name,
    String,
    Number,
    Punctuation,
    Generic,
    Whitespace,
)
from pygments.formatters import Terminal256Formatter

from cwscript.lang.grammar.CWScriptLexer import CWScriptLexer


class CWScriptPygmentsLexer(RegexLexer):
    name = "CWScript"
    aliases = ["cwscript", "cws"]
    filenames = ["*.cws"]
    mimetypes = ["text/cwscript", "text/x-cwscript"]

    string_literal = (r'"[^"]*"', String)
    type_keywords = (words(("struct", "enum", "type", "@"), suffix=r"\b"), Keyword.Type)
    stmt_keywords = (
        words(("emit", "fail", "return", "and", "or", "in"), suffix=r"\b"),
        Operator.Word,
    )
    builtin_keywords = (
        words(
            (
                "import",
                "from",
                "if",
                "else",
                "let",
                "impl",
            ),
            suffix=r"\b",
        ),
        Keyword.Reserved,
    )

    tokens = {
        "root": [
            default("base"),
        ],
        "base": [
            (r"\n", Whitespace),
            (r"\s+", Whitespace),
            (r"(//\*.*?)", Comment.Single, "cwspec"),
            (r"//(.*?)\n", Comment.Single),
            (r"(true|false|None)\b", Keyword.Constant),
            (
                r"([_a-zA-Z][_a-zA-Z0-]*)(:\s+)",
                bygroups(Text, Text),
                "typeDecl",
            ),
            string_literal,
            stmt_keywords,
            builtin_keywords,
        ],
        "cwspec": [
            (r"@param|@key", Keyword.Type, "cwspec:ident"),
            (r"@val", Keyword.Type),
            (r"[\r\n]+", Whitespace, "#pop"),
            (r"[^\s]", Comment.Single),
        ],
        "cwspec:ident": [
            (r"\\", Comment.Single),
            (r"[a-zA-Z_][a-zA-Z0-9_]*", Name.Entity, "#pop"),
        ],
    }


import sys


def main():
    with open(sys.argv[1], "r") as f:
        code = f.read()
        text = pygments.highlight(code, CWScriptPygmentsLexer(), Terminal256Formatter())
        print(text)
