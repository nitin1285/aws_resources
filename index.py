import boto3
import json

from config import (
    ECS_CLUSTER_NAME, DOCKER_IMAGE_URI, ECS_CONTAINER_NAME, 
    ECS_TASK_DEFINITION_NAME, ECS_TASK_ROLE_ARN, ECS_SERVICE_NAME
)

# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


ecsclient = boto3.client('ecs')

def get_all_clusters():
    try:
        response = ecsclient.list_clusters(
            maxResults=10
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("This is returned")
            return json.dumps(response['clusterArns'])
        else:
            return False
    except Exception as e:
        print(str(e))
        return False    

#def get_cluster_name(arn):
#    cluster_name = ecsclient.describe_clusters(**clusterarn)

#clusterarn = get_cluster_details()

#get_cluster_name(clusterarn)
print(get_all_clusters())

#clist = get_all_clusters()

#def get_cluster_name()
    

#a = ecsclient.describe_clusters(list = clist)

#print(a)

"""
response = ecsclient.list_clusters(
    maxResults=10
)
print(response)
"""

def create_task_definition():
    try:
        response = ecsclient.register_task_definition(
            family=ECS_TASK_DEFINITION_NAME,
            taskRoleArn=ECS_TASK_ROLE_ARN,
            executionRoleArn=ECS_TASK_ROLE_ARN,
            networkMode='awsvpc',
            containerDefinitions=[
                {
                    'name': ECS_CONTAINER_NAME,
                    'image': f'{DOCKER_IMAGE_URI}:latest',
                    'portMappings': [
                        {
                            'containerPort': 8080,
                            'protocol': 'tcp',
                            'name': 'httpport',
                            'appProtocol': 'http'
                        },
                    ],
                    'essential': True,
                    'logConfiguration': {
                        'logDriver': 'awslogs',
                        'options': {                            
                            'awslogs-group': f'/ecs/{ECS_TASK_DEFINITION_NAME}',
                            'awslogs-region': 'us-east-1',
                            'awslogs-stream-prefix': 'ecs'
                        }
                    }
                }
            ],
            requiresCompatibilities=[
                'FARGATE',
            ],
            cpu='1vcpu',
            memory='2GB',
            runtimePlatform={
                'cpuArchitecture': 'X86_64',
                'operatingSystemFamily': 'LINUX'
            }
        )
        return response['taskDefinition']
    except Exception as e:
        print(str(e))
        return False
    
create_task_definition()
print('Created task definition')

def create_service():
    try:
        response = ecsclient.create_service(
            cluster=ECS_CLUSTER_NAME,
            serviceName=ECS_SERVICE_NAME,
            taskDefinition=ECS_TASK_DEFINITION_NAME,
"""
            loadBalancers=[
                {
                    'targetGroupArn': 'string',
                    'loadBalancerName': 'string',
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
"""            
            serviceRegistries=[
                {
                    'registryArn': 'string',
                    'port': 123,
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
            desiredCount=1,
            clientToken='string',
            launchType='EC2'|'FARGATE'|'EXTERNAL',
            capacityProviderStrategy=[
                {
                    'capacityProvider': 'string',
                    'weight': 123,
                    'base': 123
                },
            ],
            platformVersion='string',
            role='string',
"""            
            deploymentConfiguration={
                'deploymentCircuitBreaker': {
                    'enable': True|False,
                    'rollback': True|False
                },
                'maximumPercent': 123,
                'minimumHealthyPercent': 123,
                'alarms': {
                    'alarmNames': [
                        'string',
                    ],
                    'enable': True|False,
                    'rollback': True|False
                }
            },
            
            placementConstraints=[
                {
                    'type': 'distinctInstance'|'memberOf',
                    'expression': 'string'
                },
            ],
            placementStrategy=[
                {
                    'type': 'random'|'spread'|'binpack',
                    'field': 'string'
                },
            ],
"""            
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': 'ENABLED'|'DISABLED'
                }
            },
            healthCheckGracePeriodSeconds=123,
            schedulingStrategy='REPLICA'|'DAEMON',
            deploymentController={
                'type': 'ECS'|'CODE_DEPLOY'|'EXTERNAL'
            },
            tags=[
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            enableECSManagedTags=True|False,
            propagateTags='TASK_DEFINITION'|'SERVICE'|'NONE',
            enableExecuteCommand=True|False,
"""
            serviceConnectConfiguration={
                'enabled': True|False,
                'namespace': 'string',
                'services': [
                    {
                        'portName': 'string',
                        'discoveryName': 'string',
                        'clientAliases': [
                            {
                                'port': 123,
                                'dnsName': 'string'
                            },
                        ],
                        'ingressPortOverride': 123,
                        'timeout': {
                            'idleTimeoutSeconds': 123,
                            'perRequestTimeoutSeconds': 123
                        },
                        'tls': {
                            'issuerCertificateAuthority': {
                                'awsPcaAuthorityArn': 'string'
                            },
                            'kmsKey': 'string',
                            'roleArn': 'string'
                        }
                    },
                ],
               
                'logConfiguration': {
                    'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk'|'awsfirelens',
                    'options': {
                        'string': 'string'
                    },
                    'secretOptions': [
                        {
                            'name': 'string',
                            'valueFrom': 'string'
                        },
                    ]
                }
            },
"""             
        )
        return response['service']
    except Exception as e:
        print(str(e))
        return False
