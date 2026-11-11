import datetime

agora = datetime.datetime.now()

data_formatada = f"{agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_formatada = f"{agora.hour:02d}:{agora.minute:02d}"

print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
