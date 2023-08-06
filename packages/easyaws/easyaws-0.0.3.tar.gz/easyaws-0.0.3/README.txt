ABOUT EASYAWS:
Scripts in easyaws package allow easy access to EC2 and S3 (intended to be used by developers). The goal is to create easy-to-use interfaces, analogous to 'cp', 'ssh', 'scp' (which developers are assumed to be already comfortable with), for EC2 and S3.

SETUP EASYAWS:
To setup, run 'aws configure' to enter your AWS credentials and configuration. Enter your AWS Access Key ID, AWS Secret Access Key, Default region name and Default output format (as "text").

USING EASYAWS:
Once you have configured your AWS credentials, you can use following scripts that are installed with 'easyaws' package:
  1. 'ec2list': List your EC2 instances
  2. 'ec2ssh':  SSH into EC2 instances using instance name/tag

COMING SOON:
We are working on following scripts:
  1. 'ec2scp': Script to easily 'scp' files to/from EC2 instances.
  2. 's3cp':   Script to cp files to/from S3 buckets (i.e. 'cp' for S3)
