import pandas as pd
import os
from config import *

report_folder = Report_Config.REPORT_FOLDER_PATH

if not os.path.exists(report_folder):
    os.makedirs(report_folder)

output_file = os.path.join(
    report_folder, 
    Report_Config.REPORT_FILE_NAME.format(pd.Timestamp.now().strftime("%Y%m%d_%H:%M%S"))
)

class ReportWriter:
    def __init__(self, data):
        self.data = data

    def write_report(self):
        df = pd.DataFrame(self.data)
        df.rename(columns=Report_Config.HEADERS, inplace=True)
        df.to_csv(output_file, index=False)
        print(f"Report written to {output_file}")