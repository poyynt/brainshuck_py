#/usr/bin/python3
import sys
try:
	f = open(sys.argv[1])
except:
	sys.stderr.write("Bad arguement.\n")
	sys.stderr.write("Usage: \n")
	sys.stderr.write(sys.argv[0] + " file.bf\n")
	sys.exit()

MEM = {0:0}
INDEX = 0
LOOPS = []

content = f.read()
i = 0

while i < len(content):
	char = content[i]
	if char=="+":
		MEM[INDEX] += 1
	elif char=="-":
		MEM[INDEX] -= 1
	elif char==">":
		INDEX += 1
		if not INDEX in MEM.keys():
			MEM[INDEX] = 0
	elif char=="<":
		if INDEX<=0:
			i += 1
			continue
		INDEX -= 1
	elif char==".":
		sys.stdout.write(chr(MEM[INDEX]))
	elif char==",":
		MEM[INDEX] = ord(sys.stdin.read(1))
	elif char=="[":
		LOOPS += [i]
	elif char=="]":
		if MEM[INDEX] == 0:
			i += 1
			LOOPS.pop()
			continue
		else:
			i = LOOPS[-1]
	else:
		pass
	i += 1

sys.stdout.flush()
print("", end = "")
sys.exit(0)
