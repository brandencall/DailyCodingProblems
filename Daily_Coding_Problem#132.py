
class HitCounter:

    # Properties
    timestamp_dict = {}

    # Records a hit at a given timestamp
    def record(self, timestamp):

        # Checks if the timestamp exists in our dictionary
        if timestamp in timestamp_dict:
            self.timestamp_dict[timestamp] += 1
        else:
            self.timestamp_dict[timestamp] = 1

        return

    # Returns all recorded hits
    def total(self):
        return sum(list(self.timestamp_dict.values()))

    # Returns the sum of given hits during a certian time period.
    def range(self, lower, upper):

        timestamps = self.timestamp_dict.keys()
        hits = 0

        for i in range(len(timestamps)):

            if timestamps[i] >= lower and timestamps[i] <= upper:

                hits += self.timestamp_dict.get(timestamps[i])

        return hits
