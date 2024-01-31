import grequests
from typing import List, Final

class RequestManager:
    
    API_LIMIT_PER_SECOND : Final[int] = 50 # equal to (requests per second)
    GVENT_SERVER_REQUEST_TIMEOUT : Final[int] = 10 # timeout for each api request

    @staticmethod
    def send_requests(urls) -> List:
        '''
        This method makes all http requests ready and sends them with specified API LIMIT and GVENT timeout
        you customize method to include custom request headers and other parts of requests.
        '''
        rs = (grequests.get(url, allow_redirects=True, headers={'User-Agent': 'Google Chrome'}) for url in urls)
        return grequests.map(rs, size=RequestManager.API_LIMIT_PER_SECOND,
                              exception_handler=RequestManager.handle_exception,
                              gtimeout=RequestManager.GVENT_SERVER_REQUEST_TIMEOUT)

    @staticmethod
    def handle_exception(request, exception) -> str:
        """
        this method ovverides predefined handle_exception in package
        when exception occurs in loading page , we can capture here and do custom revelent action
        """
        return request.url
