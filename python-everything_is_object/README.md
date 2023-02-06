## Python - Everything is object


----------------------------------

0. Who am I?

- What function would you use to print the type of an object?

- File: [0-answer.txt](./0-answer.txt)

---

1. Where are you?

- How do you get the variable identifier (which is the memory address in the CPython implementation)?

- File: [1-answer.txt](./1-answer.txt)

---

2. Right count

- In the following code, do a and b point to the same object? Answer with Yes or No.

```
a = 89
b = 100
```

- File: [2-answer.txt](./2-answer.txt)

---

3. Right count =

- In the following code, do a and b point to the same object? Answer with Yes or No.

```
a = 89
b = 89
```

- File: [3-answer.txt](./3-answer.txt)

---

4. Right count =

- In the following code, do a and b point to the same object? Answer with Yes or No.

```
a = 89
b = a
```

- File: [4-answer.txt](./4-answer.txt)

---

5. Right count =+

- In the following code, do a and b point to the same object? Answer with Yes or No.

```
a = 89
b = a + 1
```

- File: [5-answer.txt](./5-answer.txt)

---

6. Is equal

- What do these 3 lines print?

```
s1 = "Best School"
s2 = s1
print(s1 == s2)
```

- File: [6-answer.txt](./6-answer.txt)

---

7. Is the same

- What do these 3 lines print?

```
s1 = "Best"
s2 = s1
print(s1 is s2)
```

- File: [7-answer.txt](./7-answer.txt)

---

8. Is really equal

- What do these 3 lines print?

```
s1 = "Best School"
s2 = "Best School"
print(s1 == s2)
```

- File: [8-answer.txt](./8-answer.txt)

---

9. Is really the same

- What do these 3 lines print?

```
s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
```

- File: [9-answer.txt](./9-answer.txt)

---

10. And with a list, is it equal

- What do these 3 lines print?

```
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 == l2)
```

- File: [10-answer.txt](./10-answer.txt)

---

11. And with a list, is it the same

- What do these 3 lines print?

```
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 is l2)
```

- File: [11-answer.txt](./11-answer.txt)

---

12. And with a list, is it really equal

- What do these 3 lines print?

```
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
```

- File: [12-answer.txt](./12-answer.txt)

---

13. And with a list, is it really the same

- What do these 3 lines print?

```
l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)
```

- File: [13-answer.txt](./13-answer.txt)

---

14. List append

- What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

- File: [14-answer.txt](./14-answer.txt)

---

15. List add

- What does this script print?

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

- File: [15-answer.txt](./15-answer.txt)

---

16. Integer incrementation

- What does this script print?

```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

- File: [16-answer.txt](./16-answer.txt)

---

17. List incrementation

- What does this script print?

```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

- File: [17-answer.txt](./17-answer.txt)

---

18. List assignation

- What does this script print?

```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

- File: [18-answer.txt](./18-answer.txt)

---

19. Copy a list object

- A function def copy_list(a_list): that returns a copy of a list.

- File: [19-copy_list.py](./19-copy_list.py)

---

20. Tuple or not?

```
a = ()
```

- Is a a tuple? Answer with Yes or No.

- File: [20-answer.txt](./20-answer.txt)

---

21. Tuple or not?

```
a = (1, 2)
```

- Is a a tuple? Answer with Yes or No.

- File: [21-answer.txt](./21-answer.txt)

---

22. Tuple or not?

```
a = (1)
```

- Is a a tuple? Answer with Yes or No.

- File: [22-answer.txt](./22-answer.txt)

---

23. Tuple or not?

```
a = (1, )
```

- Is a a tuple? Answer with Yes or No.

- File: [23-answer.txt](./23-answer.txt)

---

24. Who I am?

- What does this script print?

```
a = (1)
b = (1)
a is b
```

- File: [24-answer.txt](./24-answer.txt)

---

25. Tuple or not

- What does this script print?

```
a = (1, 2)
b = (1, 2)
a is b
```

- File: [25-answer.txt](./25-answer.txt)

---

26. Empty is not empty

- What does this script print?

```
a = ()
b = ()
a is b
```

- File: [26-answer.txt](./26-answer.txt)

---

27. Still the same?

```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

- File: [27-answer.txt](./27-answer.txt)

---

28. Same or not?

```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

- File: [28-answer.txt](./28-answer.txt)

---
