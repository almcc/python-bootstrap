.PHONEY: ci test

ci:
	nosetests --with-xunit --all-modules --traverse-namespace --with-coverage --cover-package=app --cover-inclusive
	python -m coverage xml --include=app*
	pylint -f parseable -d I0011,R0801 app | tee pylint.out
	rm pylint.out .coverage

test:
	@echo
	@echo
	@echo "Unit test coverage"
	@echo "=================="
	@echo
	@-nosetests --with-coverage --cover-package=app
	@echo
	@echo
	@echo "Code quality"
	@echo "============"
	@echo
	@-pylint -r n app
	@rm .coverage
