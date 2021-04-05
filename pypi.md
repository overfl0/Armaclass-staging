Checklist to push a release to PyPi:

* Run tests
* Update version in setup.py
* git tag
* git push
* git push --tag
* python setup.py sdist
* aws --endpoint-url https://s3.fr-par.scw.cloud s3 sync s3://armaclass/<id> dist
* twine upload --repository-url https://test.pypi.org/legacy/ dist/*
* twine upload dist/something
