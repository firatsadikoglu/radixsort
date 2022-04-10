
import time
start_time = time.time()

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


# Declaring arrays
firstarray = []
tofloatarray =[]
fixedfloat =[]
optimizedarray = []

# Opening file
my_file = "./100000likliste 4.txt"
file = open(my_file, "r")

#Getting the number of lines
line_number = sum(1 for line in open(my_file))



# Fixing arrays
for i in range(line_number):
    firstarray.append(file.readline())
for i in range(len(firstarray)):
    tofloatarray.append(float(firstarray[i]))

for i in range(len(tofloatarray)):
    fixedfloat.append(int(tofloatarray[i]*1000))

radixSort(fixedfloat)

print("Unsorted List: ")
for item in range(len(firstarray)):
    print(firstarray[item], end ="")


print("Sorted List : ")

for i in range(line_number):
    optimizedarray.append(float(fixedfloat[i]/1000))
print("")
for i in range(len(optimizedarray)):
    print(optimizedarray[i],end=" ")


print("\n\t\tThis operation takes %s seconds" % (time.time() - start_time))