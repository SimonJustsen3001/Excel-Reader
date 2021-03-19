import pandas
list1 = [0,1]
excel = pandas.read_excel("this.xlsx", sheet_name='Sheet5',usecols=list1)[lambda x: x["Intensity"] > 48960]

excel = excel.sort_values(by = "Mass", ascending=False)


vertex = [[],[]]


ascending = True;
previous_value = 0;
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

print(excel_important)

excel_important.to_excel(r"Vertex.xlsx", sheet_name="Sheet1", index=False)