# Nemo AI SQS Infrastructure

AWS CDK project for deploying SQS queues for Nemo AI task processing.

## Architecture

- **FIFO SQS Queue**: `nemo-ai-tasks.fifo` for ordered task processing
- **Dead Letter Queue**: `nemo-ai-tasks-dlq.fifo` for failed messages
- **Visibility Timeout**: 20 minutes for long-running tasks
- **Auto-retry**: 1 attempt before moving to DLQ

## Directory Structure

```
├── cdk_app.py              # CDK application entry point
├── infrastructure/
│   └── sqs_stack.py        # SQS stack definition
├── .github/workflows/
│   └── deploy.yml          # CI/CD pipeline
├── requirements.txt        # Python dependencies
└── cdk.json               # CDK configuration
```

## Features

- Content-based deduplication for FIFO queues
- 7-day retention for failed messages
- CloudFormation outputs for queue ARN and URL
- Automated deployment on main branch pushes

## Deployment

### Manual
```bash
pip install -r requirements.txt
cdk deploy
```

### Automated
Pushes to `main` branch trigger automatic deployment via GitHub Actions.

## Requirements

- Python 3.12+
- AWS CDK CLI
- AWS credentials configured

## Environment

Deploys to `us-east-1` region by default.