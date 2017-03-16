
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

def sol_equa(n):
    s = []
    for l in range(n, int(math.sqrt(n)) - 1, -1):
        if n % l == 0:
            y = int((l - (n/l))/4)
            x = int(((n/l) + l)/2)
            if(x >= 0 and y >= 0 and ((x*x) - (4*y*y)) == n):
               s.append([x, y])
    return s
 */