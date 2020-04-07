class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        elif x > 0:
            super(PositiveList, self).append(x)