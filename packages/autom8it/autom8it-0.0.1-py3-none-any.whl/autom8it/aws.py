import boto3
import logging
from time import sleep
from quickbe import Log
from autom8it import AutomationTask

for log_name in ['boto', 'boto3', 'botocore', 's3transfer', 'urllib3']:
    logging.getLogger(log_name).setLevel(logging.WARNING)


class DeregisterTarget(AutomationTask):

    TARGET_GROUP_ARN_KEY = 'target_group_arn'
    TARGET_ID_KEY = 'target_id'
    PORT_KEY = 'port'

    aws_client = boto3.client('elbv2')

    def __init__(self, task_data: dict):
        super().__init__(task_data=task_data, check_done_interval=10)

    @property
    def validation_schema(self) -> dict:
        return {
            self.TARGET_GROUP_ARN_KEY: {
                'required': True,
                'type': 'string'
            },
            self.TARGET_ID_KEY: {
                'required': True,
                'type': 'string'
            },
            self.PORT_KEY: {
                'required': True,
                'type': 'integer'
            }
        }

    @property
    def task_type(self) -> str:
        return 'Deregister target'

    def do(self):
        target_group_desc = self.aws_client.deregister_targets(
            TargetGroupArn=self.get_task_attribute(self.TARGET_GROUP_ARN_KEY),
            Targets=[{
                'Id': self.get_task_attribute(self.TARGET_ID_KEY),
                'Port': self.get_task_attribute(self.PORT_KEY)
            }],
        )
        return target_group_desc

    def is_done(self) -> bool:
        target_id = self.get_task_attribute(self.TARGET_ID_KEY)
        target_group_desc = self.aws_client.describe_target_health(
            TargetGroupArn=self.get_task_attribute(self.TARGET_GROUP_ARN_KEY)
        )
        for target in target_group_desc['TargetHealthDescriptions']:
            if target['Target']['Id'] == target_id:
                Log.debug(f"Target {target_id} state: {target['TargetHealth']['State']}")
                return False

        return True


class RegisterTarget(DeregisterTarget):

    def __init__(self, task_data: dict):
        super().__init__(task_data=task_data)

    @property
    def task_type(self) -> str:
        return 'Register target'

    def do(self):
        target_group_desc = self.aws_client.register_targets(
            TargetGroupArn=self.get_task_attribute(self.TARGET_GROUP_ARN_KEY),
            Targets=[{
                'Id': self.get_task_attribute(self.TARGET_ID_KEY),
                'Port': self.get_task_attribute(self.PORT_KEY, 80)
            }],
        )
        return target_group_desc

    def is_done(self) -> bool:
        target_id = self.get_task_attribute(self.TARGET_ID_KEY)
        target_group_desc = self.aws_client.describe_target_health(
            TargetGroupArn=self.get_task_attribute(self.TARGET_GROUP_ARN_KEY)
        )
        for target in target_group_desc['TargetHealthDescriptions']:
            if target['Target']['Id'] == target_id:
                target_state = target['TargetHealth']['State']
                Log.debug(f"Target {target_id} state: {target_state}")
                if target_state in ['healthy']:
                    return True

        return False


class StopEC2Instance(AutomationTask):

    INSTANCE_ID_KEY = 'instance_id'

    @property
    def validation_schema(self) -> dict:
        return {
            self.INSTANCE_ID_KEY: {
                'required': True,
                'type': 'string'
            },
        }

    aws_client = boto3.client('ec2')

    def __init__(self, task_data: dict):
        super().__init__(task_data=task_data)

    @property
    def task_type(self) -> str:
        return 'Stop EC2 instance'

    def do(self):
        return self.aws_client.stop_instances(
            InstanceIds=[self.get_task_attribute(self.INSTANCE_ID_KEY)],
        )

    def is_done(self) -> bool:
        return self.is_state_equals(requested_state='stopped')

    def is_state_equals(self, requested_state: str) -> bool:
        instance_id = self.get_task_attribute(self.INSTANCE_ID_KEY)
        desc = self.aws_client.describe_instance_status(
            InstanceIds=[instance_id],
        )
        for data in desc['InstanceStatuses']:
            if data['InstanceId'] == instance_id:
                state = data['InstanceState']['Name']
                Log.debug(f"Instance {instance_id} state: {state}")
                if state in [requested_state]:
                    return True

        return False


class StartEC2Instance(StopEC2Instance):

    def __init__(self, task_data: dict):
        super().__init__(task_data=task_data)

    @property
    def task_type(self) -> str:
        return 'Start EC2 instance'

    def do(self):
        return self.aws_client.start_instances(
            InstanceIds=[self.get_task_attribute(self.INSTANCE_ID_KEY)],
        )

    def is_done(self) -> bool:
        return self.is_state_equals(requested_state='running')


class RebootEC2Instance(StopEC2Instance):

    def __init__(self, task_data: dict):
        super().__init__(task_data=task_data)

    @property
    def task_type(self) -> str:
        return 'Start EC2 instance'

    def do(self):
        resp = self.aws_client.reboot_instances(
            InstanceIds=[self.get_task_attribute(self.INSTANCE_ID_KEY)],
        )
        sleep(90.0)
        return resp

    def is_done(self) -> bool:
        return self.is_state_equals(requested_state='running')


class VerifyECSServicesCount(AutomationTask):

    CLUSTER_KEY = 'cluster'
    SERVICES_KEY = 'services'
    SERVICE_RUNNING_COUNT_KEY = 'runningCount'
    SERVICE_DESIRED_COUNT_KEY = 'desiredCount'

    @property
    def validation_schema(self) -> dict:
        return {
            self.CLUSTER_KEY: {
                'required': True,
                'type': 'string'
            },
            self.SERVICES_KEY: {
                'required': True,
                'type': 'list'
            },
        }

    aws_client = boto3.client('ecs')

    def __init__(self, task_data: dict):
        super().__init__(task_data=task_data)

    @property
    def task_type(self) -> str:
        return 'Verify ECS services count'

    def do(self):
        return 'OK'

    def is_done(self) -> bool:
        desc = self.aws_client.describe_services(
            cluster=self.get_task_attribute(self.CLUSTER_KEY),
            services=self.get_task_attribute(self.SERVICES_KEY),
        )
        for service in desc[self.SERVICES_KEY]:
            desired_count = service[self.SERVICE_DESIRED_COUNT_KEY]
            running_count = service[self.SERVICE_RUNNING_COUNT_KEY]
            if desired_count != running_count:
                Log.debug(
                    f"Service {service['serviceName']} is not ready, "
                    f"desired count is {desired_count} but running count is {running_count}."
                )
                return False
        return True

