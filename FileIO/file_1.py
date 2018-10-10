file = open('background.png', 'rb')
data = file.read()
file.close()

file = open('background_2.png', 'wb')
file.write(data)
file.close()