
# Agent (.NET 8, WPF)

## Сбор метрик
Использование LibreHardwareMonitor 0.9.4, сбор:
- CPU (temp, freq, load, power)
- GPU (load, temp, vram)
- RAM usage
- Disk I/O
- Fans, PSU

## Архитектура агента

```ascii
+-------------------------------+
|        WPF UI (Charts)        |
+-------------------------------+
| LiveCharts ⟷ Metrics Buffer   |
+-------------------------------+
| LibreHardwareMonitor Service  |
+-------------------------------+
| ZIP Packager & Network Sender |
+-------------------------------+
```

## Отправка данных
Файлы JSON → ZIP → POST /api/upload (multipart/form-data).

## План развития
- автообновление
- очереди повторной отправки
- улучшенная обработка ошибок драйверов
