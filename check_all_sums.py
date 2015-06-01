import os
import sys
# import pprint
# pp = pprint.PrettyPrinter(indent=2).pprint

path = os.path.dirname(os.path.abspath(__file__))
dirnames = [sys.argv[1], sys.argv[2]]

def count(mydir):
	counter = {}
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)), mydir)
	for f in os.listdir(path):
		fopen = open(os.path.join(path, f), 'rb')
		for line in fopen:
			split = line.split()
			try:
				counter[split[0].replace('"','')] += int(split[1])
			except KeyError:
				counter[split[0].replace('"','')] = int(split[1])
	return counter

def check_dict_equal(dict1, dict2):
	for k in dict1:
		try:
			if dict2[k] == dict1[k]:
				pass
			else:
				print k, dict1[k], dict2[k]
				return False
		except KeyError:
			print "Key Not Found:", k
			return False
	return True


if __name__ == "__main__":
	"""
	usage::

	python check_all_sums.py out/ emr-out/
	"""

	path = os.path.dirname(os.path.abspath(__file__))
	dirnames = [sys.argv[1], sys.argv[2]]
	a = count(dirnames[0])
	b = count(dirnames[1])

	print "Number of Addresses:", len(a), len(b)

	print "Checks that outputs are equal"
	print a == b
	print check_dict_equal(a, b)
	print check_dict_equal(b, a)
