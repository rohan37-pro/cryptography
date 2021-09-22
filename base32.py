
class base32_encryption:

	#step1 - create a dictionry for all base32 characters
	def __init__(self):
		base32_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567"
		self.base32 = {}
		for i in range(32):
			self.base32[base32_char[i]] = bin(i).replace('0b','')
		self.equals = {5:0,4:6,3:4,2:3,1:1}

	def encrypt(self,text):
		#step2 - convert each character into bytes
		byte_list = []
		for i in text:
			rw_bin = bin(ord(i)).replace('0b','')
			if len(rw_bin) < 8:
				byte = '0'*(8-len(rw_bin)) + rw_bin
			byte_list.append(byte)

		len_bytes = len(byte_list)
		#step3 - padding bytes in multiple of 40 bits
		if len_bytes%5 != 0:
			byte_list = base32_encryption.padding(byte_list)

		#step3 - Divid 40 bits of each 5-byte block into 8 groups of 5 bits
		bit_5s = base32_encryption.group(byte_list)

		#step4 create cipher text
		cipher = ""
		for i in range(len(bit_5s)-self.equals[5-(len_bytes%5)]):
			for j in self.base32:
				if int(bit_5s[i]) == int(self.base32[j]):
					cipher += j  

		#step2 extened it with equal signs
		cipher += self.equals[5-(len_bytes%5)] * '='
		return cipher

		
	def padding(lis): 
		pad_len = 5-(len(lis)%5)
		for i in range(pad_len):
			lis.append('00000000')
		return lis


	def group(lis):
		byte_str = ''.join(lis)
		bit5s = []
		for i in range(len(byte_str)//5):
			bit5s.append(byte_str[i*5:5*(i+1)])
		return bit5s



class base32_decryption:

	def __init__(self):
		pass




if __name__ == '__main__':
	text = input('enter text : ')
	base32 = base32_encryption()
	cipher = base32.encrypt(text)
	print(f"encrypted text is \n{cipher}")