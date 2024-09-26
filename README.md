# Atlas-logs

Atlas-logs is a Flask-based application for collecting, storing, and analyzing system logs using MongoDB and OpenAI integration. It provides a user-friendly interface for querying logs using natural language and generates insightful analyses.

## Features

- Syslog reception and storage in MongoDB
- User authentication and authorization
- Natural language log querying
- AI-powered log analysis using OpenAI
- RESTful API for log searches
- Web interface for easy interaction

## Prerequisites

- Python 3.8+
- MongoDB 4.4+
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/eltonlaice/atlas-logs.git
   cd atlas-logs
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   MONGODB_URI=your_mongodb_uri
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Initialize the database:
   ```
   python scripts/setup_mongodb.js
   ```

## Usage

1. Start the Flask application:
   ```
   flask run
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Log in using the default credentials:
   - Username: administrator
   - Password: password

   **IMPORTANT:** These are default credentials for initial setup only. It is crucial to change these credentials immediately after your first login, especially in a production environment.

4. After logging in, navigate to the user settings to change the default password.

5. Use the dashboard to search and analyze logs. You can enter queries in natural language, such as "Who deleted the file /opt/x?"

## Security Notes

The default credentials are provided for initial setup and testing purposes only. In a production environment, please ensure that you:

1. Change the default password immediately after the first login.
2. Use strong, unique passwords.
3. Implement additional security measures such as two-factor authentication if possible.
4. Regularly audit user access and permissions.
5. Keep your OpenAI API key secure and do not expose it in public repositories.

## Project Structure

```
atlas-logs/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── search.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── log.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── log_processor.py
│   │   └── openai_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── db.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       └── search_results.html
├── config.py
├── requirements.txt
├── run.py
├── scripts/
│   └── setup_mongodb.js
├── docs/
│   ├── api_docs.md
│   └── user_guide.md
├── tests/
│   ├── test_auth.py
│   └── test_search.py
├── .gitignore
└── README.md
```

## API Documentation

For detailed API documentation, please refer to `docs/api_docs.md`. This document outlines all available endpoints, request formats, and response structures.

## Configuration

The `config.py` file contains all the configuration settings for the application. Make sure to review and adjust these settings according to your environment needs.

## Testing

To run the tests, execute:
```
python -m pytest
```

Ensure that you have a test MongoDB instance set up before running the tests.

## Logging

Application logs are stored in the `logs/` directory. Review these logs regularly for any errors or suspicious activities.

## Backup and Recovery

Regular backups of the MongoDB database are crucial. Implement a backup strategy that fits your data retention policies and ensure you test the recovery process periodically.

## Troubleshooting

If you encounter any issues:
1. Check the application logs in the `logs/` directory.
2. Ensure all environment variables are correctly set.
3. Verify MongoDB connection and credentials.
4. Check the OpenAI API key and usage limits.

For more detailed troubleshooting steps, refer to `docs/troubleshooting.md`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Ensure that you update tests as appropriate and adhere to the existing coding style.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask team for the excellent web framework
- MongoDB team for the robust database system
- OpenAI for their powerful language models

## Support

For support, please open an issue on the GitHub repository or contact the maintainers directly at meu@eltonlaice.com.