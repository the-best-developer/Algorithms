#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

    # A negative number means this isn't a valid action
    if n < 0:
        return 0

    # Cookie monster can skip breakfast (eat 0 cookies)
    if n == 0:
        return 1
        
    # Check if cache exists and check if it has a value
    elif cache and cache[n] > 0:
        # If value found, we have already cached the result so return
        return cache[n]
    # If we have a valid number, recurse the calculation and store the results in the cache
    else:
        # This is only done once to create the cache at the start
        if not cache:
            cache = {i : 0 for i in range(0, n+1)}
        # Store results for later
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        
        # Return our results
        return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')