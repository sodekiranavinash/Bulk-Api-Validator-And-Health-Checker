import time
import pandas as pd
from request_manager import RequestManager
from response_parser import ResponseParser
from typing import List
from dotenv import load_dotenv
import os

# you can integrate this app into your python backend application easily.
if __name__ == "__main__":
    load_dotenv()
    start_time = time.time()

    df : pd.DataFrame = pd.read_csv(os.getenv("INPUT_FILE_PATH"))
    url_list : List = df.Url.tolist() # extracting api request urls.

    print(f"Total Request : {len(url_list)} || Estimated Time : {len(url_list) * 0.3 } seconds ")

    responses : List = RequestManager.send_requests(url_list) #sending bulk requests here
    the_data : pd.DataFrame = ResponseParser.parse_data(responses) # parsing data received
    the_data.to_csv(os.getenv("OUTPUT_FILE_PATH"), index=False)

    print(f"Task Completed & total time taken :  --- {time.time() - start_time} seconds ---")
