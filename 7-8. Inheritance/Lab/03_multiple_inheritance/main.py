# from project.employee import Employee
# from project.person import Person
from project.teacher import Teacher


def main():
    teach = Teacher()
    print(teach.sleep())
    print(teach.get_fired())
    print(teach.teach())


if __name__ == "__main__":
    main()
