from profile import Profile


def main():
    # Test 1
    # profile_with_invalid_password = Profile('My_username', 'My-password')

    # Test 2
    # profile_with_invalid_username = Profile('Too_long_username', 'Any')

    # Test 3
    correct_profile = Profile("Username", "Passw0rd")
    print(correct_profile)


if __name__ == "__main__":
    main()
