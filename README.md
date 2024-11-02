# Emergency Services Information System

## Project Overview

This project is an MVP (Minimum Viable Product) for a backend service that retrieves emergency services information based on a given address. It uses ChatGPT to generate the information and stores the results in a NoSQL database.

## Features

- Accepts an address as input
- Queries ChatGPT for emergency services information
- Returns a JSON response with the following details:
  - Closest intersection
  - Non-emergency police number
  - Non-emergency fire department number
  - Non-emergency medical services number
  - Poison control number
  - Gas leak reporting number
  - Veterinary hospital contact information
- Stores the response in a MongoDB database

## Tech Stack

- Backend: Python with FastAPI
- Database: MongoDB
- AI Integration: OpenAI's ChatGPT API

## Project Structure

The project follows the Directory Structure 2.0.1 (DIRS 2) standard:
# emergency-BE
