import sys
import re
data = sys.stdin.read().splitlines()
n, m = map(int, data[0].split())
listik = {data[i].strip().lower() for i in range(1, n + 1)}
word = set()
for i in range(n + 1, n + 1 + m):
    word.update(re.findall(r"[a-z]+", data[i].lower()))

if not word.issubset(listik):
    print("Some words from the text are unknown.")
elif not listik.issubset(word):
    print("The usage of the vocabulary is not perfect.")
else:
    print("Everything is going to be OK.")
