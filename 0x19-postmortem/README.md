Postmortem
Issue Summary:
On May 1st, 2023, from 12:30 PM to 14:30 PM GMT, users were unable to access the 'Buy airtime' section on our e-banking platform. This issue impacted 100% of users who tried to access the aforementioned service on our platform at those specific time periods and resulted in a loss of potential revenue for the company.

Timeline:
- 12:30 PM GMT: The issue was detected when customers started reporting errors while attempting to buy airtime for both themselves and others.
- 12:35 PM GMT: Our engineering team received alerts and promptly began investigating the issue.
- 12:45 PM GMT: The team initially suspected that the issue was related to a recent deployment that had been made to our e-banking platform.
- 13:00 PM GMT: The team rolled back the recent deployment, but the issue persisted.
- 13:15 PM GMT: The team suspected that the issue might be related to the load balancer and started investigating that component, but still no improvement.
- 13:30 PM GMT: After further investigation, the team determined that the issue was caused by an issue in a previous deployment which clashed with the most recent deployment.
- 14:00 PM GMT: The team implemented a fix for the files causing the clash.
- 14:30 PM GMT: The issue was resolved, and users were able to access the 'Buy airtime' feature once again.

Root Cause and Resolution:
The root cause of the issue was an issue with an earlier deployment clashing with recently deployed files. Specifically, bugs from the initial deployment were not totally resolved and these sprung up as soon as another deployment was made. This caused the requests to the website to fail, resulting in the inability to make airtime purchases on the platform.

To fix the issue, the engineering team first corrected the bugs from earlier deployment. Once this was done, the issues practically resolved themselves

Corrective and Preventative Measures:
To prevent similar issues in the future, the engineering team will take the following corrective and preventative measures:
- Make sure to handle ALL bugs before deploying any new features
- Increase monitoring and alerts for the 'Buy airtime' feature and related components to detect issues more quickly.
- Review the incident with the engineering team to identify areas for improvement in the incident response process.

Specific tasks to address the issue include:
- Review and update the website's configuration testing process to ensure that misconfigurations are caught before deployment to production.
- Conduct a post-incident review with the engineering team to identify areas for improvement in the incident response process.
- Document the incident and the corrective and preventative measures taken to prevent similar incidents in the future.
