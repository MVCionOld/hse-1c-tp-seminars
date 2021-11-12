```shell
python3 -m unittest strings                               # тестируем весь модуль
python3 -m unittest strings.TestStringMethods             # тестируем конкретный класс модуля
python3 -m unittest strings.TestStringMethods.test_split  # тестируем конкретный метод класса
```

```shell
# С помощью флага -v (verbose==подробный) можно получить более детальный отчёт:
python3 -m unittest -v strings
```