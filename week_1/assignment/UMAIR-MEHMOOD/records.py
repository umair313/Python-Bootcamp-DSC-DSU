
def getStudentRecord(numberOfRecords,studentlist):
    n=1
    while(numberOfRecords>0):
        student={}
        print(f"\nEnter Record for student #{n}\n")
        rollNumber = input("Enter Roll-Number : ")
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        while True:
            marks = float(input("Enter Marks( out of 100) : "))
            if marks >= 0.0 and marks <= 100.0:
                break 
        student["rollNumber"] = rollNumber
        student["name"] = name
        student["age"] = age
        student["marks"] = marks
        studentlist.append(student)
        numberOfRecords-=1
        n+=1

#returns lowest , highest , avarage scores
def getHLA(studentlist):
    marks_sum=0
    max_score =0
    min_score =studentlist[0]['marks']
    for x in studentlist:
        if x['marks'] > max_score: max_score = x['marks']
        if x['marks'] < min_score: min_score = x['marks']
        marks_sum+= x['marks']
    avg=marks_sum/len(studentlist)
    return max_score,min_score,marks_sum

def main():

    studentlist= list()
    
    print("Enter Records of Students")
    
    numberOfRecords = int(input("Enter number of Records : "))
    getStudentRecord(numberOfRecords,studentlist)
    
    max_score,min_score,class_avg=getHLA(studentlist)

    print(f"\n\n**********Records of students*******\n\n")
    print(f"{'-'*58}")
    print(f"|Roll-Number{' '*(18-len('Roll-Number'))}|\
    Name{' '*(18-len('name'))}|Age{' '*(10-len('age'))}|Marks |")
    print(f"{'-'*58}")
    for x in studentlist:
        print(
            f"|{x['rollNumber']}{' '*(18-len(x['rollNumber']))}|"\
            f"{x['name']}{' '*(19-len(x['name']))}|"\
            f"{x['age']}{' '*(11-len('age'))}|"\
            f"{x['marks']} |"
            )
    print(f"{'-'*58}")

    print(f"{'-'*50}")
    print(f"|Class Highest{' '*(15-len('class-highest'))}|"\
            f"Class Lowest{' '*(15-len('class-lowest'))}|Class-average{' '*(15-len('class-avarage'))}|")
    print(f"{'-'*50}")
    print(f"|{max_score}{' '*(24-len('class-highest'))}|"\
            f"{min_score}{' '*(23-len('class-lowest'))}|{float('{:.2f}'.format(class_avg))}{' '*(23-len('class-avarage'))}|")

    print(f"{'-'*50}")


if __name__== "__main__":
    main()