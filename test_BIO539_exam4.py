from BIO539_exam4 import *

#for these test functions I used the values and text string from the example k-mer table in the exam instructions to assure that the output values and tables were correct

#Test of the function to determine possible k-mers
  #two tests using the same sequence are included to ensure accuracy 
def test_psb_kmers_1():
  k = 3
  seq = 'ATTTGGATT'
  actual_result = psb_kmers(k, seq)
  expected_result = 7
  assert actual_result == expected_result
  
def test_psb_kmers_2():
  k = 9
  seq = 'ATTTGGATT'
  actual_result = psb_kmers(k, seq)
  expected_result = 1
  assert actual_result == expected_result
  
  
#Test of the function to determine observed k-mers
  #two tests using the same sequence are included to ensure accuracy 
def test_obv_kmers_1():
  k = 3
  seq = 'ATTTGGATT'
  actual_result = obv_kmers(k, seq)
  expected_result = 6
  assert actual_result == expected_result
  
def test_obv_kmers_2():
  k = 9
  seq = 'ATTTGGATT'
  actual_result = obv_kmers(k, seq)
  expected_result = 1
  assert actual_result == expected_result
    
  
#Test of the function to create a dataframe
import pandas as pd
def test_dataframe():
  empty_df = [[4,3], [8,5], [7,6], [6,6], [5,5], [4,4], [3,3], [2,2], [1,1], [40,35]]
  seq = 'ATTTGGATT'
  table = pd.DataFrame(empty_df, columns = ['Possible', 'Observed'], index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'TOTALS'])
  actual_result = dataframe(seq)
  expected_result = table.equals(actual_result)
  assert expected_result == True
  

#Test of the function to calculate linguistic complexity 
def ling_complex():
  empty_df = [[4,3], [8,5], [7,6], [6,6], [5,5], [4,4], [3,3], [2,2], [1,1], [40,35]]
  table = pd.DataFrame(empty_df, columns = ['Possible', 'Observed'], index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'TOTALS'])
  actual_result = ling_complex(table)
  expected_result = (35/40)
  assert actual_result == expected_result
