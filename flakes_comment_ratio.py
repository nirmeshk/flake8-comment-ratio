from __future__ import division
import sys, token, tokenize, optparse, ast

COMMENT_ERROR_CODE = 'T001'
COMMENT_ERROR_MESSAGE = 'comment to code ratio too low'
__version__ = '1.1'

class CommentToCodeRatio(object):
    name = 'flakes-comment-ratio'
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.tree = tree
        self.filename = (filename == 'stdin' and stdin) or filename

    def run(self):
        with open(self.filename, 'r') as file_to_check:
            code, comment = get_comment_count(file_to_check.readlines())
            if( code > 0 and comment/code < 0.05 ):
                yield (1, 1, COMMENT_ERROR_MESSAGE, COMMENT_ERROR_CODE)

def get_comment_count(fname):
    """ Run on just one file.
    """
    source = open(fname)
    prev_toktype = token.INDENT
    comment = 0
    docstring = 0
    code = 0

    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if toktype == token.STRING and prev_toktype == token.INDENT:
            # Docstring
            docstring += 1
            print("Docstring")
        elif toktype == tokenize.COMMENT:
            # Comment
            comment += 1
            print("COMMENT")
        else:
            code += 1

        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno
    print("comments: ", docstring+comment )
    return code, docstring+comment

if __name__ == '__main__':
    get_comment_count(sys.argv[1])
