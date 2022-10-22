from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import locale
import firebase_admin
from firebase_admin import credentials, firestore

# TẢI DỮ LIỆU TỪ FIRESTORE
cred = credentials.Certificate("iuh-20098151-firebase-adminsdk-wyb05-41ce913fdb.json")
appLoadData = firebase_admin.initialize_app(cred)

dbFireStore = firestore.client()

queryResults = list(dbFireStore.collection(u'tbl-20098151').where(u'DEALSIZE',u'==', 'Large').stream())
listQueryResult = list(map(lambda x: x.to_dict(), queryResults))

df = pd.DataFrame(listQueryResult)

df['YEAR_ID'] = df['YEAR_ID'].astype('str')
df['QTR_ID'] = df['QTR_ID'].astype('str')

df["PROFIT"] = df["SALES"] - (df["QUANTITYORDERED"] * df["PRICEEACH"])
dfGroupByYear = df.groupby("YEAR_ID").sum()
dfGroupByYear["YEAR_ID"] = dfGroupByYear.index

# TRỰC QUAN HÓA DỮ LIỆU WEB APP
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

app = Dash(__name__)
app.title = 'Trực quan hóa dữ liệu'

figDoanhSoBanHangTheoNam = px.bar(dfGroupByYear, x='YEAR_ID', y="SALES",
                                    title='Doanh số bán hàng theo năm', color='YEAR_ID',
                                    labels={'YEAR_ID': 'Năm', 'SALES': 'Doanh số'})

figLoiNhuanBanHangTheoNam = px.line(dfGroupByYear, x='YEAR_ID', y="PROFIT",
                                    title='Lợi nhuận bán hàng theo năm',
                                    labels={'YEAR_ID': 'Năm', 'PROFIT': 'Lợi nhuận'})


figTileDoanhSo = px.sunburst(df, path=['YEAR_ID', 'MONTH_ID'], values='SALES',
                             color='SALES',
                             labels={'parent': 'Năm', 'id': 'Năm/tháng','SALES': 'Doanh số', 'SALES_sum': 'Tổng doanh số'},
                             title='Tỉ lệ đóng góp của doanh số theo từng danh mục trong từng năm')

figTileLoiNhuan = px.sunburst(df, path=['YEAR_ID', 'MONTH_ID'], values='PROFIT',
                              color='PROFIT',
                              labels={'parent': 'Năm', 'id': 'Năm/tháng', 'PROFIT': 'Lợi nhuận', 'PROFIT_sum': 'Tổng lợi nhuận'},
                              title='Tỉ lệ đóng góp của lợi nhuận theo từng danh mục trong từng năm')

total_sales = locale.currency(round(df["SALES"].sum(), 2), grouping=True)
total_profit = locale.currency(round(df['PROFIT'].sum(), 2), grouping=True)
top_sales = locale.currency(df['SALES'].max(), grouping=True)
top_profit = locale.currency(round(df['PROFIT'].max(), 2), grouping=True)                              

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=['XÂY DỰNG DANH MỤC SẢN PHẨM TIỀM NĂNG'],
                    className='header_title'
                ),
                html.Div(
                    children=['IUH - DHKTPM16B - 20098151 - NGUYỄN MINH QUÂN'],
                    className='header_title'
                )
            ],
            className='header'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3('DOANH SỐ SALE'),
                                html.Div(total_sales)
                            ],
                            className='card_statistic'
                        ),
                        html.Div(
                            children=[
                                html.H3('LỢI NHUẬN'),
                                html.Div(total_profit)
                            ],
                            className='card_statistic'
                        ),
                        html.Div(
                            children=[
                                html.H3('TOP DOANH SỐ'),
                                html.Div(top_sales)
                            ],
                            className='card_statistic'
                        ),
                        html.Div(
                            children=[
                                html.H3('TOP LỢI NHUẬN'),
                                html.Div(top_profit)
                            ],
                            className='card_statistic'
                        )
                    ],
                    className='content_statistic'
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[dcc.Graph(id='doanhsotheonam',figure=figDoanhSoBanHangTheoNam)],
                            className='card_chart'
                        ),
                        html.Div(
                            children=[dcc.Graph(id='tiledoanhso',figure=figTileDoanhSo)],
                            className='card_chart'
                        ),
                        html.Div(
                            children=[dcc.Graph(id='loinhuanthoenam',figure=figLoiNhuanBanHangTheoNam)],
                            className='card_chart'
                        ),
                        html.Div(
                            children=[dcc.Graph(id='tileloinhuan',figure=figTileLoiNhuan)],
                            className='card_chart'
                        )
                    ],
                    className='content_chart'
                )
            ]
        )
    ],
    className='wrapper'
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
