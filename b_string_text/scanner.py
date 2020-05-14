from collections import namedtuple
import re


Token = namedtuple('Token', ['type', 'value'])

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>\=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


# 生成器函数
# yield的作用，函数返回生成器，生成器遇到next(),print()等函数时，继续执行
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)


# 生成器的工作流程
def foo(num):
    print("string...")
    while num < 10:
        yield num
        num += 1


for i in foo(0):
    print(i)
