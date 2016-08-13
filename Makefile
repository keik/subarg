TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
SELF="subarg"

test: init
	@echo $(TAG)$@$(END)
	flake8
	py.test --verbose tests

init: uninstall
	@echo $(TAG)$@$(END)
	pip install --upgrade --editable .

uninstall:
	@echo $(TAG)$@$(END)
	@echo no dependencies to uninstall
