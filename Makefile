###############################################################################
# Common make values.
run  = pipenv run
lint = $(run) pylint

.PHONY: all
all:				# Validate the example file.
	$(run) ./validate

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

.PHONY: lint
lint:				# Run pylint over the code.
	$(lint) journeys

.PHONY: dscheck
dscheck:			# Check the doc strings.
	$(run) pydscheck --extra-checks

.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

### Makefile ends here
