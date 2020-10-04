class Vowels:
	def __init__(self, str_input):
		self.str_input = str_input

	def check_vowels(self):
                vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
                vowel_count = 0
                message = self.str_input
                for vow in vowels:
                    if vow in message:
                        vowel_count +=1
                print("Vowel Count for " + message + ": " + str(vowel_count))


class StringCount:
	def __init__(self, str_input):
		self.str_input = str_input

	def find_bob(self): 
                message = self.str_input
                bob_count = 0
                for i in range(len(message)-2):
                    if 'bob' in message[i:i+3]:
                        bob_count += 1
                print("Bob Count for " + message + ": " + str(bob_count))

class StringReversal:
	def __init__(self, str_input):
		self.str_input = str_input
        
	def reversed_string(self):
                message = self.str_input
                print(message[::-1])


class UpperLower:
	def __init__(self, str_input):
		self.str_input = str_input

	def count_upper_lower(self):
                message = self.str_input
                upper_count = 0
                for letter in message:
                    if letter.isupper() == True:
                        upper_count += 1
                print("In " + message + "There are " + str(upper_count) + " upper case letters and " + str(len(message) - upper_count) + " lowercase letters")


class SortWords:
	def __init__(self, str_input):
		self.str_input = str_input
        

	def split_alpha(self):
                    message = self.str_input
                    message = message.split(sep=',')
                    message.sort()
                    message = ' '.join(message)
                    print(message)
        


class PalindromeChecker:
	def __init__(self, str_input):
		self.str_input = str_input

	def check_palindrome(self):
                    message = self.str_input
                    if message[::-1] == message:
                        print(message+ " is a palindrome")
                    else:
                        print(message+ " is not a palindrome")



question1 = Vowels("Hello World")
question1.check_vowels()
print("==============\n")

question2 = StringCount("HelloWorldbobsureshbosigerabob")
question2.find_bob()
print("==============\n")

question3 = StringReversal("Programming in Python")
question3.reversed_string()
print("==============\n")

question4 = UpperLower("Hello World")
question4.count_upper_lower()
print("==============\n")

question5 = SortWords("without,hello,bag,world")
question5.split_alpha()
print("==============\n")

question6a = PalindromeChecker("Suresh")
question6a.check_palindrome()

print("==============\n")
question6b = PalindromeChecker("pullup")
question6b.check_palindrome()