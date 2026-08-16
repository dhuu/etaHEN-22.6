import sys

def check_brackets(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    stack = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        in_string = False
        escape = False
        for j, char in enumerate(line):
            if escape:
                escape = False
                continue
            if char == '\\':
                escape = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            
            if char in '{[(': 
                stack.append((char, i+1, j+1))
            elif char in '}])':
                if not stack:
                    print(f"Unmatched {char} at line {i+1} col {j+1}")
                    return False
                top, l, c = stack.pop()
                if (top == '{' and char != '}') or \
                   (top == '[' and char != ']') or \
                   (top == '(' and char != ')'):
                    print(f"Mismatched {char} at line {i+1} col {j+1}. Expected match for {top} from line {l} col {c}")
                    return False
    if stack:
        print(f"Unmatched open brackets: {stack}")
        return False
    print("Syntax seems OK")
    return True

check_brackets(sys.argv[1])
