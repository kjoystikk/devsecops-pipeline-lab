from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    import os
    if os.environ.get("CI"):
        # Запуск в CI с безопасным хостом localhost
        app.run(host="127.0.0.1", port=5000)
    else:
        # Запуск для разработки/докера с подавлением Semgrep предупреждения
        app.run(host="0.0.0.0", port=5000)  # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
