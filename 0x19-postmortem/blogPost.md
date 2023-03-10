# Postmortem
The webstack outage on October 31, 2022, was caused by a misconfigured CDN, leading to slow response times and impacting 25% of our user base. The issue was resolved by updating the CDN configuration, and steps will be taken to prevent similar issues in the future through regular checks and monitoring.



![people queing](postmortem.jpeg)

## Issue Summary
On October 31, 2022, from 2:00 PM to 4:00 PM EST, our webstack experienced an outage that impacted the user experience. During this time, users reported slow load times and timeouts, affecting approximately 25% of our user base. 

## Timeline

+ 2:00 PM EST: Monitoring alerts triggered for high server load and slow response times.
+ 2:05 PM EST: An engineer noticed the alerts and began investigating 
+ 2:15 PM EST: Investigation began on the front-end application and database servers 
+ 2:30 PM EST: Initial assumption was that the front-end application was experiencing high traffic causing the server to slow down
+ 3:00 PM EST: Investigation expanded to the load balancer and CDN 
+ 3:30 PM EST: Further investigation revealed an issue with the CDN configuration
+ 4:00 PM EST: Incident was escalated to the DevOps team for resolution 


## Root Cause And Resolution
The root cause of the issue was a misconfiguration of the CDN, which was causing it to cache and serve outdated content. This caused the front-end application to send repeated requests to the server, leading to the high server load and slow response times. The issue was fixed by updating the CDN configuration to correctly cache and serve updated content. 
Corrective and PreventativeMeasures

## Corrective And Preventative Measures
+ To prevent similar issues from occurring in the future, the following corrective and preventative measures will be taken
+ Implement regular checks on the CDN configuration to ensure it is functioning correctly 
+ Add monitoring on the CDN to alert on cache hit/miss ratio and cache size 
+ Update the incident response plan to include specific steps for investigating CDN-related issues 

