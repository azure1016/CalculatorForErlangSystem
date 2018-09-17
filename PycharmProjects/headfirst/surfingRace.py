import sqlite3

def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if(row['id']==id2find):
            s={}
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
            return(s)
    cursor.close()
    return({})

surfer_id = int(input("input the surfer's id:"))
surfer = find_details(surfer_id)
if len(surfer)>0:
    print("ID:"+surfer['id'])

    print("name:"+surfer['name'])

    print("country:"+surfer['country'])

    print("average:"+surfer['average'])

    print("board:"+surfer['board'])

    print("age:"+surfer['age'])

