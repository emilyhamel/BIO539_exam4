## BIO539 Exam 4: Python
  ### Emily Hamel | May 7, 2021

### Please disregard files TEST_BIO539_exam4.py and README.txt - and instead consider test_BIO539_exam4.py and README.md respectively. These file names/types were later changed and only the most recent versions should be considered.

Toward the end of this function (at the area of def main()), I admit to hitting a mental roadblock. The function returns error messages regarding the lack of definition of terms that seem to be defined to me and will not create the necessary .csv files or print to the command line. I have reached the deadline for this project and am unsure how to remedy this error and cannot produce the correct output. The rest of the elements, however, seem to be operating correctly. 

The intention of the functions in this file is to first count the number of possible and observed k-mers within a given string of possible characters (which are defined as "A, C, G, T" for the purpose of this test.) It is then possible to calculate the overall linguistic complexity of a string of characters from the combination (and respective division) of the observed k-mers and the possible k-mers. 

A data frame containing these possible an observed values with the relevant totals is also produced from this test. 

It is, theoretically, possible to run this function from a terminal command line by typing the name of the file and the string of characters you are interested in determining the linguistic complexity for. This command could look like the following example: 
BIO539_exam4.py sample_strings.txt 
OR
BIO539_exam4.py k, seq (where k is the k value and seq is the string of ATCG characters)

This repository also includes a test file to ensure that the functions proceeding "main" operate correctly. 


### Running BIO539_exam4.py

python 3 (though this should be specified at the beginning of the code file)

BIO539_exam4.py sample_strings.txt


### Running test_BIO539_exam4.py

py.test

