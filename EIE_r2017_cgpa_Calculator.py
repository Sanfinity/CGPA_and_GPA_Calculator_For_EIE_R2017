#!/usr/bin/env python3

# Created By J.Santhosh Kumar
# I have created this cgpa and gpa calcultor only for EIE R2017 batch students
# If you want to use for other regulation or other dept just alter the eie_r2017 dictionary

# Importing important imports
import math 

# Declaring E&I 2017 Regulation with subjects and credits 
eie_r2017 = {'sem1':(('Foundational English', 4),
                     ('Mathematics', 4),
                     ('Engineering Physics', 3),
                     ('Engineering Chemistry', 3),
                     ('Computing Techniques', 3),
                     ('Basic Sciences Lab', 2),
                     ('Computer Practices Lab', 2)),
             'sem2':(('Mathematics - II', 4),
                     ('Materials Science for Technologists', 3),
                     ('Engineering Graphics', 4),
                     ('Environmental Science and Engineering', 3),
                     ('Signals and Systems', 3),
                     ('Analysis of Electric Circuits', 3),
                     ('Engineering Practices Lab', 2),
                     ('Circuit Simulation Lab', 2)),
             'sem3':(('Linear Algebra and Numerical Methods', 4),
                     ('Electrical and Electronic Measurements', 3),
                     ('Electrical Machines', 3),
                     ('Electronics for Analog Signal Processing I', 4),
                     ('Fundamentals of Pneumatics and Hydraulics', 3),
                     ('Instrument Transducers', 4),
                     ('Electrical Machines Lab', 2),
                     ('Electronics for Analog Signal Processing Lab', 2)),
             'sem4':(('Probability and Random Processes', 4),
                     ('Digital Principles and Applications', 3),
                     ('Electronics for Analog Signal Processing II', 4),
                     ('Fundamentals of Thermodynamics and Fluid Mechanics', 3),
                     ('Industrial Instrumentation I', 3),
                     ('Principles of Communication Engineering', 3),
                     ('Digital System Design Laboratory', 2),
                     ('Sensors and Signal Conditioning Circuits Laboratory', 2)),
             'sem5':(('Control Systems', 4),
                     ('Fundamentals of Data Structures and Algorithms', 3),
                     ('Industrial Instrumentation II', 3),
                     ('Microprocessors, Microcontrollers and Applications', 3),
                     ('Professional Elective I', 3),
                     ('Open Elective I', 3),
                     ('Data Structures Lab', 2),
                     ('Microprocessor and Interfacing Lab', 2)),
             'sem6':(('Discrete Time Signal Processing', 4),
                     ('Process Control', 4),
                     ('Project Management and Finance', 3),
                     ('Employability skills', 3),
                     ('Professional Elective II', 3),
                     ('Open Elective II', 3),
                     ('Industrial Instrumentation Lab', 2),
                     ('Process Control Lab', 2)),
             'sem7':(('Computer Control of Processes', 4),
                     ('Logic and Distributed Control System', 3),
                     ('Professional Elective III', 3),
                     ('Professional Elective IV', 3),
                     ('Open Elective III', 3),
                     ('Industrial Automation Lab', 2),
                     ('Instrumentation System Design Lab', 2),
                     ('Mini Project /Industrial Training /Internship', 3)),
             'sem8':(('Professional Elective V', 3),
                     ('Professional Elective VI', 3),
                     ('Project work', 10))
                      }

# Declaring Grades and there points
grades = {'O':10,'A+':9,'A':8,'B+':7,'B':6,'RA':0,'SA':0}
gpa_list = []

# Used to round the cgpa or gpa correctly
def round_half_up(n, decimals=0): 
    multiplier = 10 ** decimals 
    return math.floor(n * multiplier + 0.5) / multiplier 

