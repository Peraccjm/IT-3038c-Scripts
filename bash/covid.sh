#!/IT-3038c-Scripts/Bash
# This script dowloads covid data and displayes it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')

echo "On $TODAY, there were $POSITIVE postitve cases, $NEGATIVE negative cases, $DEATH deaths, and $HOSPITALIZED hospitalized people for COVID."
