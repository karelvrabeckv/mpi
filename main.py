from numpy import double
from solver import run

print("\n[METHOD: J | GAMA: 5]")
run("J", double(5), False)

print("[METHOD: J | GAMA: 2]")
run("J", double(2), False)

print("[METHOD: J | GAMA: 0.5]")
run("J", double(0.5), False)

print("[METHOD: GS | GAMA: 5]")
run("GS", double(5), False)

print("[METHOD: GS | GAMA: 2]")
run("GS", double(2), False)

print("[METHOD: GS | GAMA: 0.5]")
run("GS", double(0.5), False)
