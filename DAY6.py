
def prime(number):
    while True:
        divisions = 0
        for i in range(2, number):
            if number % i == 0:
                break  
            else:
                divisions+=1
        if divisions+2 == number:
            return number
        else:
            number+=1
                
