known_people = ['john', 'anna', 'marry']
# person = input('enter the person you know: ')
#
# if person in known_people:
#     print('you know {}!'.format(person))
# else:
#     print("you don't know {}!".format(person))

def who_do_you_know():
    person = input('enter the persons you know separated by commas: ')
    # split the string into list
    # return that list
    person_list = person.split(',')
    people_no_space=[]
    for person in person_list:
        people_no_space.append(person.strip())  # to remove white space after commas!

    return person_list

def ask_user():
    # ask user for a name
    # see if name is in the list of people they know
    # print ot that they know person

    person = input('enter the person you know: ')
    if person in who_do_you_know():
        print('You know this person {}'.format(person))


# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 67, 88)}


# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list

def average_grade_all_students(student_list):
    total = 0   # sum of all grades
    count = 0   # amount of all grades
    for student in student_list:
        total = total + sum(student['grades'])
        count = count + len(student['grades'])

    return total / count




