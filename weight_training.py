#1 RM
# percentage of 1 RM
# intensity
# volume
# RPE


print("Have a great workout! Get after it!")

user_weight = 0
exercise_1 = ''


def get_exercise_info():
        exercise_1 = input("""When your workout is complete type finished
Exercise: """)
        if exercise_1.lower() == "finished":
            print("Great job today!")
            quit()
        while True:
            user_sets = input("Number of sets you want to complete: ")
            try:
                num_sets = int(user_sets)
                break

            except:
                print("Type in a number")
        return num_sets

def workout(num_sets):
    for i in range(num_sets):
        print('Set:' , i + 1)
        rep_count = input("Reps: ")

while exercise_1 != 'finished':
    workout(get_exercise_info())



                           


# def workout():
#     exercise_1 = input("""When your workout is complete type finished
# Exercise: """)
#     if exercise_1.lower() == "finished":
#         print("Great job today")
#         quit()
#     else:
#         sets = 0
#         while True:
#             user_sets = input("Number of sets you want to complete: ")
#             try:
#                 num_sets = int(user_sets)
#                 break

#             except:
#                 print("Type in a number")
#         while True:
#             if sets == num_sets:
#                 break
#             sets += 1
#             print("Set:" , sets)
#             rep_count = input("Reps: ")

# exercise_1 = input("""When your workout is complete type finished
# Exersise: """)
# bench_1rm = input('How much weight can you rep on bench one time?: ')
# squat_1rm = input('How much weight can you rep on squat one time?: ')
# deaflift_1rm = input('How much weight can you rep on deadlift one time?: )

# exercise_1 = input("Exersise: ")