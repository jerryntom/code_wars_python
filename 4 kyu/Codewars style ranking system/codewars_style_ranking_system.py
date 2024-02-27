# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.ranks = [x for x in range(-8, 9) if x != 0]

    def check_activity_rank(self, activity_rank):
        if activity_rank not in self.ranks:
            raise ValueError("Rank should be in range [-8, 8]!")

    def inc_progress(self, activity_rank):
        self.check_activity_rank(activity_rank)

        difference = self.ranks.index(activity_rank) - self.ranks.index(self.rank)

        if difference < -1 or self.rank == 8:
            return None
        elif difference == -1:
            self.progress += 1
        elif difference == 0:
            self.progress += 3
        else:
            self.progress += 10 * difference * difference

        if self.progress >= 100:
            try:
                self.rank = self.ranks[self.ranks.index(self.rank) + self.progress // 100]
            except IndexError:
                self.rank = 8
                self.progress = 0
            else:
                self.progress = self.progress % 100

        if self.rank == 0:
            self.rank = 1
        elif self.rank == 8:
            self.progress = 0
