num_inputs = int(input("How many inputs do you want? "))
num_target = int(input("What is the target you want? "))
input_array = []
for i in range(num_inputs):
    input_num = int(input(f"Enter input {i+1}: "))
    input_array.append(input_num)
print("Input array:", input_array)
for i in range(num_inputs):
    for j in range(i+1, num_inputs):
        if(input_array[i] + input_array[j] == num_target):
            print(f"Output: [index:{i}, index:{j}]")

