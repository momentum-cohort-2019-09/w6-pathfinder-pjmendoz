from PIL import Image

im = Image.new('RGBA', (600, 600), 'black')
im.save('map.png')

def read_word_list(filename): 
    with open(filename) as file:   
        data = file.read().split()
        
    return data


print(read_word_list("elevation_small.txt"))

# class Map: 

#     def _init_(self): 
