from project.computer_store_app import ComputerStoreApp


def main():
    # Test code
    computer_store = ComputerStoreApp()
    print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
    print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
    # print(computer_store.build_computer("Desktop Computer", "aaaaaaaaaaaaaa", "ssssssssssssss", "AMD Ryzen 7 5700G", 128))
    # print(computer_store.sell_computer(2500, "AMD Ryzen 7 5700G", 127))
    # print(computer_store.warehouse)
    # print(computer_store.profits)


if __name__ == '__main__':
    main()
