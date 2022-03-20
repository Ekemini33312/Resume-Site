from update_lambda import lambda_handler


def test_lambda_handler():
    statusCode = lambda_handler("ctx","event") 
    assert statusCode["statusCode"] == 200
    
