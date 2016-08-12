'''For building the encrypted string:
Take every 2nd char from the string. Then the other chars.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

Have fun coding it and please don't forget to vote and rank this kata! :-)'''


def decrypt(encrypted_text, n):
	for k in range(n):
		t = encrypted_text + encrypted_text
    	string = [None] * (len(encrypted_text))
    	for i in range(0,len(encrypted_text)/2,1):
    		string[i*2 + 1] = str(t[i])
    	j = 0
    	for i in range(len(encrypted_text)/2,len(encrypted_text),1):
    		string[j] = str(t[i])
    		j += 2
    	encrypted_text = ''.join(string)

	return encrypted_text	

def encrypt(text, n):
	for i in range(n):
		if(len(text)%2 == 0):
			t = text + " " + text
		else:
			t = text + text
		string = ''
		for i in range(len(t)):
			if(i%2 != 0):
				string += str(t[i])
		text = string

	return text


print(encrypt("This kata is very interesting!", 1))