```python
import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^(\d{1,2})(:)(\d{2})\s(AM|PM)$'
    match = re.match(pattern, s)

    if match:
        hour = int(match.group(1))
        minute = int(match.group(3))
        meridiem = match .group(4)

        if hour == 12:
            hour = 0

        if meridiem == 'PM':
            hour += 12

        return f"{hour:02d}:{minute:02d}"

    pattern = r'^(\d{1,2})\s(AM|PM)$'
    match = re.match(pattern, s)

    if match:
        hour = int(match.group(1))
        meridiem = match.group(2)

        if hour == 12:
            hour = 0

        if meridiem == 'PM':
            hour += 12

        return f"{hour:02d}:00"

    raise ValueError("Invalid input format or time")



if __name__ == "__main__":
    main()

```