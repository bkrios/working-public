s_crcTable = [None] * 256

def calculateElement(data):
	crc = 0
	ii = 0
	while ii < 8:
		if ((data ^ crc) & 1) == 1:
			crc = crc >> 1 ^ 0x8408
		else:
			crc >>= 1
		data >>= 1
		ii += 1
	return crc

def computeCRC(content):
	crc = compute(0,content.encode())

def compute(crc,data):
	bytearrayData = bytearray(data)
	for (index,dataItem) in enumerate(bytearrayData):
		x = crc ^ dataItem
		crc = crc >> 8 ^ s_crcTable[x & 0xff]
	return crc
	
for (i, item) in enumerate(s_crcTable):
	s_crcTable[i] = calculateElement(i)

content = 'test'
print hex(compute(0,content))[2:]