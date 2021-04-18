import pandas as pd
import random
import csv
from matplotlib import pyplot as plt


print("Enter file name(or full path) with extention:")
file = input()
# data = pd.read_csv(r"{}.csv".format(file))
data = pd.read_csv(file)

rowofdata = len(data)
columnofdata = len(data.columns)

error = 0.0

# w is constant value
 # check categorical values
for i in range(0, columnofdata):
    for j in range(0, rowofdata):
        if (type(data.values[j][i]) == str):
            x = data.columns[i]
            # print(x)
            if j == 0:
                tem = []
                tem = [0 for i in range(1)]
                k = 0
                tem[0] = data.values[j][i]
                data[x].values[j] = 0
            else:
                k = 0
                for k in range(0, len(tem)):
                    if data.values[j][i] == tem[k]:
                        data[x].values[j] = k
                        break
                if (type(data.values[j][i]) == str):
                    tem.append(data.values[j][i])
                    data[x].values[j] = k + 1
        else:
            # print("no")
            break

w = []
for i in range(0, columnofdata):
    # print("constant value insert W", i, ":")

    w.append(0.5)
alpha = random.uniform(0.1,0.25)
# print("Learning rate:", alpha)
# Ypredict is prediction value

n = int(input("enter iteration number:"))
for k in range(0, n):
    ####print w (omega)
    # print(k + 1, ":", w)
    SumofYpredict = 0.0

    Ypredict = [0 for i in range(len(data))]
    # print(Ypredict)
    for i in range(0, rowofdata):
        for j in range(0, columnofdata):
            if j == 0:
                Ypredict[i] += w[0]
            #             print(Ypredict[i])
            elif 0 < j < columnofdata:
                Ypredict[i] += w[j] * data.values[i][j - 1]
        #     print(Ypredict[i])
        SumofYpredict += Ypredict[i]
    #     print(Ypredict)
    #     print("Sum of Yprediction: ",SumofYpredict)


    # Sd is Sum of D
    Sd = 0.0
    # D is Ypr -Yreal
    D = [0 for i in range(len(data))]

    # store the Dxn
    T = [[0 for i in range(columnofdata)] for x in range(rowofdata)]
    # print(T)

    for i in range(0, rowofdata):
        D[i] = Ypredict[i] - data.values[i][columnofdata - 1]
        #     print(D[i])
        Sd += D[i]
        error += 0.5 * D[i] * D[i]

    # print("Error", error)
    #     print("Sum of D(Ypr-Yexp):",Sd)

    for i in range(0, rowofdata):
        for j in range(0, columnofdata):
            if j == 0:
                T[i][j] = D[i]
            else:
                T[i][j] = D[i] * data.values[i][j - 1]

    # print(T)

    result = list(map(sum, zip(*T)))
    # print(result)

    for i in range(0, columnofdata):
        w[i] = w[i] - alpha * result[i]


with open("result.csv" , mode='a',newline='') as file1:
    result_writer = csv.writer(file1)
    result_writer.writerow([file,n, alpha, error])

##plot
# x=list(columnofdata)
# Ypredict
# Y_expected=data[[columnofdata]]