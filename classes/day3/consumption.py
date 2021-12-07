class Consumption:

    def lifeSupport(self, input):
        return self.co2(input, 0) * self.oxygen(input, 0)

    def co2(self, input, index):
        if len(input) == 1:
            return int(input[0], 2)

        leastCommonBit = self.leastCommonBit(input, index)
        filteredInput = self.filter(input, leastCommonBit, index)

        return self.co2(filteredInput, index + 1)

    def oxygen(self, input, index):
        if len(input) == 1:
            return int(input[0], 2)

        mostCommonBit = self.mostCommonBit(input, index)
        filteredInput = self.filter(input, mostCommonBit, index)

        return self.oxygen(filteredInput, index + 1)

    def filter(self, input, filterCriteria, index):
        result = []

        for value in input:
            if int(value[index]) == filterCriteria:
                result.append(value)

        return result

    def powerConsumption(self, input):
        gamma = self.gamma(input)
        epsilon = self.epsilon(input)

        return gamma * epsilon

    def gamma(self, input):
        gammaBinary = ""

        for index in range(len(input[0])):
            gammaBinary += str(self.mostCommonBit(input, index))

        return int(gammaBinary, 2)

    def epsilon(self, input):
        epsilonBinary = ""

        for index in range(len(input[0])):
            epsilonBinary += str(self.leastCommonBit(input, index))

        return int(epsilonBinary, 2)

    def mostCommonBit(self, input, index):
        numberOfOnes = 0

        for value in input:
            numberOfOnes += int(value[index])

        if self.hasMoreOnes(numberOfOnes, input):
            return 1
        else:
            return 0

    def leastCommonBit(self, input, index):
        numberOfOnes = 0

        for value in input:
            numberOfOnes += int(value[index])

        if self.hasMoreOnes(numberOfOnes, input):
            return 0
        else:
            return 1

    def hasMoreOnes(self, numberOfOnes, input):
        return numberOfOnes >= len(input) / 2

    def readConsumption(self, path):
        readinds = []

        with open(path) as file:
            for line in file:
                readinds.append(line.replace("\n", ""))

        return readinds


if __name__ == '__main__':
    consumption = Consumption()
    input = consumption.readConsumption("../../input/day3")
    print(consumption.powerConsumption(input))
    print(consumption.lifeSupport(input))
