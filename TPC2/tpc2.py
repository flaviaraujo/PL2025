#!/usr/bin/env python3

import sys
import os
import re
import json
from collections import defaultdict

FIELD_DELIMITER = ';'
RESULT_FILE = 'out/music_results.json'

def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def find_data_rows(file_content):
    row_pattern = r'^(.*)(?:\n {8}(.*?))*$'
    return re.findall(row_pattern, file_content, re.MULTILINE)[1:]

def parse_record(full_line):
    tokens = re.split(rf'({FIELD_DELIMITER}\")|(\"{FIELD_DELIMITER})|({FIELD_DELIMITER})', full_line)
    tokens = [token for token in tokens if token and token != '']

    parsed_fields, current_field, within_quotes = [], '', True

    for token in tokens:
        if token == f'{FIELD_DELIMITER}\"':
            parsed_fields.append(current_field)
            current_field, within_quotes = '', False
        elif token == f'\"{FIELD_DELIMITER}':
            parsed_fields.append(current_field)
            current_field, within_quotes = '', True
        elif token == FIELD_DELIMITER:
            if within_quotes:
                parsed_fields.append(current_field)
                current_field = ''
            else:
                current_field += token
        else:
            current_field += token

    if current_field:
        parsed_fields.append(current_field)
    return parsed_fields

def analyze_records(records):
    summary = {
        'artists': set(),
        'period_distribution': defaultdict(int),
        'works_by_period': defaultdict(list)
    }

    for index, record in enumerate(records, start=1):
        combined_line = ''.join(record)
        fields = parse_record(combined_line)

        if len(fields) < 7:
            print(f"Record {index} has fewer than 7 fields, skipping.")
            continue

        title, era, artist = fields[0], fields[3], fields[4]
        summary['artists'].add(artist)
        summary['period_distribution'][era] += 1
        summary['works_by_period'][era].append(title)

    summary['artists'] = sorted(summary['artists'])
    for era in summary['works_by_period']:
        summary['works_by_period'][era].sort()

    return summary

def write_output_file(summary):
    os.makedirs(os.path.dirname(RESULT_FILE), exist_ok=True)
    with open(RESULT_FILE, 'w', encoding='utf-8') as output_file:
        json.dump(summary, output_file, indent=2, ensure_ascii=False)

def display_summary(summary, total_records):
    print("Artists:")
    print(json.dumps(summary['artists'], indent=2, ensure_ascii=False))

    print("\nPeriod Distribution:")
    print(json.dumps(summary['period_distribution'], indent=2, ensure_ascii=False))

    print("\nWorks by Period:")
    print(json.dumps(summary['works_by_period'], indent=2, ensure_ascii=False))

    print(f"Processed {total_records} records")

def run():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    file_content = read_input_file(input_path)
    data_rows = find_data_rows(file_content)
    record_summary = analyze_records(data_rows)
    write_output_file(record_summary)
    display_summary(record_summary, len(data_rows))

if __name__ == '__main__':
    run()
