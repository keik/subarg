TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
SELF="subarg"

test:
	@echo $(TAG)$@$(END)
	flake8
	py.test --verbose tests
