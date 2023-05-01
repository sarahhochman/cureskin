# Created by Sarah at 4/27/2023
Feature: Sign in to CureSkin

  Scenario: enter sting on home page and get error
    Given Open Cureskin home page
    When click on email field
    And input morahhochman
    And Click Enter Email
    Then Get Error Message

  Scenario: enter valid email and sign up
     Given Open Cureskin home page
    When click on email field
    And input david.hochman@gmail.com
    And Click Enter Email
    Then Get SignUp Message