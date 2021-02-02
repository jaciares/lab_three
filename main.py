def alphabetical_states():
    pass


def search_state():
    pass


def top_five_states():
    pass


def update_state_pop():
    pass


def exit_program():
    pass


def app_banner():
    print('*' * 90)
    title = "Python State Capital and Flower List Application"
    centered_title = title.center(90, " ")
    print(centered_title)
    print('*' * 90)


def menu():
    app_banner()

    print('1. Display all U.S States in Alphabetical order along with\n\tthe '
          'Capital, State Population, and Flower\n')

    print('2. Search for a specific state and display the appropriate '
          'Capital name,\n\tState population, and an image of the associated '
          'State Flower.\n')

    print('3. Provide a Bar graph of the top 5 populated States showing '
          'their overall population.\n')

    print('4. Update the overall state population for a specific date.\n')

    print('5. Exit the program\n')

    try:
            user_selection = int(input('Please make a selection from 1-5: '))
            if user_selection == 1:
                alphabetical_states()
            if user_selection == 2:
                search_state()
            if user_selection == 3:
                top_five_states()
            if user_selection == 4:
                update_state_pop()
            if user_selection == 5:
                exit_program()

    except ValueError:
        print('Please enter a number 1 - 5!')
        menu()



def main():
    menu()


if __name__ == '__main__':
    main()
