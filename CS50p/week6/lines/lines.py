import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith('.py'):
    sys.exit("Not a Python file")

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0
in_comment = False



for line in lines:
    line = line.lstrip()

    if not line:
        # blank line
        continue

    if in_comment:
        if line.endswith('"""') or line.endswith("'''"):
            in_comment = False
        continue

    if line.startswith('#'):
        # whole-line comment
        continue

    if (line.startswith('"""') or line.startswith("'''")) and (line.endswith('"""') or line.endswith("'''")):
        # multi-line comment
        in_comment = False
        continue

    count += 1

print(count)