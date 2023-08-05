from pyramid.response import Response
from .base import BaseTestCase


class TestSettingsDefault(BaseTestCase):

    def test_setup(self):
        request = self.make_request()
        bower = request.get_bower()

        self.assertEqual(bower.publisher_signature, 'bowerstatic')
        self.assertEqual(bower.components_path, None)
        self.assertEqual(bower.components_name, 'components')

    def test_include_path(self):

        def view(request):
            request.include('myapp')
            return Response('<html><head></head><body></body></html>')

        self.config.add_route('view', '/')
        self.config.add_view(view, route_name='view')

        self.config.add_bower_components('tests:bower_components')

        self.config.add_bower_component('tests:local_component', '1.0.0')

        app = self.make_app()
        response = app.get('/')

        self.assertEqual(response.body, (
            b'<html><head>'
            b'<script type="text/javascript" src='
            b'"/bowerstatic/components/anycomponent/1.0.0/anycomponent.js">'
            b'</script>\n<script type="text/javascript" '
            b'src="/bowerstatic/components/myapp/1.0.0/myapp.js"></script>'
            b'</head><body></body></html>'))


class TestSettingsCustom(BaseTestCase):

    _settings = {
        'djed.static.publisher_signature': 'static',
        'djed.static.components_path': 'tests:bower_components',
        'djed.static.components_name': 'lib',
    }

    def test_setup(self):
        request = self.make_request()
        bower = request.get_bower()

        self.assertEqual(bower.publisher_signature, 'static')
        self.assertEqual(bower.components_path, 'tests:bower_components')
        self.assertEqual(bower.components_name, 'lib')

    def test_include_path(self):

        def view(request):
            request.include('myapp')
            return Response('<html><head></head><body></body></html>')

        self.config.add_route('view', '/')
        self.config.add_view(view, route_name='view')

        self.config.add_bower_component('tests:local_component', '1.0.0')

        app = self.make_app()
        response = app.get('/')

        self.assertEqual(response.body, (
            b'<html><head>'
            b'<script type="text/javascript" src='
            b'"/static/lib/anycomponent/1.0.0/anycomponent.js">'
            b'</script>\n<script type="text/javascript" '
            b'src="/static/lib/myapp/1.0.0/myapp.js"></script>'
            b'</head><body></body></html>'))
