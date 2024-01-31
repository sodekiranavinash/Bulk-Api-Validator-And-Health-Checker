import pandas as pd

class ResponseParser:
    @staticmethod
    def parse_data(responses) -> pd.DataFrame:
        """
        This method is responsible for parsing response data from each http request
        you can customize it as per your requirement, 
        here iam more focused on status code which gives health of url
        """
        all_data = []

        for resp in responses:
            if isinstance(resp, str):
                data_dict = {
                    'ORIGINAL_URL': '',
                    'ORIGINAL_STATUS_CODE': '',
                    'FINAL_URL': [resp],
                    'FINAL_STATUS_CODE': ["error"],  # page timeouts
                }
            elif resp.history:
                data_dict = {
                    'ORIGINAL_URL': [resp.history[0].url],
                    'ORIGINAL_STATUS_CODE': [resp.history[0].status_code],
                    'FINAL_URL': [resp.url],
                    'FINAL_STATUS_CODE': [resp.status_code],
                }
            else:
                data_dict = {
                    'ORIGINAL_URL': '',
                    'ORIGINAL_STATUS_CODE': '',
                    'FINAL_URL': [resp.url],
                    'FINAL_STATUS_CODE': [resp.status_code],
                }

            all_data.append(pd.DataFrame.from_dict(data_dict))

        return pd.concat(all_data, ignore_index=True)
