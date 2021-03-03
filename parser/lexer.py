# constants
DIGITS = "0123456789"
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# TOKEN TYPES
TT_DIGIT = "DIGITS"
TT_VARIABLE = "VARIABLE"
TT_FUNCTION = "FUNCTION"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MULTIPLY = "MULTIPLY"
TT_DIVIDE = "DIVIDE"
TT_POWER = "POWER"
TT_MODULO = "MODULO"
TT_FACTORIAL = "FACTORIAL"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"



class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Type: {self.type}" + (f"\tValue: {self.value}\n" if self.value else "\n")


class Lexer:
    def __init__(self, text):
        self.text = text
        self.currentChar:str = None
        self.index = -1
        self.tokens = []
        self.advance()

    def advance(self):
        self.index+=1;
        self.currentChar = self.text[self.index] if self.index < len(self.text) else None

    def make_token(self):
        while self.currentChar is not None:
            if self.currentChar in " \t":
                self.advance()
            elif self.currentChar == '+':
                self.tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.currentChar == '-':
                self.tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.currentChar == '/':
                self.tokens.append(Token(TT_DIVIDE))
                self.advance()
            elif self.currentChar == '(':
                self.tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.currentChar == ')':
                self.tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.currentChar == '%':
                self.tokens.append(Token(TT_MODULO))
                self.advance()
            elif self.currentChar == '!':
                self.tokens.append(Token(TT_FACTORIAL))
                self.advance()
            elif self.currentChar in DIGITS+'.':
                self.handle_digits()
            elif self.currentChar in LETTERS:
                self.handle_string()
            elif self.currentChar == '*':
                self.handle_asterisk()
        return self.tokens

    def handle_string(self):
        tokenValue = ""
        while self.currentChar is not None and self.currentChar in LETTERS:
            tokenValue+=self.currentChar
            self.advance()
        self.tokens.append(Token(TT_VARIABLE, tokenValue)) if self.currentChar != '(' else self.tokens.append(Token(TT_FUNCTION, tokenValue))

    def handle_digits(self):
        dot_counter = 0
        digit = ""
        while self.currentChar is not None and self.currentChar in DIGITS+'.':
            if self.currentChar == '.':
                dot_counter += 1
                if dot_counter>1:raise Exception("More than one decimal point in digit")
            digit+=self.currentChar
            self.advance()
        self.tokens.append(Token(TT_DIGIT, float(digit)))
        if self.currentChar is not None and self.currentChar in LETTERS:
            self.tokens.append(Token(TT_MULTIPLY))

    def handle_asterisk(self):
        counter = 0
        while self.currentChar == '*':
            counter+=1
            if(counter>2): raise Exception("Illegal character *** ")
            self.advance()
        self.tokens.append(Token(TT_POWER)) if counter == 2 else self.tokens.append(Token(TT_MULTIPLY))
        return

if __name__ == "__main__":
    while True:
        print("Math> ", end="")
        expr = input()
        if expr in ["q", "quit", "exit"]:
            break
        lex = Lexer(expr)
        try:
            print(lex.make_token())
        except Exception as e:
            print(e)


    # lex = Lexer("*")
    # lex.make_token()