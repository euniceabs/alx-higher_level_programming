#!/usr/bin/python3
"""a base model class module
"""
import json
import csv
import turtle


class Base:
    """" The base of all other classes to be created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string"""
        if json_string is None or json_string == "[]":
            return[]
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_inst = cls(1)
        else:
            dummy_inst = cls(1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                obj_dicts = cls.from_json_string(json_data)
                instances = [cls.create(**obj_dict) for obj_dict in obj_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes instances to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(*map(int, row[1:]))
                    elif cls.__name__ == "Square":
                        instance = cls(*map(int, row[1:]))
                    instance.id = int(row[0])
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        screen = turtle.Screen()
        screen.setup(800, 600)
        pen = turtle.Turtle()
        pen.speed(0)

        for obj in list_rectangles + list_squares:
            pen.penup()
            pen.goto(obj.x, obj.y)
            pen.pendown()
            if isinstance(obj, Rectangle):
                for _ in range(2):
                    pen.forward(obj.width)
                    pen.right(90)
                    pen.forward(obj.height)
                    pen.right(90)
            elif isinstance(obj, Square):
                for _ in range(4):
                    pen.forward(obj.size)
                    pen.right(90)

        turtle.done()
