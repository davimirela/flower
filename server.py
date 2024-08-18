import http.server
import socketserver

# Definimos a porta onde o servidor vai rodar (8000 é uma escolha comum)
PORT = 8000

# Configuramos o servidor para servir os arquivos da pasta atual
Handler = http.server.SimpleHTTPRequestHandler

# Criamos o servidor na porta definida
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # Mantém o servidor rodando para servir os arquivos
    httpd.serve_forever()
