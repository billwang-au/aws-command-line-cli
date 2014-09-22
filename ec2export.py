#!/usr/bin/env python

import boto.ec2

connect = boto.ec2.connect_to_region("eu-west-1")
reservations = connect.get_all_instances()

for reserv in reservations:
  for instance in reserv.instances:
    print reserv.id, instance.id,instance.tags['Name'],instance.private_ip_address,instance.state,instance.placement,instance.architecture, instance.vpc_id, instance.kernel, instance.instance_type, instance.image_id, instance.launch_time
