# plovesee
# Novemeber 15th, 2020

def compute_min_number_of_refills(d, m, stops):

    # distance between cities
    assert 1 <= d <= 10 ** 5

    # mileage available per refuel
    assert 1 <= m <= 400

    # assertion on max number of stops
    assert 1 <= len(stops) <= 300

    # asserting that the first stop has to be greater than zero (first city)
    # also that each subsequent stop has to be farther from the start than the last stop
    # additionally, the last stop has to be less than the total distance between the two cities
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # initalizing variables for tracking current loaction and number of refills
    numRefills, currentRefill = 0, 0

    # editing the stops array to include the initial location (0) and the final destination (d)
    stops.append(d)
    stops.insert(0,0)
    # creating variable to represent the total number of available stops along trip 
    n = len(stops) - 2

    # greedy algorithm based on the one shown in class
    # main while loop to run at least until current location is equal to last fuel station
    while currentRefill <= n:
        # storing the last location for comparision in greedy algorithm
        lastRefill = currentRefill
        # internal while loop to determine the optimal next fuel station
        # runs until either the last fuel station is reached, or until max mileage is reached (m)
        while (currentRefill <= n and stops[currentRefill + 1] - stops[lastRefill] <= m):
            # tracks proposed path along (stops) until maximum is hit as specified in while loop
            currentRefill += 1
        # once the next maximum postion is determined, if it is where we started, then we cannot
        # proceed and an error is returned
        if currentRefill == lastRefill:
            return -1
        # if we were able to proceed, but we were not able to make it all the way to the destination
        # then we need to refuel
        if currentRefill <= n:
            numRefills += 1
    return numRefills


if __name__ == '__main__':
    # distance between cities (d)
    input_d = int(input())
    # mileage obtainable on one tank (m)
    input_m = int(input())
    # number of available stops, to create array/list
    input_n = int(input())
    # distance from the start for each stop
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
