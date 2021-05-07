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
def test_dataframe():
  k =
  seq = ''
  actual_result = 
  expected_result =
  assert actual_result == expected_result

#Test of the function to determine the linguistic complexity
def test_ling_complex():
  actual_result =
  expected_result =
  assert actual_result == expected_result
  
