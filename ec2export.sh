#!/bin/env bash
# have AWS-CLI instlled (http://aws.amazon.com/cli/)
# have jq json parser installed. (http://stedolan.github.io/jq/)

aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId'
