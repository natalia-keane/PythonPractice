import socket
from socket import *
import random
import math
import hashlib
import time
import sys


def oddeven():
    i=int(input("What are you thinking?"))

    if (i%2==0):
        print("That's an even number!")
    else:
        print("That's an odd number! Have another?")

def main():
	"""Launcher."""
	oddeven()
	pass
 
if __name__ == "__main__":
	main()
