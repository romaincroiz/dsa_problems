from data_structure.ds_stack import DsStack

HANDLED_CHARACTERS = ['[', ']', '{', '}', '(', ')']
OPEN_TO_CLOSE_MAP = {
    '[':']',
    '{':'}',
    '(':')'}


def check_bracket(s) -> bool:
    """ Checks a given string to ensure each bracket pair is correctly formed

     - Handled brackets: [],{},()

     - Any other input characters is ignored

     - Each opening bracket must have the matching closing bracket

     - Brackets must be closed in a LIFO order

     - Valid Examples: None, [sometext], [hello([{}])],

     - Invalid Examples: ), {, ({)}

     """

    if not s:
        return True
    stack = DsStack()
    for c in s:
        if c in HANDLED_CHARACTERS and not check_bracket_with_stack(stack, c):
            return False
    # only valid if all brackets have been closed
    return stack.is_empty()

def check_bracket_with_stack(stack, bracket):
    if bracket in OPEN_TO_CLOSE_MAP:
        # push the matching closing bracket
        stack.push(OPEN_TO_CLOSE_MAP[bracket])
        return True
    # pop the stack and check if it is the expected bracket
    return not stack.is_empty() and bracket == stack.pop().data

def test_problem():
    print('==== TEST MATCHING BRACKETS ====')

    print('--- VALID ---')
    test_bracket_sequence()
    test_bracket_sequence("{}")
    test_bracket_sequence("hello")
    test_bracket_sequence("(world)")
    test_bracket_sequence("{}[]()")
    test_bracket_sequence("{} [{}] ()")
    test_bracket_sequence("  [ ]")
    test_bracket_sequence("[({})]")
    test_bracket_sequence("[sometext]")
    test_bracket_sequence("[hello([{}])]")
    test_bracket_sequence("[hello(w[o{r}l]d)]")
    test_bracket_sequence("[([{}])]{}[]()")

    print('--- INVALID ---')
    test_bracket_sequence(")")
    test_bracket_sequence("{")
    test_bracket_sequence(" ({)}")

def test_bracket_sequence(s=None):
    print(f"'{s}' : {check_bracket(s)}")

if __name__ == '__main__':
    test_problem()