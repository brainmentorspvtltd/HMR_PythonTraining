Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = [5,6,7,10.5,,True,'hello']
SyntaxError: invalid syntax
>>> list_1 = [5,6,7,10.5,True,'hello']
>>> type(list_1)
<class 'list'>
>>> list_1[0] = 'bye'
>>> a = "hello python"
>>> a[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> list_1[0:3]
['bye', 6, 7]
>>> list_1
['bye', 6, 7, 10.5, True, 'hello']
>>> list_1 = 23,
>>> list_1
(23,)
>>> even = []
>>> even.append(2)
>>> even
[2]
>>> even.append(4)
>>> even
[2, 4]
>>> even.append(6,8,10)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    even.append(6,8,10)
TypeError: append() takes exactly one argument (3 given)
>>> even = []
>>> for i in range(0,51):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> even.pop()
50
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> even.pop(5)
10
>>> even
[0, 2, 4, 6, 8, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> even.index(20)
9
>>> even.remove(7)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    even.remove(7)
ValueError: list.remove(x): x not in list
>>> even.remove(6)
>>> even.insert(6,100)
>>> even
[0, 2, 4, 8, 12, 14, 100, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> odd = [i for i in range(1,50)]
>>> odd
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> odd = [i for i in range(1,50) if i % 2 != 0]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> even.append(odd)
>>> even
[0, 2, 4, 8, 12, 14, 100, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]]
>>> even.pop()
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> even.extend(odd)
>>> evenm
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    evenm
NameError: name 'evenm' is not defined
>>> even
[0, 2, 4, 8, 12, 14, 100, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> sorted(even)
[0, 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 100]
>>> even
[0, 2, 4, 8, 12, 14, 100, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> even.sort()
>>> even
[0, 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 100]
>>> even.sort(reverse = True)
>>> even
[100, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9, 8, 7, 5, 4, 3, 2, 1, 0]
>>> tuple_1 = 1,2,34,5,6,7,8
>>> tuple_1
(1, 2, 34, 5, 6, 7, 8)
>>> tuple_1[0] = 12
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    tuple_1[0] = 12
TypeError: 'tuple' object does not support item assignment
>>> d = {'name':'ram','age':30,'sal':35000,'company':'TCS'}
>>> d.keys()
dict_keys(['name', 'age', 'sal', 'company'])
>>> d.values()
dict_values(['ram', 30, 35000, 'TCS'])
>>> d.items()
dict_items([('name', 'ram'), ('age', 30), ('sal', 35000), ('company', 'TCS')])
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'ram'
>>> for data in dL
SyntaxError: invalid syntax
>>> for data in d:
	print(data)

	
name
age
sal
company
>>> for data in d.items():
	print(data)

	
('name', 'ram')
('age', 30)
('sal', 35000)
('company', 'TCS')
>>> data = {'name':['ram','shyam','gopal'], 'company' : ['tcs','hcl','ibm']}
>>> data['name']
['ram', 'shyam', 'gopal']
>>> for i in range(len(data['name'])):
	print(data['name'][i], data['company'][i])

	
ram tcs
shyam hcl
gopal ibm
>>> set_1 = {2,4,5,6,7,8,9,12,14,15}
>>> set_2 = {9,8,7,6,12,14,18,91}
>>> set_1 & set_2
{6, 7, 8, 9, 12, 14}
>>> set_1.intersection(set_2)
{6, 7, 8, 9, 12, 14}
>>> set_1 | set_2
{2, 4, 5, 6, 7, 8, 9, 12, 14, 15, 18, 91}
>>> set_1.union(set_2)
{2, 4, 5, 6, 7, 8, 9, 12, 14, 15, 18, 91}
>>> 
 RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/MovieSimilarity/example_1.py 
Similarity is 0.25
>>> 
 RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/MovieSimilarity/example_1.py 
Similarity is 25.0
>>> 
