# my_history

### Usage
`mh` 명령어와 -s, -t, -d 인자를 받아 데이터를 출력합니다.

-s	search_query	해당 단어를 포함하는 명령어의 사용횟수를 출력합니다.
-t	tail		
-d	date		

```bash
$ mh -s ll 
ll 사용 횟수는 2039회 입니다.
```

인자를 제공하지 않으면 기본적으로 'aws'가 몇 번 사용되었는지 출력합니다.
```bash
$ print-cnt                                                                                                             aws을 포함하는 command는 34번 사용되었습니다.
```

### Dependency
- pandas

### Licence
MIT
