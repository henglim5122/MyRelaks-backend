# Travel Planning Database

## Overview
This document provides an overview of the Travel Planning Database, including its structure, tables, and usage instructions.

## Table of Contents
1. [Database Schema](#database-schema)
2. [Tables](#tables)
   - [Destinations](#destinations)
   - [Itineraries](#itineraries)
   - [Payments](#payments)
   - [Users](#users)
3. [Usage](#usage)
4. [Installation](#installation)
5. [Contributing](#contributing)
6. [License](#license)

## Database Schema
The Travel Planning Database consists of four main tables designed to manage users, destinations, itineraries, and payment information.

## Tables

### Destinations
- **Table Name**: `destinations`
- **Description**: Stores information about travel destinations.
- **Columns**:
  - `destination_id` (integer, Primary Key): Unique identifier for each destination.
  - `name` (string): Name of the destination.
  - `location` (string): Geographical location of the destination.
  - `state` (string): State where the destination is located.
  - `description` (text): Description of the destination.
  - `coordinates` (point): Geographical coordinates (latitude and longitude).
  - `ratings_review` (text): User reviews and ratings.
  - `price` (numeric): Price associated with the destination.
  - `liked_by` (integer array): List of user IDs who liked this destination.

### Itineraries
- **Table Name**: `itineraries`
- **Description**: Stores planned itineraries for users.
- **Columns**:
  - `itinerary_id` (integer, Primary Key): Unique identifier for each itinerary.
  - `trip_name` (string): Name of the trip.
  - `trip_dates` (daterange): Date range for the trip.
  - `activities` (text): Planned activities during the trip.
  - `total_budget` (numeric): Total budget for the trip.
  - `estimated_cost` (numeric): Estimated cost of the trip.
  - `users_id` (integer, Foreign Key): ID of the user associated with this itinerary.
  - `destination_id` (integer, Foreign Key): ID of the destination included in the itinerary.

### Payments
- **Table Name**: `payments`
- **Description**: Records payment information related to user subscriptions.
- **Columns**:
  - `payment_id` (integer, Primary Key): Unique identifier for each payment.
  - `amount` (numeric): Amount of the payment.
  - `payment_method` (string): Method used for payment (e.g., credit card, PayPal).
  - `payment_status` (string): Status of the payment (e.g., completed, pending).
  - `payment_date` (timestamp): Date and time when the payment was made.
  - `encrypted_payment_info` (text): Encrypted information related to the payment.
  - `users_id` (integer, Foreign Key): ID of the user who made the payment.

### Users
- **Table Name**: `users`
- **Description**: Stores user information.
- **Columns**:
  - `users_id` (integer, Primary Key): Unique identifier for each user.
  - `first_name` (string): User's first name.
  - `last_name` (string): User's last name.
  - `email` (string): User's email address.
  - `password` (string): User's encrypted password.
  - `subscription_type` (string): Type of subscription plan the user is on.

## Usage
To use the database, ensure you have a PostgreSQL environment set up. You can execute SQL queries to interact with the tables and manage data.

## Installation
Instructions for setting up the database locally or on a server.

1. Clone the repository:
   ```bash
   git clone <repository-url>