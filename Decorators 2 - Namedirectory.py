# HackerRank / Python / Decorators 2 - Name directory
# Author: Tzu-Wen Lee

def wrapper(func):
    def standardize(people):
        standardized = []
        for i in xrange(len(people)):
            person = people[i]
            person = person.split()
            info = {'id': i, 'first name': person[0], 'last name': person[1], 
                    'age': int(person[2]), 'gender': person[3]}
            if info['gender'] == 'M':
                info['name'] = 'Mr. ' + info['first name'] + ' ' + info['last name']
            else:
                info['name'] = 'Ms. ' + info['first name'] + ' ' + info['last name']
            standardized.append(info)
        return func(standardized)
    return standardize

@wrapper
def sorting(people):
    return sorted(people, key=lambda x: (x['age'], x['id']))

print '\n'.join(map(lambda p: p['name'], sorting([raw_input() for _ in xrange(input())])))