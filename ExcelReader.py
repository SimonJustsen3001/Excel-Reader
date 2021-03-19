import pandas
import math

filename = input("Enter the name of the file without .xlsx: ")
sheetname = input("Enter the name of the sheet in excel (Remember to capitalise letters): ")
column_input = input("(If you want column 'A' you should write '0')\n(If you want column 'B' you should write '1', etc.)\nEnter the number of the columns containing Mass and Intensity (Separated by a single space): ")
columns = []

if (column_input.count(' ') == 1):
    columns = column_input.split(' ')
    columns = [int(i) for i in columns]
else:
    raise Exception("There should be two rows for analysis")

threshhold = int(input("Enter highest value of 'Intensity': "))

threshhold = math.floor(threshhold * 0.02)

print(f"Threshhold calculated to be {threshhold}")
print("Extracting excel columns...")
excel = pandas.read_excel(filename + ".xlsx", sheet_name=sheetname,usecols=columns)[lambda x: x["Intensity"] > threshhold]
print("Sorting values by Mass...")
excel = excel.sort_values(by = "Mass", ascending=False)

vertex = [[],[]]
ascending = True;
previous_value = 0;
print("Finding vertices...")
for x in excel["Intensity"]:
    if(ascending == True):
        if(x <= previous_value):
            vertex.append([excel["Mass"].iloc[excel.index.get_loc(excel.index[excel["Intensity"]==previous_value][0])], x])
            ascending = False
        previous_value = x
    elif(ascending == False):
        if(x >= previous_value):
            ascending = True
        previous_value = x
filtered_vertex = list(filter(None,vertex))

excel_important = pandas.DataFrame(filtered_vertex, columns=["Mass", "Intensity"], dtype = float)
print("Complete!\n")
print(excel_important)
document = input("Enter the name of new excel document to be created: ")
print("Exporting to excel...")
excel_important.to_excel(rf"{document}.xlsx", sheet_name="Sheet1", index=False)
print("Process Complete!")