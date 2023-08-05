GitHub Sloth CI validator that validates the `GitHub <https://github.com/>`_ payload against username and repo name (obtained from the Sloth app config).

Usage in the app config::

    provider:
        github:
            # Repository owner. Mandatory parameter.
            owner: moigagoo

            # Repository title as it appears in the URL, i.e. slug.
            # Mandatory parameter.
            repo: sloth-ci

            # Only pushes to these branches will initiate a build.
            # Skip this parameter to allow all branches to fire builds.
            branches:
                - master
                - staging


