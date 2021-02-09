import re

needle = input()
haystack = input()

print(len(re.findall(f"(?={needle})", haystack)))