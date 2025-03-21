#!/usr/bin/env python3

import json
import sys
import os

def generate_html_report(json_file, html_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Basic HTML structure and styling
    html_content = """
<html>
<head>
    <meta charset="utf-8"/>
    <title>Behave Test Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { background: #EEE; padding: 10px; }
        h2 { color: #333; margin-top: 30px; }
        h3 { margin-top: 20px; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #CCC; padding: 8px; text-align: left; }
        th { background: #F5F5F5; }
        .passed { color: green; }
        .failed { color: red; }
        .skipped { color: orange; }
    </style>
</head>
<body>
<h1>Behave Test Report</h1>
"""

    # Loop through each feature in the JSON
    for feature in data:
        feature_name = feature.get('name', 'N/A')
        html_content += f"<h2>Feature: {feature_name}</h2>"

        # Each "element" is effectively a scenario
        for scenario in feature.get('elements', []):
            scenario_name = scenario.get('name', 'N/A')
            html_content += f"<h3>Scenario: {scenario_name}</h3>"

            # Build a table of steps
            html_content += "<table>"
            html_content += "<tr><th>Step</th><th>Status</th><th>Duration (s)</th></tr>"
            for step in scenario.get('steps', []):
                step_name = step.get('name', 'N/A')
                result = step.get('result', {})
                status = result.get('status', 'N/A')
                duration = result.get('duration', 0)

                # Simple class-based styling for pass/fail/skip
                css_class = status
                html_content += (
                    f"<tr>"
                    f"<td>{step_name}</td>"
                    f"<td class='{css_class}'>{status}</td>"
                    f"<td>{duration:.2f}</td>"
                    f"</tr>"
                )
            html_content += "</table>"

    html_content += "</body></html>"

    # Write final HTML to file
    os.makedirs(os.path.dirname(html_file), exist_ok=True)
    with open(html_file, 'w', encoding='utf-8') as out:
        out.write(html_content)

def main():
    if len(sys.argv) < 3:
        print("Usage: python json2html_report.py <input.json> <output.html>")
        sys.exit(1)

    input_json = sys.argv[1]
    output_html = sys.argv[2]

    generate_html_report(input_json, output_html)
    print(f"HTML report generated at: {output_html}")

if __name__ == "__main__":
    main()
