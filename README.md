
# 全球恐怖主义数据库分析与可视化

本项目使用Python对全球恐怖主义数据库（[GTD](https://www.start.umd.edu/gtd/)）进行分析，并利用各种数据可视化技术展示分析结果。GTD是一个包含从1970年到2019年全球恐怖事件信息的综合数据集。

## 项目概述

本项目涉及以下内容：

1. **本项目涉及以下内容：** 使用Pandas加载GTD数据集，按国家和年份进行数据聚合，并进行预处理以备进行可视化。

2. **数据可视化：**

    - **全球恐怖袭击地图：** 利用GeoPandas和Matplotlib在世界地图上显示各国恐怖袭击事件数量。
    - **时间序列上的恐怖袭击：** 使用Seaborn显示每5年一个段的恐怖袭击分布。
    - **恐怖袭击最多的前10个国家：** 展示恐怖袭击次数最多的前10个国家的柱状图。
    - **恐怖袭击类型分布：** 使用水平条形图展示恐怖袭击的不同类型分布。

3. **使用的库**：

    - Pandas：数据处理与分析。
    - Seaborn：统计数据可视化。
    - Matplotlib：Python绘图库。
    - GeoPandas：用于处理地理空间数据的扩展库。

4. **文件结构：**

    - `data/`：包含GTD数据集文件 (globalterrorismdb_0522dist.csv和xlsx) 的目录。
    - `natural_earth_vector/`：包含世界地图形状文件 (ne_110m_admin_0_countries.shp) 的目录。
    - `visualization.py`：主要的Python脚本，用于数据加载、处理和可视化。
    - `README.md`：Markdown格式的文件，包含项目概述、设置说明和使用方法。

## 设置说明

要在本地运行项目：

1. 克隆存储库：

```bash
git clone https://github.com/HeTongRe4per/statistical_data_visualization.git
```

2. 安装所需的Python库：

```bash
pip install pandas seaborn matplotlib geopandas
```

3. 运行可视化脚本：

```bash
python visualization.py
```

## 结果

生成的可视化图表展示了全球多年来恐怖主义活动的情况，突出显示了受影响最严重的地区、常见的袭击类型和时间趋势。