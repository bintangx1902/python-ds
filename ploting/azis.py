datas = {
    "totalmain": 0,
    "goals": 0,
    "totalmenang": 0,
    "totalkalah": 0,
    "totaldraws": 0,
    "totalgolkemasukan": 0,
    "totalselisihgol": 0,
    "totalpoint": 0,
}

with open('number/azis.txt', 'r') as f:
    isi_file = f.read().splitlines()

teams = {}


def klasemen(hasilklasemen):
    for isi in hasilklasemen:
        list_temp = isi.split()

        team1 = list_temp[0]
        team2 = list_temp[3]

        goal1 = int(list_temp[1])
        goal2 = int(list_temp[2])

        if team1 not in teams:
            teams[team1] = datas.copy()

        if team2 not in teams:
            teams[team2] = datas.copy()

        teams[team1]["totalmain"] += 1
        teams[team2]["totalmain"] += 1

        teams[team1]["goals"] += goal1
        teams[team2]["goals"] += goal2

        if goal1 > goal2:
            teams[team1]["totalmenang"] += 1
            teams[team2]["totalkalah"] += 1

            teams[team1]["totalgolkemasukan"] += goal2
            teams[team2]["totalgolkemasukan"] += goal1

            teams[team1]["totalselisihgol"] += goal1 - goal2
            teams[team2]["totalselisihgol"] += goal2 - goal1

            teams[team1]["totalpoint"] += 3
            teams[team2]["totalpoint"] += 0

        elif goal1 < goal2:
            teams[team2]["totalmenang"] += 1
            teams[team1]["totalkalah"] += 1

            teams[team2]["totalgolkemasukan"] += goal1
            teams[team1]["totalgolkemasukan"] += goal2

            teams[team1]["totalselisihgol"] += goal2 - goal1
            teams[team2]["totalselisihgol"] += goal1 - goal2

            teams[team2]["totalpoint"] += 3
            teams[team1]["totalpoint"] += 0

        else:
            teams[team1]["totaldraws"] += 1
            teams[team2]["totaldraws"] += 1
            teams[team1]["totalgolkemasukan"] += 0
            teams[team2]["totalgolkemasukan"] += 0


klasemen(isi_file)

for key, value in teams.items():
    diff = teams[key]['goals'] - teams[key]['totalgolkemasukan']
    teams[key]['totalselisihgol'] = diff


for key, value in teams.items():
    print(f"{key} : {value}", end='\n\n')


