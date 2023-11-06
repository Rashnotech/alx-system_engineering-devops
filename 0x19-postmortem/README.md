## WEBSTACK DEBUG Post Mortem Report
### Incident Summary
**Date and Time:** November 5, 2023, 21:30 - 23:45(UTC)
**Incident Duration:** 2 hours 15 minutes
**Team/Individual Responsible:** Webdev Team
**Description:** On November 5, 2023, a critical bug was discovered on our web service that caused an unexpected service outage for approximately 2,000 users. The incident was reported by our monitoring system, which detected a spike in error rates and performance  degradation.
 
### Incident Timeline
1. Detection and Discovery (Nov 5, 2023, 21:30): The incident was detected by our monitoring system, which triggered alerts for high error rates and slow response times.
2. Initial Response (Nov 5, 2023, 21:30): The on-call engineer, Rashnotech acknowledged the alert and started investigating the issue.
3. Isolation (Nov 5, 2023, 21:50): Rashnotech identified the faulty component responsible for the issue (nginx server) and isolated it to prevent further damage.
4. Resolution (Nov, 5, 2023, 22:15): After further investigation, Rashnotech fixed the bug in the service, and the web application’s performance returned to normal.
5. Communication (Nov, 5 2023 22:30): An incident report was sent to all stakeholders, explaining the issue, the actions taken, and an apology to affected users.
6. Root Cause Analysis (Nov, 5, 23:00): The engineering team conducted a thorough analysis to identify the root cause of the bug.
7. Preventive Measure (Nov 5,2023, 23:45): Based on the analysis, the team outlined a plan for preventing similar incidents.
 
### Corrective and Preventive Actions 
#### Short-Term Fixes:
i. Reverted the error and configuration change.
ii. Monitored the system to ensure stable performance.
#### Long-Term Preventive Measures:
1. Implemented stricter configuration review processes.
2. Improved monitoring and alerting for Nginx server service performance.
3. Scheduled regular performance audits for critical system components.

