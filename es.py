import csv
from elasticsearch import Elasticsearch, helpers
def main():
    es = Elasticsearch([{'host': 'http://53.137.133.247', 'port': 9200}])
    random = 'db-data.csv'
    with open(random) as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader, index='nodegoat')
if __name__ == '__main__':
    main()
