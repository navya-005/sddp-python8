# Python3 program to print  
#  even length words in a string  
  
def printWords(s): 
      
    # split the string  
    s = s.split(' ')  
      
    # iterate in words of string  
    for word in s:  
          
        # if length is even  
        if len(word)%2==0: 
            print(word)  
  
  
# Driver Code  
s =  'Print every word in this sentence that has an even number of letters'
printWords(s) 
