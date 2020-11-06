import random

# skal være den måned/periode vagterne skal være i
weekdays = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
'''"Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday", "Sunday"'''


# de personer der har ønsket vagt den dag
choices = [
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"],
        [ "A", "B", "C", "D"]
        
        ]

def choose_random_candidate():
    return [ random.choices(choice) for choice in choices ]

def check_candidate(candidate):
    """ checks that a candidate week assigment is valid
    """
    for i in range(len(candidate) - 1):
        if candidate[i] == candidate[i + 1]:
            return False
    return True

candidate = choose_random_candidate()

for i in range(1000):
    if check_candidate(candidate): break
    candidate = choose_random_candidate()


for day, choice in zip(weekdays, candidate):
    print(day, choice)
    
def count_days:
    #tæl hvor mange vagter man har i perioden
