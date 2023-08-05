
import os

from noseapp.plugins.base import AppPlugin


class AppConfigurePlugin(AppPlugin):

    name = 'app-configure'

    def options(self, parser, env=os.environ):
        super(AppConfigurePlugin, self).options(parser, env=env)

        parser.add_option(
            '--app-processes',
            dest='app_processes',
            default=0,
            type=int,
            help='Num of processes for running. one process == one suite.'
        )
        parser.add_option(
            '--gevent',
            dest='gevent_pool',
            default=0,
            type=int,
            help='Num of greenlets for running. One greenlet == one suite.'
        )
        parser.add_option(
            '--greenlets',
            dest='gevent_greenlets',
            default=0,
            type=int,
            help='Num of greenlets for running. One greenlet == one test case.'
        )
        parser.add_option(
            '--threads',
            dest='thread_pool',
            default=0,
            type=int,
            help='Num of threads for running. If app processes is set, one thread == one test case, '
                 'else one thread == one suite.'
        )
        parser.add_option(
            '--ls',
            dest='ls',
            action='store_true',
            default=False,
            help='Show suites tree.'
        )
        parser.add_option(
            '--doc',
            dest='doc',
            action='store_true',
            default=False,
            help='Show docstring of test cases.'
        )
        parser.add_option(
            '-t', '--test',
            dest='run_test',
            default='',
            type=str,
            help='Test case or suite name for running.'
        )

        try:  # if app instance is does not pushed to plugin,
            # AttributeError will be passed.
            self.app.parser = parser
            self.app.add_options()
        except AttributeError:
            pass
