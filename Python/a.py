still_alive = input('Answer this question with true or false, are you still alive : ')


while (still_alive !="false" and still_alive !="true"):
    still_alive = input('your answer need to be true or false, type again : ')

username = input('Type your name here: ')


if still_alive == "true":
    for i in range(3):
        print('Wear mask ' +username)

if still_alive =="false":
    print('it was nice to know you ' +username+ ' \n R.I.P')