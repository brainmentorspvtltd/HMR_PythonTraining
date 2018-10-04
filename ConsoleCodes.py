Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/02-Loops/04-FibSeries.py =
0
1
1
2
3
5
8
13
21
34
55
89
>>> 
= RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/02-Loops/04-FibSeries.py =
01123581321345589
>>> 
= RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/02-Loops/04-FibSeries.py =
0 1 1 2 3 5 8 13 21 34 55 89 
>>> 
==== RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/01-IfElse.py ====
Enter your message : hello
Hi there...
>>> 
==== RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/01-IfElse.py ====
Enter your message : Hello
I Don't Understand
>>> 
==== RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/01-IfElse.py ====
Enter your message : hello
Hi there...
>>> 
 RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/02-LogicalOperators.py 
Enter your message : hi
Hi there...
>>> 
 RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/02-LogicalOperators.py 
Enter your message : hi
Hi there...
Enter your message : hey
Hi there...
Enter your message : hello
Hi there...
Enter your message : bye
Bye
>>> 
 RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/02-LogicalOperators.py 
Enter your message : hiee
I Don't Understand
Enter your message : bye
Bye
>>> hello_intent = ['hello', 'hi', 'hie', 'hey']
>>> for word in hello_intent:
	if word == "hi":
		print("Found")

		
Found
>>> for i in range(len(hello_intent)):
	if hello_intent[i] == 'hello':
		print("Found")

		
Found
>>> "hello" in hello_intent
True
>>> 
 RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/03-MembershipOperator.py 
Enter your message : hello
Hi there...
Enter your message : yo
Hi there...
Enter your message : bye
Bye
>>> import webbrowser
>>> webbrowser.open('google.com')
True
>>> usermessage = "open facebook"
>>> usermessage.split()
['open', 'facebook']
>>> usermessage.split()[1]
'facebook'
>>> usermessage.split()[1] + '.com'
'facebook.com'
>>> 
 RESTART: C:/Users/asus/Desktop/HMR_PythonTraining/Chat/03-MembershipOperator.py 
Enter your message : hi
Hi there...
Enter your message : hello
Hi there...
Enter your message : open google
Enter your message : open facebook
Enter your message : bye
Bye
>>> 
