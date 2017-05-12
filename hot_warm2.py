def user_input(message, incorrect):
    user_input = input(message)
    while len(user_input) != 3:
        user_input = input(incorrect)
    return user_input


def set_difficulty():
    tries = 0
    while tries not in ['1', '2', '3']:
        tries = input('''Choose your difficulty level
        1 - hard
        2 - medium
        3 - easy\n''')
    if tries == '1':
        tries = 5
    elif tries == '2':
        tries = 10
    elif tries == '3':
        tries = 15
    return tries


def seach_known_with_guess(serch_number, know_number):
    cont = 0
    list_output = []
    for digit in know_number:
        if digit == serch_number[cont]:
            list_output.append('Hot')
        elif digit in serch_number:
            list_output.append('Warm')
        cont += 1
    if list_output == []:
        list_output.append('Cold')
    return list_output


def play_single_game(know_number, tries):
    main_count = 0
    list_output = []
    while list_output != ['Hot', 'Hot', 'Hot']:
        serch_number = user_input('Guess the number: ', 'It has to be 3 digit long: ')
        list_output = seach_known_with_guess(serch_number, know_number)
        print(' '.join(list_output))
        main_count += 1
        if main_count == tries:
            exit()

play = True
while play:
    know_number = user_input("Choose nuber to guess: ", "Incorrect, it has to be 3 digit long: ")
    tries = set_difficulty()
    play_single_game(know_number, tries)
    break


