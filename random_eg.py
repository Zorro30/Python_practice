'To extract only dates from a string without using regex'

string1 = 'hi 20-18-2018 hello i am good what is the time 10:20. I am supposed to go abroad on 20-09-2018'

dates = [w for w in string1.split(' ') if not w.isalpha() and len(w)==10]
print(dates)