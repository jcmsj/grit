from location import Location

class State():
    def __init__(self, location:Location|None=None):
        self.location = Location.random() if location == None else location

def main():
    '''Run if main module'''
    a = {loc:0 for loc in Location}
    for _ in range(100):
        a[Location.random()] += 1
    print(a)

if __name__ == '__main__':
    main()
