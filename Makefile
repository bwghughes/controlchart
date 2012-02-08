ci: 
	sniffer .

cov:
	nosetests --with-coverage --cover-package=controlchart --xunit-file=nosetests.xml

hudson:
	nosetests --with-xunit --xunit-file=test-reports/coverage.xml --with-coverage --cover-package=controlchart --cover-html-dir=./test-reports --cover-html

docs: 
	hg log > HISTORY.rst





