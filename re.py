python3 -c 'with open("range.txt","w") as f:
 for p in range(72,161):
  f.write(f"# Puzzle {p}\n{1<<(p-1):x}:{(1<<p)-1:x}\n")'
