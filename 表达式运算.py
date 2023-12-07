def delim(c):
    return c == ' '

def is_op(c):
    return c == '+' or c == '-' or c == '*' or c == '/'

def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return -1

def process_op(st, op):
    r = st.pop()
    l = st.pop()
    if op == '+' :
        st.append(l + r)
    elif op ==  '-': 
        st.append(l - r)
    elif op ==  '*': 
        st.append(l * r)
    elif op ==  '/': 
        st.append(l // r)
    else:
        print("invalid operator")

def evaluate(s):
    st = []
    op = []
    for i in range(len(s)):
        if delim(s[i]):
            continue
        if s[i] == '(':
            op.append('(')
        elif s[i] == ')':
            while op and op[-1] != '(':
                process_op(st, op.pop())
            op.pop()
        elif is_op(s[i]):
            cur_op = s[i]
            while op and priority(op[-1]) >= priority(cur_op):
                process_op(st, op.pop())
            op.append(cur_op)
        else:
            number = 0
            while i < len(s) and s[i].isdigit():
                number = number * 10 + ord(s[i]) - ord('0')
                i += 1
            i -= 1
            st.append(number) 
    while op:
        process_op(st, op.pop())
    return st[0] if st else 0
evaluate(' 2*(1+(3+2)*5- (2+1)*3)   ')