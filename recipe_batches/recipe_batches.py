#!/usr/bin/python

import math
recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 103, 'butter': 480, 'flour': 51 }

def recipe_batches(recipe, ingredients):

  # This number has to be large so we can compare a smaller number to it
  min_batches = 1000

  # Iterate through the dictionary keys
  for rkey in recipe:
      # Check if key exists
      if rkey in ingredients:
          # Calculate how many batches of the recipe we can make with our ingredients
          batches = ingredients[rkey] // recipe[rkey]
          # If 0, return here since we can't make a recipe
          if batches == 0:
              return 0

          # If not, find the smallest amount, this is the maximum batches you can make
          elif batches < min_batches:
            min_batches = batches
      # If key wasn't found, return 0
      else:
        return 0

  return min_batches

recipe_batches(recipe, ingredients)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))