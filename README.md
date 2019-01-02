# Database Expt.
for database course

### Connect to MySQL
```python
from orm import Database

Database.connect(
    host='localhost',
    port=3306,
    user='mysql',
    password='mysql',
    database='test'
)
```

### Model Defination
```python
from orm import Model, Field

class TestModel(Model):
    table = 'Test'

    a = Field()
    b = Field()
```

### Insert
```python
test = TestModel()
test.a = 1
test.b = 2
test.c = 3
test.d = 4
test.save()
```

### Query
```python
for t in TestModel.where(a=1).select():
    print(t.a, t.b, t.c, t.d)

for t in TestModel.where(TestModel.a<2).select():
    print(t.a, t.b, t.c, t.d)

for t in TestModel.where(TestModel.a<2, TestModel.b>1, c=3, d = 4).select():
    print(t.a, t.b, t.c, t.d)
```

### Count
```python
print(TestModel.where(TestModel.a < 2).count())
```

### Update
```python
print(TestModel.where(a=1).update(a=5))
```