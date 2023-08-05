"""
Fixer for division: from __future__ import division if needed
"""

from lib2to3 import fixer_base
from lib3to2.fixer_util import token, future_import

def match_division(node):
    """
    __future__.division redefines the meaning of a single slash for division,
    so we match that and only that.
    """
    slash = token.SLASH
    return node.type == slash and not node.next_sibling.type == slash and \
                                  not node.prev_sibling.type == slash

class FixDivision(fixer_base.BaseFix):

    def match(self, node):
        """
        Since the tree needs to be fixed once and only once if and only if it
        matches, then we can start discarding matches after we make the first.
        """
        return match_division(node)

    def transform(self, node, results):
        future_import("division", node)
