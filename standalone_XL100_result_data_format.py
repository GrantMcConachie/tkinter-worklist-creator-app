from pathlib import Path
from datetime import datetime
import csv

result_data_dir = "path\\to\\data\\"
one_day = 95378.95542693138  # seconds
one_day_ago = datetime.now().timestamp() - one_day  # seconds

# Looks for files made by standalone biomicro in result data dir
for path in Path(result_data_dir).rglob('gross_tare_*'):
    fraction_dict = {}
    file_creation_time = path.stat().st_mtime

    # Determines if the file was made within the last day
    if file_creation_time > one_day_ago:
        with open(path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            # Goes through the rows of the CSV and splits them up
            for i, row in enumerate(spamreader):
                # Skipping the first row
                if i == 0:
                    continue

                else:
                    fraction_rack = row[0][-3:]
                    # Putting the values into a dictionary based on which rack they're in
                    try:
                        fraction_dict[fraction_rack].append(row[0:4])
                    except:
                        fraction_dict[fraction_rack] = [row[0:4]]

    # Using fraction_dict to make new csv files
    for rack, contents in (fraction_dict.items()):
        run_number = contents[0][0][0:8]
        with open(result_data_dir + run_number + rack + '_tareFINAL.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['SrcRack', 'SrcPos', 'Src2D', 'TareWt'])
            spamwriter.writerows(contents)
