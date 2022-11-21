class Labyrinthe:
    def __init__(self):
        self.labyrinthe = np.array([[1] * 4] * 4)
        self.labyrinthe[2][0] = 0
        self.labyrinthe[1][1] = 0
        print(self.look_neighbourhood(2, 2))

    def look_neighbourhood(self, x, y):
        for neighbour_x in range(4):
            for neighbour_y in range(4):
                print(neighbour_x, neighbour_y)

    def __repr__(self):
        return "\n" + "\n".join(" ".join(map(str, e)) for e in self.labyrinthe)
