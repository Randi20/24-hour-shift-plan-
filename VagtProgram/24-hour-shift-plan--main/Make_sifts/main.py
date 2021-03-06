import json
import random

# ---- relative path
import pathlib
currentPath = pathlib.Path().absolute()

import datetime
from datetime import date


today = date.today()

checkPeriod = 30 # Tne amount of the days that must be checked  
StartDay = today # The start day
endDay = StartDay + datetime.timedelta(days=checkPeriod) # Calculate the end day for check


# Read the data from the json file

data = []
with open(str(currentPath) + r'\..\lite2\Wiches.json') as f:
    for line in f:
        data.append(json.loads(line))

# Change the data from person to date
dateDic = {}
missingDays = []

for person in data:
    for vagtDay in person["Dates"]:
        if vagtDay in dateDic.keys():
            tempList = dateDic[vagtDay]
            tempList.append(person['User'])
            dateDic[vagtDay] =  tempList
        else:
            dateDic[vagtDay] = [person['User']]

sortedDateDic=sorted(dateDic)

print("\n\n List of the days and people allowd for lottery and chosen one:\n\n")
selection = {}
PeopleInSecondDay = []
chekDay = StartDay
while chekDay != endDay:
    #datetime.datetime.strptime(regDate, '%Y-%m-%d').date()
    peopleAllowdForLot = []
    if str(chekDay) in dateDic.keys():
        dayPeople = dateDic[str(chekDay)]
        dayBefore = chekDay + datetime.timedelta(days=-1)
        if str(dayBefore) in dateDic.keys():
            for person in dayPeople:
                if person in dateDic[str(dayBefore)]:
                    PeopleInSecondDay.append(person + " not allowed day  " + str(chekDay))
                else:
                    peopleAllowdForLot.append(person)
        else:
            peopleAllowdForLot = dayPeople
        if len(peopleAllowdForLot) != 0:
            #chosenOneIndex = random.randrange(len(peopleAllowdForLot))
            #chosenOne = peopleAllowdForLot[chosenOneIndex]
            chosenOne = random.choice(peopleAllowdForLot)
            selection[chekDay] = chosenOne
            print(str(chekDay), peopleAllowdForLot, " chosen one:", chosenOne)
        else:
            missingDays.append(str(chekDay))
                    
        
        
    else:
        missingDays.append(str(chekDay))

    chekDay = chekDay + datetime.timedelta(days=1)

print("\nPople who are not allowed to participate in specific day:\n\n",PeopleInSecondDay)

print("\n\nDays when nobdoy chosed to work:\n\n",missingDays)


def assigning_shifts(prefereces, dates, users):
    """

    :return:
    """
    # selection : date -> user
    selection = {}

    def check_if_allowed(user, date):
        # TODO: check if user is used more than his or hers share
        yesterday = date - datetime.timedelta(days=1)
        if yesterday in selection:
            return selection[yesterday] != user
        else:
            return True

    def find_valid_users(people):
        return [ user for user in people if check_if_allowed(user, date) ]

    for date in dates:
        valid_users = find_valid_users(prefereces.get(date, []))
        if not valid_users:
            valid_users = find_valid_users(users)
        if not valid_users:
            return None
        selection[date] = random.choice(valid_users)

    return selection

def date_range(start, end):
    """
    :param start: the start date
    :param end: the end date (non-inclusive)
    :return: a list of dates between start and end
    """
    dates = []
    while start != end:
        dates.append(start)
        start = start + datetime.timedelta(days=1)
    return dates

def print_shifts(shifts, dates):
    """
    :param shifts: the dictionary of choices of shifts
    :param dates: the dates to print
    """
    for date in dates:
        print(date, shifts[date])


#print("Yes")
dates =  date_range(StartDay, endDay)
#print(dates)
preferences = {StartDay: ["Randi"]}

while True:
    # Try to assing shifts.

    shifts = assigning_shifts(preferences, dates, ["Randi", "Christian"])

    if shifts is None:
        break
    else:
        # If it does not, delte a preference and try again.
        key = random.choice(list(preferences))
        del preferences[key]


print_shifts(shifts, dates)

'''

def lod():
    global data
    selectedDate = today
    yesterday = today - datetime.timedelta(days=1)
    todayPeople = []
    yestPeople = []
    peopleDayAmountDict = {}
    
    rtnMessage = ""
    for person in data:
        for regDate in person['Dates']:
            date_object = datetime.datetime.strptime(regDate, '%Y-%m-%d').date()
            if str(date_object + datetime.timedelta(days=1)) in person['Dates']:
                rtnMessage += "\n" + str(date_object + datetime.timedelta(days=1)) + " Ikke muligt " + person['User'] + "\n\n"
            if person['User'] in peopleDayAmountDict.keys():
                peopleDayAmountDict[person['User']] = peopleDayAmountDict[person['User']] + 1
            else:
                peopleDayAmountDict[person['User']] = 1
                
            if regDate == str(selectedDate):
                todayPeople.append(person['User'])
            if regDate == str(yesterday):
                yestPeople.append(person['User'])
            if regDate == str(yesterday):
                yestPeople.append(person['User'])
            
    
    
    periodDays = 30
    totalPeople = len(peopleDayAmountDict)
    allowedRate = int(periodDays/totalPeople)
    print("---------",len(todayPeople))
    chosenOneIndex = random.randrange(len(todayPeople))  
    chosenOne = todayPeople[chosenOneIndex]
    if allowedRate < peopleDayAmountDict[chosenOne]:
        rtnMessage += " More than legal watch days\n"
    rtnMessage += "Chosen one is: " + chosenOne + " she have " + str(peopleDayAmountDict[chosenOne]) + " vagter \n"
    if (chosenOne in yestPeople):
        rtnMessage += chosenOne + " har haft vagt i går!\n"
    return rtnMessage

print(lod())
#print(" peoples : ",todayPeople)
#print(" yes peoples : ",yestPeople)
        
#    dateDiff = days_between(str(today), str(person['Dates'][0]))
#    print(person['User'], dateDiff, person['Dates'][0])

  
'''
