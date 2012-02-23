% 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
% What is the sum of the digits of the number 2**1000?

-module(problem_16).
-import(math, [pow/2]).
-export([sum_of_the_digits_of_the_number_2_pow_1000/0]).

sum_of_the_digits_of_the_number_2_pow_1000()->
	BigNumber = erlang:integer_to_list(trunc(math:pow(2, 1000))),
	lists:sum([erlang:list_to_integer(X) || X<-re:split(BigNumber, "", [{return, list}, trim])]).