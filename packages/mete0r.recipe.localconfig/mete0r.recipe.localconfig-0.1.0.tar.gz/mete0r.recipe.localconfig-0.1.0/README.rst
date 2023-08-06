mete0r.recipe.localconfig
=========================

override default config with local files


example::

        [buildout]
        parts = config

        [config]
        recipe = mete0r.recipe.localconfig
        localconfig.path = local-config.json

        foo = default-value

        [deploy]
        recipe = some-recipe-to-deploy
        option = ${config:foo}


local-config.json::

        {
                "foo": "local-value"
        }


Options
-------

`localconfig.path` (required)

path to external config file.

`localconfig.required` (optional, default: false)

whether the external config file should exists
