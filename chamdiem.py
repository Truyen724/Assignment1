# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import pandas as pd
from IPython.display import display
lst = os.listdir("Data")
print(lst)



def kt(id):
    if(len(id)!=9):
        return False
    elif(id[1:].isnumeric()==False):
        return False
    elif(id[0:1]!="N"):
        return False
    else: return True

def tinh(ls,results):
    diem = 0
    for i in range(len(ls)):
        if(ls[i]==results[i]):
            diem+=4
        elif(ls[i]!=results[i] and ls[i]!=""):
            diem-=1
    return(diem)
def trungvi(list):
    list.sort()
    if(len(list)%2 ==1):
        return list[len(list)//2+1]
    else:
        des= len(list)//2
        re = (list[des]+list[des+1])/2
        return re
global str
def __main__():
    while(True):
        cls=input("Nhập vào tên lớp để chấm điểm(từ class1 đến class8), nhập -1 để kết thúc:")
        if(cls=="-1"):
            break
        if((cls+".txt") in lst):
            with open("Data/"+cls+".txt","r") as file:
                print("Successfully opened "+cls+".txt")
                print("**** ANALYZING ****")
                st = file.read()
                slst= st.split("\n")
                s = []
                invalid = 0
                valid = 0
                tb=0
                for line in slst:
                    str2 =line.split(",")
                    if(len(str2)>26):
                        print("Invalid line of data: does not contain exactly 26 values:")
                        print(line)
                        invalid +=1
                        tb=1
                    elif(kt(str2[0])==False):
                        print("Invalid line of data: N# is invalid")
                        invalid +=1
                        print(line)
                        tb=1
                    else:
                        s.append(tuple(line.split(",")))
                        valid +=1
                if(tb==0):
                    print("No errors found!")
                df = pd.DataFrame(data = s, columns = ['Mã số','Câu 1','Câu 2','Câu 3','Câu 4','Câu 5','Câu 6','Câu 7','Câu 8','Câu 9','Câu 10','Câu 11','Câu 12',                    'Câu 13','Câu 14','Câu 15','Câu 16','Câu 17','Câu 18','Câu 19','Câu 20','Câu 21','Câu 22','Câu 23','Câu 24','Câu 25'])
                print("*****Report*****")
                print("Total valid lines of data: ", valid)
                print("Total invalid lines of data: ", invalid)
                result= chamdiem(answer_key, df)
                luudiem(cls,result)
        else:
            print("Không tồn tại file danh sách đã chon vui long nhập lại từ class1-->class8")

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
def chamdiem(answer_key, dataFrame):
    lst_answer = answer_key.split(",")
    Result =[]
    Result2 =[]
    for i in range(dataFrame.shape[0]):
        ls = list(dataFrame.iloc[i])
        diem= tinh(ls[1:],lst_answer)
        Result.append(ls[0]+","+str(diem))
        Result2.append(diem)

    print("Mean (average) score:",sum(Result2)/len(Result2))
    print("Highest score:", max(Result2))
    print("Lowests score:", min(Result2))
    print("Range of scores:",max(Result2)-min(Result2))
    print("Median score:",trungvi(Result2))
    return Result

    
def luudiem(cls, result):
    for i in range(len(result)-1):
        result[i]=result[i]+"\n"
    with open("Result/"+cls+"_grades",'w') as f:
        f.writelines(result)




if __name__ == "__main__":
    __main__()
        
    






