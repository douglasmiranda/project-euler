% The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
% Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
-module(problem_48).
-import(lists, [sum/1, seq/1]).
-import(string, [str/1]).
-export([the_last_ten_digits/0]).

% This implementation of pow function
% is necessary because the math:pow have
% a limit to work with big exponentiation
% maybe could lose a bit of performance, but
% I don't know another way to fix this
pow(N, M) -> pow(N, M, 1).
pow(_N, 0, Total) -> Total;
pow(N, M, Total) ->
	pow(N, M - 1, Total * N).

the_last_ten_digits()->
	IntResult = lists:sum([pow(X,X) || X <- lists:seq(1,1000)]),
	StringResult = erlang:integer_to_list(IntResult),
	erlang:list_to_integer(string:substr(StringResult, string:len(StringResult)-9, 10)).