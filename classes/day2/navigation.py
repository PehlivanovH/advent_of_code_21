class Navigation:

    def position(self, input):
        horizontal = 0
        depth = 0
        aim = 0

        for movement in input:
            move = movement.split()

            if move[0] == "forward":
                horizontal += int(move[1])
                depth += aim * int(move[1])
            elif move[0] == "down":
                aim += int(move[1])
            elif move[0] == "up":
                aim -= int(move[1])

        return horizontal * depth

    def readDirections(self, path):
        directions = []

        with open(path) as file:
            for line in file:
                directions.append(line)

        return directions


if __name__ == '__main__':
    navigation = Navigation()
    input = navigation.readDirections("../../input/day2");
    print(navigation.position(input))
