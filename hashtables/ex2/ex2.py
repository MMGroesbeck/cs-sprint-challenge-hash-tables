#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    sources = { ticket.source: ticket for ticket in tickets}
    this_ticket = sources["NONE"]
    route = [this_ticket.destination]
    while this_ticket.destination != "NONE":
        this_ticket = sources[this_ticket.destination]
        route.append(this_ticket.destination)
    return route