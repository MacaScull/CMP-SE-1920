#Author: Macauley Scullion 
#Creation date: 04/11/2019 

import string as Str

class terms:
    #Object Init function
    def __init__(self):
        self.frequencyData = []
        self.stopWordList = ['a','as','and','are','as','at','be','by','for','from','has','he','in','is','it','its','of','on','that','the','to','was','were','will','with']

    #tfSplit will take a string input and remove all punctuation then tokenized it
    def tfSplit(self, t):
        #If more characters like this appear we could replace this code with regex code
        t = t.replace('/', ' ')
        translator =  t.maketrans('','', Str.punctuation)
        t = t.translate(translator)
        return t.split()

    #tfRemove will remove all stop words from the dictionary producing a more roounded dictionary of less common terms
    def tfRemove(self, d):
        for i in self.stopWordList:
            if i in d:
                del d[i]

    #tf will count terms then calculate the term frequecy for each term within t, t being an input string
    def tf(self, t):
        t = self.tfSplit(t)
        counter = {}
        i = 0
        for word in t:
            i += 1
            if word not in counter:
                counter[word] = 0
            counter[word] += 1       
        
        self.tfRemove(counter)

        counter = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)

        self.frequencyData = counter

'''
#Below is an example on how to use this class for term frequency
string = 'Hello  world/world/world/world, this is is is a test!'

t = terms()
t.tf(string)
print(t.frequencyData[0][0])
# To go through each part of the dictionary change the first [] in the frequencyData i.e. frequencyData[0][0], frequencyData[1][0]
# To get the full dictionary instead of specific keys print frequencyData
'''