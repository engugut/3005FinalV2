import psycopg2
import os
import sys

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        port="5432")

cursor = conn.cursor()

def getAllUsers():
    cursor.execute("SELECT * FROM users")

    print(cursor.fetchall())
   
def getAllTrainers():
    cursor.execute("SELECT * FROM trainers")

    print(cursor.fetchall())

def getAllAdmins():
    cursor.execute("SELECT * FROM adminstaff")

    print(cursor.fetchall()) 
    
def getTrainerSche():
    cursor.execute("SELECT * FROM trainerschedule")

    print(cursor.fetchall()) 
    
def addUser(name, height, weight, gender, fitness_goals, weight_goal, time_goal, health_metrics):
    cursor.execute('''INSERT INTO users (name, height, weight, gender, fitness_goals, weight_goal, time_goal, health_metrics) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''', (name,height,weight,gender,fitness_goals,weight_goal,time_goal,health_metrics))
    conn.commit()
    #print(cursor.fetchall())
    
def addTrainerSche(trainer_id, app_time_start, app_time_end, day_available):
    cursor.execute('''INSERT INTO trainerschedule (trainer_id, app_time_start, app_time_end, day_available) VALUES(%s,%s,%s,%s)''', (trainer_id,app_time_start,app_time_end,day_available))
    conn.commit()
    #print(cursor.fetchall())
    
def addUserSche(user_id, app_time_start, app_time_end, day_available):
    cursor.execute('''INSERT INTO userschedule (user_id, app_time_start, app_time_end, day_available) VALUES(%s,%s,%s,%s)''', (user_id,app_time_start,app_time_end,day_available))
    conn.commit()
    #print(cursor.fetchall())

def updateUser(user_id, weight, fitness_goals, weight_goal, time_goal, health_metrics):
    cursor.execute(""" UPDATE students SET weight = %s, fitness_goals = %s, weight_goal = %s, time_goal = %s, health_metrics = %s WHERE user_id = %s""", (weight,fitness_goals,weight_goal,time_goal,health_metrics,user_id))
    conn.commit()
    #print(cursor.fetchall())

def getUserExercices(user_id):
    cursor.execute(""" SELECT * FROM exercices WHERE user_id = %s""", (user_id,))
    conn.commit()
    print(cursor.fetchall())

def getMember(name):
    cursor.execute(""" SELECT * FROM users WHERE name = %s""", (name,))
    conn.commit()
    print(cursor.fetchall())
    
def updateRoomNumber(user_id, trainer_id, room_number):
    cursor.execute(""" UPDATE userschedule SET room_number = %s WHERE user_id = %s""", (room_number,user_id))
    cursor.execute(""" UPDATE trainerschedule SET room_number = %s WHERE trainer_id = %s""", (room_number,trainer_id))
    cursor.execute(""" UPDATE rooms SET available = false WHERE room_number = %s""", (room_number,))
    conn.commit()
    #print(cursor.fetchall())
    
def checkEquipment(equipment_id):
    cursor.execute(""" UPDATE equipment SET needs_maintenance = false WHERE equipment_id = %s""", (equipment_id,))
    conn.commit()
    #print(cursor.fetchall())
    
def addClassSche(trainer_id, app_time_start, app_time_end, day_available, room_number):
    cursor.execute('''INSERT INTO classschedule (trainer_id, user_id, app_time_start, app_time_end, day_available, room_number) VALUES(%s,ARRAY[1,2,3],%s,%s,%s,%s)''', (trainer_id,app_time_start,app_time_end,day_available,room_number))
    cursor.execute(""" UPDATE rooms SET available = false WHERE room_number = %s""", (room_number,))
    conn.commit()
    #print(cursor.fetchall())
    
def addPayment(user_id, card_number, expire_date, cvc):
    cursor.execute('''INSERT INTO payments (user_id, card_number, expire_date, cvc, paid) VALUES(%s,%s,%s,%s,true)''', (user_id,card_number,expire_date,cvc))
    conn.commit()
    #print(cursor.fetchall())

if __name__ == '__main__':
	select1 = input("Press 1 for User, 2 for Trainer, and 3 for Admin Staff ")
	
	if select1 == '1':
		userselect = input("Press 1 for New User, 2 for Existing User ")
		if userselect == '1':
			Uname = input("Please enter your Name ")
			Uheight = input("Please enter your height ")
			Uweight = input("Please enter your weight ")
			Ugender = input("Please enter your gender ")
			Ufit = input("Please enter your fitness goals ")
			Uwgoal = input("Please enter your weight goal ")
			Utime = input("Please enter your time goal ")
			Uhealth = input("Please enter your current health ")
			addUser(Uname, Uheight, Uweight, Ugender, Ufit, Uwgoal, Utime, Uhealth)
			print("Thank you for registering")
			os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
		if userselect == '2':
			userselectexist = input("Press 1 to update profile, 2 to view exercices, 3 to add a new appointment ")
			if userselectexist == '1':
				Uid = input("Please enter your ID ")
				Unweight = input("Please enter your new weight ")
				Unfit = input("Please enter your new fitness goals ")
				Unwgoal = input("Please enter your new weight goal ")
				Untime = input("Please enter your new time goal ")
				Unhealth = input("Please enter your new current health ")
				updateUser(Uid, Unweight, Unfit, Unwgoal, Untime, Unhealth)
				os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
			if userselectexist == '2':
				Uid = input("Please enter your ID ")
				getUserExercices(Uid)
				os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
			if userselectexist == '3':
				getTrainerSche()
				Uid = input("Please enter your ID ")
				time_start = input("Please enter your starting time (24-hour format) ")
				day = input("Please enter the day you would like (1999-01-01 format) ")
				addUserSche(Uid, time_start, str(int(time_start[:2]) + 2)+":00:00", day)
				os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
	if select1 == '2':
		userselect = input("Press 1 for view members, 2 for editing your available times ")
		if userselect == '1':
			name = input("Please enter member's name ")
			getMember(name)
			os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
		if userselect == '2':
			Tid = input("Please enter your ID ")
			time_start = input("Please enter your starting time (24-hour format) ")
			day = input("Please enter the day you would like (1999-01-01 format) ")
			addTrainerSche(Tid, time_start, str(int(time_start[:2]) + 2)+":00:0", day)
			os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
	if select1 == '3':
		userselectexist = input("Press 1 to book a room, 2 to check equipment, 3 to book a class, and 4 to take a payment ")
		if userselectexist == '1':
			Uid = input("Please enter the User to book's ID ")
			Tid = input("Please enter the trainer to book's ID ")
			r_n = input("Please enter the room number ")
			updateRoomNumber(Uid, Tid, r_n)
			os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
		if userselectexist == '2':
			equipid = input("Please enter the equipment ID ")
			checkEquipment(equipid)
			os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
		if userselectexist == '3':
			getTrainerSche()
			Tid = input("Please enter the trainer's ID ")
			time_start = input("Please enter your starting time (24-hour format) ")
			day = input("Please enter the day you would like (1999-01-01 format) ")
			r_n = input("Please enter the room number")
			addClassSche(Tid, time_start, str(int(time_start[:2]) + 2)+":00:00", day, r_n)
			os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
		if userselectexist == '4':
			Uid = input("Please enter the User's ID ")
			c_n = input("Please enterthe Card Number ")
			e_d = input("Please enter the expiry date (1999-01-01 format) ")
			cvc = input("Please enter the cvc ")
			addPayment(Uid, c_n, e_d, cvc)
			os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
				
				
