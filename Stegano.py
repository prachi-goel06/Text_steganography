import sys
import math
class Steganography:
    def user_input(self):
    # taking user input for Student Name
        self.student_name = input("'Please enter your name, Note that name should be 10 letters longs': ")
    # check for the length: student name to be equal to 10, if less than 10 exit the program
        name_length = len(self.student_name)
        if name_length != 10:
            print("'The name entered is not 10 digits, closing the program'")
            sys.exit()
        elif self.student_name.isalpha():
            print("'Input accepted: '")
        else:
            print("'The name entered contains characters other than alphabets'")
            sys.exit()
            # check for the length: student id should be equal to 10, if less than 10 exit the program
        self.student_ID = input("'Please enter your student ID, Note that student id should have 10 digit': ")
        id_length = len(self.student_ID)
        if id_length != 10:
            print("'The student id entered is not 10 digits, closing the program'")
            sys.exit()
        elif self.student_ID.isdigit():
            print("'Input accepted'")
        else:
            print("'ID should be only digits'")
            sys.exit()
        return self.student_name, self.student_ID

    #Converting the input into binary
    def letters_to_binary(self, alphabets):
        # letter conversion to 6 bit
        name_binary = ""
        for i in range(0, len(alphabets)):
            name_binary += format((ord(alphabets[i]) - ord('a') + 1), '06b')
        return name_binary

    def id_to_binary(self, student_id):
        # number conversion to 6 bit
        id_binary = ""
        for i in range(0, len(student_id)):
            id_binary += format((ord(student_id[i]) - ord('0') + 27), '06b')
        return id_binary

    def dot_space_to_binary(self):
        # dot conversion to bit
        dot_binary = format(ord('.') - 9, '06b')
        # space conversion to bit
        space_binary = format(ord(' ') + 6, '06b')
        return dot_binary, space_binary

        # Message to encrypt
    def message_to_encrypt(self, binary_name, binary_space, binary_id, binary_dot):
        message_to_encrypt = (binary_name + binary_space + binary_id + binary_dot)
        return message_to_encrypt

    def bit_manipulation(self,Bit,message):
        bit_gap =1300
        if len(Bit)<bit_gap:  #nth bit is 1300. so first bit modulation occurs at 1300 then 2*1300 and so on
            print("Data too less for Stegnography")
        else:
            Bit = [Bit[i:i + 1] for i in range(0, len(Bit), 1)]
            #bit manipulation according to the message
            for i in range (1,len(message)+1):
                Bit[i*bit_gap]=message[i-1]
            bit=""
            for i in range(0, len(Bit)):
                bit += (Bit[i])
            #decoding binary to literal.
            n=8
            Byte = [bit[i:i + n] for i in range(0, len(bit), n)]
            decoded_literal=[]
            for i in range (0,len(Byte)):
                equi_number = int(Byte[i], 2)
                decoded_literal.append(chr(equi_number))
            bit = ""
            for i in range(0, len(decoded_literal)):
                bit += (decoded_literal[i])
            #Creating a new file.
            f=open("Stegano.txt",'w')
            f.write(bit)
            print("Your Stegano file is created with Name 'Stego.txt' in the same folder as your python file")
if __name__ == '__main__':
    #opening a text file(encoded UTF-8) for reading
    reader=open('Original.txt','r+')
    #reading the data of text file Line by Line
    data=reader.read()
    #to check if reached enf of line
    if not data:
        print("End of Line")
    #print("".join(map(bin, bytes('\n', "UTF-8"))))
    #print("".join(map(bin, bytes('A', "UTF-8"))))
    #changing the content to string of bits
    #z=" ".join(map(bin, bytes(data, "UTF-8")))
    Data=""
    for i in range(0,len(data)):
        Data += format(ord(data[i]), '08b')
    encryption = Steganography()
    user_SName_SID = encryption.user_input()
    user_Name = (user_SName_SID[0])
    user_ID = (user_SName_SID[1])
    # binary conversion of string,number,date,dot and space
    binary_name = encryption.letters_to_binary(user_Name)
    binary_id = encryption.id_to_binary(user_ID)
    binary_dot_space = encryption.dot_space_to_binary()
    binary_dot = binary_dot_space[0]
    binary_space = binary_dot_space[1]
    message = encryption.message_to_encrypt(binary_name, binary_space, binary_id, binary_dot)
    Manipulated_Message=encryption.bit_manipulation(Data,message)
    #print(Manipulated_Message)

