
import random

def getp(pmin=20, pmax=70):
	found = [2,3]
	pafter = random.randint(pmin, pmax)
	c = 4

	while True:
		c +=1
		for f in found:
			if c % f == 0:
				break
		else:	
			found.append(c)
	
		if c > pafter:
			return c
			#break


if __name__ == "__main__":
	print ">>>> %d <<<<" % getp()
