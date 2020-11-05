prefrence = input("Hi there, \nWhat to like ,more TV or Movies? ")
drama_shows = ["got", "mr robot", "breaking bad", "house", "sv", "shameless", "prison break"]
drama_shows_question = "Chose your favorite tv show from the following: GOT, house, breaking bad,\
 \nprison break, la casa depapel, Mr robot, SV, shameless. "
action_shows_question = "Chose your favorite tv show from the following: banshee, stranger things, the boys,\
 \nvikings, peaky blinders, ncis, the walking dead, limitless"
action_shows = ["banshee", "stranger things", "the boys", "vikings", "limitless"]
comedy_shows_question = ("Chose your favorite tv show from the following: tbbt, friends, \nthe office, himym, \
brooklyn99,the it crowd ")
comedy_shows = ["tbbt", "friends", "the office"]
movie_drama_question = ("Chose your favorite movie: the godfather, pulp fiction, \nshawshank redemption, notebook,\
 moonlight, the shape of water ")
movie_drama = ["the godfather", "pulp fiction", "shawshank redemption"]
movie_action_question = ("Chose your favorite movie: kill bill, bad boys, \nfast and furious, john wick,\
 sharknado, crank ")
movie_action = ["kill bill", "bad boys", "john wick"]
movie_comedy_question = ("Chose your favorite movie: friday, 21 jump street, \nted, zoolander, spy, Pixels ")
movie_comedy = ["friday", "21 jump street", "ted"]


if str(prefrence.lower()) == "tv":
    genretv = input("What's your favorite genre? Drama, Action, Comedy ")
    if genretv.lower() == "drama":
        favshowdrama = input(drama_shows_question)
        if favshowdrama.lower() in drama_shows:
            print("Good Taste!")
        else:
            print("Not the best!")
    elif genretv.lower() == "action":
        favshowaction = input(action_shows_question)
        if favshowaction.lower() in action_shows:
            print("Good Taste!")
        else:
            print("Not the best!")
    elif genretv.lower() == "comedy":
        favshowcomedy = input(comedy_shows_question)
        if favshowcomedy.lower() in comedy_shows:
            print("Good Taste!")
        else:
            print("Not the best!")
elif str(prefrence.lower()) == "movies":
    genremovies = input("What's your favorite genre? Drama, action, comedy ")
    if genremovies.lower() == "drama":
        favmoviedrama = input(drama_shows_question)
        if favmoviedrama.lower() in drama_shows:
            print("Good Taste!")
        else:
            print("Not the best!")
    elif genremovies.lower() == "action":
        favmovieaction = input(movie_action_question)
        if  favmovieaction.lower() in movie_action:
            print("Good Taste!")
        else:
            print("Not the best!")
    elif genremovies.lower() == "comedy":
        favmoviecomedy = input (movie_comedy_question)
        if favmoviecomedy.lower() in movie_comedy:
            print("Good Taste!")
        else:
            print("Not the best!")
else:
    print("Try Again!")