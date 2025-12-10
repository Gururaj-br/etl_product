import pandas as pd
import os
from config import *

class ReportWriter:
    def __init__(self, data, engine_type):
        self.data = data
        self.report_folder = Report_Config.REPORT_FOLDER_PATH

        if not os.path.exists(self.report_folder):
            os.makedirs(self.report_folder)

        timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
        self.output_file = os.path.join(
            self.report_folder, 
            Report_Config.REPORT_FILE_NAME.format(engine_type, timestamp)
        )

    def write_report(self):
        df = pd.DataFrame(self.data)
        df.rename(columns=Report_Config.HEADERS, inplace=True)
        df.to_csv(self.output_file, sep=';', index=False)
        print(f"Report written to {self.output_file}")