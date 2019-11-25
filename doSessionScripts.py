
import pdb


def make_a_sound():
    print("quack")

make_a_sound()

def agree():
    return True

if agree():
    print("Splendid")
else:
    print("That was unexpected")

def echo(aString):
    return aString + " " + aString

echo("Pystarters")

pdb.set_trace()
