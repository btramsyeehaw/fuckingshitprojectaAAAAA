import pandas as pd
#asking for team1
list = pd.ExcelFile('M25_list.xlsx')
tlist = pd.read_excel(list, 'teamlist')
print("Here is a list of teams")
for teamlist in tlist['short']:
    print(teamlist)
while True:
    try:
            teamnumber = int(input('Enter team id: '))
            if teamnumber < 0 or teamnumber > 31:
                raise ValueError
                break
    except ValueError:
        print("Please enter a number between 1 and 30, stop trying to break the program im trying my best")
    except:
        print("Something went horribly wrong")

tl1 = pd.read_excel(list, 'Orioles')
tl2 = pd.read_excel(list, 'Red Sox')
tl3 = pd.read_excel(list, 'Blue Jays')

for a in tl{teamnumber}['date']:
    print(a)
    
#xls = pd.ExcelFile('M25_t1.xlsx')

#df1 = pd.read_excel(xls, 'BAL')
#df2 = pd.read_excel(xls, 'TOR')
#print(df.head())
#for v in df2['id1']:
#    print(v)
