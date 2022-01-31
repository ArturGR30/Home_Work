############## NUMERIC DATA  ##################
integers = [-5, 0, 5, 10, -10, 15]

def selectPositive( vector ):
    if type(vector) != list:
        print("ERROR: selectPosive works only with lists !!!")
        return
    pos_vector = []
    for v in vector:
        if v >= 0:
            pos_vector.append(v)
    return pos_vector

## HW 2. receives a vector of ints, returns a vector of negative ints
## HW 2*. make sure these funtion work only with: lists, sets, tuples
def selectNegative( vector):
    if type(vector) != list:
        if type(vector) != tuple:  
            if type(vector) != set:
                print("ERROR: selectNegative works only with lists, sets, tuples !!!")
                return  

    negative_vector = []
    for v in vector:
        if v < 0:
            negative_vector.append(v)
    return negative_vector

print(selectPositive(integers))
print(selectNegative(integers))