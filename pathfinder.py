from PIL import Image

class Map: 

    def _init_(self, file):
        self.file = file

    def read_file(self, file): 

        with open(file) as text_file:   
            text_contents = text_file.read()

        self.elevations = [[int(x) for x in line.split()] for line in text_contents.split("\n")]
    
    def find_min_and_max(self):

        min = self.elevations[0][0]
        max = self.elevations[0][0]

        for x in self.elevations: 
            for integer in x:   
                if integer < min: 
                    min = integer
                if integer > max: 
                    max = integer           

    def create_color_list(self):
        colors_big_list = []
        little_rows_of_colors = []

        for rows in self.elevations: 
            for number in rows: 
                color_int = round(((number - min) / (max-min)) * 255)
                little_rows_of_colors.append(color_int)    
            colors_big_list.append(little_rows_of_colors)
            little_rows_of_colors = []
     
    def create_map_image(self):
        im = Image.new('RGB', (600, 600), 'black')
        im.save('map.png')


if __name__ == "__main__":
    map = Map("elevation_small.txt")


      

