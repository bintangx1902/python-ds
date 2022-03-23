n, k = list(map(int, input().split()))
data = []
trans = []


def append_data(name, balance):
    d_key = ('name', 'balance')
    d_val = (name, balance)
    d_data = dict(zip(d_key, d_val))
    data.append(d_data)


def append_trans(sd, rec, amount):
    d_key = ('from', 'rec', 'amount')
    d_val = (sd, rec, amount)
    d_data = dict(zip(d_key, d_val))
    trans.append(d_data)


for name in range(n):
    nm, bal = list(map(str, input().split()))
    append_data(nm, int(bal))

for tr in range(k):
    sd, rec, amount = list(map(str, input().split()))
    append_trans(sd, rec, int(amount))

"""
check balance if want trans 
if balance is greater then sended them do it else cancel it

"""


def check():
    for tr in trans:
        sender = tr['from']
        to = tr['rec']
        amount = tr['amount']
        # check sender balance
        # for dt in data:
        #     if dt['name'] == sender:
        #         balance = dt['balance']
        #         if amount < balance:
        #             dt['balance'] -= amount
        #         if dt['name'] == to:
        #             dt['balance'] += amount
        for z in data:
            for key, val in z.items():
                if sender == val:
                    data[z]['balance'] -= amount
                if to == val:
                    data[z]


    print("\n")
    for x in data:
        print(f"{x['name']} {x['balance']}")


check()
