#use python3

# you can just use the following commands in a python or ipython shell to install dependent libraries

##import nltk
###nltk.download('punkt')
###nltk.download('maxent_treebank_pos_tagger')


#####################program starts from here#####################################
import nltk
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

import re

data = '''Nearly ten years had passed since the Dursleys had woken up to find their nephew on the front 
step, but Privet Drive had hardly changed at all. The sun rose on the same tidy front gardens
and lit up the brass number four on the Dursleys' front door; it crept into their living room, which
was almost exactly the same as it had been on the night when Mr. Dursley had seen that fateful
news report about the owls. Only the photographs on the mantelpiece really showed how much
time had passed. Ten years ago, there had been lots of pictures of what looked like a large pink
beach ball wearing different-colored bonnets - but Dudley Dursley was no longer a baby, and
now the photographs showed a large blond boy riding his first bicycle, on a carousel at the fair,
playing a computer game with his father, being hugged and kissed by his mother. The room held
no sign at all that another boy lived in the house, too.
Yet Harry Potter was still there, asleep at the moment, but not for long. His Aunt Petunia was
awake and it was her shrill voice that made the first noise of the day.
"Up! Get up! Now!"
Harry woke with a start. His aunt rapped on the door again.
"Up!" she screeched. Harry heard her walking toward the kitchen and then the sound of the
frying pan being put on the stove. He rolled onto his back and tried to remember the dream he
had been having. It had been a good one. There had been a flying motorcycle in it. He had a
funny feeling he'd had the same dream before.
His aunt was back outside the door.
"Are you up yet?" she demanded.
"Nearly," said Harry.
"Well, get a move on, I want you to look after the bacon. And don't you dare let it burn, I want
everything perfect on Duddy's birthday."
Harry groaned.
"What did you say?" his aunt snapped through the door.
"Nothing, nothing . . ."

Dudley's birthday - how could he have forgotten? Harry got slowly out of bed and started looking
for socks. He found a pair under his bed and, after pulling a spider off one of them, put them on.
Harry was used to spiders, because the cupboard under the stairs was full of them, and that
was where he slept.
When he was dressed he went down the hall into the kitchen. The table was almost hidden
beneath all Dudley's birthday presents. It looked as though Dudley had gotten the new
computer he wanted, not to mention the second television and the racing bike. Exactly why
Dudley wanted a racing bike was a mystery to Harry, as Dudley was very fat and hated exercise
- unless of course it involved punching somebody. Dudley's favorite punching bag was Harry,
but he couldn't often catch him. Harry didn't look it, but he was very fast.
Perhaps it had something to do with living in a dark cupboard, but Harry had always been small
and skinny for his age. He looked even smaller and skinnier than he really was because all he
had to wear were old clothes of Dudley's, and Dudley was about four times bigger than he was.
Harry had a thin face, knobbly knees, black hair, and bright green eyes. He wore round glasses
held together with a lot of Scotch tape because of all the times Dudley had punched him on the
nose. The only thing Harry liked about his own appearance was a very thin scar on his forehead
that was shaped like a bolt of lightning. He had had it as long as he could remember, and the
first question he could ever remember asking his Aunt Petunia was how he had gotten it.
"In the car crash when your parents died," she had said. "And don't ask questions."
Don't ask questions - that was the first rule for a quiet life with the Dursleys.
Uncle Vernon entered the kitchen as Harry was turning over the bacon.
"Comb your hair!" he barked, by way of a morning greeting.'''


#########################determining proper noun#############################################
word_data = data

#####################data cleansing###############################################################
data = data.lower()    #<------------making entire string lowercased for easy implementation
data = data.rstrip("\n")
newdata = data.replace("?", "@").replace("!", "$").replace(". . .", "#.")

#####################using nltk tools###############################################################
x= tokenize.sent_tokenize(newdata)


final_data = []
for i in range(len(x)):
    final_data.append((x[i]).replace("@","?").replace("$", "!").replace("#.", ". . ."))
  

#####################find list of sentences######################################################################################
def func1():

    for s in range(len(final_data)):
        print(str(s) +"th " + "sentence is: "+ final_data[s].replace("\n"," ").capitalize(), end="\n\n\n")

#####################finding total counting of word in entire string########################################
def func2():
    print("please enter a word")
    find_occurance_of = input()
    print("Occurance of word " + str(find_occurance_of) + " is: " + str(data.count(find_occurance_of)), end="\n\n\n")  ###replace "harry" with any other word


#######################################################################################################



#######################finding all sentences containing a specific word#####################################################
def func3():
    count_3 = 0
    print("please enter a valid word")
    sentences_contained_this_word = input()
    for  z in range(len(final_data)):
        if(sentences_contained_this_word in final_data[z]):      ###replace "harry" with any other word
            count_3 = count_3+1
            print("This is " + str(z) + "th sentence of excerpt in which",sentences_contained_this_word,"is found :  "+ final_data[z].replace("\n"," ").capitalize() , end="\n\n")
 
    if count_3 == 0:
        print("word not found", end="\n")
        func3()

##########################finding all conversation sentences############################################################# 
chatting = []
   
for  z in range(len(final_data)):
    chats = re.findall('^".*.|!$', final_data[z])
    if chats :
        chatting.append(chats)

final_chatting=[]
for m in range(len(chatting)):
    chat=str(chatting[m]).replace("[","").replace("]","").replace("\'","").replace("\\","'")
    final_chatting.append(chat)


def func4():
    

    for f in range(len(final_chatting)):
        print(str(f) + "th conversation is : "+ str(final_chatting[f]), end="\n\n\n")


#finding all conversation in which word appear and count the occurance of word associated chat########### 
def func5():
    count_5=0
    print("Enter a valid word: ")
    chat_specific_word = input()
    for l in range(len(final_chatting)):
        if chat_specific_word in final_chatting[l]:
            count_5 = count_5 + 1
            print("conversation is : " + str(final_chatting[l]) + "  and count of " ,chat_specific_word ," in conversation is: " + str(final_chatting[l].count(chat_specific_word)), end="\n\n\n")

    if count_5 == 0:
        print("word not found", end="\n")
        func5()  

###################finding proper  noun####################################33333333333333333
def func6():
    POS=[]
    part_of_speech= pos_tag(word_tokenize(word_data))
    for h in range(len(part_of_speech)):
        if part_of_speech[h][1] == "NNP" :
            if part_of_speech not in POS:
                POS.append(part_of_speech[h][0])
    setpos=set(POS)
    common_noun= {'Uncle','Aunt', 'Drive', 'Mr.', 'Comb', 'Well',  }

    print("Set of proper nouns is:  ",setpos.difference(common_noun),end="\n\n\n")


##take input form user
while True:
    ################################starting of functions###################
    print("###########################################################################")
    print("please enter corresponding number::",end="\n\n")
    print("To list all Sentences in Excerpt, Enter 1: ", end="\n")
    print("How many times does the word occur in the excerpt, Enter 2: ", end="\n")
    print("List all sentences in which the word appears, Enter 3: ", end="\n")
    print("List all conversations in the excerpt above, Enter 4: ", end="\n")
    print("Is the word mentioned in a conversation? Which ones and how many times, Enter 5: ", end="\n")
    print("Find all proper nouns in the excerpt, Enter 6: ", end="\n")
    inp = input()
    print("###########################################################################")
    if inp=="1":
        func1()

    elif inp=="2":
        func2()

    elif inp=="3":
        func3()   

    elif inp=="4":
        func4() 

    elif inp=="5":
        func5() 

    elif inp=="6":
        func6() 
        