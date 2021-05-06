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
  
  Returns:
  The number of k-mers possible. Presented as the minimun of either the number of possible characters to the value of k or the length of the string minus k plus 1.
  In order to return locally (independent of this file), continue definition as follows:
    possible = psb_kmers(k, seq)
    print(possible)
  """
    string = len(seq)
    a = 4**k
    b = string - k + 1
    if a > b: #in order to return the possible k-mer with the lowest value
        return b
    else:
        return a


#calculate the observed k-mers relevant to a given string
def obs_kmers(k, seq):
  """
  This function is used to determine the actual number of k-mers observed related to a string of characters. These values are distinct from the possible k-mers (defined in the above function) as they are typically a lesser value than the k-mers possible.
  
  Parameters:
    k (int) = the length of a given string
    seq (string) = the string (or sequence) of characters in question
    
  Returns:
  The observed length of the k-mer for the sequence of characters.
  In order to return locally (independent of this file), continue definition as follows:
    observed = obv_kmers(9,'ATTTGGATT')
    print(observed)
  """
