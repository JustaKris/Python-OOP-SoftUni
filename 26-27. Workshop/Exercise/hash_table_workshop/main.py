from hash_table import HashTable


def main():
    table = HashTable()
    table["name"] = "Peter"
    table["age"] = 25
    print(table)
    print(table.get("name"))
    print(table["age"])
    print(len(table))


if __name__ == '__main__':
    main()