# GPA and CGPA calculator
class cgpa_gpa_calculator:

    def __init(self):
        self.decide_factor = 'no'
        self.cgpa_val = 0

    # Getting User Information and Calculation Mode
    def get_user_info(self):
        self.username = input("Enter Your Name : ")
        self.reg_no = int(input("Enter Your Reg No : "))
        print("\nWelcome",self.username,"!")
        self.decide_factor=input("Are you a Student of Electronics and Instrumentation regulation-2017 (y or n) : ")
        if self.decide_factor.lower() == 'y' or self.decide_factor.lower() == 'yes':
            print(str(self.username)+", What you would like to calculate :-\n\n\tMode\t\t\tKey\n\tGPA only\t\t1\n\tCGPA from GPA\t\t2\n\tBoth GPA and CGPA\t3")
            self.choice = int(input("\nEnter Your Corresponding Key : "))
        else:
            print("This Program is not yet optimized for you yet...sorry:(")
            return
    # For calculating the GPA only
    def gpa(self,sem_no):
        print("\nEnter Your Grades for the Corresponding Subjects in Semester {}:-\n".format(sem_no))
        total = 0
        total_no_of_credits = 0
        for i in eie_r2017['sem'+str(sem_no)]:
            mark = grades[input('Enter Your Grade in '+ i[0] +' : ').upper()]
            total += mark * i[1]
            total_no_of_credits += i[1]

        gpa = total/total_no_of_credits
        print('\nYour GPA in Semester {} is {} '.format(sem_no,round_half_up(gpa,2)))
        gpa_list.append(round_half_up(gpa,2))
        return total,total_no_of_credits

    # For Calculating CGPA from GPA
    def cgpa(self):
        total_no_of_sems = int(input('\nEnter the Total No of Semester You want to find CGPA for : '))
        total = 0
        for i in range(1,total_no_of_sems+1):
            gpa = float(input('Enter the GPA for Semester {} : '.format(i)))
            gpa_list.append(round_half_up(gpa,2))
            total += gpa
        cgpa = total/total_no_of_sems
        print('\nYour CGPA after {} Semesters is {}'.format(i,round_half_up(cgpa,2)))
        self.cgpa_val = round_half_up(cgpa,2)

    # For Calculating Both GPA and CGPA
    def cgpa_and_gpa(self):
        total_no_of_sems = int(input("\nEnter the Total No of Semester You want to find GPA and CGPA for : "))
        grand_total = 0
        temp_total = 0
        temp_total_credits=0
        grand_total_credits = 0
        for i in range(1,total_no_of_sems+1):
            temp_total,temp_total_credits = self.gpa(i)
            grand_total += temp_total
            grand_total_credits += temp_total_credits
        cgpa = grand_total/grand_total_credits
        print('\nYour CGPA after {} Semesters is {}'.format(i,round_half_up(cgpa,2)))
        self.cgpa_val = round_half_up(cgpa,2)

    # For Creating a Final Report of all your GPA and CGPA
    def create_report(self, sem_no = None):
        print("\n\n***********GENERATED REPORT***********")
        print("Name\t\t:",self.username)
        print("Register_No\t:",self.reg_no)
        print("Department\t: Electronics and Instrumentation")
        if sem_no == None:
            for i in range(0,len(gpa_list)):
                print("Semester {} GPA\t: {}".format(i+1,gpa_list[i]))
        else:
            print("Semester {} GPA\t: {}".format(sem_no,gpa_list[0]))

        try:
            print("CGPA \t\t:",self.cgpa_val)
        except:
            pass
    # This Run the calculations in correct order and generate results
    def run(self):
        self.get_user_info()
        sem_no = 0
        if self.decide_factor.lower() != 'y' and self.decide_factor.lower() != 'yes':
            return
        if self.choice == 1:
            sem_no = int(input('\nWhich Semester would you like to calculate the GPA : '))
            self.gpa(sem_no)
        elif self.choice == 2:
            self.cgpa()
        elif self.choice == 3:
            self.cgpa_and_gpa()
        else:
            print("Please Try Again with correct Key !!!")
            return
        if sem_no == 0:
            self.create_report()
        else:
            self.create_report(sem_no)



# Python's Main
if __name__ == '__main__':
    # Creating the instance of the cgpa_gpa calculator class
    Calc = cgpa_gpa_calculator()
    # Starts the Calculator
    Calc.run()
    # End of Program
    print("\nProgram Ends.... :)")