from preprocess import *
from define import *
from analyse import *
from model_AI import *
from model_math import *


if __name__ == '__main__':
    # 定义开始日期和结束日期
    start_date = datetime(2023, 7, 1)
    end_date = datetime(2023, 7, 7)
    # 生成日期列表
    date_list = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]

    # 打印生成的日期列表
    print(date_list)

    column_group = ['水生根茎类', '花叶类', '花菜类', '茄类', '辣椒类', '食用菌']
    for date in date_list:
        for column_name in column_group:
            print(date, column_name, 10)
            profit = model_each(column_name, date, 13)
            print(profit)



