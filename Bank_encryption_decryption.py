'''
One such practical scenario is contract between the Banks to perform fund / message transfer. The information has to be confidential and each bank might use its own encryption & decryption techniques. The Reserve Bank might setup an Interface giving the method names and not worrying about the implementation. 
 
1. Create an interface BankTransfers

2. Add two methods with the following prototype    

   -- public String encrypt(String a);  

   -- public String decrypt(String a);

3. Create class ICICI which implements the BankTransfers Interface & implement a simple encryption technique.

4. Create class HDFC which implements the BankTransfers Interface & implement a simple encryption technique.

5. Encrypt technique followed by both banks:

      ICICI - add 1 with the ASCII value of the character and insert number '1' after every character.

      HDFC - add 1 with the ASCII value of the character in the even Index and subtract 1 with the ASCII value of the character in the odd Index .It does not encrypt the space.

      The reverse of both will be decrept message (i.e original text)

Input Description:
Select a Bank Type the user name

Output Description:
Output should have a Encrypted input

Sample Input :
1 welcome all
Sample Output :
x1f1m1d1p1n1f1!1b1m1m1
'''

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
