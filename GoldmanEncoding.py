import huffman
import ChunkManager1
import ExtraModules
import io

# Binary files to DNA String Convertor
# Input : fileName and fileID to be used
# Output : file converted to it's DNA string. To be later converted into chunks to get 4 fold redundancy  
# Limitation: 3GB is the limitation 
def file2DNA(fileName,fileId):
  totalLen = 0          
  myFile = io.open(fileName, "rb")
  outFile = io.open(fileName+'.dnac',"w")
  chunkManager = ChunkManager1.ChunkManager(outFile,fileId)
  prevBase = 'A'
  while True:
    byte = myFile.read(1)
    if (not byte):
       break
    tritString = str(huffman.encode(byte))
    totalLen = totalLen + len(tritString)
    dnaString = ExtraModules.encodeSTR(tritString,prevBase)
    prevBase = dnaString[-1]
    
    chunkManager.addString(dnaString)
  S2 = ExtraModules.intToBase3(totalLen,20)
  currLen = 20 + totalLen
  lenOfS3 = 25 - (currLen%25)
  S3 = '0'*lenOfS3
  dnaString1 = ExtraModules.encodeSTR(S3+S2,prevBase)
  chunkManager.addString(dnaString1)
  chunkManager.close()

str1 = raw_input()
file2DNA(str1,'10')
