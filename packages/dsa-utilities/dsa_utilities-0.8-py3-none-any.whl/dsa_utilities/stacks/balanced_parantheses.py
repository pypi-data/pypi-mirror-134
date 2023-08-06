from dsa_utilities.stacks import stack

def balanced_parantheses(parantheses: str) -> bool:
    """Use stack to check if a string of parantheses is balanced or not.
    >>> balanced_parantheses("([]{})")
    True
    >>> balanced_parantheses("[()]{}(()){}[()()]")
    True
    >>> balanced_parantheses("[({)]")
    False
    >>> balanced_parantheses("[(])")
    False
    >>> balanced_parantheses("1+2*3-4")
    True
    >>> balanced_parantheses("")
    True
    >>> balanced_parantheses("()")
    True
    >>> balanced_parantheses("()[]{}")
    True
    >>> balanced_parantheses("(]")
    False
    """
    s = stack.Stack[str]()
    bracket_parist = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    for bracket in parantheses:
        if bracket in "[{(":
            s.push(bracket)
        elif bracket in ")}]":
            if s.is_empty() or bracket_parist[s.pop()] != bracket:
                return False

    return s.is_empty()


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    sample_parantheses = ["((()))", "((())", "(()))", "()"]
    for parantheses in sample_parantheses:
        print(f"{parantheses} is {balanced_parantheses(parantheses)} balanced")

