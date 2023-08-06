test:
	check-manifest .
	flake8 collective/recipe/database_url/*.py
	pyroma .
	python setup.py test
	viewdoc

release:
	python setup.py sdist --format=zip upload
