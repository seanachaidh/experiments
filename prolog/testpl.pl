/*
 * Eerste prolog testjes
 */
 
append([], L, L).
append([H|T], L2, [H|L3]) :- append(T, L2, L3).

/*
suffix([], []).
suffix(X, X).
suffix([H|T], [H1|T1]) :- suffix(T, [H1|T1]).
*/

limit(X) :- X > 0,X < 6
Baker(X) :- X =\= 5.
Cooper(X) :- X =\= 1.
Fletcher(X) :- X =\= 1, X =\= 5.
Miller(X, Y) :- X = Y + 1.
Smith(X, Y) :- 