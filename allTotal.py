import pandas as pd

# 1. 加载数据
file_path = 'data\globalterrorismdb_0522dist.csv'
df = pd.read_csv(file_path, encoding='UTF-8')  # 根据你的文件编码调整

# 2. 数据处理和分析
# 按国家进行分组，并计算每个国家的事件数量
attacks_by_country = df.groupby('country_txt').size().reset_index(name='total_attacks')

# 3. 按数量从高到低排序
attacks_by_country_sorted = attacks_by_country.sort_values(by='total_attacks', ascending=False)

# 4. 输出所有结果，不要省略中间行
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(attacks_by_country_sorted)