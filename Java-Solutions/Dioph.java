
/*
In mathematics, a Diophantine equation is a polynomial equation, 
usually in two or more unknowns, 
such that only the integer solutions are sought or studied.

In this kata we want to find all integers x, y (x >= 0, y >= 0) 
solutions of a diophantine equation of the form

 x ^ 2 - 4 * y ^ 2 = n
where the unknowns are x and y and n is a given positive number. 
Solutions x, y will be given as an array of arrays (Ruby, Python, Clojure, JS, CS, TS)

 [[x1, y1], [x2, y2] ....]
as an array of tuples (Haskell, C++, Elixir)

 [(x1, y1), (x2, y2) ....] or { {x1, y1}, {x2, y2} ....} or [{x1, y1}, {x2, y2} ....]
as an array of pairs (C, see example tests)

{{x1, y1}{x2, y2} ....}
and as a string (Java, C#)

 "[[x1, y1], [x2, y2] ....]"
in decreasing order of the positive xi. If there is no solution returns [] or "[]".

Examples:

sol_equa(90005) -->  [[45003, 22501], [9003, 4499], [981, 467], [309, 37]]

sol_equa(90002) --> []

(Java, C#)

solEquaStr(90005) --> "[[45003, 22501], [9003, 4499], [981, 467], [309, 37]]"

solEquaStr(90002) --> "[]"
Hint: x ^ 2 - 4 y ^ 2 = (x - 2y) (x + 2y).
*/


public class Dioph {
	
	public static void main(String[] args){
		System.out.println(solEquaStr(90000004));
	}

	public static String solEquaStr(long n) {
		long x, y;
		String s = "[";
	    
		for(long l = n; l >= Math.sqrt(n); l--)
			if(n % l == 0){
				y = (l - (n/l)) / 4;
				x = ((n/l) + l) / 2;
				if (x >= 0 && y >=  0 && ((x*x) - (4*y*y)) == n){
					s += "[" + String.valueOf(x) +", " + String.valueOf(y) + "], ";
				}
		  }

		if (!s.equals("["))
			s = s.substring(0, s.length()-2) + "]";
		else
			s += "]";
		return s;
	}
	
	
}

/*

import math
from itertools import chain, cycle, accumulate # last of which is Python 3 only

def factors(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))
    
    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r

def sol_equa(n):
    s = []
    f = sorted(factors(n), reverse=True)
    for l in f:
        if n % l == 0:
            y = int((l - (n/l))/4)
            x = int(((n/l) + l)/2)
            if(x >= 0 and y >= 0 and ((x*x) - (4*y*y)) == n):
               s.append([x, y])
    return s


===================================
Best Practices:

import math
def sol_equa(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            if (i + j) % 2 == 0 and (j - i) % 4 == 0:
                x = (i + j) // 2
                y = (j - i) // 4
                res.append([x, y])
            
    return res
 */