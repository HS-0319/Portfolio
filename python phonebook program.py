class Phonebook:
    def __init__(self, name, number):
        self.name = name
        self.number = number


    def print_info(self):
        print("이름: " + self.name)
        print("전화번호: " + self.number)

def set_phonebook():
    name = input("이름: ")
    number = input("전화번호: ")
    phonebook = Phonebook(name, number)
    return phonebook

def print_menu():
    print("연락처 입력: 1번/ 연락처 삭제: 2번/ 연락처 출력:3번/ 전화번호부 종료:4번")

    menu = input("어떤 메뉴를 선택하시겠습니까? : ")
    return int(menu)

def print_phonebook(phonebook_list):
    for phonebook in phonebook_list:
        phonebook.print_info()

def delete_phonebook(phonebook_list, name):
    for i, phonebook in enumerate(phonebook_list):
        if phonebook.name == name:
            del phonebook_list[i]


def run():

    phonebook_list = []

    while 1:
        menu = print_menu()
        if menu == 1:
            phonebook = set_phonebook()
            phonebook_list.append(phonebook)
        elif menu == 2:
            name = input("삭제할 연락처: ")
            delete_phonebook(phonebook_list, name)
        elif menu == 3:
            print_phonebook(phonebook_list)
        elif menu == 4:
            break

if __name__ == "__main__":
    run()
