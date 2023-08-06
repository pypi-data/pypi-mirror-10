collective.recipe.database_url
==============================

Use `dj-database-url <https://github.com/kennethreitz/dj-database-url>`_ to parse DATABASE_URL for Buildout environments

::

    [buildout]
    develop = .
    extends =
        https://raw.githubusercontent.com/plock/pins/master/plone-4-3
        https://raw.githubusercontent.com/plock/pins/master/dev
    #    https://raw.githubusercontent.com/plock/pins/master/relstorage

    # https://raw.githubusercontent.com/plock/pins/master/relstorage
    [plone]
    eggs += 
        RelStorage
        psycopg2
    parts += database_url
    rel-storage =
        dbname ${database_url:name}
        host ${database_url:host}
        type ${database_url:engine}
        user ${database_url:user}
        password ${database_url:password}

    [database_url]
    recipe = collective.recipe.database_url
