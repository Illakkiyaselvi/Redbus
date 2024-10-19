# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## Project Overview

The **Redbus Data Scraping and Filtering with Streamlit Application** project aims to streamline the process of collecting, analyzing, and visualizing bus travel data from the Redbus website. By leveraging **Selenium** for web scraping and **Streamlit** for interactive data filtering, this project provides valuable insights into bus routes, schedules, prices, seat availability, and much more.

This project is designed to improve operational efficiency and strategic planning within the transportation industry by offering data-driven decision-making tools.

## Skills Gained

- Web Scraping using Selenium
- Python Programming
- Interactive Data Filtering using Streamlit
- SQL Database Design and Queries

## Domain

**Transportation**

---

## Problem Statement

This project addresses the need for a comprehensive system to collect and analyze bus travel data from the Redbus platform. It automates data extraction such as bus routes, schedules, prices, and seat availability, and presents the data in an interactive interface using Streamlit.

By automating this process, transportation businesses can leverage data insights for:

- **Travel Aggregators**: Providing real-time bus schedules and seat availability.
- **Market Analysis**: Identifying travel patterns and preferences.
- **Customer Service**: Offering customized travel recommendations based on data.
- **Competitor Analysis**: Comparing services and pricing with competitors.

## Business Use Cases

1. **Travel Aggregators**: Displaying real-time bus schedules and availability.
2. **Market Analysis**: Understanding traveler preferences and popular routes.
3. **Customer Service**: Improving user experience through data-driven travel suggestions.
4. **Competitor Analysis**: Evaluating pricing strategies and service levels across competitors.

---

## Approach

### 1. Data Scraping
- Use **Selenium** to extract bus information from the Redbus website, including:
  - Bus routes
  - Schedules
  - Prices
  - Seat availability

### 2. Data Storage
- Store the scraped data in a **SQL database** for structured analysis.

### 3. Streamlit Application
- Develop a **Streamlit** application to allow users to:
  - View bus data
  - Apply filters (bus type, route, price range, star rating, availability)

### 4. Data Analysis/Filtering
- Implement **SQL queries** to filter data based on user input.
- Use **Streamlit** to create an interactive dashboard for data filtering and analysis.

---

## Project Deliverables

- **Source Code**: Python scripts for web scraping, SQL database interaction, and Streamlit application.
- **Documentation**: Detailed explanations of the code, data collection, and application usage.
- **Database Schema**: SQL scripts to create and populate the database.
- **Streamlit Application**: Screenshots or links showcasing the application with data filtering capabilities.

---

## Data Set

- **Source**: Data will be scraped from the [Redbus Website](https://www.redbus.in/).
- **Format**: Data will be stored in an SQL database.
- **Required Fields**: 
  - Bus route link
  - Bus route name
  - Bus name
  - Bus type (Sleeper/Seater/AC/Non-AC)
  - Departure time
  - Duration
  - Arrival time
  - Star rating
  - Price
  - Seat availability

### Data Set Requirements

The dataset should contain the following fields:

| Column          | Data Type  | Description                                          |
|-----------------|------------|------------------------------------------------------|
| `route_name`    | TEXT       | Information on the bus route                         |
| `route_link`    | TEXT       | Link to detailed route information                   |
| `busname`       | TEXT       | Name of the bus or service provider                  |
| `bustype`       | TEXT       | Type of bus (Sleeper/Seater/AC/Non-AC)               |
| `departing_time`| TIME       | Scheduled departure time                             |
| `duration`      | TEXT       | Journey duration                                     |
| `reaching_time` | TIME       | Expected arrival time                                |
| `star_rating`   | FLOAT      | Rating of the bus service                            |
| `price`         | DECIMAL    | Ticket price                                         |
| `seats_available`| INT       | Number of seats available                            |

---

## Database Schema

The database schema for this project consists of a single table `bus_routes` with the following structure:

| Column Name       | Data Type   | Description                                          |
|-------------------|-------------|------------------------------------------------------|
| `id`              | INT         | Primary Key (Auto-increment)                         |
| `route_name`      | TEXT        | Name of the bus route                                |
| `route_link`      | TEXT        | Link to the route details                            |
| `busname`         | TEXT        | Name of the bus operator                             |
| `bustype`         | TEXT        | Type of the bus (Sleeper/Seater/AC/Non-AC)           |
| `departing_time`  | TIME        | Departure time                                       |
| `duration`        | TEXT        | Duration of the journey                              |
| `reaching_time`   | TIME        | Expected arrival time                                |
| `star_rating`     | FLOAT       | Rating of the bus                                    |
| `price`           | DECIMAL     | Ticket price                                         |
| `seats_available` | INT         | Number of seats available                            |

---



 
     

                                
    
