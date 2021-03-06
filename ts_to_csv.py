import tushare as ts
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--code", help="股票代码",default='000856')
parser.add_argument("--start", help="开始日期",default='2019-06-01')

args = parser.parse_args()

code = args.code
start  = args.start 

df = ts.get_k_data(code,start=start,index=False,ktype='D')

#选择保存  default first is date
#按照事件升序排序
df = df.set_index('date').sort_index(ascending=True)


df.to_csv('./datas/ts_'+code+'.csv',columns=['open', 'high', 'low', 'close', 'volume'])
