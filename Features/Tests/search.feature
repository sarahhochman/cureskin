# Created by Sarah at 4/21/2023
Feature: Tests for search function

  Scenario: Use Search to find product
    Given Open Cureskin home page
    When Click on search
    And Input SPF into search field
    And Click Enter
    Then Product results for SPF are shown

