import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        port="5432")

cursor = conn.cursor()

def getAllStudents():
    cursor.execute("SELECT * FROM users")

    print(cursor.fetchall())
   
def getAllTrainers():
    cursor.execute("SELECT * FROM trainers")

    print(cursor.fetchall())

def getAllAdmins():
    cursor.execute("SELECT * FROM adminstaff")

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

def updateUser(user_id, weight, fitness_goals, time_goal, health_metrics):
    cursor.execute(""" UPDATE students SET weight = %s, fitness_goals = %s, time_goal = %s, health_metrics = %s WHERE user_id = %s""", (weight,fitness_goals,time_goal,health_metrics,user_id))
    conn.commit()
    #print(cursor.fetchall())

def getUserExercices(user_id):
    cursor.execute(""" SELECT * FROM exercices WHERE user_id = %s""", (user_id))
    conn.commit()
    print(cursor.fetchall())

def getMember(name):
    cursor.execute(""" SELECT * FROM users WHERE name = %s""", (name))
    conn.commit()
    print(cursor.fetchall())
    
def updateRoomNumber(room_id, room_number):
    cursor.execute(""" UPDATE userschedule SET room_number = %s WHERE room_id = %s""", (room_number,room_id))
    cursor.execute(""" UPDATE trainerschedule SET room_number = %s WHERE room_id = %s""", (room_number,room_id))
    conn.commit()
    #print(cursor.fetchall())
    
def updateRoomNumber(equipment_id):
    cursor.execute(""" UPDATE equipment SET needs_maintenance = true WHERE equipment_id = %s""", (equipment_id))
    conn.commit()
    #print(cursor.fetchall())
    
def addClassSche(trainer_id, app_time_start, app_time_end, day_available, room_number):
    cursor.execute('''INSERT INTO userschedule (trainer_id, user_id, app_time_start, app_time_end, day_available, room_number) VALUES(%s,ARRAY[1,2,3],%s,%s,%s,%s)''', (user_id,app_time_start,app_time_end,day_available,room_number))
    conn.commit()
    #print(cursor.fetchall())
    
def addPayment(user_id, card_number, expire_date, cvc):
    cursor.execute('''INSERT INTO payments (user_id, card_number, expire_date, cvc, paid) VALUES(%s,%s,%s,%s,true)''', (user_id,card_number,expire_date,cvc))
    conn.commit()
    #print(cursor.fetchall())

if __name__ == '__main__':
	#getAllStudents()
	#updateStudentEmail("2", "jane.human@earth.com")
	#addStudent("Bob", "Morbly" , "bobbybob@bob.xyz", "2023-03-19")
	#deleteStudent("2")
