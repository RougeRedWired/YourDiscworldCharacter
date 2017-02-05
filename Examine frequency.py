""" Frequency in a string is determined by the number of occurences/length of the string
So first count the number of occurences for a letter and then divide it by len(string)Return the frequency
"""
#Get frequency of a letter

def frequency_return(string,letter):
    count=0
    ranging_string=len(string)
    for letters in string:
        
       if letters==letter:
           count+=1
    return count



index={}

#Scan all letters: if a letter has not been searched then count

def word_frequency_letters(string):
    range_string=string
    length_string=len(string)
    datastore=[]
    target=0
    frequency=0
    

    if string not in index:
        while len(range_string)!=0:
            datastore.append(range_string[target])
            frequency = (int(frequency_return(range_string,range_string[target]))/length_string)
            datastore.append(frequency)
            range_string = range_string.replace(range_string[target],'')
    index.update({string: datastore})
    return index

print (word_frequency_letters("books"))


    
    
   
        
