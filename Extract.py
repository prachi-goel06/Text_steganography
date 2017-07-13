import sys
import math
class Steganography:
#function to extract the data
    def bit_extraction(self,Bit):
        bit_gap =1300  #nth bit is 1300. so first bit modulation occurs at 1300 then 2*1300 and so on
        if len(Bit)<bit_gap:
            print("Data was too less for Stegnography")
        else:
            Bit = [Bit[i:i + 1] for i in range(0, len(Bit), 1)]
            message=[ 0 for i in range (1,133)]
            #extraction bits from the text file
            for i in range (1,133):
                message[i - 1]=(Bit[i*bit_gap])
            bit=""
            for j in range(0, len(message)):
                bit += (message[j])
            n=6
            #changing bits to plain texts.
            Byte = [bit[i:i + 6] for i in range(0, len(bit), 6)]
            decoded_literal=[]
            PlainMessage=""
            for i in range (0,len(Byte)):
                equi_number = int(Byte[i], 2)
                if equi_number > 0 and equi_number < 27:
                    decoded_literal = chr((equi_number - 1) + ord('a'))
                elif equi_number > 26 and equi_number < 37:
                    decoded_literal = chr((equi_number - 27) + ord('0'))
                elif equi_number == 37:
                    decoded_literal = chr(equi_number + 9)
                elif equi_number == 38:
                    decoded_literal = chr(equi_number - 6)
                PlainMessage += decoded_literal
            print("Your Hidden Message is: ",PlainMessage)

if __name__ == '__main__':
    #opening a text file(encoded UTF-8) for reading
    reader=open('Stegano.txt','r+')
    #reading the data of text file Line by Line
    data=reader.read()
    #to check if reached end of line
    if not data:
        print("End of Line")
    Data=""
    for i in range(0,len(data)):
        #changing the data into bits
        Data += format(ord(data[i]), '08b')
    encryption = Steganography()
    # Fucnction to extract hidden message
    Manipulated_Message=encryption.bit_extraction(Data)
