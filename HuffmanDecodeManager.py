import huffman

class HuffmanDecodeManager(object):
   tritString = []
   currLenOfTritString = 0
   fileFinal = None 
   startIndex = 0
   maxRAMCapacity = 500000

   def addTrit(self,trit):
    self.tritString.append(trit)
    self.currLenOfTritString = self.currLenOfTritString + 1
    if self.currLenOfTritString == 6 :
       self.updateManager()

   def addString(self,string1):
     for trit in string1:
        self.addTrit(trit)

   def readFromFile(self,fileIn,len12):
     CHUNK_SIZE = 1000000
     currLen = 0
     while True:
        toRead = min(len12-currLen,CHUNK_SIZE)
        if toRead==0:
           break
        currLen = currLen + toRead
        tritString1 = fileIn.read(currLen)
        if tritString1 is None:
           break
        else:
           self.addString(tritString1)

   def updateManager(self):
     trit1 = ''.join(self.tritString[self.startIndex:])
     num1 = huffman.decode(trit1)
     if num1 == -1:
       num1 = huffman.decode(trit1[:-1])
       self.startIndex = self.startIndex + 5;
       self.currLenOfTritString=1
     else:
        self.startIndex = self.startIndex + 6;
        self.currLenOfTritString=0
     tempList = []
     tempList.append(num1)
     self.fileFinal.write(bytearray(tempList))
     if self.startIndex>=self.maxRAMCapacity:
        if self.currLenOfTritString==1:
           self.tritString = self.tritString[-1:]
        else:
           self.tritString = []
        self.startIndex = 0

   def close(self):
     if self.currLenOfTritString !=0:
        self.updateManager()
     self.fileFinal.close()
  
   def __init__(self,fileFinal1):
     self.fileFinal = fileFinal1
     self.tritString = []
     self.currLenOfTritString = 0
     self.startIndex = 0
     self.maxRAMCapacity = 500000
     huffman.setReverseHuffman()
