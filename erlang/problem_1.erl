% Problem 1

% If we list all the natural numbers below 10 that are multiples
% of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
% Find the sum of all the multiples of 3 or 5 below 1000.

-module(problem_1).
-import(lists, [sum/1, seq/1]).
-export([sum_of_multiples_below_1000/0]).

sum_of_multiples_below_1000()->
	lists:sum([X || X <- lists:seq(1,999), X rem 3 == 0 orelse X rem 5 == 0]).