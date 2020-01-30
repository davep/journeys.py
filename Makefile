###############################################################################
# Common make values.
run  = pipenv run
lint = $(run) pylint
mypy = $(run) mypy

##############################################################################
# Perform a test run.
.PHONY: all
all:				# Validate the example file.
	$(run) ./validate

##############################################################################
# Setup/update packages the system requires.
.PHONY: setup
setup:				# Install development/tool dependencies.
	pipenv sync --dev

.PHONY: depsoutdated
depsoutdated:			# Show a list of outdated dependencies.
	pipenv update --outdated

.PHONY: depsupdate
depsupdate:			# Update all dependencies.
	pipenv update --dev

.PHONY: repl
repl:				# Run a Python repl in the correct environment.
	$(run) python

##############################################################################
# Checking/testing/linting/etc.
.PHONY: lint
lint:				# Run pylint over the code.
	$(lint) journeys

.PHONY: dscheck
dscheck:			# Check the doc strings.
	$(run) pydscheck --extra-checks

.PHONY: typecheck
typecheck:			# Perform static type checks with mypy
	$(mypy) validate journeys

.PHONY: stricttypecheck
stricttypecheck:	        # Perform a strict static type checks with mypy
	$(mypy) --strict validate journeys

##############################################################################
# Utility.
.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

### Makefile ends here
