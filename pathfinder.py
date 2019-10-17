from PIL import Image

im = Image.new('RGB', (600, 600), 'black')
im.save('map.png')

def read_word_list(filename): 

    with open(filename) as file:   
        data = file.read()
        data_points = [[int(x) for x in line.split()] for line in data.split("\n")]

    min = data_points[0][0]
    max = data_points[0][0]

    for x in data_points: 
        for integer in x:   
            if integer < min: 
                min = integer
            if integer > max: 
                max = integer           

    colors_big_list = []
    little_rows_of_colors = []

    for rows in data_points: 
        for number in rows: 
            color_int = round(((number - min) / (max-min)) * 255)
            little_rows_of_colors.append(color_int)    
        colors_big_list.append(little_rows_of_colors)
        little_rows_of_colors = []

    print(colors_big_list[0][0])
    print(len(colors_big_list[0]))       
    return data

read_word_list("elevation_small.txt")    

