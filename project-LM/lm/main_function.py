
from functions import add_book, add_faculty, add_student, issue_book_facutly,archive,issue_book_student, return_book_facutly,\
    return_book_student, print_student_details, print_faculty_details, print_book_details, search_book


def show_menu():
    print("")
    print(' '*56 + "~"*40+" "*60)
    print(' '*60 + 'Welcome To Library Management System')
    print('~'*160)
    #print(' '*60 + ""*50+" "*50)
    print('\n')
    #print(' '*58 + "~"*40+" "*60)
    print(' '*60 +'Library Main Menu')
    print(' '*58 + "`"*40+" "*60)
    print(' '*60 +'1. Add student ')
    print(' '*60 +'2. Add faculty ')
    print(' '*60 +'3. Add book')
    print(' '*60 +'4. Issue book to student.')
    print(' '*60 +'5. Issue book to faculty')
    print(' '*60 +'6. Return book by student')
    print(' '*60 +'7. Return book by faculty')
    print(' '*60 +'8. Search book')
    print(' '*60 +'9. Print all students')
    print(' '*60 +'10. Print all faculties ')
    print(' '*60 +'11. Print all books')
    print(' '*58 + "~"*40+" "*60)
    print('~'*160)
    print("dev. by shyam")
    print(' '*135+"submitted to prof.Rahul dubey")

    print("")
    print("")


def show_search_menu():
    print(' '*60 +'1. Search book by ISBN(13) number')
    print(' '*60 +'2. Search book by title.')
    print(' '*60 +'3. Search book by author.')


def get_choice():
    return int(input('Enter number of  the following operations / Press 12 for exit: '))


def get_search_choice():
    return int(input('Enter number of  the following opeartions/ Press 4 for exit: '))


def main():
    show_menu()
    choice = get_choice()

    while choice != 12:
        if choice == 1:
            add_student()
            show_menu()
            
        elif choice == 2:
            add_faculty()
            show_menu()
            
        elif choice == 3:
            add_book()
            show_menu()
            
        elif choice == 4:
            issue_book_student()
            show_menu()
            
        elif choice == 5:
            issue_book_facutly()
            show_menu()
            
        elif choice == 6:
            return_book_student()
            show_menu()
            
        elif choice == 7:
            return_book_facutly()
            show_menu()
            
        elif choice == 8:
            show_search_menu()
            while True:
                try:
                    schoice = get_search_choice()
                    break
                except ValueError:
                    print('Invalid Input. Try again.')
                    
                  #  except ValueError:
                  #  print('Invalid Input. Try again.')
            while schoice != 4:
                if schoice == 1:
                    try:
                        data = int(input('Enter ISBN-13: '))
                    except ValueError:
                        print('Invalid Input, Enter A number.')
                    else:
                        search_book('i', data)
                elif schoice == 2:
                    try:
                        data = input('Enter Title of book: ')
                    except ValueError:
                        print('Invalid Input.')
                    else:
                        search_book('t', data)
                elif schoice == 3:
                    try:
                        data = input('Enter Author Name: ')
                    except ValueError:
                        print('Invalid Input.')
                    else:
                        search_book('a', data)
                else:
                    print('Invalid Input. Try again.')
                show_search_menu()
                schoice = get_search_choice()
                
        elif choice == 9:
            print_student_details()
            show_menu()
            
        elif choice == 10:
            print_faculty_details()
            show_menu()
            
        elif choice == 11:
            print_book_details()
            show_menu()
            
        else:
            print(' '*60 + "----------------Warning--------------")
            print(' '*60 + 'Invalid Choice, Enter Choice Again!')
            show_menu()
        choice = get_choice()


if __name__ == "__main__":
    archive()
    main()

    
    
    
#            show_menu()
            
#         else:
#             print(' '*60 + "----------------Warning--------------")
#             print(' '*60 + 'Invalid Choice, Enter Choice Again!')
#             show_menu()
#         choice = get_choice()
    

