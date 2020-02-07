#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
  # This is a hack to start at a very low price to compare a better price too
  best_price = -1000000000000000

  # Check if valid array/list
  if len(prices) == 0:
    return 0
  
  # Loop over the array
  for i in range(0, len(prices)):
      # Take the current item and compare with the rest of the array
      for j in range(i + 1, len(prices)):
          # We calculate the profit from current price subtracted from another price from the array
          curr_price = prices[j] - prices[i]
          # If these buy/sell prices are more the most profitable so far, set the profit as best_price
          if best_price < curr_price:
              best_price = curr_price

  return best_price


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))