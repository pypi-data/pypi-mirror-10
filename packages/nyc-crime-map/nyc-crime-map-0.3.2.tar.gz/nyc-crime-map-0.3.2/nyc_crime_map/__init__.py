import os, logging

from .download import table_features_first, table_features_tail
from .serialize import geojson, csv

logger = logging.getLogger('nyc_crime_map')

def nyc_crime_map(today, table_id, select, startPageToken = None):
    if startPageToken:
        pageToken = startPageToken
    else:
        logger.info('Loading data for the initial search, without pageToken')
        results = table_features_first(today, table_id, select).json()
        yield from results.get('features', [])
        pageToken = results.get('nextPageToken')

    while pageToken:
        logger.info('Loading data for pageToken %s' % pageToken)
        results = table_features_tail(today, table_id, select, pageToken).json()
        yield from results.get('features', [])
        pageToken = results.get('nextPageToken')

def cli():
    import datetime
    from .args import parser
    today = datetime.date.today()
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.INFO)
        fp_stream = logging.StreamHandler()
        fp_stream.setLevel(logging.INFO)
        logger.addHandler(fp_stream)

    if not os.path.isdir(args.directory):
        os.makedirs(args.directory, exist_ok = True)

    logger.info('Beginning run')
    for table_id, select in [
         ('02378420399528461352-17772055697785505571', 'YR,MO,geometry,X,Y,TOT,CR'),
         ('02378420399528461352-11853667273131550346', 'YR,MO,geometry,X,Y,TOT'),
    ]:
        logger.info('Starting on table %s with query %s' % (table_id, select))
        data = list(nyc_crime_map(today, table_id, select))
        basename = os.path.join(args.directory, table_id)
        for f in [geojson, csv]:
            logger.info('Generating %s' % f.__name__)
            with open('%s.%s' % (basename, f.__name__), 'w') as fp:
                f(select, data, fp)
