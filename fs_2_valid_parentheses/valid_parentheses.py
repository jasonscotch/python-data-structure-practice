def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack = []

    # Iterate over each character in the string
    for c in parens:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    # All parentheses are closed if the stack is empty at the end
    return len(stack) == 0