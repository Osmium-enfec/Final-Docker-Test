FROM python:3.11-slim

# Security: no cache, no pip cache, no root
RUN useradd -m judgeuser && \
    mkdir -p /app && chown judgeuser:judgeuser /app && \
    mkdir -p /tmp && chmod 1777 /tmp
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir django>=4.2 pytest pytest-django

# Copy Django project files to /app
# Structure: /app/manage.py, /app/settings.py, /app/urls.py, /app/app/ (with views.py)
COPY manage.py /app/manage.py
COPY settings.py /app/settings.py
COPY urls.py /app/urls.py
COPY pytest.ini /app/pytest.ini
COPY app/ /app/app/
COPY tests/ /app/tests/
COPY runner.sh /runner.sh
RUN chmod +x /runner.sh

ENV PYTHONPATH=/app

USER judgeuser
ENTRYPOINT ["/runner.sh"]
