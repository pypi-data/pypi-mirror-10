import asyncio
import aiohttp
import aiohttp_mako
from aiohttp import web

from aiohttp_debugtoolbar import (toolbar_middleware_factory,
                                  setup as tbsetup, APP_KEY)

from .base import BaseTest


class TestExceptionViews(BaseTest):
    @asyncio.coroutine
    def _setup_app(self, handler, **kw):
        app = web.Application(loop=self.loop,
                              middlewares=[toolbar_middleware_factory])

        tbsetup(app, **kw)
        lookup = aiohttp_mako.setup(app, input_encoding='utf-8',
                                    output_encoding='utf-8',
                                    default_filters=['decode.utf8'])
        tplt = "<html><body><h1>${head}</h1>${text}</body></html>"
        lookup.put_string('tplt.html', tplt)

        app.router.add_route('GET', '/', handler)

        srv = yield from self.loop.create_server(
            app.make_handler(), '127.0.0.1', self.port)
        self.addCleanup(srv.close)
        return app

    def test_view_source(self):
        @asyncio.coroutine
        def func(request):
            raise NotImplementedError

        @asyncio.coroutine
        def go():
            app = yield from self._setup_app(func)
            # make sure that exception page rendered
            resp = yield from aiohttp.request('GET', self.url, loop=self.loop)
            txt = yield from resp.text()
            self.assertEqual(500, resp.status)
            self.assertTrue('<div class="debugger">' in txt)

            token = app[APP_KEY]['pdtb_token']
            exc_history = app[APP_KEY]['exc_history']

            for frame_id in exc_history.frames:
                url = '{}/_debugtoolbar/source?frm={}&token={}'.format(
                    self.url, frame_id, token)
                exc_history = app[APP_KEY]['exc_history']
                resp = yield from aiohttp.request('GET', url,
                                                  loop=self.loop)
                yield from resp.text()
                self.assertEqual(resp.status, 200)

        self.loop.run_until_complete(go())

    def test_view_execute(self):
        @asyncio.coroutine
        def func(request):
            raise NotImplementedError

        @asyncio.coroutine
        def go():
            app = yield from self._setup_app(func)
            # make sure that exception page rendered
            resp = yield from aiohttp.request('GET', self.url, loop=self.loop)
            txt = yield from resp.text()
            self.assertEqual(500, resp.status)
            self.assertTrue('<div class="debugger">' in txt)

            token = app[APP_KEY]['pdtb_token']
            exc_history = app[APP_KEY]['exc_history']

            for frame_id in exc_history.frames:
                params = {'frm': frame_id, 'token': token}
                url = '{}/_debugtoolbar/source'.format(self.url)
                resp = yield from aiohttp.request('GET', url, params=params,
                                                  loop=self.loop)
                yield from resp.text()
                self.assertEqual(resp.status, 200)

                params = {'frm': frame_id, 'token': token,
                          'cmd': 'dump(object)'}
                url = '{}/_debugtoolbar/execute'.format(self.url)
                resp = yield from aiohttp.request('GET', url, params=params,
                                                  loop=self.loop)
                yield from resp.text()
                self.assertEqual(resp.status, 200)

            # wrong token
            params = {'frm': frame_id, 'token': 'x', 'cmd': 'dump(object)'}
            resp = yield from aiohttp.request('GET', url, params=params,
                                              loop=self.loop)
            self.assertEqual(resp.status, 400)
            # no token at all
            params = {'frm': frame_id, 'cmd': 'dump(object)'}
            resp = yield from aiohttp.request('GET', url, params=params,
                                              loop=self.loop)
            self.assertEqual(resp.status, 400)

        self.loop.run_until_complete(go())

    def test_view_exception(self):
        @asyncio.coroutine
        def func(request):
            raise NotImplementedError

        @asyncio.coroutine
        def go():
            app = yield from self._setup_app(func)
            # make sure that exception page rendered
            resp = yield from aiohttp.request('GET', self.url, loop=self.loop)
            txt = yield from resp.text()
            self.assertEqual(500, resp.status)
            self.assertTrue('<div class="debugger">' in txt)

            token = app[APP_KEY]['pdtb_token']
            exc_history = app[APP_KEY]['exc_history']

            tb_id = list(exc_history.tracebacks.keys())[0]
            url = '{}/_debugtoolbar/exception?tb={}&token={}'.format(
                self.url, tb_id, token)

            resp = yield from aiohttp.request('GET', url,
                                              loop=self.loop)
            yield from resp.text()
            self.assertEqual(resp.status, 200)
            self.assertTrue('<div class="debugger">' in txt)

        self.loop.run_until_complete(go())
