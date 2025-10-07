from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    CfnOutput,
)
from constructs import Construct

class NemoAISqsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "NemoAIQueue",
            queue_name="nemo-ai-tasks.fifo",
            fifo=True,
            content_based_deduplication=True,
        )

        CfnOutput(self, "NemoAIQueueArn", value=queue.queue_arn, export_name="NemoAIQueueArn")
        CfnOutput(self, "NemoAIQueueUrl", value=queue.queue_url, export_name="NemoAIQueueUrl")
