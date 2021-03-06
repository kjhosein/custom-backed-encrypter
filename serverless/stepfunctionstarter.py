import boto3
import json


class StepFunctionStarter:
    
    def __init__(self, instance_id, step_function_arn, region):
        self.instance_id = instance_id
        self.step_function_arn = step_function_arn
        self.region = region
        self.session = boto3.session.Session(region_name=self.region)

    def start(self):

        sfn_client = self.session.client("stepfunctions")

        try:
            input_data = {
                "instance_id": self.instance_id,
                "region": self.region
            }

            sfn_response = sfn_client.start_execution(
                stateMachineArn=self.step_function_arn,
                input=json.dumps(input_data)
            )

            print sfn_response

        except Exception as lambda_e:

            print "Step Function Starter failed with the following information:\n\n" \
                  "Exception arguments:\n{}\n\n" \
                  "Exception message:\n{}\n\n".format(lambda_e.args, lambda_e.message)
