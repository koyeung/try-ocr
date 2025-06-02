default:
    just --list

# Update dependencies versions in lock files (no sync to venv)
update:
    uv lock --upgrade

# Perform audit check
audit:
    #!/usr/bin/env bash
    osv-scanner scan --lockfile requirements.txt:<(uv export --quiet --frozen)

# Upgrade venv
upgrade:
    uv sync --all-packages

# Format check
format:
    ruff format --check --diff
# Fix format issues
format-fix *FILE:
    ruff format {{ FILE }}

# Static analysis
lint *FILE:
    ruff check {{ FILE }}
# Show fix to static analysis issue
lint-diff *FILE:
    ruff check --diff {{ FILE }}
# Apply fix to static analysis issue
lint-fix *FILE:
    ruff check --fix {{ FILE }}

check: lint format
