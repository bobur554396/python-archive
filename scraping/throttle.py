import urlparse

from datetime import *


class Throttle:
    """
    Add a delay between downloads to the same domain
    """
    def __init__(self, delay):
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                # domain has been accessed recently
                # need to sleep
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()
