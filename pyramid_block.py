blocks = int(input('Enter number of blocks: '))
height=0
layer=1


while blocks >=layer:
    blocks -= layer
    height +=1
    layer +=1
    
print('Height of the pyramid is:', height)
    

