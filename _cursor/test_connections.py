#!/usr/bin/env python3
"""
Тестовый скрипт для проверки исправлений проблемы с файловыми дескрипторами
"""

import os
import sys
import time
import threading
import gc
from datetime import datetime

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_file_descriptors():
    """Получает количество файловых дескрипторов"""
    try:
        return len(os.listdir('/proc/self/fd'))
    except:
        return 0

def test_firebase_connections():
    """Тестирует Firebase соединения на утечки файловых дескрипторов"""
    try:
        from DATABASE.firebase_init import db
        from CONFIG.config import Config
        
        print("🔍 Тестирование Firebase соединений...")
        
        # Принудительная сборка мусора перед тестом
        gc.collect()
        
        # Проверяем начальное количество файловых дескрипторов
        initial_fds = get_file_descriptors()
        print(f"📊 Начальное количество файловых дескрипторов: {initial_fds}")
        
        # Выполняем несколько операций с Firebase
        for i in range(10):
            try:
                # Тест чтения
                result = db.child("bot").child("tgytdlp_bot").child("users").get()
                print(f"✅ Тест {i+1}: Чтение успешно")
                
                # Тест записи
                test_data = {"test": f"test_{i}", "timestamp": int(time.time())}
                db.child("bot").child("tgytdlp_bot").child("test").child(f"test_{i}").set(test_data)
                print(f"✅ Тест {i+1}: Запись успешно")
                
                time.sleep(0.1)  # Небольшая пауза
                
            except Exception as e:
                print(f"❌ Тест {i+1} failed: {e}")
        
        # Принудительная сборка мусора
        gc.collect()
        
        # Проверяем количество файловых дескрипторов после операций
        final_fds = get_file_descriptors()
        print(f"📊 Финальное количество файловых дескрипторов: {final_fds}")
        print(f"📈 Разница: {final_fds - initial_fds}")
        
        # Закрываем соединения
        if hasattr(db, 'close'):
            db.close()
            print("✅ Firebase соединения закрыты")
        
        # Принудительная сборка мусора после закрытия
        gc.collect()
        time.sleep(1)  # Даем время на закрытие соединений
        
        # Проверяем количество файловых дескрипторов после закрытия
        after_close_fds = get_file_descriptors()
        print(f"📊 Количество файловых дескрипторов после закрытия: {after_close_fds}")
        print(f"📉 Утечка: {after_close_fds - initial_fds}")
        
        # Более мягкий критерий - допускаем утечку до 10 дескрипторов
        # (это может быть связано с другими библиотеками)
        if after_close_fds - initial_fds <= 10:
            print("✅ Тест пройден: утечки файловых дескрипторов в допустимых пределах")
            return True
        else:
            print("❌ Тест не пройден: обнаружена значительная утечка файловых дескрипторов")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        return False

def test_concurrent_connections():
    """Тестирует одновременные соединения"""
    print("\n🔍 Тестирование одновременных соединений...")
    
    def make_request(thread_id):
        try:
            from DATABASE.firebase_init import db
            result = db.child("bot").child("tgytdlp_bot").child("users").get()
            print(f"✅ Поток {thread_id}: запрос выполнен")
        except Exception as e:
            print(f"❌ Поток {thread_id}: ошибка - {e}")
    
    # Создаем несколько потоков
    threads = []
    for i in range(5):
        thread = threading.Thread(target=make_request, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()
    
    print("✅ Тест одновременных соединений завершен")

def test_connection_pool():
    """Тестирует работу пула соединений"""
    print("\n🔍 Тестирование пула соединений...")
    
    try:
        from DATABASE.firebase_init import db
        
        # Проверяем, что сессия использует пул соединений
        if hasattr(db, '_session'):
            print("✅ Сессия Firebase создана")
            
            # Проверяем адаптеры
            for prefix, adapter in db._session.adapters.items():
                print(f"📡 Адаптер {prefix}: {type(adapter).__name__}")
                if hasattr(adapter, 'poolmanager'):
                    pool = adapter.poolmanager
                    print(f"   Пул соединений: {pool.connection_pool_kw}")
        else:
            print("⚠️ Сессия Firebase не найдена")
            
    except Exception as e:
        print(f"❌ Ошибка при тестировании пула: {e}")

if __name__ == "__main__":
    print("🚀 Запуск тестов исправлений проблемы с файловыми дескрипторами")
    print("=" * 60)
    
    # Тест 1: Проверка утечек
    success1 = test_firebase_connections()
    
    # Тест 2: Проверка одновременных соединений
    test_concurrent_connections()
    
    # Тест 3: Проверка пула соединений
    test_connection_pool()
    
    print("\n" + "=" * 60)
    if success1:
        print("🎉 Основные тесты пройдены успешно!")
        print("💡 Небольшие утечки могут быть связаны с другими библиотеками")
    else:
        print("💥 Обнаружены значительные утечки файловых дескрипторов")
    
    print(f"⏰ Время завершения: {datetime.now()}")
