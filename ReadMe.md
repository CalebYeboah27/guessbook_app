# Serverless Guestbook

This project implements a simple guestbook application using AWS Lambda and Amazon API Gateway. Users can submit their names and messages, which are then stored temporarily and can be retrieved later.

## Setup and Deployment

### Prerequisites

- An AWS account
- AWS CLI installed and configured

### Step 1: Frontend Interface

1. Create an HTML form with fields for name and message (`index.html`).
2. Apply basic styling using CSS (`styles.css`).

### Step 2: AWS Lambda Setup

1. Create a Lambda function in the AWS Management Console or using AWS CLI.
2. Write the Lambda function logic to process guestbook entries (`lambda_function.py`).
3. Deploy the Lambda function.

### Step 3: API Gateway Integration

1. Set up an API Gateway endpoint to trigger the Lambda function.
2. Define the API's resources and methods for submitting and retrieving entries.

### Step 4: Viewing Guestbook Entries

1. Create another Lambda function to retrieve stored entries.
2. Configure a separate API Gateway endpoint for retrieving entries.

### Step 5: Testing and Validation

1. Deploy the Lambda function and API Gateway to AWS.
2. Test the guestbook by submitting entries through the website and retrieving them.

### Step 6: Error Handling and Logging

1. Implement error handling in the Lambda function to handle invalid input.
2. Set up logging to track Lambda function activity.

## Usage

- Access the guestbook form by opening `index.html` in a web browser.
- Submit your name and message using the form.
- View submitted entries by retrieving them through the provided API endpoints.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
