class Solution:
    def fizzBuzz(self, n: int):
        array = []
        for i in range(1, n + 1):

            if i % 5 == 0 and i % 3 == 0:

                array.insert(i - 1, "FizzBuzz")

            elif i % 5 == 0:
                array.insert(i - 1, "Buzz")
            elif i % 3 == 0:
                array.insert(i - 1, "Fizz")

            else:
                array.append(str(i))

        return array
