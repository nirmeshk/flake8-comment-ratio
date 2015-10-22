from __future__ import division
import sys, token, tokenize, optparse, ast
from sys import stdin

COMMENT_ERROR_CODE = 'T001'
COMMENT_ERROR_MESSAGE = 'Comment to Code ratio too low'
__version__ = '1.1'

class CommentToCodeRatio(object):
    name = 'flakes-comment-ratio'
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = (filename == 'stdin' and stdin) or filename

    def run(self):
        if self.filename == stdin:
            token = get_tokens(self.filename)
        else:
            with open(self.filename, 'r') as file_to_check:
                token = get_tokens(file_to_check.readlines())
        code, comment = get_comment_count(token)
        if( code > 0): ratio = comment/code
        else:          ratio = 0
        if(ratio < 0.05):
            COMMENT_ERROR_CODE += str(ratio)
        yield (1, 1, COMMENT_ERROR_MESSAGE, COMMENT_ERROR_CODE)

def get_tokens(code):
    tokens = tokenize.generate_tokens(lambda L=iter(code): next(L))
    return tokens

def get_comment_count(tokgen):
    """ Run on just one file.
    """
    prev_toktype = token.INDENT
    comment = 0
    docstring = 0
    code = 0
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if toktype == token.STRING and prev_toktype == token.INDENT:
            docstring += 1  # Docstring
        elif toktype == tokenize.COMMENT:
            comment += 1    # Comment
        else:
            code += 1

        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno
    return code, docstring+comment

if __name__ == '__main__':
    get_comment_count(sys.argv[1])
