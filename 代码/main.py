from preprocess import *
from define import *
from analyse import *
from model_AI import *
from model_math import *


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    mpl.rcParams['font.family'] = 'SimHei'

    # df1 = preprocess1()
    # print('df1 done')
    # df2 = preprocess2()
    # print('df2 done')
    # df3 = preprocess3()
    # print('df3 done')

    # column_group = ['水生根茎类', '花叶类', '花菜类', '茄类', '辣椒类', '食用菌']
    # for column_name in column_group:
    #     plot3(column_name)

    # plot1('分类名称')
    # plot1('单品名称')

    # column_group = ['水生根茎类', '花叶类', '花菜类', '茄类', '辣椒类', '食用菌']
    # for column_name in column_group:
    #     train_GPR(column_name)

    get_index()