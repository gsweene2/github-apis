from github_apis import main

from mock import patch

@patch("github_apis.main.logging")
def test_main(mock_logging):
    # Arrage

    # Act
    main.hello_world()

    # Assert
    print(f"Call args: {mock_logging.call_args_list}")
    mock_logging.info.assert_called_with("[hello_world]")
