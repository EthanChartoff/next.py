class Pixel:
    def __init__(self, x = 0, y = 0, red = 0, green = 0, blue = 0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue
 
    def set_coords(self, x: int, y: int) -> None:
        """Set the coordinates of the pixel."""
        self._x = x
        self._y = y
    
    def set_grayscale(self):
        self._red = self._green = self._blue = (self._red + self._green + self._blue) // 3

    def print_pixel_info(self):
        """ 
        Print a string representation of the pixel. 
        If 2 color values are 0 and the other is greater then 50.
        """
        if self._red == 0 and self._green == 0 and self._blue > 50:
            print(f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) BLUE')
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            print(f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) RED')
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            print(f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) GREEN')
        else:
            print(f'X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})')

def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()