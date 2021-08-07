def balanced_parens(n):
    return_list = []
    if n > 0:
        str = [""] * 2 * n
        _printParenthesis(str, 0, n, 0, 0, return_list)
        return return_list
    else:
        return [""]

def _printParenthesis(str, pos, n, open, close, return_list):
    end = ''
    if close == n:
        for i in str:
            end += i
        return_list.append(end)
    else:
        if open > close:
            str[pos] = ')'
            _printParenthesis(str, pos + 1, n, open, close + 1, return_list)
        if open < n:
            str[pos] = '('
            _printParenthesis(str, pos + 1, n, open + 1, close, return_list)


for n,exp in [ [0, [""]],
               [1, ["()"]],
               [2, ["(())","()()"]],
               [3, ["((()))","(()())","(())()","()(())","()()()"]],
               [5, ['((((()))))', '(((()())))', '(((())()))', '(((()))())', '(((())))()', '((()(())))', '((()()()))', '((()())())', '((()()))()', '((())(()))', '((())()())', '((())())()', '((()))(())', '((()))()()', '(()((())))', '(()(()()))', '(()(())())', '(()(()))()', '(()()(()))', '(()()()())', '(()()())()', '(()())(())', '(()())()()', '(())((()))', '(())(()())', '(())(())()', '(())()(())', '(())()()()', '()(((())))', '()((()()))', '()((())())', '()((()))()', '()(()(()))', '()(()()())', '()(()())()', '()(())(())', '()(())()()', '()()((()))', '()()(()())', '()()(())()', '()()()(())', '()()()()()']]]:
    actual = balanced_parens(n)
    actual.sort()
    print(actual == exp)
    print(actual)
    print(exp)