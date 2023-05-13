import re
import sys

"""
Implement a function called `parse` that expects a `str` of HTML as input,
extracts any YouTube URL that’s the value of a `src` attribute of an `iframe` element therein,
and returns its shorter, shareable `youtu.be` equivalent as a `str`.
Assume that the value of `src` will be surrounded by double quotes.
And assume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None.
"""

def main():
    html = input("HTML: ")
    youtu_be_url = parse(html)
    if youtu_be_url:
        print(youtu_be_url)
    else:
        sys.exit()

def parse(html: str) -> str:
    pattern = r'<iframe.*?src="(https?://)?(www\.)?youtube\.com/embed/([^\s"/]*)".*?</iframe>'
    match = re.search(pattern, html)
    if match:
        video_id = match.group(3)
        return f'https://youtu.be/{video_id}'
    else:
        return None



if __name__ == "__main__":
    main()