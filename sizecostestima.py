import io
import math
#
#
# function to estimate size of dna chunk created and its
# cost

# filesize: size of input file
# encoding: golay or goldman

def golayestimadnasize(filename,filesize):
    # each 
    nameparts = filename.split(".")
  
    numberOfFileNameChunks = int(math.ceil(len(nameparts[0]) /9.0)) #divide by 9 because max 9 bytes in a chunk
    numberOfChunks=int( math.ceil(filesize/9.0) + numberOfFileNameChunks +1.0 ) # payload + filename
    
    
    # no file extension, god chunk remaining
    sizeExtensionchunk = 6 + len(nameparts[1])*5
    
    
    
    tritsforfilesize = 11* ( (math.log(filesize)/math.log(2))/8 )
    x = math.ceil((99-18)/(tritsforfilesize))
    sizeGodChunk = 1+11+2+2+2+ tritsforfilesize *x
    
    return math.ceil(sizeGodChunk + sizeExtensionchunk + (numberOfChunks)*11); 
    
    # chunks generated from the payload data and then indexing information is added
def goldmanestimadnasize(filesize):
    payloadchunks=math.ceil(filesize*5/25.0)
    lengthofdna = 0.0
    
    if payloadchunks<4:        
        lengthofdna= 117
    else:
        lengthofdna= 117*payloadchunks
        
    return lengthofdna
    
def getsize(encoding,filesize):
    if encoding=="Goldman":
        return  goldmanestimadnasize(filesize)
    else:
        return  golayestimadnasize(filesize)          
