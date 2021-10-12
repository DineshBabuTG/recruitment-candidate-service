Run the following docker command to run the candidate service container

docker run -d -p 8000:8000 -e dbhostname=<DB-Hostname> -e awsacceskey=<AWS-Access-Key> -e awssecretkey=<AWS-Secret-Key>  tgdinababu/candidateapp:latest