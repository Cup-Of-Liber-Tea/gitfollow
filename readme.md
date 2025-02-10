# GitHub Auto Follow

A simple tool to automatically follow back users who follow you on GitHub using the GitHub API.

## Features

- Automatically follows back new followers.
- Scheduled to run daily with Apache Airflow.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/github-auto-follow.git
   cd github-auto-follow
   ```

2. Install dependencies:
   ```bash
   pip install apache-airflow PyGithub
   ```

3. Set your GitHub token:
   ```bash
   export GITHUB_ACCESS_TOKEN='your-token'
   ```

## Usage

1. Start Airflow:
   ```bash
   airflow webserver --port 8080
   airflow scheduler
   ```

2. Enable the `github_auto_follow` DAG in the Airflow UI.

## Testing

Run the test script:
```bash
python tests/test_github_follow.py
```

## License

MIT License.