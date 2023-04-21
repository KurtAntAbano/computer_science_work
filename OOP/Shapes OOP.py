class Shapes():
    def __init__(self, given_fill, given_outline_colour, given_outline_thickness):
        self.fill = given_fill
        self.outline_colour = given_outline_colour
        self.outline_thickness = given_outline_thickness
        self.degrees = 2

    def set_rotate(self, given_angle):
        new_degrees = self.degrees + int(given_angle)
        print("This shape has been rotated", str(new_degrees), "degrees clockwise")
        self.degrees = new_degrees


    def copy(self):
        print("shape has been copied")

    def set_enlarge(self, given_percentage):
         print("This shape has been enlarged by", given_percentage+"%")



class circle(Shapes):
    def __init__(self,given_radius, given_centre, given_fill, given_outline_colour,
                 given_outline_thickness):
        super().__init__(given_fill, given_outline_colour, given_outline_thickness)
        self.radius = given_radius
        self.centre = given_centre
        self.flag = "circle"

    def set_Change_Outline_Colour(self, new_colour):
        self.outline_colour = new_colour
        print("Outline colour has been changed to", self.outline_colour)

    def set_enlarge(self, given_percentage):
        multiplier = (given_percentage/ 100) +1
        self.radius *= multiplier
        print("new radius is", self.radius)

    def properties(self):
        print()




class rectangle(Shapes):
    def __init__(self,given_length, given_width, given_fill, given_outline_colour,
                 given_outline_thickness):
        super().__init__(given_fill, given_outline_colour, given_outline_thickness)
        self.length = given_length
        self.width = given_width
        self.flag = "rectangle"
        self.text = ""


    def set_add_text(self, text):
        print("text has been added to the rectangle")
        self.text = text

    def set_enlarge(self, given_percentage):
        multiplier = (given_percentage / 100) + 1
        self.length *= multiplier
        self.width *= multiplier

        print("length is now", self.length, "width is now", self.width)












# c = circle(10,"(2,1)","black","black", 2 )
# c.set_Change_Outline_Colour("blue")
# c.set_enlarge(50)

r = rectangle(10, 10, "black", "black", 2)
r.set_enlarge(50)










