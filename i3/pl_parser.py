#!/usr/bin/env python

from pl_syntaxexception import SyntaxException
from pl_node import *
from pl_scanner import Scanner
from pl_token import Token

class Parser(object):
    """ generated source for class Parser """
    def __init__(self):
        self.scanner = None

    def match(self, s):
        """ generated source for method match """
        self.scanner.match(Token(s))

    def curr(self):
        """ generated source for method curr """
        return self.scanner.curr()

    def pos(self):
        """ generated source for method pos """
        return self.scanner.position()

    def parseAssn(self):
        """ generated source for method parseAssn """
        nid = self.curr()
        self.match("id")
        self.match("=")
        num = self.curr()
        self.match("num")
        assn = NodeAssn(nid.lex(), num)
        return assn

    def parseStmt(self):
        """ generated source for method parseStmt """
        if self.curr() == Token("id"):
            assn = self.parseAssn()
            return NodeStmt(assn)
        return None

    def parseBlock(self):
        """ generated source for method parseBlock """
        stmt = self.parseStmt()
        rest = None
        if self.curr() == Token(";"):
            self.match(";")
            rest = self.parseBlock()
        block = NodeBlock(stmt, rest)
        return block


    def parse(self, program):
        """ generated source for method parse """
        if program == '': return None
        self.scanner = Scanner(program)
        self.scanner.next()
        return self.parseBlock()

