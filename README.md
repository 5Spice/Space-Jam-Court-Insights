# Space-Jam-Court-Insights

Space Jam Court Insights is a web application that allows users to access and analyze basketball player statistics, view shot charts, and retrieve player summaries. This project combines a Django backend for data storage and retrieval with an Angular frontend for a user-friendly interface.


## Features

- **Player Summary:** Retrieve detailed player statistics, including points, assists, rebounds, and more, by providing a player's ID.
- **Shot Charts:** Visualize player shot data on a basketball court chart, showing successful and missed shots.
- **Error Handling:** Gracefully handle errors, such as missing data or invalid player IDs, to provide a smooth user experience.
- **Retry Mechanism:** Allow users to retry loading player summary data in case of errors.


### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Backend:** Docker was used to install PostgreSQL.  The Django backend must be set up and running, including the database for player statistics.  Package requirements are in requirements.txt

- **Frontend:** The Angular frontend must be installed and configured properly.

#### Getting Started

- **Backend:** Ensure database is up.  Migrate and run python manage.py load_data.py.  Start server on http://localhost:8000/
- **Frontend:** Frontend is installed and hosted via Node on http://localhost:4200/
