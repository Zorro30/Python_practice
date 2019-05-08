import webbrowser

def T20():
    print("So you seem an IPL fan!")
    print ("if you want to know about recent T20 tournaments:")
    print ("Press 1: For IPL."\
           "\nPress 2: For Super Smash."\
           "\nPress 3: For Big Bash.")
    option= int(input(">"))
    
    if option == 1:
        webbrowser.open('http://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/matches')    
    elif option == 2:
        webbrowser.open('http://www.cricbuzz.com/cricket-series/2605/super-smash-2017-18/matches')
    elif option == 3:
        webbrowser.open('http://www.cricbuzz.com/cricket-series/2600/big-bash-league-2017-18/matches')
    else:
        print ("Wrong Option.")  
    

def Test():
    print ("Hey OldMan, It's good to see that people still love test.")
    print ("if you want to know recent Test Series:")
    print ("Press 1: For Ashes."\
           "\nPress 2: For India vs South Africa."\
           "\nPress 3: For Pakistan vs New Zealand.")

    option1 = int(input(">"))
    
    if option1 == 1:
        webbrowser.open('http://www.cricbuzz.com/cricket-series/2538/the-ashes-2017-18/matches')
    elif option1 == 2:
        webbrowser.open('http://www.cricbuzz.com/cricket-series/2632/india-tour-of-south-africa-2017-18/matches')
    elif option1 == 3:
        webbrowser.open('http://www.cricbuzz.com/cricket-series/2603/pakistan-tour-of-new-zealand-2018/matches')
    else:
        print ("Wrong Option.")