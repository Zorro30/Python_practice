'''
Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill=[2,4,6]. Anna declines to eat item k=bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2=3. If he includes the cost of bill[2], he will calculate (2+4+6)/2=6. In the second case, he should refund 3 to Anna.

eg:
input:
4 1
3 10 2 9
12
output:
5

input:
4 1
3 10 2 9
7
output:
Bon Appetit

'''

def bonAppetit(bill, k, b):
    count = 0
    for i in range(len(bill)):
        if i==k:
            continue
        else:
            count+=bill[i]
    if count/2==b:
        return ("Bon Appetit")
    else:
        return int(b-count/2)

nk = input().rstrip().split()

n = int(nk[0])

k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)