'''The number n is Evil if it has an even number of 1's in its binary expansion.
First ten: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

The number n is Odious if it has an odd number of 1's in its binary expansion.
First ten: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

You have to write a function that determine if a number is Evil of Odious, 
function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.

good luck :)'''


def evil(n):
    bin = "{0:b}".format(n)
    count = {}
    for s in bin:
    	if s in count:
    		count[s] += 1
    	else:
    		count[s] = 1

    if(count['1']%2 == 0):
    	return "It's Evil!"
    else:
    	return "It's Odious!"

'''def evil(n):
    return "It's %s!" % ["Evil","Odious"][bin(n).count("1")%2]'''


'''def evil(n):
    return 'It\'s {}!'.format(('Evil', 'Odious')[bin(n).count('1') % 2])'''