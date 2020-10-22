import sys
class Compute:
    def readParameters(self,x,y):
        # The first and second input arguments are initialized with threshold and limit variables.
        self.__threshold = float(sys.argv[x])
        self.__limit = float(sys.argv[y])

    def collectInput(self):
        """
         Assuming standard input is a text file. This method will read stdin then removes the trailing character and
         converts them to float values. If no valid value is present it breaks from the loop.
        """
        self.__inputs = []
        for item in sys.stdin.readlines():
            try:
                self.__inputs.append(float(item.rstrip()))
            except ValueError:
                break

    def __prob_logic(self,input_item, threshold, limit):
        """
        prob_logic is responsible for implementing threshold and limit constraints.
            :param1 input_item: Given input
            :param2 threshold: the value on which threshold constraint should be implemented
            :param3 limit: the value on which limit constraint should be implemented
            :return: The rounded output_amount and the limit value
        """
        # Threshold Constraint
        if (input_item > threshold):
            output_amount = input_item - threshold
        else:
            output_amount = 0.0
        # Limit Constraint
        if (output_amount < limit):
            return round(output_amount, 1), limit - output_amount
        else:
            return round(limit, 1), 0.0

    def processOutput(self):
        """
        This function iterates through the inputs list and for each input_item it calls the prob_logic function and calculates the cumulative sum.
         :return: the list with all the output_amount values and their cumulative sum
        """
        self.__outputs = []
        for input_item in self.__inputs:
            output_amount, self.__limit = self.__prob_logic(input_item, self.__threshold, self.__limit)
            self.__outputs.append(output_amount)
        cumulative_sum = float(sum(self.__outputs))
        self.__outputs.append(cumulative_sum)
        return self.__outputs

    def tabularOutput(self):
        # This function writes tabular (single-column) output by iterating every item in outputs list.
        for output_item in self.__outputs:
            print(output_item)

if __name__=='__main__':
    process = Compute()
    process.readParameters(1,2)
    process.collectInput()
    process.processOutput()
    process.tabularOutput()
