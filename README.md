# REST-Full-API-for-Text-Analysis-and-Search
About This Python code implements a REST API for text analysis, including user authentication, word tokenization, word-to-paragraph indexing, paragraph ID generation, search functionality, and PostgreSQL data storage.
It is a text analysis API that provides functionalities for managing paragraphs, tokenization, and search operations.

## Table of Contents
1. [Purpose and Goal](#purpose-and-goal)
2. [Target Audience](#target-audience)
3. [Features and Functionalities](#features-and-functionalities)
   - [User Authentication](#user-authentication)
   - [Tokenization](#tokenization)
   - [Word Indexing](#word-indexing)
   - [Unique IDs Generation](#unique-ids-generation)
   - [Paragraph Definition](#paragraph-definition)
   - [Search Functionality](#search-functionality)
   - [RESTful API Design](#restful-api-design)
   - [Data Storage](#data-storage)
4. [User Inputs](#user-inputs)
5. [Application Outputs](#application-outputs)

## Purpose and Goal
The main purpose of the application is to create a REST API that processes multiple paragraphs of text, stores them along with word-to-paragraph mappings in a PostgreSQL database, and allows users to search for a word and retrieve the top 10 paragraphs containing that word.

## Target Audience
The target audience for this application includes developers or individuals who work with text data and require search functionality.

## Features and Functionalities

### User Authentication
- Login
- Signup

### Tokenization
- Splitting words at whitespace
- Converting words to lowercase

### Word Indexing
- Indexing words against the paragraphs they belong to

### Unique IDs Generation
- Generating unique IDs for paragraphs

### Paragraph Definition
- Defining a paragraph as two newline characters

### Search Functionality
- Searching for a word and retrieving the top 10 paragraphs containing that word

### RESTful API Design
- Implementing typical RESTful API design patterns

### Data Storage
- Storing data in a PostgreSQL database

## User Inputs
- Login credentials (email, password)
- Multiple paragraphs of text as input

## Application Outputs
- Top 10 paragraphs containing the searched word
- Proper authentication and error handling responses

---
