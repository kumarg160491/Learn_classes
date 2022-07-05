from abc import ABC, abstractmethod


class Bank_transfer_interface:

    @abstractmethod
    def encrypt(self, inp=None):
        pass

    @abstractmethod
    def decrypt(self, inp=None):
        pass


class ICICI(Bank_transfer_interface):

    def encrypt(self, inp=None):
        print('ICICI - encryption is done')
        '''
         ICICI - add 1 with the ASCII value of the character and insert number '1' after every character.
        '''
        temp = []
        for i in inp:
            value = str(ord(i) + 1) + '1'
            temp.append(value)
        return temp

    def decrypt(self, inp=None):
        print('ICICI - decryption is done')
        temp = []
        for i in inp:
            a = i[0:-1]
            value = chr(int(a) - 1)
            temp.append(value)
        return ''.join(temp)


class HDFC(Bank_transfer_interface):

    def encrypt(self, inp=None):
        print('HDFC - encryption is done')
        '''
        HDFC - add 1 with the ASCII value of the character in the even Index and subtract 1 with the ASCII 
        value of the character in the odd Index .It does not encrypt the space.
        '''
        temp1 = []
        for index, value in enumerate(inp):
            if value != ' ':
                if index % 2 == 0:
                    temp1.append(str(ord(value) + 1) + '1')
                else:
                    temp1.append(str(ord(value) - 1) + '1')
            else:
                temp1.append(value)
        return temp1

    def decrypt(self, inp=None):
        print('HDFC - decryption is done')
        temp1 = []
        for index, value in enumerate(inp):
            if value != ' ':
                value = value[0:-1]
                if index % 2 == 0:
                    temp1.append(chr(int(value) - 1))
                else:
                    temp1.append(chr(int(value) + 1))
            else:
                temp1.append(value)
        return ''.join(temp1)


print('Select Bank - Press 1. ICICI, 2. HDFC')
user_input = input()
user_input = user_input[0]
if user_input == '1':
    icici = ICICI()
    icici_encrypted_data = icici.encrypt('abcde')
    print(icici_encrypted_data)
    print(icici.decrypt(icici_encrypted_data))

elif user_input == '2':
    hdfc = HDFC()
    hdfc_encrypted_data = hdfc.encrypt('abcde')
    print(hdfc_encrypted_data)
    print(hdfc.decrypt(hdfc_encrypted_data))
else:
    print('invalid input')