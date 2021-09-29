#!/usr/bin/env python
""" generated source for module Node """

#  (C) 2013 Jim Buffenbarger
#  All rights reserved.

class Node(object):
    """ generated source for class Node """
    pos = 0

    def __str__(self):
        """ generated source for method toString """
        result = ""
        result += str(self.__class__.__name__)
        result += " ( "
        fields = self.__dict__
        for field in fields:
            result += "  "
            result += str(field)
            result += str(": ")
            result += str(fields[field])
        result += str(" ) ")
        return result

    def eval(self, env):
        """ generated source for method eval """
        raise EvalException(self.pos, "cannot eval() node!")

class NodeAssn(Node):
    """ generated source for class NodeAssn """

    def __init__(self, id, num):
        """ generated source for method __init__ """
        super(NodeAssn, self).__init__()
        self.id = id
        self.num = num

    def eval(self, env):
        """ generated source for method eval """
        return env.put(self.id, self.expr.eval(env))

class NodeBlock(Node):
    """ generated source for class NodeBlock """

    def __init__(self, stmt, block):
        """ generated source for method __init__ """
        super(NodeBlock, self).__init__()
        self.stmt = stmt
        self.block = block

class NodeStmt(Node):
    """ generated source for class NodeStmt """

    def __init__(self, assn):
        """ generated source for method __init__ """
        super(NodeStmt, self).__init__()
        self.assn = assn


