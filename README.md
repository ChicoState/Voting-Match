[![Lint Code Base](https://github.com/ChicoState/Voting-Match/actions/workflows/linter.yml/badge.svg?branch=main)](https://github.com/ChicoState/Voting-Match/actions/workflows/linter.yml)

# Voting-Match

## Running the project locally
To launch the website:

```Shell
sudo docker compose up
```

Once the website is running, you can connect on it through `localhost:8000`

To apply database migrations (required when changing anything in VotingMatch/core/models.py):

```Shell
sudo docker compose run web python VotingMatch/manage.py makemigrations
sudo docker compose run web python VotingMatch/manage.py migrate
```
