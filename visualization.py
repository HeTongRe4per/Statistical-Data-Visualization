import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd

# 读取GTD数据
df = pd.read_csv('data/globalterrorismdb_0522dist.csv', low_memory=False)

# 聚合数据，计算每个国家的恐怖袭击数量
country_attacks = df['country_txt'].value_counts().reset_index()
country_attacks.columns = ['country_txt', 'attacks']

# 读取世界地图数据
world = gpd.read_file('natural_earth_vector/ne_110m_admin_0_countries.shp')

# 将恐怖袭击数据合并到世界地图数据中
world = world.merge(country_attacks, how='left', left_on='NAME', right_on='country_txt')
world['attacks'] = world['attacks'].fillna(0)

# 设置绘图风格
sns.set(style="whitegrid")

# 创建一个 2x2 的子图
fig, axes = plt.subplots(2, 2, figsize=(20, 12))

# 图 1: 世界地图
world.boundary.plot(ax=axes[0, 0])
world.plot(column='attacks', ax=axes[0, 0], cmap='OrRd', scheme='quantiles', k=5, legend=False)
axes[0, 0].set_title('Global Terrorist Attacks')

# 手动设置图例
norm = plt.Normalize(world['attacks'].min(), world['attacks'].max())
sm = plt.cm.ScalarMappable(cmap='OrRd', norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=axes[0, 0], orientation='vertical', pad=0.02)
cbar.set_label('Number of Attacks')

# 图 2: 按年份统计的恐怖袭击次数（每5年一段）
sns.countplot(x=pd.cut(df['iyear'], bins=range(1970, 2020, 5)), ax=axes[0, 1])
axes[0, 1].set_title('Number of Terrorist Attacks by Year (Every 5 Years)')
axes[0, 1].set_ylabel('Number of Attacks')
axes[0, 1].tick_params(axis='x', rotation=30)
axes[0, 1].set_xlabel('')

# 图 3: 按国家统计的恐怖袭击次数
top_countries = df['country_txt'].value_counts().head(10).index
sns.countplot(y='country_txt', data=df[df['country_txt'].isin(top_countries)], ax=axes[1, 0])
axes[1, 0].set_title('Top 10 Countries with Most Terrorist Attacks')
axes[1, 0].set_xlabel('Number of Attacks')
axes[1, 0].set_ylabel('Country')

# 图 4: 恐怖袭击类型分布
sns.countplot(y='attacktype1_txt', data=df, ax=axes[1, 1], order=df['attacktype1_txt'].value_counts().index)
axes[1, 1].set_title('Distribution of Attack Types')
axes[1, 1].set_xlabel('Number of Attacks')
axes[1, 1].set_ylabel('Attack Type')

# 调整布局
plt.tight_layout()
plt.show()
