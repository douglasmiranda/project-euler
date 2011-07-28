% The sum of the squares of the first ten natural numbers is,

% 1**2 + 2**2 + ... + 10**2 = 385

% The square of the sum of the first ten natural numbers is,

% (1 + 2 + ... + 10)**2 = 55**2 = 3025

% Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

% Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

-module(problem_6).
-import(lists, [sum/1, seq/1]).
-export([difference/0]).

difference()->
	Square_of_sum = math:pow(lists:sum([X || X <- lists:seq(1,100)]), 2),
	Sum_of_square = lists:sum([X*X || X <- lists:seq(1,100)]),
	round(Square_of_sum - Sum_of_square).