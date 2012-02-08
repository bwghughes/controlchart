ci: 
	sniffer . -x--with-coverage -x--cover-package=controlchart 

cov:
	nosetests --with-coverage --cover-package=controlchart --xunit-file=nosetests.xml

hudson:
	nosetests --with-xunit --xunit-file=test-reports/coverage.xml --with-coverage --cover-package=controlchart --cover-html-dir=./test-reports --cover-html

docs: 
	hg log > HISTORY.md

clean:
	rm -rf build
	rm -rf dist
	rm -rf controlchart.egg-info 
	rm nosetests.xml
	rm -rf test-reports





