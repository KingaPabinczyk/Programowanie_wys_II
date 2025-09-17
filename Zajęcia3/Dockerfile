FROM python:3.11-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj requirements i zainstaluj
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj cały projekt
COPY . .

# Ustaw domyślny entrypoint na bash, żeby łatwo było uruchamiać różne rzeczy
CMD ["/bin/bash"]
