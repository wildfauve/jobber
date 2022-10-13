from jobber.util import code_block

def test_generates_code():
    ifblock = code_block.CodeBlock('if x>0', ['print x', 'print "Finished."'])
    block = code_block.CodeBlock('def print_success(x)', [ifblock, 'print "Def finished"'])
