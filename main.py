from app import create_app
from app.models import station, line


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return { "station" : station, "line": line}
    
    
