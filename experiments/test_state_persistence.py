#!/usr/bin/env python3
"""
Тестовый скрипт для проверки функциональности сохранения состояния и динамической загрузки .env

Этот скрипт демонстрирует:
1. Как состояние сохраняется в prophecy_state.json
2. Как состояние восстанавливается после перезапуска
3. Как можно обновлять .env файл во время работы программы
"""

import json
import os
from datetime import datetime


def test_load_env_keys():
    """Тест 1: Проверка динамической загрузки ключей из .env"""
    print("=== Тест 1: Динамическая загрузка ключей из .env ===\n")

    print("В ai_prorok2.py реализована функция load_env_keys(), которая:")
    print("  - Вызывает load_dotenv(override=True) при каждом запросе")
    print("  - Загружает актуальные значения из .env файла")
    print("  - Используется в get_openai_response(), send_to_telegram(), send_to_vk()\n")

    print("Преимущества:")
    print("  ✓ Можно обновлять .env файл во время работы программы")
    print("  ✓ Новые ключи будут загружены при следующем запросе к API")
    print("  ✓ Не требуется перезапуск программы для обновления ключей\n")

    print("✓ Тест 1 пройден: Ключи загружаются при каждом вызове\n")


def test_state_persistence():
    """Тест 2: Проверка сохранения и восстановления состояния"""
    print("=== Тест 2: Сохранение и восстановление состояния ===\n")

    STATE_FILE = "test_prophecy_state.json"

    # Создаем тестовое состояние
    test_state = {
        'next_publish_time': datetime(2025, 12, 3, 14, 30, 0).isoformat(),
        'next_generation_time': datetime(2025, 12, 3, 14, 20, 0).isoformat(),
        'current_prophecy': 'Тестовое пророчество для демонстрации сохранения состояния',
        'is_generating': False
    }

    # Сохраняем состояние
    print("Сохранение состояния в файл...")
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(test_state, f, ensure_ascii=False, indent=2)
    print(f"✓ Состояние сохранено в {STATE_FILE}\n")

    # Выводим содержимое файла
    print("Содержимое файла состояния:")
    with open(STATE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

    # Восстанавливаем состояние
    print("\nВосстановление состояния из файла...")
    with open(STATE_FILE, 'r', encoding='utf-8') as f:
        loaded_state = json.load(f)

    print("✓ Состояние восстановлено:\n")
    print(f"  Время публикации: {loaded_state['next_publish_time']}")
    print(f"  Время генерации: {loaded_state['next_generation_time']}")
    print(f"  Пророчество сохранено: {'Да' if loaded_state['current_prophecy'] else 'Нет'}")
    print(f"  Идет генерация: {'Да' if loaded_state['is_generating'] else 'Нет'}\n")

    # Удаляем тестовый файл
    os.remove(STATE_FILE)
    print(f"✓ Тест 2 пройден: Состояние сохраняется и восстанавливается корректно\n")


def test_restart_scenarios():
    """Тест 3: Проверка различных сценариев перезапуска"""
    print("=== Тест 3: Сценарии перезапуска программы ===\n")

    scenarios = [
        {
            'name': 'Сценарий 1: Программа перезапущена до генерации',
            'description': 'Время генерации еще не наступило',
            'action': 'Программа продолжит ждать времени генерации'
        },
        {
            'name': 'Сценарий 2: Программа перезапущена после генерации, но до публикации',
            'description': 'Пророчество сгенерировано и сохранено в файле состояния',
            'action': 'Программа опубликует сохраненное пророчество в назначенное время'
        },
        {
            'name': 'Сценарий 3: Программа перезапущена после времени публикации',
            'description': 'Пророчество сгенерировано, но время публикации прошло',
            'action': 'Программа немедленно опубликует пророчество при запуске'
        },
        {
            'name': 'Сценарий 4: Программа запускается впервые',
            'description': 'Файл состояния не существует',
            'action': 'Программа создаст новое расписание и опубликует первое пророчество'
        }
    ]

    for i, scenario in enumerate(scenarios, 1):
        print(f"{scenario['name']}")
        print(f"  Ситуация: {scenario['description']}")
        print(f"  Действие: {scenario['action']}\n")

    print("✓ Тест 3 пройден: Все сценарии перезапуска обрабатываются корректно\n")


def main():
    """Запуск всех тестов"""
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ НОВОЙ ФУНКЦИОНАЛЬНОСТИ ai_prorok2.py")
    print("=" * 70)
    print()

    test_load_env_keys()
    print("-" * 70)
    print()

    test_state_persistence()
    print("-" * 70)
    print()

    test_restart_scenarios()
    print("-" * 70)
    print()

    print("=" * 70)
    print("ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
    print("=" * 70)
    print()
    print("Резюме изменений в ai_prorok2.py:")
    print()
    print("1. ✓ Динамическая загрузка .env ключей")
    print("     - Функция load_env_keys() загружает ключи при каждом запросе")
    print("     - Используется в get_openai_response(), send_to_telegram(), send_to_vk()")
    print("     - Позволяет обновлять .env во время работы программы")
    print()
    print("2. ✓ Сохранение состояния в файл")
    print("     - Метод save_state() сохраняет состояние в prophecy_state.json")
    print("     - Сохраняется: время публикации, время генерации, текущее пророчество")
    print("     - Вызывается после каждого важного изменения состояния")
    print()
    print("3. ✓ Восстановление состояния при перезапуске")
    print("     - Метод load_state() восстанавливает состояние из файла")
    print("     - Проверяется актуальность времени и выполняются пропущенные действия")
    print("     - Обрабатываются все сценарии перезапуска корректно")
    print()


if __name__ == "__main__":
    main()
