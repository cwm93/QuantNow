import tushare as ts

def inputData():
    df = ts.realtime_boxoffice()
    df.to_json('d:/boxr.json',orient='records')
    print(df)

if  __name__ == '__main__':
    inputData()
