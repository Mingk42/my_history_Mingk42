# my_history
![image](https://github.com/user-attachments/assets/eadf0f51-50f1-4748-9c9d-0edaa2ac0a2f)

### Usage
`print-cnt` 명령어와 인자 하나를 받아 인자가 포함되는 명령어가 몇 번 사용되었는지 출력합니다.

```bash
$ print-cnt ls
ls을 포함하는 command는 255번 사용되었습니다.
```

인자를 제공하지 않으면 기본적으로 'aws'가 몇 번 사용되었는지 출력합니다.
```bash
$ print-cnt                                                                                                             aws을 포함하는 command는 34번 사용되었습니다.
```

### Dependency
- pandas

### Licence
MIT
