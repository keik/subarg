TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
DEV_DEPS="requirements-dev.txt"

test: init
	@echo $(TAG)$@$(END)
	flake8
	py.test tests --cov subarg --verbose

test-all: uninstall-all test
	@echo

init: uninstall-subarg
	@echo $(TAG)$@$(END)
	pip install --upgrade -r $(DEV_DEPS)
	pip install --upgrade --editable .

uninstall-all: uninstall-subarg
	@echo $(TAG)$@$(END)
	- pip uninstall --yes -r $(DEV_DEPS) 2>/dev/null

uninstall-subarg:
	@echo $(TAG)$@$(END)
	- pip uninstall --yes subarg 2>/dev/null
