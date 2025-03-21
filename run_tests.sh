#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

# Ensure the reports directory exists
mkdir -p reports

echo "Running Behave tests with coverage..."
coverage run -m behave --format json --outfile=reports/report.json

echo "Generating coverage report in console..."
coverage report

echo "Generating HTML coverage report..."
coverage html

echo "HTML report generated at: htmlcov/index.html"
