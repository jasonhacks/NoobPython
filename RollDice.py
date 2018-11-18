"""This is a program that rolls some dice and calculates some output. I am probably going to fuck this up."""

from random import randint
from time import sleep

def get_user_guess():
	guess = int(raw_input("Enter your guess: "))
  	return guess
  
def roll_dice(number_of_sides):
	first_roll = randint(1,number_of_sides)
	second_roll = randint(1,number_of_sides)
	max_val = number_of_sides * 2
	print "The maximum possible roll is %d" % (max_val)
	guess = get_user_guess()
	if guess > max_val:
		print "Your guess is too high."
	else:
		print "Rolling..."
		sleep(2)
		print str("The first roll is %d") % (first_roll)
		sleep(1)
		print str("The second roll is %d") % (second_roll)
		total_roll = first_roll + second_roll
		print "Result..."
		sleep(1)
		if guess == total_roll:
				print "YOU'RE THE WINNER!"
		else:
				print "You are a big ol loser."
				
roll_dice(6)
