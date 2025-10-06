# 🚀 Промпт для полного рефакторинга tg-ytdlp-bot

## 📋 Задача
Провести полный clean up, refactoring и optimization кода Telegram бота для скачивания видео. Цель: сделать код чистым, красивым, лаконичным и оптимально работающим.

## 🎯 Основные цели
1. **Удалить неиспользуемые импорты** - найти и удалить все неиспользуемые import statements
2. **Устранить дублирование кода** - объединить дублирующиеся функции в одну копию
3. **Оптимизировать импорты** - заменить wildcard импорты на конкретные, сгруппировать по модулям
4. **Добавить типизацию** - добавить type hints для всех функций и переменных
5. **Улучшить структуру** - разбить длинные функции, улучшить читаемость
6. **Добавить документацию** - добавить docstrings для всех функций
7. **Оптимизировать производительность** - убрать избыточные вычисления, оптимизировать циклы

## 🔍 Конкретные проблемы для исправления

### 1. Дублирование импортов
- `from datetime import datetime` - 11 раз в разных файлах
- `from CONFIG.messages import Messages, get_messages_instance` - множество раз
- `from HELPERS.logger import *` - wildcard импорты

### 2. Неиспользуемые импорты
- `import glob` в magic.py (не используется)
- `import hashlib` в magic.py (не используется)
- `import io` в magic.py (не используется)
- `import json` в magic.py (не используется)
- `import logging` в magic.py (не используется)
- `import math` в magic.py (не используется)
- `import random` в magic.py (не используется)
- `import threading` в magic.py (не используется)
- `import time` в magic.py (не используется)
- `from types import SimpleNamespace` в magic.py (не используется)
- `from typing import Tuple` в magic.py (не используется)
- `import chardet` в magic.py (не используется)

### 3. Дублирование функций
- `log()` функция в `update_from_repo.py` и других модулях
- `safe_write_file()` может быть дублирована
- Функции работы с файлами в разных модулях

### 4. Wildcard импорты (import *)
Найти и заменить на конкретные импорты:
```python
# Плохо
from HELPERS.download_status import *
from HELPERS.filesystem_hlp import *
from HELPERS.limitter import *
from HELPERS.logger import *
from HELPERS.porn import *
from HELPERS.qualifier import *
from HELPERS.safe_messeger import *

# Хорошо
from HELPERS.download_status import set_active_download, clear_download_start_time
from HELPERS.filesystem_hlp import sanitize_filename, cleanup_user_temp_files
from HELPERS.limitter import TimeFormatter, humanbytes, check_user
from HELPERS.logger import logger, send_to_logger, send_to_user
```

### 5. Длинные функции
- `magic.py` - 335 строк, нужно разбить
- `always_ask_menu.py` - 5312 строк, критически нужно разбить
- `down_and_up.py` - 2622 строки, нужно разбить
- `image_cmd.py` - 3883 строки, нужно разбить

### 6. Отсутствие типизации
Добавить type hints для всех функций:
```python
# Плохо
def process_video(url, quality):
    pass

# Хорошо
def process_video(url: str, quality: str) -> bool:
    """Process video download with specified quality.
    
    Args:
        url: Video URL to process
        quality: Quality setting for download
        
    Returns:
        True if successful, False otherwise
    """
    pass
```

## 🛠️ План выполнения

### Этап 1: Анализ и очистка импортов
1. Сканировать все файлы на неиспользуемые импорты
2. Удалить неиспользуемые импорты
3. Заменить wildcard импорты на конкретные
4. Сгруппировать импорты по стандарту PEP8

### Этап 2: Устранение дублирования
1. Найти дублирующиеся функции
2. Создать общие утилиты в HELPERS/
3. Заменить дублирующийся код на вызовы общих функций

### Этап 3: Добавление типизации
1. Добавить type hints для всех функций
2. Добавить типы для переменных классов
3. Создать типы для сложных структур данных

### Этап 4: Рефакторинг больших файлов
1. Разбить `always_ask_menu.py` на логические модули
2. Разбить `down_and_up.py` на специализированные функции
3. Разбить `image_cmd.py` на отдельные команды
4. Упростить `magic.py`

### Этап 5: Оптимизация производительности
1. Убрать избыточные вычисления
2. Оптимизировать циклы
3. Добавить кэширование где необходимо
4. Улучшить обработку ошибок

### Этап 6: Документация
1. Добавить docstrings для всех функций
2. Добавить комментарии к сложной логике
3. Создать README для каждого модуля

## 📝 Специфические инструкции

### Для magic.py:
- Удалить неиспользуемые импорты (glob, hashlib, io, json, logging, math, random, threading, time, SimpleNamespace, Tuple, chardet)
- Заменить wildcard импорты на конкретные
- Разбить на логические блоки
- Добавить типизацию

### Для always_ask_menu.py:
- Разбить на модули по функциональности
- Создать отдельные классы для разных типов меню
- Вынести общую логику в базовые классы

### Для down_and_up.py:
- Разбить на функции по этапам обработки
- Создать отдельные модули для разных типов контента
- Вынести общую логику в утилиты

### Для image_cmd.py:
- Разбить на отдельные команды
- Создать базовый класс для команд
- Вынести общую логику обработки изображений

## 🎯 Ожидаемый результат

После рефакторинга код должен:
1. ✅ Не содержать неиспользуемых импортов
2. ✅ Не содержать дублирующегося кода
3. ✅ Иметь конкретные импорты вместо wildcard
4. ✅ Содержать type hints для всех функций
5. ✅ Иметь функции не длиннее 50 строк
6. ✅ Содержать docstrings для всех функций
7. ✅ Быть оптимизированным по производительности
8. ✅ Быть легко читаемым и поддерживаемым

## 🚀 Начать с файлов в порядке приоритета:
1. `magic.py` - главный файл, много проблем
2. `always_ask_menu.py` - самый большой файл
3. `down_and_up.py` - критически важный модуль
4. `image_cmd.py` - большой файл с командами
5. Остальные файлы по размеру

Выполняй рефакторинг пошагово, проверяя каждый файл на работоспособность после изменений.
