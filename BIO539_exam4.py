#!/usr/bin/env python3

#necessary libraries 
import argparse
import pandas as pd


#calculate the possible k-mer values for a sequence of characters
def psb_kmers(k, seq):
  """
  This function is used in order to caluculate the number of k-mers possible for a given string of ATCG characters.
  
  Parameters:
  k (int) = the length of a given string
  seq (string) = the string (or sequence) of characters in question
  
  Return:
  value = the number of k-mers possible. Presented as the minimun of either the number of possible characters to the value of k or the length of the string minus k plus 1.
  
  In order to return locally (independent of this file), continue definition as follows:
    possible = psb_kmers(k, seq)
    print(possible)
  """
  string = len(seq) #counts the length of the given string of characters
  a = 4**k
  b = string - k + 1
  if a > b: #in order to return the possible k-mer with the lowest value
    return b
  else:
    return a
        
        
#calculate the observed k-mers relevant to a given string
def obv_kmers(k, seq):
  """
  This function is used to determine the actual number of k-mers observed related to a string of characters. These values are distinct from the possible k-mers (defined in the above function) as they are typically a lesser value than the k-mers possible - though they may be of equal value..
  
  Parameters:
    k (int) = the length of a given string
    seq (string) = the string (or sequence) of characters in question
    
  Return:
  count (value) = the observed length of the k-mer for the sequence of characters.
  
  In order to return locally (independent of this file), continue definition as follows:
    observed = obv_kmers(k, seq)
    print(observed)
  """
  list_complete = list() #list to be populated
  list_other = list() #list to be populated
  count = 0 
  string = len(seq)
  for i in range(1, string+1): #with "i" being an integer within a given range and the range extending from 1 to the value of characters in the string. The string must also include +1 in order for the dataframe to print the correct number of rows per sequence.
    kmer_value = seq[(i-1):(i-1+k)] #calculates the k-mer for the k-value specified in the parameters. (+k-1 is used due to it being the opposite method utilized to determine a minimum possible k-mer value)
    if len(kmer_value) == k: #only include the kmer_value for the specified k value
      list_complete.append(kmer_value) #create a list of the relevant k-mers
    for item in list_complete:
      if item not in list_other: #if other k-mers exist that are not included in "list_complete", create a new list of these unique values
        count += 1 #add one to the count of the values if there are additional values not included in the "list_complete"
        list_other.append(item) 
  return(count) #produce the count of the observed k-mers


#create a data frame containing the all k values (between 1 and the given parameter) and the corresponding possible and observed k-mers
def dataframe(seq):
  """
  This function is used to create a data frame of the possible k-mers and the observed k-mers, along with their respective totals.
  
  Parameters:
  seq (string) = the string (or sequence) of characters in question
  
  Return:
  data frame = a table of correct values with a row to sum each column
  
  In order to return locally (independent of this file), continue definition either by defining values for psb_kmers and obv_kmers functions or by running those functions in conjunction with is one - and by defining a value for k independent of the data frame function:
    DF = dataframe(seq)
    print(DF)
  """
  empty_df = list() #list to be populated
  string = len(seq)
  for i in range(1, string+1): #the "+1" was added to the string in order to troubleshoot the table printing one row less than the number of characters in a string, I am unsure why this was the case (but adding this +1 to the ranges in this function and the obv_kmers function fixes this issue)
    k = i #sets the value of k equal to the range from 1 to the length of the string (which is defined above as the "i", or index, value)
    empty_df.append([psb_kmers(k, seq), obv_kmers(k, seq)]) #add the values from the psb_kmers and the obv_kmers to the empty_df list
  df = pd.DataFrame(empty_df, index = range(1, string+1), columns = ['Possible', 'Observed'])
  df.loc['TOTALS'] = df.sum() #sums the values
  return(df)



#calculate the linguistic complexity of the string of characters
def ling_complex(dataframe):
  """
  This function is used to calculate the linguistic complexity of a given string of characters. This linguistic complexity is defined as the total number of observed k-mers divided by the total number of possible k-mers.
  
  Parameters:
  dataframe = the data frame created by the "dataframe" function and the totals calculated within the table are used to divide these total values
  
  Return:
  LC (value) = the calculated linguistic complexity of a given string
  
  In order to return locally (independent of this file), continue definition as follows:
    value_lc = ling_complex(dataframe(seq))
    print(value_lc)
  """
  LC = dataframe.loc['TOTALS', 'Observed']/dataframe.loc['TOTALS', 'Possible'] #division of the total observed k-mers and the total possible k-mers to determine the linguistic complexity
  return(LC)


#the main function seeks to combine the functions written above (psb_kmers, obv_kmers, dataframe, and ling_complex) to output the information as its own file
def main(args):
  """
  The main function looking at the functions defined above. This function seeks to create an output file that shows the data frame and the linguistic complexity of a given series of characters as defined in the 'sample_strings.txt' file.
  
  Parameters:
  Text File (.txt) = a file containing strings of characters that the user wishes to analyse 
  
  Returns:
  File (.csv) = an output file containing the dataframe for the string of characters
  Linguistic Complexity (command line statement) = a statement on the command line outlining the calculated linguistic complexity for the string of characters
  
  I am aware that something is amiss with this function and I am unable to determine the missing piece
  """
  file_seq = 'sample_strings.txt'
  with open(file_seq, 'r') as string_file: #read in the file from the command line
    char_sequence = string_file.read()
  create_df = dataframe(char_sequence) #build a data frame using the ATCG string from the file
  create_lc = ling_complex(char_sequence) #calculate the linguistic complexity of the ATCG string from the file
  create_df.to.csv('output')
  print("linguistic complexity =", create_lc, "for", char_sequence)


#argument parser function, written in order to define main function arguments from the command line
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(args.seq, type=argparse.FileType('r')) #in order to read the strings from the text file
  args = parser.parse_args()
  main(args)  



