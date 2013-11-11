.PHONEY: test

test:
	@echo
	@echo
	@echo "Unit test coverage"
	@echo "=================="
	@echo
	@nosetests --with-coverage --cover-package=app
	@echo
	@echo
	@echo "Code quality"
	@echo "============"
	@echo
	@pylint -r n app
