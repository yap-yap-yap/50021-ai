import queue, copy

class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time

    def __str__(self):
        return str((self.start_city, self.start_time))+ '->' + str((self.end_city, self.end_time))
    __repr__ = __str__

    # PART 2
    def matches(self, city, time):
        if self.start_city == city and self.start_time >= time:
            return True
        return False


flightDB = [Flight('Rome', 1, 'Paris', 4),
            Flight('Rome', 3, 'Madrid', 5),
            Flight('Rome', 5, 'Istanbul', 10),
            Flight('Paris', 2, 'London', 4),
            Flight('Paris', 5, 'Oslo', 7),
            Flight('Paris', 5, 'Istanbul', 9),
            Flight('Madrid', 7, 'Rabat', 10),
            Flight('Madrid', 8, 'London', 10),
            Flight('Istanbul', 10, 'Constantinople', 10)]   


# PART 3
def find_itinerary(start_city, start_time, end_city, deadline):

    frontier = queue.LifoQueue() # depth first search
    frontier.put((start_city, start_time, [(start_city, start_time)]))
    while not frontier.empty():
        # take deepest unexplored node
        current_city, current_time, current_path = frontier.get()
        # print(current_city)
        # print(current_path)

        # check if it is goal state
        if current_city == end_city:
            # print(current_city)
            return current_path

        # add children to frontier
        for flight in flightDB:
            if flight.matches(current_city, current_time) and flight.end_time <= deadline:
                child_path = copy.deepcopy(current_path)
                child_path.append((flight.end_city, flight.end_time))
                child = (flight.end_city, flight.end_time, child_path)
                # print(child)
                frontier.put(child)

    return False

# PART 4
def find_shortest_itinerary(start_city, end_city):
    start_time = 10
    for flight in flightDB:
        if flight.start_city == start_city and flight.start_time < start_time:
            start_time = flight.start_time
    deadline = start_time

    while deadline <= 10:
        path = find_itinerary(start_city, start_time, end_city, deadline)
        if path is not False:
            return path
        deadline += 1
    return False


def main():
    # path = find_itinerary('Istanbul', 10, 'Constantinople', 10) # PART 3: set parameters here
    path = find_shortest_itinerary('Rome', 'Istanbul') # PART 4: set parameters here

    if path is False:
        print('No valid itinerary')
    else:
        print(path)

if __name__ == '__main__':
    main()




