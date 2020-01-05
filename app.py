from flask import Flask, render_template, request
import pandas as pd
import plotly.offline as py
import cufflinks as cf
import numpy as np
import plotly.graph_objs as go
import webbrowser
import folium
from pandas import DataFrame

app = Flask(__name__, static_folder="templates")

# 导入数据
data = pd.read_csv('forbes.csv')
regions_available = list(data.values)
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()
N = pd.read_csv('forbes.csv', encoding="utf8",
                keep_default_na=False, na_values='na_rep')
N.head()

# Count crime numbers in each neighborhood
data5 = N.iloc[0:100, :]

disdata5 = pd.DataFrame(data['行业'].value_counts())
disdata5.reset_index(inplace=True)
disdata5.rename(columns={'index': '分类', 'PdDistrict': 'Count'}, inplace=True)

data4 = N.iloc[0:20, :]

disdata4 = pd.DataFrame(data['行业'].value_counts())
disdata4.reset_index(inplace=True)
disdata4.rename(columns={'index': '分类', 'PdDistrict': 'Count'}, inplace=True)



# def entry_page() -> 'html':
#    return render_template('首页.html')

@app.route('/all', methods=['GET'])
def for_bes_2019():
    # def 首页() -> 'html':
    # return render_template('首页.html')
    data_str = data.to_html()
    #fig = data.iplot(kind="bar", x="行业", y="国籍", asFigure=True)
   # py.offline.plot(fig, filename="行业（全部）.html", auto_open=False)
    with open("行业（全部）.html", encoding="utf8", mode="r") as f:
      plot_all = "".join(f.readlines())

    # regions_available = regions_available_loaded  # 下拉选单有内容
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           # the_select_region=regions_availa
                           )


@app.route('/city', methods=['POST'])
def star_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = disdata4.query("region=='{}'".format(the_region))
    df_summary = dfs.groupby("行业").agg(
        {"数量": "number"}).sort_values(by="数量", ascending=False)
    print(df_summary.head(5))  # 在后台检查描述性统计
    # 显示前100名富豪所在的国籍的地图
    latitude = 39.92
    longitude = 116.46

    from folium import plugins

    # let's start again with a clean copy of the map of San Francisco
    san_map = folium.Map(location=[latitude, longitude], zoom_start=4)

    # instantiate a mark cluster object for the incidents in the dataframe
    incidents = plugins.MarkerCluster().add_to(san_map)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(d2.y, d2.x, N.中文姓名):
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup=label,
        ).add_to(incidents)

    # add incidents to map
    san_map.add_child(incidents)


@app.route('/forbes', methods=['GET'])
def hu_run_select() -> 'html':
    limit = request.args.get("limit")  # 取得用户交互输入
    print(limit)  # 检查用户输入, 在后台

    if limit == '20':
        data_str = data4.to_html()
        kind_data = disdata4[:20].to_html()
        file = "行业20.html"
    else:
        data_str = data5.to_html()
        kind_data = disdata5[:100].to_html()
        file = "行业100.html"
    print(file)
    with open(file, encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    # regions_available = regions_available_loaded  # 下拉选单有内容
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           the_select_region=regions_available,
                           kind_data=kind_data
                           )


@app.route('/allmap')
def allmap() -> 'html':
    return render_template('地图（全部）.html')


@app.route('/map20')
def map20() -> 'html':
    return render_template('地图（20）.html')


@app.route('/map100')
def map100() -> 'html':
    return render_template('地图（100）.html')


@app.route('/')
@app.route('/首页')
def entry_page() -> 'html':
    return render_template('首页.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)   # debug=True, 在py使用, 在ipynb不使用
