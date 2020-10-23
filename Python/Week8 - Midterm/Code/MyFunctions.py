def InputNumber():
    Number = int(input("Enter a number: "))
    return Number
# A2 Part 1
print(InputNumber())

def OutputNumber(GetOutputNumber):
    print(f"You entered the number {GetOutputNumber}")
# A2 Part 2
OutputNumber(InputNumber())

def DataProcessing(GetProcessedNumber):
    ProcessedNumber = GetProcessedNumber + 100
    return ProcessedNumber
#A2 Part 3
print(DataProcessing(InputNumber()))

#A2 Part 4
print(OutputNumber(DataProcessing(InputNumber())))