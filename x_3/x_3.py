import os
import pandas as pd
import string
import random


class CsvHanlder:
    def __init__(self):
        path = os.path.abspath(os.getcwd())
        try:
            os.mkdir(os.path.join(path,'ilovecoffee'))
        except:
            print('檔案已存在')

    def create_csv(self):
        customer_id = []
        number = ''.join(str(x) for x in range(0,10))
        only_letter = string.ascii_lowercase[:26]+string.ascii_uppercase[:26]
        letter_number = string.ascii_lowercase[:26]+string.ascii_uppercase[:26]+number
        for c in range(500):
            random_id = []
            for i in range(8):
                if i==0:
                    random_id.append(random.choice(only_letter))
                random_id.append(random.choice(letter_number))
            customer_id.append(''.join(random_id))

        name_list = ['tome','petter','david','amy','angela','tim','cindy', 'jack','lisa','rose']
        customer_name = []
        for i in customer_id:
            customer_name.append(random.choice(name_list)+'.'+i)

        number = ''.join(str(x) for x in range(0, 10))
        customer_mobile = []
        for i in range(500):
            combine_number = []
            while True:
                for j in range(9):
                    combine_number.append(random.choice(number))
                mobile_number = '+866' + ''.join(combine_number)
                customer_mobile.append(mobile_number)
                if mobile_number in customer_mobile:
                    break

        frequency = []
        for i in range(500):
            frequency.append(random.choice(range(0,21)))
        data = list(zip(customer_id,customer_name,customer_mobile,frequency))
        df = pd.DataFrame(data,columns=['customer_id','customer_name','customer_mobile','frequency'])
        df.to_csv(os.getcwd()+'/ilovecoffee/customers.csv')
        print('檔案寫入完畢')

    def calculate_csv(self):
        df = pd.read_csv(os.getcwd()+'/ilovecoffee/customers.csv')
        med = df['frequency'].median()
        mean = round(df['frequency'].mean(),5)
        mode = df['frequency'].mode()
        print('中位數',med)
        print('平均數',mean)
        print('眾數',mode)


if __name__ == '__main__':
    obj = CsvHanlder()
    obj.create_csv()
    obj.calculate_csv()