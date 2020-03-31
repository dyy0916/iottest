### 配置数据库
修改 setting.py 修改数据库配置，如下所示：
```python
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'PCTEST',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 3306,
        }
    }
```
### 创建数据库
mysql数据库中执行:
```mysql
CREATE DATABASE `PCTEST`  DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
然后终端下执行:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
### 创建超级用户

```bash
python3 manage.py createsuperuser
```

### 导入数据
进入数据库执行
```
source init.sql
```
### 开始运行
```bash
python3 manage.py runserver 0.0.0.0:8000
```
