import pandas as pd
import sys

def cnt(q):
    df=read_parquet()
    fdf = df[df['cmd'].str.contains(q)]
    cnt = fdf['cnt'].sum()

    return cnt


def query():
    q=sys.argv[1]
    i=cnt(q)

    print(f'질의 {q}에 대한 결과는 {i}입니다.')
    print(f'질의 %10s에 대한 결과는 %s입니다.' %  (q,i))
    print('질의 ',q,'에 대한 결과는 ',i,'입니다.')


def read_parquet(path="~/tmp/history.parquet"):
    df=pd.read_parquet(path)
    return df
