Interpretacion del ejercicio python3 chined.py 1 2

Tareas del Event Loop:

X [main]
X [chain(1)] -> "result1 => result1-B => result1-A"
X [chain(2)] -> "result2 => result2-B => result2-A"
X [primera(1)] -> "result1-A"
X [sleep(5)]  p1
X [primera(2)] -> "result2-A"
X [sleep(6)]  p2
X [primera(1] -> "result2-A")] -> "result1-B => result1-A"
X [sleep(5)]  s1
X [primera(2] -> "result2-A")] -> "result2-B => result2-A"
X [sleep(3)]  s2

