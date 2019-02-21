Terraform with AWS(EC2 and RDS) deploying Mediawiki

- EXECUTION
```console
$ terraform init
$ terraform apply
```

- EXPLANATION

    1. ec2-instance created 
    2. rds-mysql-instance created
    3. mediawiki requires some specific configurations, that's why have file transfering
    4. mediawiki requires a move to LocalSettings.php to its folder in server, which requires a post script to transfer

- PROBLEMS

    1. mediawiki requires special configurations on LocalSettings.php, related to endpoint in:
        - $wgDBserver         = "mediawiki.ctvhdy9vaiz1.us-east-1.rds.amazonaws.com";
            - The ctvhdy9vaiz1 can't be predicted, which implicates in a post script to alter it getting the output variable from terraform
