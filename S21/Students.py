StudentList = [{"Name":"Zahra", "Age":18, "Avg":15.98},
               {"Name":"Fateme", "Age":19, "Avg":18.08},
               {"Name":"Ali", "Age":17, "Avg":13.15},
               {"Name":"Zoha", "Age":21, "Avg":19.12},
               {"Name":"Mahdi", "Age":16, "Avg":14.81},
               {"Name":"Elnaz", "Age":17, "Avg":19.98},
               {"Name":"Melika", "Age":22, "Avg":12.76},
               {"Name":"Hoda", "Age":16, "Avg":18.89},
               {"Name":"Mohsen", "Age":20, "Avg":15.56},
               {"Name":"Saman", "Age":22, "Avg":18.63},
               {"Name":"Hosna", "Age":23, "Avg":10.18},
               ]


def AvgAvg(STDList):
    if len(STDList)==0:
        return 0
    
    sum = 0
    for dic in STDList:
        sum += dic["Avg"]
    
    return round(sum/len(STDList),2)

print(AvgAvg(StudentList))


def AvgAge(STDList):
    if len(STDList)==0:
        return 0
    sum = 0
    for item in STDList:
        sum += item["Age"]

    return round(sum/len(STDList),2)

print(AvgAge(StudentList))