from numpy import double
from solver import run
from sys import argv

# Check the number of arguments
if len(argv) not in {3, 4}:
  print("[ERROR] Wrong number of arguments.")
  exit()

# Check the iterative method
if argv[1] not in {"J", "GS"}:
  print("[ERROR] Wrong iterative method.")
  exit()

# Check the gama parameter
try:
  double(argv[2])
except ValueError:
  print("[ERROR] Wrong gama parameter.")
  exit()

# Check the verbose parameter
if (len(argv) == 4) and argv[3] != "-v":
  print("[ERROR] Wrong verbose parameter.")
  exit()

run(argv[1], double(argv[2]), False if (len(argv) == 3) else True)
