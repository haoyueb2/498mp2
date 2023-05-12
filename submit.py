import requests
import json

''' Fill in the following information '''
# General information
YOUR_EMAIL = "haoyueb2@illinois.edu"  # <put your coursera account email>,
YOUR_SECRET = "KsDskZQ5RY9FxMzD"  # <put your secret token from coursera>

# Section 1
# <put your first EC2 instance's IP address:port>
IP_ADDRESS1 = "18.212.90.93:5000"
IP_ADDRESS2 = "44.211.172.48:5000"  # <put your second instance's IP address:port>
# <put your load_balancer address for section 1>
YOUR_LOAD_BALANCER1 = "498mp2-876040303.us-east-1.elb.amazonaws.com"
# Section 2
# <put your load_balancer address for section 2>,
YOUR_LOAD_BALANCER2 = "internal-mp2-scale-1179342540.us-east-1.elb.amazonaws.com"

''' Don't change the following '''
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
input = {
    'ip_address1': IP_ADDRESS1,
 			'ip_address2': IP_ADDRESS2,
 			'load_balancer1': YOUR_LOAD_BALANCER1,
 			'load_balancer2': YOUR_LOAD_BALANCER2,
 			'submitterEmail': YOUR_EMAIL,
 			'secret': YOUR_SECRET,
}
payload = {"input": json.dumps(input),
           "stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
           }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
