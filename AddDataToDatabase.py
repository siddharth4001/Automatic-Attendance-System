import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-92301-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Randi",
            "major": "cse",
            "starting_year":2017,
            "total_attendance":8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:11"
        },
    "852741":
        {
            "name": "Randi2",
            "major": "ece",
            "starting_year":2011,
            "total_attendance":75,
            "standing": "G",
            "year": 8,
            "last_attendance_time": "2022-12-11 00:54:11"
        },
    "963852":
        {
            "name": "Randi3",
            "major": "mba",
            "starting_year":2019,
            "total_attendance":9,
            "standing": "B",
            "year": 7,
            "last_attendance_time": "2022-12-11 00:54:11"
        },
    "20204204":
        {
            "name": "Siddharth",
            "major": "cse",
            "starting_year":2020,
            "total_attendance":41,
            "standing": "G",
            "year": 8,
            "last_attendance_time": "2022-12-11 00:54:11"
        }
}

for key,value in data.items():
    ref.child(key).set(value)