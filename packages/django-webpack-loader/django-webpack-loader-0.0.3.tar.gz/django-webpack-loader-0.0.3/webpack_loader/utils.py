import json
import time

from django.conf import settings

bundle_url = getattr(settings, 'WEBPACK_BUNDLE_URL', 'webpack_bundles/')
stats_file = getattr(settings, 'WEBPACK_STATS_FILE_PATH', 'webpack-stats.json')


__all__ = ('get_bundle',)


class WebpackException(BaseException):
    pass


def get_assets():
    try:
        return json.loads(
            open(stats_file).read())
    except ValueError:
        return {'status': 'compiling'}


def get_bundle(bundle_name):
    assets = get_assets()

    while assets['status'] == 'compiling':
        time.sleep(0.5)
        assets = get_assets()

    if assets.get('status') == 'done':
        bundle = assets['chunks'][bundle_name]
        for F in bundle:
            F['url'] = '{}{}'.format(bundle_url, F['name'])
        return bundle

    elif assets.get('status') == 'error':
        error = """
        {error} in {file}
        {message}
        """.format(**assets)
        raise WebpackException(error)
