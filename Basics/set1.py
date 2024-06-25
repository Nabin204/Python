# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
s=student_id

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 118, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

student_id.add(80)
print(student_id)
student_id.remove(115)
print(student_id)
student_id.discard(80)
print(student_id)
student_id.pop()
print(student_id)

print(s.intersection(vowel_letters))
print(s.union(vowel_letters))
print(s.symmetric_difference(mixed_set))
print(s)

s.difference_update(mixed_set)
print(s)