from integer import Integer


def main():
    first_num = Integer(10)
    print(first_num.value)
    second_num = Integer.from_roman("IV")
    print(second_num.value)
    print(Integer.from_float("2.6"))
    print(Integer.from_string(2.6))


if __name__ == "__main__":
    main()
