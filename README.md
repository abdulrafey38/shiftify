# Shiftify ![Downloads](https://static.pepy.tech/badge/shiftify) ![Repo Size](https://img.shields.io/github/repo-size/abdulrafey38/shiftify)


Shiftify is a versatile Python package that provides efficient tools for converting data between a wide variety of formats. Whether your source data is in CSV or JSON format, Shiftify offers a comprehensive set of conversion tools—including SQL, HTML, plain text, YAML, XML, TSV, TOML, NDJSON, Excel, Markdown, binary (via pickle), and INI formats. It is designed to handle large files efficiently through streaming.

## Features

### CSV Conversions
- **CSV to JSON**: Convert CSV files into JSON arrays.
- **CSV to SQL**: Generate SQL `INSERT` statements from CSV rows.
- **CSV to HTML**: Create an HTML table representation of CSV data.
- **CSV to Plain Text**: Write each CSV row as a pretty‐printed JSON string on a new line.
- **CSV to YAML**: Convert CSV files to YAML (with optional key wrapping).
- **CSV to XML**: Convert CSV rows to XML where each row is an `<Item>` element.
- **CSV to TSV**: Transform CSV files into tab-separated values.
- **CSV to TOML**: Convert CSV rows to TOML format.
- **CSV to NDJSON**: Generate newline-delimited JSON (NDJSON) from CSV rows.
- **CSV to Excel**: Convert CSV files into Excel spreadsheets.
- **CSV to Markdown Table**: Create Markdown formatted tables from CSV data.
- **CSV to Binary**: Serialize CSV rows into a binary file using pickle.
- **CSV to INI**: Convert CSV data into an INI file, storing each row as a separate section.

### JSON Conversions
- **JSON to CSV**: Convert JSON arrays into CSV format.
- **JSON to SQL**: Generate SQL `INSERT` statements from JSON objects.
- **JSON to HTML**: Create an HTML table representation of JSON data.
- **JSON to Plain Text**: Write each JSON object as a pretty‐printed string on a new line.
- **JSON to YAML**: Convert JSON arrays to YAML (with optional key wrapping).
- **JSON to XML**: Convert JSON arrays to XML where each object is an `<Item>` element.
- **JSON to TSV**: Transform JSON data into TSV format.
- **JSON to TOML**: Convert JSON arrays to TOML format.
- **JSON to NDJSON**: Generate newline-delimited JSON (NDJSON) from JSON objects.
- **JSON to Excel**: Convert JSON arrays into Excel spreadsheets.
- **JSON to Markdown Table**: Create Markdown tables from JSON data.
- **JSON to Binary**: Serialize JSON objects into a binary file using pickle.
- **JSON to INI**: Convert JSON arrays into an INI file, storing each object as a separate section.

## Installation

To install Shiftify, run the following command in your terminal:

```bash
pip install Shiftify
```

## Usage

Shiftify provides two main classes—CSV and JSON—that handle conversions from CSV and JSON files respectively. (Will roll out new formats soon)

Using the CSV Class

```python
from shiftify import CSV

# Initialize the CSV converter with your CSV file
csv_converter = CSV('path/to/your/input.csv')

# Convert CSV to JSON
csv_converter.to_json('path/to/your/output.json')

# Convert CSV to SQL (and save the SQL statements to a file)
csv_converter.to_sql('path/to/your/output.sql', table_name="my_table")

# Convert CSV to HTML table
csv_converter.to_html('path/to/your/output.html')

# Convert CSV to YAML (with optional key wrapping)
csv_converter.to_yaml('path/to/your/output.yaml', key="record")

# Convert CSV to XML with a custom root element
csv_converter.to_xml('path/to/your/output.xml', root_element="Data")

# Other conversions include:
# to_text, to_tsv, to_toml, to_ndjson, to_excel, to_markdown_table, to_binary, and to_ini.
```

Using the JSON Class

```python
from shiftify import JSON

# Initialize the JSON converter with your JSON file
json_converter = JSON('path/to/your/input.json')

# Convert JSON to CSV
json_converter.to_csv('path/to/your/output.csv')

# Convert JSON to SQL statements
json_converter.to_sql('path/to/your/output.sql', table_name="my_table")

# Convert JSON to HTML table
json_converter.to_html('path/to/your/output.html')

# Convert JSON to YAML (with optional key wrapping)
json_converter.to_yaml('path/to/your/output.yaml', key="record")

# Convert JSON to XML with a custom root element
json_converter.to_xml('path/to/your/output.xml', root_element="Data")

# Other conversions include:
# to_text, to_tsv, to_toml, to_ndjson, to_excel, to_markdown_table, to_binary, and to_ini.
```


## Customizing Options

For CSV-to-JSON (or vice versa) conversions, you can customize options such as delimiters and quote characters. For example:

```python
from shiftify import JSON

json_converter = JSON('path/to/your/input.json')
# Use a semicolon as delimiter and a single quote as quotechar when converting to CSV
json_converter.to_csv('path/to/your/output.csv', delimiter=';', quotechar="'")
```

# Contributing
Contributions to Shiftify are welcome! Please feel free to fork the repository, make your improvements, and submit a pull request. Whether you're fixing bugs, adding new conversion formats, or improving the documentation, your help is appreciated.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
