# Rekognition-image-analyzer
This project contains an AWS Lambda function designed to analyze images using AWS Rekognition. The Lambda function processes images, identifies labels, and extracts useful data such as objects, scenes, or activities from the images.

## Key Features:
- **Image Analysis with AWS Rekognition**: Leverages AWS Rekognition to detect labels, faces, text, and more.
- **Serverless Architecture**: Fully implemented using AWS Lambda, allowing for a scalable and cost-efficient solution.
- **Customizable**: Easily configurable for different use cases, such as facial recognition, object detection, or text extraction.

## Files:
- `src/lambda_function.py`: Contains the main Lambda function code.
- `template.yml`: AWS SAM template for defining the Lambda function and other resources.
- `assets/`:
  - `Recognition_image_Analyzer.pdf`: Document containing evidence or detailed results.

## Setup Instructions


### Step 1: Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/rekognition-image-analyzer.git
cd rekognition-image-analyzer
