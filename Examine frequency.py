

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
    
#basically what I want to achieve is compare the frequency between the two strings. I need to collect those frequencies from the first string. Once it is done several tests: Which string has the most identical letters and if there are several of them, match them against their respective probabilities. Structure is as follow: compare the keys with nested loops? What I would do is compare the element against all the indexed elemnts and see how much the element scores against each then return the word with which it has the best score. use map/filter and the likes forget the clunky tools.

#step 0 have both strings letter frequencies ready
#step 1:union of set to find letters common in both strings
#step 2: calculate the frequency for the target string ( just the common letters each times)
#step 3: compare the keys in word_target and word_index

def compare_frequency(word_target,word_index):
  word_target_frequency = get_frequency(word_target)
  #loop starts here
  word_index_frequency = index[word_index]
  word_target = set(word_target)
  word_index = set(word_index)
  to_check = word_target&word_index
  #loop compares each letter in the loop set for their frequency
  i = 0
  #used to store the relative values of each common letters in the set 
  relative_index=[]
  #stores the total ranking value once the relative_index has been reduced to the sumn of its points
  global_relative_index={word_target:relative_index}
  while i<=len(to_check):
    if abs(word_index[to_check[i]]-word_target[to_check[i]]) >0.06:
      relative_index.append(0)
    if abs(word_index[to_check[i]]-word_target[to_check[i]]) >0.04:
      relative_index.append(2)
    if abs(word_index[to_check[i]]-word_target[to_check[i]]) >0.02:
      relative_index.append(4)
    if abs(word_index[to_check[i]]-word_target[to_check[i]]) == 0.00:
      relative_index.append(8)
  i+=1
 #reduce the relative index numbers #once I got that number I put it with its compared number in a dictionary
  global_relative_index.update{word_index:(reduce(lambda x, y: x+y, relative_index))}
  
#once this is all finished I start it all over again... 
  


  
print(compare_frequency("house","present"))
  
"""
index_string("string")
index_string("string")
index_string("balloon")
index_string("drapeau")

print(index)

compare_frequency("pablo")"""
