from app import create_app

app = create_app()

if __name__ == '__main__':
    # debug=True es vital para que veas los errores en el navegador
    print("🚀 Levantando servidor en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)