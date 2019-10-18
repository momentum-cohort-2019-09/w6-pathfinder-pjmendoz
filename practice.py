import math
from PIL import Image

with open('elevation_small.txt') as text_file:   
        text_contents = text_file.read()

        elevations = [[int(x) for x in line.split()] for line in text_contents.split("\n")]

        map_height = (len(elevations))
        map_width = (len(elevations))

        min = elevations[0][0]
        max = elevations[0][0]

        for x in elevations: 
            for integer in x:   
                if integer < min: 
                    min = integer
                if integer > max: 
                    max = integer           

        colors_big_list = []
        little_rows_of_colors = []

        for rows in elevations: 
            for number in rows: 
                color_int = round(((number - min) / (max-min)) * 255)
                little_rows_of_colors.append(color_int)    
            colors_big_list.append(little_rows_of_colors)
            little_rows_of_colors = []
     
        im = Image.new('RGB', (map_width, map_height), 'black')
        im.save('map.png')



      

