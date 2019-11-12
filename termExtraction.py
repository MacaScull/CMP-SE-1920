#Author: Macauley Scullion 
#Creation date: 04/11/2019 

import string as Str

class terms:
    #Object Init function
    def __init__(self):
        self.frequencyData = []

    #tfSplit will take a string input and remove all punctuation then tokenized it
    def tfSplit(self, t):
        translator =  t.maketrans('','', Str.punctuation)
        t = t.translate(translator)
        return t.split()

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
        
        counter = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)

        self.frequencyData = counter

'''
#Below is an example on how to use this class for term frequency
string = 'Hello  world world world world, my name is macauley macauley macauley'

t = terms()
t.tf(string)
print(t.frequencyData[0][0])
# To go through each part of the dictionary change the first [] in the frequencyData i.e. frequencyData[0][0], frequencyData[1][0]
'''