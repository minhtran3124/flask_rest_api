function active_env() {
    source venv/bin/activate
}

function run_app() {
    cd football_api/
    gunicorn --bind 127.0.0.1:5000 wsgi:app
}

function deactivate_env() {
    cd ..
    deactivate
}


active_env
