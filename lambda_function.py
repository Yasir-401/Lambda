import json

def lambda_handler(event, context):
    if 'operation' not in event or 'operand1' not in event or 'operand2' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input. Please provide operation, operand1, and operand2.'}),
        }

    operation = event['operation']
    operand1 = float(event['operand1'])
    operand2 = float(event['operand2'])

    result = None
    if operation == 'add':
        result = operand1 + operand2
    elif operation == 'subtract':
        result = operand1 - operand2
    elif operation == 'multiply':
        result = operand1 * operand2
    elif operation == 'divide':
        if operand2 != 0:
            result = operand1 / operand2
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Cannot divide by zero.'}),
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid operation. Supported operations: add, subtract, multiply, divide.'}),
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result}),
    }
