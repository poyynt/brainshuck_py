#/usr/bin/python3
import sys

def _mod(a, b):
	return a%b if a>=0 else a if a>=-128 else a%b
class int8(int):
	def __add__(self, value):
		self._val = _mod(value+self._val, 128)
		return _mod(value+self.__int__(), 128) 
	def __int__(self):
		return _mod(self._val, 128)
	def _chr(self):
		return chr(self.__int__())



try:
	f = open(sys.argv[1])
except:
	sys.stderr.write("Bad arguement. Exiting...\n")
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
#		 sys.stderr.write("Loop is not currently supported.\n")
#		 break
	elif char=="]":
		if MEM[INDEX] == 0:
			i += 1
			LOOPS.pop()
			continue
		else:
			i = LOOPS[-1]
#		 sys.stderr.write("Loop is not currently supported.\n")
#		 break
	else:
		pass
	i += 1

sys.stdout.flush()
print("", end = "")
sys.exit(0)
