This implementation uses `re.findall` to find all occurrences of the word "um" in the input string `s`, case-insensitively. The `r"\bum\b"` pattern matches "um" as a whole word, surrounded by word boundaries (i.e., not as part of another word).

```python
import re
import sys


def main():
    text_input = input("Text: ").lower()
    print(count(text_input))

def count(s):
    # se regex to find all occurences of "um" as a word
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
```