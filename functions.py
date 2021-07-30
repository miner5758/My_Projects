# function that spells word for 
import random
def print_word(word):
    count = 1
    for letter in word:
        if letter == ' ':
            print('The',count,'letter in', word,'is a space')
        else:
            print('The',count, 'letter in', word, 'is', letter)
        count = count + 1
#print_word('Hi how are you?')
#print('THats how you spell this word!')

def what_are_you(fname,Lname):
    alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabetL = alphabet.lower()
    if fname[0] in alphabet[11:] and Lname[0] in alphabet[11:]:
        print(fname + ',','you are a shy but confident person and you prefer to keep to yourself. you are smart but your ego sometimes gets the better of you, so make sure you work on that!')
    elif fname[0] in alphabet[:11] and Lname[0] in alphabet[:11]:
        print(fname + ',','you are a little brash and quick to act, your upbeat and love to meet new people, which makes you a real people person!')
    elif fname[0] in alphabet[:11] and Lname[0] in alphabet[11:]:
        print(fname + ',','you are unique in almost everyway possible, you may seem a little werid but your happy and thats what matters.')
    elif fname[0] in alphabet[11:] and Lname[0] in alphabet[:11]:
        print(fname + ',','you are someone who usually alters their personality for whatever situation they are in, whether your in a clam enviorment and a peaceful one. its up to you to decide whether this is a good thing or a bad thing.')
    elif fname[0] in alphabetL[11:] and Lname[0] in alphabetL[11:]:
        print(fname + ',','you are a shy but confident person and you prefer to keep to yourself. you are smart but your ego sometimes gets the better of you, so make sure you work on that!')
    elif fname[0] in alphabetL[:11] and Lname[0] in alphabetL[:11]:
        print(fname + ',','you are a little brash and quick to act, your upbeat and love to meet new people, which makes you a real people person!')
    elif fname[0] in alphabetL[:11] and Lname[0] in alphabetL[11:]:
        print(fname + ',','you are unique in almost everyway possible, you may seem a little werid but your happy and thats what matters.')
    elif fname[0] in alphabetL[11:] and Lname[0] in alphabetL[:11]:
        print(fname + ',','you are someone who usually alters their personality for whatever situation they are in, whether your in a clam enviorment and a peaceful one. its up to you to decide whether this is a good thing or a bad thing.')
    else:
        print('the first letters on your first and last name must both be capitals or lowercase')
        
        
def your_number_is(*numbers):
    result = []
    for num in numbers:
        num = num/3
        num = num*256
        num = num+21
        num = num-249
        num = num/40
        result.append(num)
    result = sum(result)
    if result == 666:
        print('you got',result,'0_0,','not only are you gonna take over the wold but you are very very horny.')
    elif result >= 1000:
        print('you got',result,'that means your going to become rich and famous for sure!')
    elif result >= 500:
        print('you got',result,'that means your bound to have a bright future!')
    elif result >= 100:
        print('you got',result,'that means your bound to have a good day')
    elif result >= 10:
        print('you got',result,'that means your day is bound to go as normal!')
    elif result <= 0:
        print('you got',result,'thats a negitive number so it means bad luck!')
    else:
        print('Im sorry, but you got',result,'your gonna end up on the streets')
        
        
def what_should_you_do(op_1,op_2,op_3):
    choices = (op_1,op_2,op_3)
    answer = (random.choice(choices))
    choicesL = ('is a good choice!','seems like a good choice but im not completley sure','has a 99% chance of being correct for you')
    answerL = random.choice(choicesL)
    print(answer,answerL)
    
    
def number_big(**number):
    answer = number['one_five'] / number['five_ten']
    Random = number['rando']
    if answer > Random:
        print(answer, '>',Random)
    else:
        print(answer,'<',Random)
        
        
        
def is_bigger(number = 16):
    num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    rando = random.choice(num)
    if number > rando:
        print(number, 'is bigger than',rando)
    else:
        print(number,'is smaller than',rando)
        
        
        
        
def letter_count(word,letter):
    result = []
    for x in word:
        if x == letter or x.lower() == letter.lower() or x == letter.lower():
            result.append(x)
    if len(letter) > 1:
        print('you must insert only 1 letter.')
    elif len(result) == 0:
            print(word, 'has no',letter.upper()+"('s)",'in it')
    elif len(result) == 1:
        print(word,'has 1',letter.upper(),'in it.')
    else:
        print(word,'has',len(result), letter.upper()+"'s",'in it')
        
        
        
def calculate_name_length_by_25(name,symbol):
    if symbol == '/':
        return len(name) / 25
    elif symbol == '*':
        return len(name) * 25
    elif symbol == '+':
        return len(name) + 25
    elif symbol == '-':
        return len(name) - 25
    

def myfunction():
  pass



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
  print("\n\nRecursion Example Results")

    