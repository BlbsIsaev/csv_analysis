# Небольшой скрипт для анализа csv файла вида ["name", "brand", "price", "rating"].

Скрипт вычисляет усредненный рейтинг по каждому бренду. 

Сохраняет в отчет в файл, выводит таблицу в stdout

В архитектуре заложена возможность добавления других отчетов.

## Пример запуска:


```python main.py -f ./file_one.csv ./file_two.csv -r rep.csv -t rating```


где флаг -f это файлы; флаг -r это название отчета; а флаг -t это тип отчета (rating или price).


<img width="632" height="201" alt="image" src="https://github.com/user-attachments/assets/c1468675-d686-47ce-9819-7c389fa9b7db" />

### для запуска тестов используйте ```pytest -v```

<img width="1280" height="196" alt="image" src="https://github.com/user-attachments/assets/fc40c27c-9809-4e75-8e2b-402f42fa65d2" />
