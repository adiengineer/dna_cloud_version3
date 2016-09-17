import io
import GolayDictionary
import ExtraModules
import math
import os
import random

# Binary files to DNA String Convertor
# Input : fileName and fileID to be used
# Output : file converted to it's DNA string. Each chunk contains at most 9 bytes. 
# Limitation: No Limitation on size of file 

numberOfFiles = 9

def encode(fileName,fileId,fileExtension):
    wholeFileName = ''
    if not fileExtension:
       wholeFileName = fileName
    else:
       wholeFileName = fileName + '.' + fileExtension
    currFile = io.open(wholeFileName, "rb")
    outputFile = io.open(wholeFileName+'.dnac',"w")
    
    global numberOfFiles
    fileIdInTrits=ExtraModules.intToBase3(fileId, int(math.ceil( math.log(numberOfFiles,3) )) ) 
    
    # calculating no of trits required for chunk ID
    fileLength= os.path.getsize(wholeFileName)
    numberOfChunks=int( math.ceil(fileLength/9.0) + math.ceil( len(fileName)/9.0 ) +1.0 ) #ceil apparently gives real number and not int
    mu=int( math.ceil( math.log(numberOfChunks,3) ) ) #number of trits required to address chunk indices
   
    # creating the meta chunks

    # writing the header chunk 
    numberOfFileNameChunks = int(math.ceil(len(fileName) /9.0))
    headerchunkpart1= ExtraModules.encodeSTR(GolayDictionary.encodeDirect(numberOfFileNameChunks),'A') 
    headerchunkpart2= ExtraModules.encodeSTR( fileSizeEncoding(fileLength),headerchunkpart1[-1])
    headerFinal = headerchunkpart1+headerchunkpart2
    headerChunk = addGuardBases(headerFinal+getExtraTrits(fileIdInTrits,"",headerFinal[-1]))
    outputFile.write(unicode(headerChunk+'\n'))
    
    #file extension goes here in the next chunk
    extensionData = ExtraModules.encodeSTR(GolayDictionary.encodeSTR(fileExtension),'A')
    #print fileExtension,' ',GolayDictionary.encodeSTR(fileExtension),' ',extensionData ,' Hello ', extensionData[-1]
    extensionChunk = addGuardBases(extensionData+getExtraTrits(fileIdInTrits,'0'*mu,extensionData[-1]))
    outputFile.write(unicode(extensionChunk+'\n'))
    
    #file name chunks go on here onwards and thereafter the loop for data
    chunkIndex=1
    for i in xrange(0,numberOfFileNameChunks,9):
        chunkIdinTrits=ExtraModules.intToBase3(chunkIndex,mu)
        fileNameData = ExtraModules.encodeSTR(GolayDictionary.encodeSTR(fileName[i:i+9]),'A')
        fileNameCurrChunk = addGuardBases(fileNameData+getExtraTrits(fileIdInTrits,chunkIdinTrits,fileNameData[-1]))
        outputFile.write(unicode(fileNameCurrChunk+'\n'))
        chunkIndex=chunkIndex+1
    
    #writting the payload
    prevBase='A'
    
    while True:
        currChunkElements = currFile.read(9)
        if (not currChunkElements):   # There are no bytes left in the file
            break
        payLoadData = ExtraModules.encodeSTR( GolayDictionary.encodeSTR(currChunkElements),prevBase ) #make this chunk creator
        prevBase = payLoadData[-1]
        chunkIndexInTrits= ExtraModules.intToBase3(chunkIndex,mu)
        chunkIndex=chunkIndex+1
        payloadChunk = addGuardBases(payLoadData+getExtraTrits(fileIdInTrits,chunkIndexInTrits,payLoadData[-1]))
        outputFile.write(unicode(payloadChunk+'\n'))
        
def generateParity(chunkIndexInTrits,fileIdInTrits):
    header= fileIdInTrits+chunkIndexInTrits
    lengthHeader=len(header)
    p = 0
    for x in xrange(0,lengthHeader,2):
       p = p + int(header[x])
    p = p % 3
    return str(p)

def getExtraTrits(fileIDInTrits,chunkIDInTrits,prevBase):
   parityInTrits = generateParity(chunkIDInTrits,fileIDInTrits)
   extra = fileIDInTrits + chunkIDInTrits + parityInTrits
   #print fileIDInTrits,chunkIDInTrits,parityInTrits
   #print extra
   return ExtraModules.encodeSTR(extra,prevBase)

# Input : Size of the file	
def fileSizeEncoding(input1):
    output=[]
    while input1!=0:
        output.append(GolayDictionary.encodeDirect((input1%256)))
        input1 = input1//256             
    return ''.join(output)      
    

def addGuardBases(input1):
    if input1[0] == 'A' :
        startBase = 'T'
    elif input1[0] == 'T' :
        startBase = 'A'
    else :
        randomNum = random.random()
        if randomNum > 0.5:
          startBase = 'A'
        else:
          startBase = 'T'

    if input1[-1] == 'C' :
        endBase = 'G'
    elif input1[-1] == 'G' :
        endBase = 'C'
    else :
        randomNum = random.random()
        if randomNum > 0.5 :
          endBase = 'C'
        else:
          endBase = 'G'
    return startBase + input1 + endBase

fileName12 = (raw_input()).rstrip()
fileID12 = int(raw_input())
fileExtension12 = raw_input().rstrip()

encode(fileName12,fileID12,fileExtension12)
        
