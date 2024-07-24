import pandas as pd
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-s')
parser.add_argument('-t')
parser.add_argument('-d')

args=parser.parse_args()

df=pd.read_parquet('~/data/parquet')

def call():
    if args.s==None and args.d==None and args.t==None:
        print("[알림] -s, -d, -t인자 모두 입력되지 않았습니다. 모든 데이터를 출력합니다.")
        print("***************************************************************************")
        print(df)
        print("***************************************************************************")
    if args.s!=None:
        print(f"{args.s} 사용 횟수는 {df.loc[df['cmd'].str.contains(args.s)].cnt.sum()}회 입니다.")
#    if args.t != None and args.d != None:
#        print(df.loc[df.dt==args.d].drop(['dt'],axis=1).tail(int(args.t)).to_string(index=False))
    if args.d != None:
#        print(df.loc[df.dt==args.d].drop(['dt'], axis=1).to_string(index=False))
        print(df.loc[df.dt==args.d].drop(['dt'],axis=1).tail(int(args.t if args.t else 5)).to_string(index=False))
    elif args.t != None:
        print(df.tail(int(args.t)).drop(['dt'],axis=1).to_string(index=False))
    else:
        pass

#call()
