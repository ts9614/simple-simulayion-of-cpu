import re
import math
class Memory(object):
    #定义一个内存类，使用bytearray数据结构，可变的字节串序列。大小位2**32
    def __init__(self):
        self.mem = bytearray(2**32)
    def get_memint(self, addr):
        #big_endian采用大端存储，存数据
        data=0x00000000
        data = data | (self.mem[addr * 4] << 24)
        data = data | (self.mem[addr * 4 + 1] << 16)
        data = data | (self.mem[addr * 4 + 2] << 8)
        data = data | (self.mem[addr * 4 + 3])
        return data

    def set_memint(self,addr,data):
        #取数据
        self.mem[addr * 4] = (data & 0xff000000) >> 24
        self.mem[addr * 4+1] = (data & 0x00ff0000) >> 16
        self.mem[addr * 4+2] = (data & 0x0000ff00) >> 8
        self.mem[addr * 4+3] = (data & 0x000000ff)


Mem=Memory()
Mem.mem[0]=1
Mem.mem[4]=2
Reg=[0 for i in range(0,32) ]
#Reg[2]=12345
stopword=''
opcode=[]
for line in iter(input, stopword):
  opcode.append(line)
print(opcode)
for i in opcode:
  code=re.split(r'[,\s]',i)
  if code[0]=='load':
      Reg[int(code[1].lstrip('r'))]=Mem.get_memint(int(code[2].lstrip('#')))
  elif code[0]=='store':
      Mem.set_memint(int(code[2].lstrip('#')),Reg[int(code[1].lstrip('r'))])
  elif code[0]=='add':
      Reg[int(code[1].lstrip('r'))]=Reg[int(code[2].lstrip('r'))]+Reg[int(code[3].lstrip('r'))]
print(Mem.mem[0:16])
print(Reg)
'''
class cpu:
    def __init__(self):
        Reg=[0 for i in range(0,32)]
        pc=2**16
        ir=bytearray(4)
        self.init_mem()
    def fetch(self):
        
'''
