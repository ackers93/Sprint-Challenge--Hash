#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # init a dict to store routes
    storage = dict()
    # init a list to store final list in order
    flights = list()

    # iterate over each ticket
    for ticket in tickets:
        # key(ticket.source) value(ticket.destination)
        storage[ticket.source] = ticket.destination

    # set index to loop over flights list
    ind = 0
    # set the current destination to init the list
    current_dest = "NONE"

    while ind < length:
        # set current destination to be new source of next iteration
        current_dest = storage.get(current_dest)
        # append on each iteration the ordered routes
        flights.append(current_dest)
        # move to next iteration
        ind += 1

    # return the ordered flight routes at the end
    return flights
