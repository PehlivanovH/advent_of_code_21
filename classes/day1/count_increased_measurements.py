class CountIncreasedMeasurements:

    def countIncreasedMeasurements(self, input):
        numberOfIncreases = 0

        for index, measurement in enumerate(input[1:]):
            previousMeasurement = input[index]

            if(measurement > previousMeasurement):
                numberOfIncreases += 1

        return numberOfIncreases

    def countIncreasedMeasurementsInWindow(self, input):
        numberOfIncreases = 0
        middleOfWindowIndex = 2

        while(middleOfWindowIndex < len(input) - 1):
            previousWindow = self.windowSum(middleOfWindowIndex - 1, input)
            currentWindow = self.windowSum(middleOfWindowIndex, input)

            if(previousWindow < currentWindow):
                numberOfIncreases += 1

            middleOfWindowIndex += 1

        return numberOfIncreases

    def windowSum(self, windowIndex, input):
        return input[windowIndex - 1] + input[windowIndex] + input[windowIndex + 1]

    def readInput(self, path):
        measurements = []

        with open(path) as file:
            for line in file:
                measurements.append(int(line))

        return measurements

if __name__ == '__main__':
    counter = CountIncreasedMeasurements()
    input = counter.readInput("../../input/day1")
    result = counter.countIncreasedMeasurementsInWindow(input)

    print(result)