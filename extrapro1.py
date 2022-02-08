# 1. Create a class Rectangle with attributes length and width,
# each of which defaults to 1. Provide methods that calculate
# the perimeter and the area of the rectangle. Also, provide
# setter and getter for the length and width attributes.
# The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:
    """
    descibes rectangle
    """

    def __init__(self):
        """
        constructor for Rectange class

        """
        self.__length = 1
        self.__width = 1

    def __str__(self):
        return 'Rectangle: perimeter is ' + str(self.perim()) + ' square is ' + str(self.square())

    def set_sides(self, length: (int, float), width: (int, float)):
        """
        setter for Rectangle class
        :param length:
        :param width:
        :return:
        """
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError('Must be int or float')
        if 0.0 < length < 20.0 and 0.0 < width < 20.0:
            self.__length = length
            self.__width = width
        else:
            raise ValueError('Width and length must be in range(0< <20)')

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def perim(self):
        """
        calculate a perimeter of rectangle
        :return: perimiter
        """
        return self.__width * 2 + self.__length * 2

    def square(self):
        """
        calculate a square of rectangle
        :return: square
        """
        return self.__width * self.__length


if __name__ == '__main__':
    rect1 = Rectangle()
    try:
        rect1.set_sides(10, 5)
        print(rect1)
        print(rect1.get_length())
        print(rect1.get_width())
    except Exception as error:
        print('Error : ', error)

