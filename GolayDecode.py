import io
import GolayDictionary
import ExtraModules
import math
# header Chunk = FLAG(1) + noOfChunksForFileName(1*11) + fileSize(vriable) + FILEID(2) + PARITY(1) + FLAG(1)


def decodeGolay(fileToRead):
   GolayDictionary.initDict()  
   inputFile = io.open(fileToRead,"r")   # file object for .dnac file
   headerChunk = inputFile.readline()    # main chunk of .dnac file
   extensionChunk = inputFile.readline() # extension chunk for file
   noOfChunksForFileName = getChunksForFilename(headerChunk)
   extraTrits = 2 + 1 + 1 + getNumberOfTritsForChunkID(headerChunk) + 1   # 2 for FILE ID + 1 for PARITY + 1 FOR FLAG + CHUNK ID SIZE + 1 for \n
   extension = '.' + getString(extensionChunk[1:-1*extraTrits])
   #print extraTrits,' ',getNumberOfTritsForChunkID(headerChunk)
   fileNameList = []
   for i in range(1,noOfChunksForFileName+1):
      fileNameChunk = inputFile.readline() 
      #print getString(fileNameChunk[1:-1*extraTrits])
      fileNameList.append(getString(fileNameChunk[1:-1*extraTrits]))
   fileName = ''.join(fileNameList)
   finalFileName = fileName + extension
   outputFile = io.open(finalFileName,"wb")  # decoded FILE object
        
   prevBase = 'A'                        # maintaning previous base for differential decoding
   for chunk in inputFile:
      data = chunk[1:-1*extraTrits]
      #print data
      trits = ExtraModules.getTrits(data,prevBase)
      prevBase = data[-1]
      outputFile.write(bytearray(GolayDictionary.decodeSTR(trits)))  

def getNumberOfTritsForChunkID(str1):
   noOfChunks =  getChunksForFilename(str1) + 1   # 1 for extension + n chunks for file name
   noOfChunksForData = int(math.ceil(getSize(str1)/9))  # n chunks for actual data ceil((size/9))
   #print 'WHY? ',getSize(str1)
   return int(math.ceil(math.log(noOfChunks + noOfChunksForData,3))) # taking log base 3 and then taking ceiling and taking int of it.

def getSize(str1):
  return getBase256Int(str1[12:-5],str1[11])   # 1 extra for \n

def getChunksForFilename(str1):
  return int(GolayDictionary.decode(ExtraModules.getTrits(str1[1:12],'A')))

def getBase256Int(dnaString,prevBase):
  #print GolayDictionary.decodeSTR(ExtraModules.getTrits(dnaString,prevBase))
  return ExtraModules.base256ToInt(GolayDictionary.decodeSTR(ExtraModules.getTrits(dnaString,prevBase)))
  
def getString(str1):
  byteArr = GolayDictionary.decodeSTR(ExtraModules.getTrits(str1,'A'))
  list1 = []
  for byte in byteArr:
    list1.append(unichr(byte))
  return ''.join(list1)

fileNameDNAC = raw_input()
decodeGolay(fileNameDNAC)
