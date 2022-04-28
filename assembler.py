import sys
from xmlrpc.client import Boolean





n=len(sys.argv)

if n!=2:
    print("invaild arguments");

asmFileName=sys.argv[1]

if asmFileName.endswith(".asm")==False:
    print("invaild file name shoule be .asm");

hackFileName=asmFileName.replace(".asm",".hack");

file=open(asmFileName,"r");
outFile=open(hackFileName,"w");

def isCommentOrEmptyLine(line)->Boolean:
        if line.strip()=='':
            return True

        if line.startswith("//"):
            return True

        return False


def instructionType(line):
    if line.startswith("@"):
        return "A_CMD"
    elif '=' or ';' in line:
        return "C_CMD"


def parserA_Cmd(line):
    val=int(line.replace('@',''))
    address= '{0:016b}'.format(val)

    return address


def getDestCompJump(inst):
    dest='null'
    comp='null'
    jump='null'


    if '=' in inst and ';' in inst:
        
        dest=inst.split("=")[0]
        compAndjump=inst.split("=")[1]
        comp=compAndjump.split(";")[0]
        jump=compAndjump.split(";")[1]


    elif '=' in inst:
        dest=inst.split("=")[0]
        comp=inst.split("=")[1]



    elif ';' in inst :
        comp=inst.split(";")[0]
        jump=inst.split(";")[1]
        


    else:

        comp=inst


    return dest,comp,jump




def parseC_Cmd(inst):

    compAzero={"0":"101010",
                "1":"111111",
                "-1":"111010",
                "D":"001100",
                "A":"110000",
                "!D":"001101",
                "!A":"110001",
                "-D":"001111",
                "-A":"110011",
                "D+1":"011111",
                "A+1":"110111",
                "D-1":"001110",
                "A-1":"110010",
                "D+A":"000010",
                "D-A":"010011",
                "A-D":"000111",
                "D&A":"000000",
                "D|A":"010101"
    }

    compAnotzero={
                "M":"110000",
                "!M":"110001",
                "-M":"110011",
                "M+1":"110111",
                "M-1":"110010",
                "D+M":"000010",
                "D-M":"010011",
                "M-D":"000111",
                "D&M":"000000",
                "D|M":"010101"
    }

    destMap={"null":"000",
         "M":"001",
         "D":"010",
         "MD":"011",
         "A":"100",
         "AM":"101",
         "AD":"110",
         "AMD":"111"
    
    }

    jumpMap={"null":"000",
    "JGT":"001",
    "JEQ":"010",
    "JGE":"011",
    "JLT":"100",
    "JNE":"101",
    "JLE":"110",
    "JMP":"111"

    }

    dest,comp,jump=getDestCompJump(inst)
    jump=jump.strip("\n")
    jump=jump.strip("\t")
    comp=comp.strip("\n")
    comp=comp.strip("\t")



    parseInst="111"

    if comp in compAzero:
        parseInst+="0"
        parseInst+=compAzero[comp]

    elif comp in compAnotzero:

        parseInst+="1"
        parseInst+=compAnotzero[comp]

    if dest in destMap:

        parseInst+=destMap[dest]

    if jump in jumpMap:
        parseInst+=jumpMap[jump]


    print(parseInst)

    outFile.write(parseInst+"\n");


    







    






lines=file.readlines();

for line in lines:
    if isCommentOrEmptyLine(line):
        pass

    else:
        if instructionType(line)=="A_CMD":
            print(parserA_Cmd(line))
            outFile.write(parserA_Cmd(line)+"\n");

        elif instructionType(line)=="C_CMD":
            parseC_Cmd(line)


outFile.close()


    








