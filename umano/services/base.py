from abc import ABC
from optparse import make_option, OptionParser

from umano.hal.data import store


class UmanoService(object):
    help = "unknown umano service usage"
    option_list = [
        make_option(
            '-n',
            '--name',
            dest='NAME',
            type=str,
            default="unknown umano service",
            help='service name (default "unknown umano service")'
        ),
    ]

    def __init__(self) -> None:
        super().__init__()

    def create_parser(self):
        parser = OptionParser(option_list=self.option_list)
        parser.set_usage(self.help)
        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser):
        pass

    def run(self, *args, **options):
        try:
            self.execute(args, options)
        except KeyboardInterrupt:
            pass

    def execute(self, *args, **options):
        raise NotImplementedError()

    def print_help(self):
        parser = self.create_parser()
        parser.print_help()


class UmanoStreamService(UmanoService, ABC):
    option_list = UmanoService.option_list + [
        make_option(
            '-p',
            '--port',
            dest='PORT',
            type=int,
            default=5000,
            help='port to listen to (default 5000)'
        ),
        make_option(
            '-i',
            '--ip',
            dest='HOST',
            type=str,
            default="0.0.0.0",
            help='ip to bind to (default "0.0.0.0")'
        ),

    ]

