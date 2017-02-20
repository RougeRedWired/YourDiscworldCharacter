def score(string):
      score = 5
      index = "Goliath"
      if string.find(letter)!=-1:
         if string[letter][frequency] == index[string][letter][frequency]:
            score +=5
         elif (string[letter][frequency] - index[string][letter][frequency] <= 1):
         score +=3

         elif (string[letter][frequency] - index[string][letter][frequency] > 1):
         score +=1

      return score
