robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}


def fight(robot_1, robot_2, tactics):
    if not robot_1['speed'] >= robot_2['speed']:
        robot_1, robot_2 = robot_2, robot_1

    while robot_1['health'] > 0 and robot_2['health'] > 0:
        if robot_1["tactics"]:
            robot_2['health'] -= tactics[robot_1["tactics"][0]]
            robot_1["tactics"].pop(0)
        if robot_2["tactics"]:
            robot_1['health'] -= tactics[robot_2["tactics"][0]]
            robot_2["tactics"].pop(0)
        if not robot_1["tactics"] and not robot_1["tactics"]:
            if robot_1['health'] > robot_2['health']:
                return f'{robot_1["name"]} has won the fight.'
            if robot_2['health'] > robot_1['health']:
                return f'{robot_2["name"]} has won the fight.'
            return 'The fight was a draw.'
    return f'{robot_1["name"]} has won the fight.' if robot_1['health'] > robot_2['health'] else f'{robot_2["name"]} has won the fight.'


print(fight(robot_1, robot_2, tactics))