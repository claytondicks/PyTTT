'''
Created on Apr 18, 2014

@author: Clayton
'''

def checkEqual(iterator):
	try:
		iterator = iter(iterator)
		first = next(iterator)
		return all(first == rest for rest in iterator)
	except StopIteration:
		return True