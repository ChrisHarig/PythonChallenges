'''
This challenge is inspired by nonogram puzzles, but you don't need to be familiar with these puzzles in order to complete the challenge.

A binary array is an array consisting of only the values 0 and 1. Given a binary array of any length, return an array of positive integers that represent the lengths of the 
sets of consecutive 1's in the input array, in order from left to right.

nonogramrow([]) => []
nonogramrow([0,0,0,0,0]) => []
nonogramrow([1,1,1,1,1]) => [5]
nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) => [5,4]
nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) => [2,1,3]
nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) => [2,1,3]
nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) => [1,1,1,1,1,1,1,1]
As a special case, nonogram puzzles usually represent the empty output ([]) as [0]. If you prefer to do it this way, that's fine, but 0 should not appear in the output 
in any other case.
https://www.reddit.com/r/dailyprogrammer/comments/o4uyzl/20210621_challenge_395_easy_nonogram_row/
'''

# Initial Solution: Iterate through the array and keep a running total of the number of consectutive "1"'s. When a "0" is reached, append the current sum to the list 
# and set the current sum back to 0.

nonograminput = [0,1,0,1,1,1,0,1]
listtotal = []
currentsum = 0

def nonogramrow(nonograminput):
    for number in nonograminput:
        if number == 1:
            currentsum += 1
        else:
            listtotal.append(currentsum)
            currentsum = 0
            