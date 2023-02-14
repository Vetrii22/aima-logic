import aima
from aima.utils import *
import aima.logic
clauses = []
clauses.append(aima.utils.expr(" (American (x) & Weapon (y) & Sells (x, y, z) & Hostile (z)) ==> Criminal (x) "))
clauses.append(aima.utils.expr ("Enemy (Nono, America)"))
clauses.append(aima.utils.expr ("Owns (Nono, M1)"))
clauses.append(aima.utils.expr("Missile (M1) "))
clauses.append(aima.utils.expr (" (Missile (x) & Owns (Nono, x)) ==> Sells (West, x, Nono)"))
clauses.append(aima.utils.expr ("American (West) "))
clauses.append(aima.utils.expr ("Missile (x) ==> Weapon (x) "))
KB=aima.logic.FolKB (clauses)
KB.tell(aima.utils.expr('Enemy (Coco, America)'))
KB. tell (aima.utils.expr ('Enemy (Jojo, America)'))
KB. tell (aima.utils.expr ("Enemy (x, America) ==> Hostile (x)"))
hostile=aima.logic.fol_fc_ask (KB, aima.utils.expr('Hostile (x)'))
criminal=aima.logic.fol_fc_ask (KB, aima.utils.expr ('Criminal (x)'))
print (list (hostile))
print('\nCriminal?')
print (list (criminal))
