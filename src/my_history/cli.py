import pandas as pd
import sys

a=sys.argv[1] if len(sys.argv)>1 else 'aws'

def cnt():
    df = pd.read_parquet("~/tmp/history.parquet")

    search_keyword=sys.argv[1] if len(sys.argv)>1 else 'aws'
    
    fdf = df[df['cmd'].str.contains(search_keyword)]

    cnt = fdf['cnt'].sum()

    print(f'{search_keyword}을 포함하는 command는 {cnt}번 사용되었습니다.')
