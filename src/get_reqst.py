from http.server import BaseHTTPRequestHandler, HTTPServer


class ContactServer(BaseHTTPRequestHandler):
    """Класс для соединения с сетью"""
    def do_GET(self):
        """метод запроса"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("{'message': 'OK'}", "utf-8"))

        try:
            with open("contact_web.html.", "r", encoding="utf-8") as file:
                content = file.read()
                self.wfile.write(content.encode("utf-8"))
        except Exception as e:
            self.send_error(500, f"Ошибка сервера: {e}")


def run_server():
    """Метод реализации"""
    server_address = ("localhost", 8080)  # Хост и порт
    httpd = HTTPServer(server_address, ContactServer)
    print("Сервер запущен на http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

