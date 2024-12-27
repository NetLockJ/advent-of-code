import hashlib

src = open("./input.txt", 'r').read()
result = ""
i = 0

while(result[:6] != "000000"):
	hash = hashlib.md5(str.format(src + "{}", i).encode())
	result = hash.hexdigest()
	i += 1
print(i - 1)
