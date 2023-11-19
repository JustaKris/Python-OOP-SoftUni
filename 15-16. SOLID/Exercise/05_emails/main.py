from emails import Email, MyContent


def main():
    email = Email('IM')
    email.set_sender('qmal')
    email.set_receiver('james')
    content = MyContent('Hello, there!')
    email.set_content(content)
    print(email)


if __name__ == '__main__':
    main()
