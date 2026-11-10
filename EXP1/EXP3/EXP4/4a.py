class InfixToPostfix:
    def __init__(self):
        # Operator precedence dictionary
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def convert(self, infix_expr):
        stack = []
        postfix = []

        # Remove spaces for smooth parsing (optional, but handles spaced/unspaced expressions)
        # However, keeping characters intact if user enters spaces or no spaces:
        # We process token by token or character by character.
        
        for char in infix_expr:
            if char.isspace():
                continue
            
            # If operand (letter or digit), add to postfix
            if char.isalnum():
                postfix.append(char)
            
            # If '(', push to stack
            elif char == '(':
                stack.append(char)
            
            # If ')', pop until '(' is found
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop() # Discard '('
            
            # If operator
            elif char in self.precedence:
                while (stack and stack[-1] != '(' and 
                       self.precedence.get(stack[-1], 0) >= self.precedence[char]):
                    postfix.append(stack.pop())
                stack.append(char)

        # Pop all remaining operators from the stack
        while stack:
            postfix.append(stack.pop())

        return "".join(postfix)


# Driver code matching expected output
if __name__ == "__main__":
    print("Successful Conversion:")
    infix = input("Enter infix expression: ")
    
    converter = InfixToPostfix()
    result = converter.convert(infix)
    
    print(f"Postfix Expression: {result}")
