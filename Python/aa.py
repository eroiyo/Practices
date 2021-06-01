still_alive = input('Answer this question with true or false, are you still alive : ')


while still_alive == "true":
    username = input('Type your name here: ')
    for i in range(3):
        print('Wear mask ' +username)
    break
if still_alive == 'false':
    username = input('Type your name here: ')
    print('it was nice to know you ' +username+ ' \n R.I.P')
if (still_alive !="false" and still_alive !="true"):
    print('your answer need to be true or false')