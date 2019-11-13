import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from optparse import make_option

from umano.services.base import UmanoServerService


class HttpServer(UmanoServerService):
    option_list = UmanoServerService.option_list + [
        make_option(
            '--directory',
            dest='DIRECTORY',
            type=str,
            default=os.getcwd(),
            help='directory to serve from (default cwd)'
        ),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.description = "Http server from directory"

    def execute(self, args, options):
        server_address = ('', options.PORT)
        handler_class = partial(SimpleHTTPRequestHandler, directory=options.DIRECTORY)
        with ThreadingHTTPServer(server_address, handler_class) as httpd:
            sa = httpd.socket.getsockname()
            serve_message = "Serving HTTP on {host} port {port} (http://{host}:{port}/) ..."
            self.log(msg=serve_message.format(host=sa[0], port=sa[1]))
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                self.terminate()


if __name__ == "__main__":
    service = HttpServer()
    service.run()
