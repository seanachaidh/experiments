def chunks (l, n):
	final = []
	for x in range(0, len(l), n):
		final.append(l[x:x+n])
	return final

def latin(l)
    #We spreiden eerst de lijst over drie lijsten. Telkens drie elementen nemend
    x = []
    y = []
    z = []

    for i in range(0, len(l), 3):
        if x%9 == 0:
            z.append(l[i:i+3])
        elif x%6 == 0:
            y.append(l[i:i+3])
        elif x%3 == 0:
            x.append(l[i:i+3])
    final = []
    lenlist = len(x) / 9
    xfin = chunks(x, 9)
    yfin = chunks(y, 9)
    zfin = chunks(z, 9)

    final.append(xfin)
    final.append(yfin)
    final.append(zfin)

    return final


def vertical(l, n):
	final = []
	for x in range(n):
		final.append(l[x:len(l):n])
	return final

#functies die kijken of alles uniek is

def is_unique(l):
    seen = list() #ik kan hier ook gebruik maken vanh een set om ervoor te zorgen dat het een beetje sneller gaat
    return not any(i in seen or seen.append(i) for i in l)

class Base:
    def __init__(self):
	pass
    def is_goal(self):
	pass
    def init_state(self):
	pass
    def succ(self):
	pass
	#voorlopig gaan we geen heuristiek toepassen
class Sudoku(Base):
    def __init__(self, init):
        Base.__init__()
        self._init = init
        self._board = init

    def is_goal(self):
        #Eerst kijken we horizontaal
        firstcheck  = any(is_unque(i) for i in chunks(self._board, 9))
        secondcheck = any(is_unique(i) for i in latin(self._board))
        thirdcheck = any(is_unique(i) for i in vertical(self._board, 9))

        return firstcheck and secondcheck and thirdcheck
    
    def init_state(self):
        return self._init
    def succ(self):
        tryrange = range(1, 10)
        
        
