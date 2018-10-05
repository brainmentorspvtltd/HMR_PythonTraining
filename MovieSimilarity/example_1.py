dataset = [
    {"action" : ['thor','hulk','superman','batman',
                 'spiderman','bahubali','avengers','dhoom',
                 'terminator','mad max', 'saw', 'narnia'
                 ],
     "comedy" : ['padman','stree','3 idiots']
     'biopic' : ['sanju']
        }
    ]

user_1 = {'thor','hulk','superman','batman','padman',
          'spiderman','bahubali','avengers','dhoom','saw'}

user_2 = {'terminator','superman','hulk','saw','bahubali',
          'narnia','mad max','stree','sanju','3 idiots'}

intersection = user_1.intersection(user_2)
union = user_1.union(user_2)

dist = len(intersection) / len(union)
print("Similarity is",dist*100)
