# TODO: add your users and hashed passwords here
import bcrypt
users = [{'john@doe.com': '$2b$12$/TYFvXOy9wDQUOn5SKgTzedwiqB6cm.UIfPewBnz0kUQeK9Eu4mSC'},
         {'dan@mail.com':'$2b$12$o4LEmadAC71hdf4pnqJbyuPE0DxkrPmKThB7s2diKDEZnZ6ebY6GS'}]

questions = {
    "I ______ bus on Mondays.": {
        "a. 'm going to work with": False,
        "b. 'm going to work by": False,
        "c. go to work with": False,
        "d. go to work by": True
    },
    "Sorry, but this chair is ______.": {
        "a. me": False,
        "b. mine": True,
        "c. my": False,
        "d. our": False
    },
    "A: 'How old ______?'   B: 'I ______ .'": {
        "a. are you / am 20 years old.": True,
        "b. have you / have 20 years old.": False,
        "c. are you / am 20 years.": False,
        "d. do you have / have 20 years.": False
    },
    "I ______ to the cinema.": {
        "a. usually don't go": False,
        "b. don't usually go": True,
        "c. don't go usually": False,
        "d. do not go usually": False
    },
    "Where ______ ?": {
        "a. your sister works": False,
        "b. your sister work": False,
        "c. does your sister work": True,
        "d. do your sister work": False
    }
}

def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


if __name__ == '__main__':
    # Test the above functions manually
    original_password = 'my_very_secureP4ssword!'  # From registration form
    print('original_password: ' + original_password)

    hashed_password = hash_password(original_password)  # This shall be saved in the DB
    print('hashed_password: ' + hashed_password)

    user_input_password = 'Hey Siri, what is my password?'  # From a login form, a mistyped input
    is_matching = verify_password(user_input_password, hashed_password)
    print('is_matching: ' + str(is_matching))

    user_input_password = 'my_very_secureP4ssword!'  # From a login form, the correct input
    is_matching = verify_password(user_input_password, hashed_password)
    print('is_matching: ' + str(is_matching))
