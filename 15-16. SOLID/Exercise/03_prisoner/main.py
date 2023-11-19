from prisoner import Prisoner


def main():
    prisoner = Prisoner()
    print("The prisoner trying to walk to north by 10 and east by - 3.")
    try:
        prisoner.walk_north(10)
        prisoner.walk_east(-3)
    except:
        pass
    print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
    print(f"The current position of the prisoner: {prisoner.position}")


if __name__ == '__main__':
    main()
