import dj_database_url
import os


DATABASE_URL = 'postgres://plone:plone@localhost:5432/plone'
ENGINES = {
    'django.db.backends.postgresql_psycopg2': 'postgresql'
}


class Recipe(object):
    """
    """

    def __init__(self, buildout, name, options):
        """
        """

        parsed_options = dj_database_url.parse(
            os.getenv(
                'DATABASE_URL',
                DATABASE_URL))
        options['engine'] = ENGINES[parsed_options['ENGINE']]
        options['host'] = parsed_options['HOST']
        options['name'] = parsed_options['NAME']
        options['password'] = parsed_options['PASSWORD']
        options['port'] = str(parsed_options['PORT'])
        options['user'] = parsed_options['USER']

    def install(self):
        """
        """
        return tuple()
