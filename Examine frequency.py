

####################################Don't Touch!########################################################
#data handling function

index={}
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
   
index_string("pablo")
index_string("rocky")
index_string("rigo")
index_string("nino")

print (index)

###############################################################################################

def comparator(string,database):
  target = string
  indextarget = database[0]
  return database[0]
  
 




print(comparator("bono", index))
















 
