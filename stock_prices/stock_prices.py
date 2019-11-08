#!/usr/bin/python

import argparse
from cmath import inf
def find_max_profit(prices):
    global_min = -inf
    for i in range(len(prices)-1):
       mn = max(prices[i+1:])
       if  mn-prices[i] >global_min:
           global_min = mn-prices[i]
    return global_min


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
