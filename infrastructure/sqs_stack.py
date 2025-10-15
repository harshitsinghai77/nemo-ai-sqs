from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    Duration,
    CfnOutput,
)
from constructs import Construct

class NemoAISqsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        dlq = sqs.Queue(
            self, "NemoAIDlq",
            queue_name="nemo-ai-tasks-dlq.fifo",
            fifo=True,
            content_based_deduplication=True,
            retention_period=Duration.days(7)  # Optional: how long to keep failed messages
        )

        queue = sqs.Queue(
            self, "NemoAIQueue",
            queue_name="nemo-ai-tasks.fifo",
            fifo=True,
            content_based_deduplication=True,
            visibility_timeout=Duration.seconds(1200),
            dead_letter_queue=sqs.DeadLetterQueue(
                max_receive_count=1,
                queue=dlq
            )
        )

        CfnOutput(self, "NemoAIQueueArn", value=queue.queue_arn, export_name="NemoAIQueueArn")
        CfnOutput(self, "NemoAIQueueUrl", value=queue.queue_url, export_name="NemoAIQueueUrl")
