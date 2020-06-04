# Get the Token elements
def getNumOrSign(Token, s, i):
    if s[i] == '.' or s[i].isdigit():
        # Calculate the integer part
        integer = 0.0
        # Calculate the integer part
        decimal = 0.0
        dot = 0
        # Keta
        n = 0.1
        while i < len(s) and (s[i].isdigit() or s[i] == '.'):
            if s[i] == '.':
                dot += 1
                if dot >= 2: raise Exception
            else:
                # dot = 0 which means we are calculating integer
                if not dot:
                    integer = 10 * integer + int(s[i])
                # dot = 1 which means we need to calculate decimal part
                if dot:
                    decimal += int(s[i]) * n
                    n *= 0.1
            i += 1
        # The integer part and decimal part are separated, so we need to combine them
        Token.append(float(integer + decimal))
    # When s[i] is +-*/()
    else:
        Token.append(s[i])
        i += 1
    return Token, i


# Do the multiple and divide calculations.
def mulDivCal(Token):
    # If Token[-1] is a number
    # ALEXNOTE: I like how you are using the native type of the token to determine its type
    #           (versus the class template, which had a separate type field in an dictionary entry)
    if isinstance(Token[-1], float):
        # This part of While is for
        # combined + or - to the number if 2 sequent sign appeared like [3,*,-,2], to [3,*,-2]
        # But for [3,-,2], we should not combine because will be [3,-2] and get wrong
        while len(Token) >= 3 and Token[-2] in plusMinus and not isinstance(Token[-3], float):
            num = Token.pop()
            sign = Token[-1]
            Token[-1] = num if sign == '+' else -num

        # If we found * or / before number, we should directly calculate them, like [2,+,3,*,2] to [2,+,6]
        if len(Token) >= 3 and Token[-2] in mulDiv:
            num = Token.pop()
            sign = Token.pop()
            Token[-1] *= num if sign == '*' else 1 / num
    return Token


# Do the calculation when ( ) appeared
def parenCal(Token):
    # When the first right paren appeared, we start finding it's closest left paren
    if Token[-1] == ')':
        Token.pop()
        if Token[-1] == '(': raise Exception
        # val is the value in the pair of parens
        val = 0
        while Token[-1] != '(':
            num = Token.pop()
            # Because we do the mulDivCal before, Token[-1] must be a num or it's a miss
            if not isinstance(num, float): raise Exception
            if Token[-1] != '(':
                sign = Token.pop()
            else:
                # After we pop the num at line 62, if Token[-1] == '(' means it's the first num after '(' like
                # [(1+...], so we give the sign '+'
                # ALEXNOTE: line numbers change. It's not ideal to refer to line numbers in comments.
                sign = '+'
            if sign not in plusMinus: raise Exception
            val += num if sign == '+' else -num
        # Token[-1] is '('
        Token[-1] = val
    return Token


# Do the plus and minus calculations.
def plusMinusCal(Token):
    if not Token: raise Exception
    val = 0
    while len(Token) >= 2:
        # We have 1 number and 1 sign
        num = Token.pop()
        sign = Token.pop()
        # Because we do all muldiv and paren calculations already, so the last sign must be plus or minus
        if sign not in plusMinus: raise Exception
        val += num if sign == '+' else -num
    if len(Token) == 1:
        val += Token[-1]
    return val


passTest = ['1', '1.1', '.1', '- 1.1', '(1+1)', '1.-.1', '+(-(+(-(+1))))', '((((((((1))))))))',
            '-1.0 + 2 * (- 3.1 415926 + .4) / - (5.+ (-3)  ) + (1.4000) ','-2.2+5*((6-2)*3.1)+1/4']
errorTest = ['', 'a', '1a', '1+1)', '(1+1', '1*/1', '1/0', '1.1.1', '3(4)', '(3)4', '()', '(+)1', '3*(a1+5)']

# ALEXNOTE: organizing the test cases in must-pass and must-faile is nice.
#           in the errorTest, how about concatenated operators?  ** ?  // ... etc
#           how about embedded spaces?  should they pass or fail?

mulDiv = {'*', '/'}
plusMinus = {'+', '-'}

for s in passTest + errorTest:
    print(s)
    s = s.replace(' ', '')
    Token = []
    i = 0
    try:
        # 1st mulDivCal: do the mulDiv all we can do now except * or / which before '(',
        # like [1.1+2*(5+3*5)] --> [1.1+2*(5+15)]
        # parenCal: do the paren calculation,
        # like [1.1+2*(5+15)] --> [1.1+2*20]
        # 2nd mulDivCal: do the mulDiv before the '('
        # like [1.1+2*20] --> [1.1+40]
        # plusMinusCal: [1.1+40] --> [41.1]
        while i < len(s):
            Token, i = getNumOrSign(Token, s, i)
            # ALEXNOTE: parenthesis mathematically take precedence over multiplication or division.
            #           I can't prove it right now, but I think there's cases where the logic below produces incorrect results.
            #            Also:  a wrapper function for all 3 steps below would be nice.  They are unlikely to be used
            #            individually, as they are all pieces of a larger program.
            Token = mulDivCal(Token)
            Token = parenCal(Token)
            Token = mulDivCal(Token)
        val = plusMinusCal(Token)
        print('%f' % val)
    except:
        print('Input Error')
