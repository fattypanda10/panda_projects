"""
Script to extract survey data (unstructured)
"""

import os
from natsort import natsorted

from extraction_functions import get_sheetnames, extract_data, export_to_csv


def main():
    companies_list = [i for i in natsorted(os.listdir(os.getcwd())) if
                      not i.endswith(('.DS_Store', '.py', '.xlsx', '.csv', 'extras'))]
    for company in companies_list[0:1]:
        print(f"Company: {company}")
        curr_company_path = os.path.join(os.getcwd(), company)
        files = [i for i in natsorted(os.listdir(curr_company_path)) if not i.endswith(('.DS_Store', '.csv'))]
        file_paths = [os.path.join(curr_company_path, i) for i in files]
        print(f"\tTotal files: {len(file_paths)}")
        for idx1, path in enumerate(file_paths):
            final_data = []
            sheet_names = get_sheetnames(path)
            for idx2, sheet in enumerate(sheet_names):
                final_data.extend(extract_data(path, sheet))
            print(f"\tFile {idx1 + 1} - {path.split('/')[-1]}")
            export_to_csv(final_data, f"data_{company}.csv")


if __name__ == '__main__':
    main()
