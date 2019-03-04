class Editor:
    def view_document(self):
        print("Some document")

    def edit_document(self):
        print("Access denied")


class Pro_Editor(Editor):
    def edit_document(self):
        print("Access accepted")


def main():
    password = input("Input password: ")
    if password == "123":
        obj = Pro_Editor()
    else:
        obj = Editor()
    obj.view_document()
    obj.edit_document()


if __name__ == '__main__':
    main()
