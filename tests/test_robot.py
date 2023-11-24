from lib.robot import *

def test_robot_instantiates_with_three_hands():
    robot = Robot()

    actual = robot.hands
    expected = 3

    assert actual == expected

# robot should say hi
def test_robot_says_hi():
    robot = Robot()

    actual = robot.says_hi()
    expected = 'Robot says hi'
    assert actual == expected