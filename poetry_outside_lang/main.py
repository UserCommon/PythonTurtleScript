import turtle
from poetry_outside_lang.settings import SETTING


class Executor:
    """
        This class contains Commands & functions that works on this command
    """
    def __init__(self) -> None:
        self.curr_turtle = SETTING.GLOB_TURTLES[SETTING.GLOB_TURTLE_INDEX]
        self.commands: dict = {
                "": self.curr_turtle.do_nothing,
                "S": self.change_turtle,
                "F": self.curr_turtle.move_forward,
                "B": self.curr_turtle.move_backward,
                "L": self.curr_turtle.move_left,
                "R": self.curr_turtle.move_right,
                "G": self.curr_turtle.goto,
                "SS": self.curr_turtle.set_speed,
                }

    def change_turtle(self, turtle_index) -> None:
        SETTING.GLOB_TURTLE_INDEX = turtle_index
        self.curr_turtle = SETTING.GLOB_TURTLES[SETTING.GLOB_TURTLE_INDEX]

    def execute_func(self, command: str, args) -> None:
        print(args)
        self.commands[command](*args)


class Reader:
    """
        Reading file :^)
    """
    def __init__(self, name) -> None:
        self.file = open(name, "r")

    def read(self) -> list[str]:
        return list(map(lambda x: x.replace("\n", ""), self.file.readlines()))


class Interpreter(Reader, Executor):
    """
        Inherits Reader & Executor and makes work
    """
    def __init__(self, name, turtle) -> None:
        Reader.__init__(self, name)
        Executor.__init__(self)
        self.turtle = turtle

    def make_work(self):
        parsed_file = self.read()

        for element in parsed_file:
            if element != "":
                args = element.split()
                first = str(args[0])
                other = list(map(int, args[1:]))
                self.execute_func(first, other)


class Turtle:
    def __init__(self) -> None:
        self.turtle = turtle.Turtle()

    def event_cycle(self) -> None:
        while True:
            pass

    def move_forward(self, quantity) -> None:
        self.turtle.forward(quantity)

    def move_backward(self, quantity) -> None:
        self.turtle.backward(quantity)

    def move_left(self, quantity) -> None:
        self.turtle.left(quantity)

    def move_right(self, quantity) -> None:
        self.turtle.right(quantity)

    def goto(self, x, y) -> None:
        self.turtle.goto(x, y)

    def set_speed(self, quantity) -> None:
        self.turtle.speed(quantity)

    @staticmethod
    def do_nothing(*args, **kwargs):
        pass 



def main():
    SETTING.GLOB_TURTLES.append(Turtle())
    interpreter = Interpreter("poetry_outside_lang/script.do", SETTING.GLOB_TURTLES[SETTING.GLOB_TURTLE_INDEX])
    interpreter.make_work()
    while True:
        pass
    

