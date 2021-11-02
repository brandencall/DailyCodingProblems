
class HitCounter:

    # Properties
    timestamp_dict = {}

    def record(self, timestamp):

        if timestamp in timestamp_dict:
            self.timestamp_dict[timestamp] += 1
        else:
            self.timestamp_dict[timestamp] = 1

        return

    def total(self):
        return sum(list(self.timestamp_dict.values()))

    def range(self, lower, upper):

        timestamps = self.timestamp_dict.keys()
        hits = 0

        for i in range(len(timestamps)):

            if timestamps[i] >= lower and timestamps[i] <= upper:

                hits += self.timestamp_dict.get(timestamps[i])

        return hits
