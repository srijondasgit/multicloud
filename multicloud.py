import sys
import random
import argparse
import boto3
import json
from teststub import stubs
from abc import ABC, abstractmethod

class Multicloud(ABC):
    def __init__(self):
        self.mem = "2G"
        self.cpu = 1
        self.cloud = 'Aws'

    @abstractmethod
    def describe(self):
        print("This function prints all the running instances")

    @abstractmethod
    def provision(self, cloud, instances, mem):
        print("This function provisions the instances")

    @abstractmethod
    def start(self, instanceId):
        print("this function starts the instances provided")


class aws_cloud(Multicloud):
    def __init__(self):
        self.imageId = "ami-1234567"
        self.instanceType = "t2.small"
        self.securityGroup = ['sg-1f39854x', 'sg-1f39999x']

    def describe(self):
        # ec2 = boto3.client('ec2')
        # response = ec2.describe_instances()
        # print(response)
        print("All instances currently running ...")
        stub = stubs()
        js = stub.aws_teststub()
        for instance in js['Instances']:
            print(instance['InstanceId'])

    def provision(self, cloud, instances, mem):
        print("Provisioned instances in : " + cloud + " , number of instances : " + instances, " , with memory : "+mem)
        # client = boto3.client('ec2', region_name='us-west-2')
        # response = client.run_instances(
        #     BlockDeviceMappings=[
        #         {
        #             'DeviceName': '/dev/xvda',
        #             'Ebs': {
        #
        #                 'DeleteOnTermination': True,
        #                 'VolumeSize': 8,
        #                 'VolumeType': 'gp2'
        #             },
        #         },
        #     ],
        #     ImageId=self.imageId,
        #     InstanceType=self.instanceType,
        #     MaxCount=instances,
        #     MinCount=instances,
        #     Monitoring={
        #         'Enabled': False
        #     },
        #     SecurityGroupIds=self.securityGroup,
        # )
        print("Id and Status of provisioned instances...")
        stub = stubs()
        js = stub.aws_teststub()
        for instance in js['Instances']:
            print("Instance id : " + instance['InstanceId'] + " , status : " + instance['Status'])


    def start(self, instanceId):
        print("Starting instances ...")
        instanceId = instanceId[1:-1]
        list = instanceId.split(',')
        for l in list:
            print(l)



# Python boilerplate.
if __name__ == "__main__":
    # provision, start, stop, print number of vms
    parser = argparse.ArgumentParser(description='Program to start and manage cloud instances.')
    parser.add_argument('command', choices=['provision', 'start', 'stop', 'display', 'installmariadb'], type=str,
                        help='number of instances to be started')
    parser.add_argument('--cloud', default='Aws', choices=['Aws', 'Gcp', 'Azure'],
                        help='choose the cloud provider Aws/Google/Azure (default: Aws cloud)')
    parser.add_argument('--mem', default='2G', choices=['2G', '3G', '4G', '5G', '6G', '7G'],
                        help='memory of the cloud instance')
    parser.add_argument('--cpu', default=1,
                        choices=[1,2,3,4,8,16],
                        help='number of CPU in cloud instance')
    parser.add_argument('--vmtype', default='t2.small', choices=['t2.small', 't2.medium', 't2.large', 't2.xlarge', 't2.2xlarge'], help='type of VM of the cloud instance')
    parser.add_argument('--instances', default=1, help='total number of instances to be started')
    parser.add_argument('--instanceId', default=[], help='list of instance ids')

    args = parser.parse_args()

    #create an instance of Aws cloud
    a=aws_cloud()

    if args.command == 'display' and args.cloud=='Aws':
        a.describe()

    if args.command == 'provision' and args.cloud=='Aws':
        a.provision(args.cloud, args.instances, args.mem)

    if args.command == 'start' and args.cloud=='Aws':
        a.start(args.instanceId)


