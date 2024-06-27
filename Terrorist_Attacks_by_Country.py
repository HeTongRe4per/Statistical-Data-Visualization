import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 读取GTD数据
df = pd.read_csv('data/globalterrorismdb_0522dist.csv')

# 聚合数据，计算每个国家的恐怖袭击数量
country_attacks = df['country_txt'].value_counts().reset_index()
country_attacks.columns = ['country_txt', 'attacks']

# 读取世界地图数据
world = gpd.read_file('natural_earth_vector/ne_110m_admin_0_countries.shp')

# 将恐怖袭击数据合并到世界地图数据中
world = world.merge(country_attacks, how='left', left_on='NAME', right_on='country_txt')
world['attacks'] = world['attacks'].fillna(0)

# 绘制地图
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax)
world.plot(column='attacks', ax=ax, legend=True,
           legend_kwds={'label': "Number of Terrorist Attacks by Country",
                        'orientation': "horizontal"})
ax.set_title('Global Terrorist Attacks')
plt.show()
