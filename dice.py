class Dice():
    def __init__(self, top, front):
        # [top, front, bottom, rear, right, left]
        self.A = [top, front, 7 - top, 7 - front]
        for i in range(4):
            t = (self.A[i-1], self.A[i])
            if t == (6, 4):
                self.A += [5, 2]
            elif t == (4, 6):
                self.A += [2, 5]
            elif t == (6, 5):
                self.A += [3, 4]
            elif t == (6, 2):
                self.A += [4, 3]
            elif t == (5, 4):
                self.A += [1, 6]
            elif t == (5, 3):
                self.A += [6, 1]
            else:
                continue
            break

    def top(self):
        return self.A[0]

    def front(self):
        return self.A[1]

    def bottom(self):
        return self.A[2]

    def rear(self):
        return self.A[3]

    def right(self):
        return self.A[4]

    def left(self):
        return self.A[5]

    # di: 0 == front, 1 == rear, 2 == right, 3 == left
    def rotate(self, di):
        a = self.A
        if di == 0:
            self.A = [a[3], a[0], a[1], a[2], a[4], a[5]]
        elif di == 1:
            self.A = [a[1], a[2], a[3], a[0], a[4], a[5]]
        elif di == 2:
            self.A = [a[5], a[1], a[4], a[3], a[0], a[2]]
        elif di == 3:
            self.A = [a[4], a[1], a[5], a[3], a[2], a[0]]
