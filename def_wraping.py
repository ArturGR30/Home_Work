
def wrap_brackets( text ):
  return "(" + text + ")"


def wrap_brackets1():
  return "[[[" + wrap_brackets("12345") + "]]]"

def wrap_brackets2():
  return "<<<" + wrap_brackets1() + ">>>"

