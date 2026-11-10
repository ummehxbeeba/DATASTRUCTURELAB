class PostfixEvaluator:
    @staticmethod
    def evaluate(postfix_expr):
        stack = []
        # Split expression by whitespace to handle multi-digit numbers or tokens correctly
        tokens = postfix_expr.split()

        for token in tokens:
            # If token is a number (handles multi-digit integers/floats)
            if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
                if '.' in token:
                    stack.append(float(token))
                else:
                    stack.append(int(token))
            # If token is an operator
            elif token in {'+', '-', '*', '/', '^'}:
                val2 = stack.pop() # Right operand
                val1 = stack.pop() # Left operand
                
                if token == '+':
                    res = val1 + val2
                elif token == '-':
                    res = val1 - val2
                elif token == '*':
                    res = val1 * val2
                elif token == '/':
                    res = val1 / val2
                elif token == '^':
                    res = val1 ** val2
                
                stack.append(res)
            else:
                # Fallback for single-character operands if no spaces were provided
                for char in token:
                    if char.isdigit():
                        stack.append(int(char))
                    elif char in {'+', '-', '*', '/', '^'}:
                        val2 = stack.pop()
                        val1 = stack.pop()
                        if char == '+': res = val1 + val2
                        elif char == '-': res = val1 - val2
                        elif char == '*': res = val1 * val2
                        elif char == '/': res = val1 / val2
                        elif char == '^': res = val1 ** val2
                        stack.append(res)

        return float(stack[0]) if stack else 0.0


# Driver code matching expected output
if __name__ == "__main__":
    sample_expr = "2 3 1 * + 9 -"
    print(f"Postfix Expression: '{sample_expr}'")
    
    result = PostfixEvaluator.evaluate(sample_expr)
    print(f"Evaluation Result: {result}")
