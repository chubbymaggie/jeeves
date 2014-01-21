'''
List-type functions for Jeeves containers.
'''
import JeevesLib
from fast.AST import FExpr

@JeevesLib.supports_jeeves
def jhasElt(lst, f):
  acc = False
  # Short circuits.
  for elt in lst:
    isElt = f(elt) # TODO: This should eventually be japply of f to elt.
    if isinstance(isElt, FExpr):
      acc = JeevesLib.jor(lambda: isElt, lambda: acc)
    else:
      if isElt:
        return True
  return acc

@JeevesLib.supports_jeeves
def jhas(lst, v):
  return jhasElt(lst, lambda x: x == v)

@JeevesLib.supports_jeeves
def jall(lst):
  acc = True
  for elt in lst:
    acc = JeevesLib.jand(lambda: elt, lambda: acc)
  return acc
