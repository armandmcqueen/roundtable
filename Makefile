.PHONY: install test typecheck lint fmt clean build publish all check

# Default target
all: install typecheck fmt lint test

# Run all checks
check: test typecheck lint


# Install dependencies
install:
	uv sync

# Run tests
test:
	uv run pytest

# Run type checking
typecheck:
	uv run mypy .

# Run linter
lint:
	uv run ruff check .

# Format code
fmt:
	uv run ruff check . --fix

# Clean up build artifacts
clean:
	rm -rf build dist .pytest_cache .mypy_cache .ruff_cache roundtable.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete

# Build the project
build:
	uv run flit build

publish:
	uv run flit publish


