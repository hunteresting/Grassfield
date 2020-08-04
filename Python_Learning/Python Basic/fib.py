previous = 0
current = 1
count = 20
i = 0

while i < count:
    print(current)
    
    current += previous
    previous = current
    
    i += 1