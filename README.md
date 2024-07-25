# my_history

##### v0.2.0
![image](https://github.com/user-attachments/assets/8c3effd6-6d2e-4c82-b825-41103f8288aa)
***
##### v0.1.0
![image](https://github.com/user-attachments/assets/eadf0f51-50f1-4748-9c9d-0edaa2ac0a2f)

### Usage
##### v0.2.0
`mh` 명령어와 -s, -t, -d 인자를 받아 데이터를 출력합니다.

mh -s <search_query>			해당 단어를 포함하는 명령어의 사용횟수를 출력합니다.
```bash
$ mh -s ll 
ll 사용 횟수는 2039회 입니다.
```

mh -t <int>						인수로 주어진 마지막 t개 열의 데이터를 출력합니다. 인수가 주어지지 않으면 5를 기본으로 합니다.
```bash
$ mh -t 3
                     cmd  cnt
~//app/saveHistory/sv.sh   12
 ~/app/saveHistory/sv.sh   12
                       탶   12
```

mh -d <yyyy-mm-dd>				인수로 주어진 날짜의 데이터를 출력합니다.
```bash
$ mh -d 2024-07-17
                      cmd  cnt
                    which   25
~///app/saveHistory/sv.sh   17
 ~//app/saveHistory/sv.sh   17
  ~/app/saveHistory/sv.sh   17
                        탶   17
```

mh -t <int> -d <yyyy-mm-dd>		-t인자와 -d인자는 함께 사용될 수 있습니다.
```bash
$ mh -d 2024-07-17 -t 3
                     cmd  cnt
~//app/saveHistory/sv.sh   17
 ~/app/saveHistory/sv.sh   17
                       탶   17
```

모든 인자가 주어질 경우 -s인자에 대한 결과와 -t & -d 결과(총 2개)가 출력됩니다.
```bash
$ mh -s ll -d 2027-07-17 -t 3
```

모든 인자가 주어지지 않는 경우 모든 데이터가 출력됩니다.
```bash
$ mh
[알림] -s, -d, -t인자 모두 입력되지 않았습니다. 모든 데이터를 출력합니다.
***************************************************************************
                            cmd  cnt          dt
0                                 27  2024-07-12
1                        "1000"   21  2024-07-12
2                            $!   21  2024-07-12
3                          $AWS    4  2024-07-12
4                            ''   21  2024-07-12
...                         ...  ...         ...
1265                          ~   12  2024-07-22
1266  ~///app/saveHistory/sv.sh   12  2024-07-22
1267   ~//app/saveHistory/sv.sh   12  2024-07-22
1268    ~/app/saveHistory/sv.sh   12  2024-07-22
1269                          탶   12  2024-07-22

[1270 rows x 3 columns]
***************************************************************************
```

***
##### v0.1.0
`print-cnt` 명령어와 인자 하나를 받아 인자가 포함되는 명령어가 몇 번 사용되었는지 출력합니다.

```bash
$ print-cnt ls
ls을 포함하는 command는 255번 사용되었습니다.
```

인자를 제공하지 않으면 기본적으로 'aws'가 몇 번 사용되었는지 출력합니다.
```bash
$ print-cnt
aws을 포함하는 command는 34번 사용되었습니다.
```

### Dependency
##### v0.2.0
- pandas
- pyarrow
- argparse

***
##### v0.1.0
- pandas

### Licence
MIT
