Feature: Order Transaction
    Tests related to order transactions
  Scenario Outline:: Verify order Messages shown in details page
    Given Place the item order with <username> and <password>
    When I login to portal with <username> and <password>
    And navigate to orders page Select the OrderId
    Then Order message is successfully displayed
    Examples:
    | username          | password   |
    | omtest@gmail.com  | Ssl12345#  |