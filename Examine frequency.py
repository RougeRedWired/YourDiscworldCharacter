

index={}

#data handling function

#Create a file to put the data in


#Get frequency of a letter

def frequency_return(string,letter):
    count=0
    
    for letters in string:
       if letters==letter:
           count+=1
    return count

#Scan all letters: if a letter has not been searched then count
def get_frequency(string):
  range_string=string
  length_string=len(string)
  datastore={}
  target=0
  frequency=0
  while len(range_string)!=0:
           # datastore.append(range_string[target])
            frequency = (int(frequency_return(range_string,range_string[target]))/length_string)
            frequency = format(frequency, '.2f')
            datastore.update({range_string[target]:frequency})
            range_string = range_string.replace(range_string[target],'')
  return datastore          
          
def index_string(string):
  
    if string not in index:
      
      index.update({string: (get_frequency(string))})
    return index
    
#basically what I want to achieve is compare the frequency between the two strings. I need to collect those frequencies from the first string. Once it is done several tests: Which string has the most identical letters and if there are several of them, match them against their respective probabilities


def compare_frequency(name):
  name_datastore=get_frequency(name)
  
  
  

index_string("string")
index_string("string")
index_string("balloon")
index_string("drapeau")

print(index)







    
    
   
        
