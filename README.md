
# WeatherApp FastAPI Lambda Deployment
Demo repo for Weather App using FastAPI
This repository contains a FastAPI application deployed on AWS Lambda with API Gateway. The deployment process is automated using GitHub Actions and Terraform.

## Workflow

1. **GitHub Actions**: Automates the CI/CD pipeline to deploy to AWS.
2. **Terraform**: Manages the infrastructure provisioning for AWS Lambda, API Gateway, and ECR.
3. **Docker**: Builds a Docker image of the FastAPI app and pushes it to ECR.

## How to Use

1. Fork the repository.
2. Set up your AWS credentials and ECR repository in GitHub Secrets.
3. Push your code to the `main` branch to trigger the deployment.

## Deployment Environments

The project supports multiple environments such as `staging` and `production`, controlled via GitHub Actions matrix.

## License

MIT License

## Author

Adaramola Bukola Omolewa
