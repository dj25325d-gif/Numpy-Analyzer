import numpy as np


class DataAnalytics:

    def __init__(self):
        self.array = None


    def __check_array(self):
        if self.array is None:
            print("\nPlease create an array first!")
            return False
        return True


    def create_array(self):

        print("""
Select the type of array to create:
    1. 1D Array
    2. 2D Array
    3. 3D Array
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            numbers = input("Enter elements separated by space: ")
            numbers = numbers.split()

            numbers = [int(x) for x in numbers]

            self.array = np.array(numbers)

            print("\nArray created successfully:")
            print(self.array)


        elif choice == 2:

            rows = int(input("\nEnter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            total = rows * cols

            data = input(f"Enter {total} elements for the array separated by space: ")
            data = data.split()

            data = [int(x) for x in data]

            self.array = np.array(data).reshape(rows, cols)

            print("\nArray created successfully:")
            print(self.array)

            self.index_slice_menu()


        elif choice == 3:

            depth = int(input("Enter depth: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            total = depth * rows * cols

            values = input(f"Enter {total} elements separated by space: ")
            values = values.split()

            values = [int(x) for x in values]

            self.array = np.array(values).reshape(depth, rows, cols)

            print("\nArray created successfully:")
            print(self.array)


    def index_slice_menu(self):

        print("""
Choose an operation:
    1. Indexing
    2. Slicing
    3. Go Back
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            row = int(input("Enter row index: "))
            col = int(input("Enter column index: "))

            print("\nSelected Element:")
            print(self.array[row][col])


        elif choice == 2:

            row_range = input("Enter the row range (start:end): ")
            col_range = input("Enter the column range (start:end): ")

            r1, r2 = map(int, row_range.split(":"))
            c1, c2 = map(int, col_range.split(":"))

            sliced = self.array[r1:r2, c1:c2]

            print("\nSliced Array:")
            print(sliced)



    def math_operations(self):

        if not self.__check_array():
            return

        print("""
Mathematical Operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
""")

        choice = int(input("Enter your choice: "))

        numbers = input("\nEnter the same-size array elements (6 elements separated by space): ")
        numbers = numbers.split()

        numbers = [int(x) for x in numbers]

        second_array = np.array(numbers).reshape(self.array.shape)

        print("\nOriginal Array:")
        print(self.array)

        print("\nSecond Array:")
        print(second_array)

        if choice == 1:

            result = self.array + second_array

            print("\nResult of Addition:")
            print(result)

        elif choice == 2:

            result = self.array - second_array

            print("\nResult of Subtraction:")
            print(result)

        elif choice == 3:

            result = self.array * second_array

            print("\nResult of Multiplication:")
            print(result)

        elif choice == 4:

            result = self.array / second_array

            print("\nResult of Division:")
            print(result)



    def combine_split(self):

        if not self.__check_array():
            return

        print("""
Choose an option:
    1. Combine Arrays
    2. Split Array
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            numbers = input("\nEnter the elements of another array to combine (6 elements separated by space): ")
            numbers = numbers.split()

            numbers = [int(x) for x in numbers]

            second_array = np.array(numbers).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            combined = np.vstack((self.array, second_array))

            print("\nCombined Array (Vertical Stack):")
            print(combined)

        elif choice == 2:

            parts = np.array_split(self.array, 2)

            print("\nSplit Arrays:")
            for p in parts:
                print(p)


    def search_sort_filter(self):

        if not self.__check_array():
            return

        print("""
Choose an option:
    1. Search a value
    2. Sort the array
    3. Filter values
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            value = int(input("\nEnter value to search: "))

            result = np.where(self.array == value)

            print("\nValue found at indices:")
            print(result)


        elif choice == 2:

            print("\nOriginal Array:")
            print(self.array)

            sorted_array = np.sort(self.array, axis=1)

            print("\nSorted Array:")
            print(sorted_array)
            print("(Sorting applied row-wise.)")


        elif choice == 3:

            limit = int(input("Enter minimum value to filter: "))

            filtered = self.array[self.array > limit]

            print("\nFiltered Values:")
            print(filtered)


    def statistics(self):

        if not self.__check_array():
            return

        print("""
Choose an aggregate/statistical operation:
     1. Sum
     2. Mean
     3. Median
     4. Standard Deviation
     5. Variance
""")

        choice = int(input("Enter your choice: "))

        print("\nOriginal Array:")
        print(self.array)

        if choice == 1:
            print("\nSum of Array:", np.sum(self.array))

        elif choice == 2:
            print("\nMean of Array:", np.mean(self.array))

        elif choice == 3:
            print("\nMedian of Array:", np.median(self.array))

        elif choice == 4:
            print("\nStandard Deviation:", np.std(self.array))

        elif choice == 5:
            print("\nVariance:", np.var(self.array))



def main():

    tool = DataAnalytics()

    while True:

        print("""
===================================
Welcome to the NumPy Analyzer!
===================================

Choose an option:
    1. Create a Numpy Array
    2. Perform Mathematical Operations
    3. Combine or Split Arrays
    4. Search, Sort, or Filter Arrays
    5. Compute Aggregates and Statistics
    6. Exit""")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            tool.create_array()

        elif choice == 2:
            tool.math_operations()

        elif choice == 3:
            tool.combine_split()

        elif choice == 4:
            tool.search_sort_filter()

        elif choice == 5:
            tool.statistics()

        elif choice == 6:
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break


if __name__ == "__main__":
    main()
