from robots import Robot, ChefRobot, MedicalRobot, WarRobot


def main():
    def number_of_robot_sensors(robot):
        print(robot.sensors_amount())

    basic_robot = Robot('Robo')
    da_vinci = MedicalRobot('Da Vinci')
    moley = ChefRobot('Moley')
    griffin = WarRobot('Griffin')

    number_of_robot_sensors(basic_robot)
    number_of_robot_sensors(da_vinci)
    number_of_robot_sensors(moley)
    number_of_robot_sensors(griffin)


if __name__ == '__main__':
    main()
