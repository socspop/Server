from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith('.exe'):  # Verifica la extensión del archivo
            file.save('archivo_cargado.exe')  # Guarda el archivo en el servidor
            return send_file('archivo_cargado.exe', as_attachment=True)
        else:
            return 'Error: Solo se permiten archivos .exe'
    return '''
        <h1>Web de carga y descarga de archivos</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Cargar archivo">
        </form>
    '''

if __name__ == '__main__':
    app.run()
