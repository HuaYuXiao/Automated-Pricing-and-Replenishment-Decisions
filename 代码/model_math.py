from define import *


def get_index():
    os.chdir(xlsx_path)

    # 使用pandas的read_excel函数读取文件并转换为DataFrame
    df_sale = pd.read_excel(csv3_name, sheet_name='销量', header=0)
    df_sale['销售日期'] = pd.to_datetime(df_sale['销售日期'], format='%Y-%m-%d')
    # 使用dt.day_name()函数将日期转换为星期几，并将结果添加为新的列
    df_sale['星期'] = df_sale['销售日期'].dt.day_name()
    # 删除"销售日期"列
    df_sale.drop(columns=['销售日期'], inplace=True)
    df_sale = df_sale[['星期'] + [col for col in df_sale.columns if col != '星期']]
    # 将"星期"列设置为索引列
    df_sale.set_index('星期', inplace=True)
    # 使用pivot_table计算销量平均值
    pivot_df_sale = df_sale.pivot_table(index='星期', aggfunc='mean')
    # 使用ExcelWriter将两个DataFrame写入到同一个Excel文件的不同sheet中
    with pd.ExcelWriter(csv5_name, engine='openpyxl', mode='a') as writer:
        pivot_df_sale.to_excel(writer, sheet_name='销量')

    # 使用pandas的read_excel函数读取文件并转换为DataFrame
    df_cost = pd.read_excel(csv3_name, sheet_name='批发价格', header=0)
    df_cost['销售日期'] = pd.to_datetime(df_cost['销售日期'], format='%Y-%m-%d')
    # 使用dt.day_name()函数将日期转换为星期几，并将结果添加为新的列
    df_cost['星期'] = df_cost['销售日期'].dt.day_name()
    # 删除"销售日期"列
    df_cost.drop(columns=['销售日期'], inplace=True)
    df_cost = df_cost[['星期'] + [col for col in df_cost.columns if col != '星期']]
    # 将"星期"列设置为索引列
    df_cost.set_index('星期', inplace=True)
    # 使用pivot_table计算销量平均值
    pivot_df_cost = df_cost.pivot_table(index='星期', aggfunc='mean')
    # 使用ExcelWriter将两个DataFrame写入到同一个Excel文件的不同sheet中
    with pd.ExcelWriter(csv5_name, engine='openpyxl', mode='a') as writer:
        pivot_df_cost.to_excel(writer, sheet_name='批发价格')

    return


def model_profit():















    return









