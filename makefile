ENV=poetry run

all:
	@echo "try 'make help'"

help: # show all commands
	@sed -n 's/:.#/:/p' makefile | grep -v @

clean: clean-eggs clean-build # clean cached files
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .pytest_cache/
	@rm -fr *.egg-info
	@rm -rf .eggs/
	@rm -fr build/
	@rm -fr dist/

lint: # lint all files
	$(ENV) pre-commit run -a

test: # run tests
	$(ENV) py.test
