from homework import Homework
from exam import Exam

print(" _________________ HOMEWORK ___________________")
g = Homework()
g.grade = 95
assert g.grade >= 95
print(f"ocena: {g.grade}")

print(" _________________ EXAM ___________________")
ex= Exam()
ex.part_a_grade = 88
ex.part_b_grade = 65

assert ex.part_a_grade >=33
assert ex.part_b_grade >=33

print(f'wyniki egzaminu -> part a: {ex.part_a_grade}, part b: {ex.part_b_grade}')
