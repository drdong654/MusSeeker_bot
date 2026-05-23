# MusSeeker_bot

## Запуск

```bash
# Установка
uv pip install .

# Запуск
python __main__.py
```

Требуется `TOKEN=...` в `.env`.

## Структура проекта

```
musbot/
├── __init__.py          # пакет
├── __main__.py          # точка входа, polling
├── config.py            # TOKEN, DOWNLOAD_DIR, конфиги
├── keyboards.py         # reply + inline клавиатуры
├── handlers/
│   ├── __init__.py
│   ├── commands.py      # /start, /menu, /help, /lol
│   └── download.py      # скачивание по ссылке + callback
└── services/
    ├── __init__.py
    └── downloader.py    # yt-dlp обёртка (UUID, обработка ошибок)
```

## Архитектура

- Каждый файл хендлеров создаёт свой `Router`, который регистрируется в `dp` через `include_router()`.
- Клавиатуры вынесены в `keyboards.py` — единый источник правды.
- Конфиг в `config.py` — токен, пути, настройки.
- `services/downloader.py` — синхронная обёртка yt-dlp с UUID-файлами.

## Зависимости

- `aiogram>=3.0`
- `python-dotenv>=1.0`
- `yt-dlp>=2024.0`
