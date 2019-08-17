"""
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

eg:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
"""

#Not efficient solution.
def flight_booking(bookings, n):
    tot_list = []
    for i in range(1,n+1):
        j = 0
        summ = 0
        while j<len(bookings): 
            if i in range(bookings[j][0],(bookings[j][1])+1):
                summ+=bookings[j][2]
            j+=1
        tot_list.append(summ)
    print(tot_list)

flight_booking([[1,2,10],[2,3,20],[2,5,25]],5)