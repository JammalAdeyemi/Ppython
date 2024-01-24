# Given the array requests, for each request return the string "{status: 200, message: OK}" if the request can be processed. 
# otherwise return "{status: 429, message: Too many requests}".
# Example: Suppose  n=9 and requests== ["www.xyz.com", "www.abc.com", "www.xyz.com", "www.pqr.com", "www.abc.com", 
# "www.xyz.com",  "www.xyz.com", "www.abc.com", "www.xyz.com"]

# Hence the answer is ["{status: 200, message: OK}", "{status: 200, message: OK}", "{status: 200, message: OK}", 
# "{status: 200, message: OK}", "{status: 200, message: OK}", "{status: 200, message: OK}", "{status: 429, message: Too many requests}",
#  "{status: 200, message: OK}", "{status: 200, message: OK}"]

def getRequestStatus(requests):
    request_count = {}
    result = []
    for request in requests:
        if request in request_count:
            request_count[request] += 1
        else:
            request_count[request] = 1
        if request_count[request] > 5:
            result.append("{status: 429, message: Too many requests}")
        else:
            result.append("{status: 200, message: OK}")
    return result
