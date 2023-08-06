#!/usr/bin/env python

"""tzwhere.py - time zone computation from latitude/longitude.

Ordinarily this is loaded as a module and instances of the tzwhere
class are instantiated and queried directly, but the module can be run
as a script too (this requires the docopt package to be installed).
Run it with the -h option to see usage.

"""

import csv
import datetime
try:
    import json
except ImportError:
    import simplejson as json
import math
import os
import pickle

# We can save about 222MB of RAM by turning our polygon lists into
# numpy arrays rather than tuples, if numpy is installed.
try:
    import numpy
    WRAP = numpy.array
except ImportError:
    WRAP = tuple


class tzwhere(object):

    SHORTCUT_DEGREES_LATITUDE = 1
    SHORTCUT_DEGREES_LONGITUDE = 1
    # By default, use the data file in our package directory
    DEFAULT_JSON = os.path.join(os.path.dirname(__file__),
                                'tz_world_compact.json')
    DEFAULT_PICKLE = os.path.join(os.path.dirname(__file__),
                                  'tz_world.pickle')
    DEFAULT_CSV = os.path.join(os.path.dirname(__file__),
                               'tz_world.csv')

    def __init__(self, input_kind='json', path=None):

        # Construct appropriate generator for (tz, polygon) pairs.
        if input_kind in ['json', 'pickle']:
            featureCollection = tzwhere.read_tzworld(input_kind, path)
            pgen = tzwhere._feature_collection_polygons(featureCollection)
        elif input_kind == 'csv':
            pgen = tzwhere._read_polygons_from_csv(path)
        else:
            raise ValueError(input_kind)

        # Turn that into an internal mapping.
        self._construct_polygon_map(pgen)

        # Construct lookup shortcuts.
        self._construct_shortcuts()

    def _construct_polygon_map(self, polygon_generator):
        """Turn a (tz, polygon) generator, into our internal mapping."""
        self.timezoneNamesToPolygons = {}
        for (tzname, raw_poly) in polygon_generator:
            if tzname not in self.timezoneNamesToPolygons:
                self.timezoneNamesToPolygons[tzname] = []
            self.timezoneNamesToPolygons[tzname].append(
                WRAP(tzwhere._raw_poly_to_poly(raw_poly)))

        # Convert polygon lists to numpy arrays or (failing that)
        # tuples to save memory.
        for tzname in self.timezoneNamesToPolygons.keys():
            self.timezoneNamesToPolygons[tzname] = \
                WRAP(self.timezoneNamesToPolygons[tzname])

    def _construct_shortcuts(self):

        self.timezoneLongitudeShortcuts = {}
        self.timezoneLatitudeShortcuts = {}
        for tzname in self.timezoneNamesToPolygons:
            for polyIndex, poly in enumerate(self.timezoneNamesToPolygons[tzname]):
                lats = [x[0] for x in poly]
                lngs = [x[1] for x in poly]
                minLng = (math.floor(min(lngs) / self.SHORTCUT_DEGREES_LONGITUDE)
                          * self.SHORTCUT_DEGREES_LONGITUDE)
                maxLng = (math.floor(max(lngs) / self.SHORTCUT_DEGREES_LONGITUDE)
                          * self.SHORTCUT_DEGREES_LONGITUDE)
                minLat = (math.floor(min(lats) / self.SHORTCUT_DEGREES_LATITUDE)
                          * self.SHORTCUT_DEGREES_LATITUDE)
                maxLat = (math.floor(max(lats) / self.SHORTCUT_DEGREES_LATITUDE)
                          * self.SHORTCUT_DEGREES_LATITUDE)
                degree = minLng
                while degree <= maxLng:
                    if degree not in self.timezoneLongitudeShortcuts:
                        self.timezoneLongitudeShortcuts[degree] = {}

                    if tzname not in self.timezoneLongitudeShortcuts[degree]:
                        self.timezoneLongitudeShortcuts[degree][tzname] = []

                    self.timezoneLongitudeShortcuts[degree][tzname].append(polyIndex)
                    degree = degree + self.SHORTCUT_DEGREES_LONGITUDE

                degree = minLat
                while degree <= maxLat:
                    if degree not in self.timezoneLatitudeShortcuts:
                        self.timezoneLatitudeShortcuts[degree] = {}

                    if tzname not in self.timezoneLatitudeShortcuts[degree]:
                        self.timezoneLatitudeShortcuts[degree][tzname] = []

                    self.timezoneLatitudeShortcuts[degree][tzname].append(polyIndex)
                    degree = degree + self.SHORTCUT_DEGREES_LATITUDE

        # Convert things to tuples to save memory
        for degree in self.timezoneLatitudeShortcuts:
            for tzname in self.timezoneLatitudeShortcuts[degree].keys():
                self.timezoneLatitudeShortcuts[degree][tzname] = \
                    tuple(self.timezoneLatitudeShortcuts[degree][tzname])
        for degree in self.timezoneLongitudeShortcuts.keys():
            for tzname in self.timezoneLongitudeShortcuts[degree].keys():
                self.timezoneLongitudeShortcuts[degree][tzname] = \
                    tuple(self.timezoneLongitudeShortcuts[degree][tzname])

    def _point_inside_polygon(self, x, y, poly):
        n = len(poly)
        inside = False

        p1x, p1y = poly[0][1], poly[0][0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n][1], poly[i % n][0]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

    def tzNameAt(self, latitude, longitude):
        latTzOptions = self.timezoneLatitudeShortcuts[
            (math.floor(latitude / self.SHORTCUT_DEGREES_LATITUDE)
             * self.SHORTCUT_DEGREES_LATITUDE)
        ]
        latSet = set(latTzOptions.keys())
        lngTzOptions = self.timezoneLongitudeShortcuts[
            (math.floor(longitude / self.SHORTCUT_DEGREES_LONGITUDE)
             * self.SHORTCUT_DEGREES_LONGITUDE)
        ]
        lngSet = set(lngTzOptions.keys())
        possibleTimezones = lngSet.intersection(latSet)
        if possibleTimezones:
            if False and len(possibleTimezones) == 1:
                return possibleTimezones.pop()
            else:
                for tzname in possibleTimezones:
                    polyIndices = set(latTzOptions[tzname]).intersection(set(lngTzOptions[tzname]))
                    for polyIndex in polyIndices:
                        poly = self.timezoneNamesToPolygons[tzname][polyIndex]
                        if self._point_inside_polygon(longitude, latitude, poly):
                            return tzname

    @staticmethod
    def read_tzworld(input_kind='json', path=None):
        reader = tzwhere.read_json if input_kind == 'json' else tzwhere.read_pickle
        return reader(path)

    @staticmethod
    def read_json(path=None):
        if path is None:
            path = tzwhere.DEFAULT_JSON
        print('Reading json input file: %s' % path)
        with open(path, 'r') as f:
            featureCollection = json.load(f)
        return featureCollection

    @staticmethod
    def read_pickle(path=None):
        if path is None:
            path = tzwhere.DEFAULT_PICKLE
        print('Reading pickle input file: %s' % path)
        with open(path, 'rb') as f:
            featureCollection = pickle.load(f)
        return featureCollection

    @staticmethod
    def write_pickle(featureCollection, path=DEFAULT_PICKLE):
        print('Writing pickle output file: %s' % path)
        with open(path, 'wb') as f:
            pickle.dump(featureCollection, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def _read_polygons_from_csv(path=None):
        if path is None:
            path = tzwhere.DEFAULT_CSV
        print('Reading from CSV input file: %s' % path)
        with open(path, 'r') as f:
            for row in f:
                row = row.split(',')
                yield(row[0], [float(x) for x in row[1:]])

    @staticmethod
    def write_csv(featureCollection, path=DEFAULT_CSV):
        print('Writing csv output file: %s' % path)
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for (tzname, polygon) in tzwhere._feature_collection_polygons(
                    featureCollection):
                writer.writerow([tzname] + polygon)

    @staticmethod
    def _feature_collection_polygons(featureCollection):
        """Turn a feature collection into an iterator over polygons.

        Given a featureCollection of the kind loaded from the json
        input, unpack it to an iterator which produces a series of
        (tzname, polygon) pairs, one for every polygon in the
        featureCollection.  Here tzname is a string and polygon is a
        list of floats.

        """
        for feature in featureCollection['features']:
            tzname = feature['properties']['TZID']
            if feature['geometry']['type'] == 'Polygon':
                polys = feature['geometry']['coordinates']
                for poly in polys:
                    yield (tzname, poly)

    @staticmethod
    def _raw_poly_to_poly(raw_poly):
        # WPS84 coordinates are [long, lat], while many conventions
        # are [lat, long]. Our data is in WPS84. Convert to an
        # explicit format which geolib likes.
        assert len(raw_poly) % 2 == 0
        poly = []
        while raw_poly:
            lat = raw_poly.pop()
            lng = raw_poly.pop()
            poly.append((lat, lng))
        return poly


HELP = """tzwhere.py - time zone computation from latitude/longitude.

Usage:
  tzwhere.py [options] write_pickle [<input_path>] [<output_path>]
  tzwhere.py [options] write_csv [<input_path>] [<output_path>]

Modes:

  write_pickle - write out a pickle file of a feature collection;
                 <input_path> is as with test.  <output_path> is also
                 optional, and defaults to {default_pickle}.
                 N.b.: don't do this with -k csv

  write_csv - write out a CSV file.  Each line contains the time zone
              name and a list of floats for a single polygon in that
              time zone.  <input_path> is as with test.  <output_path>
              is also optional, and defaults to {default_csv}.
              N.b.: don't do this with -k csv

Options:
  -k <kind>, --kind=<kind>  Input kind. Should be json or csv or pickle
                            [default: json].
  -m, --memory              Report on memory usage before, during, and
                            after operation.
  -h, --help                Show this help.

""".format(**{
    'default_json': tzwhere.DEFAULT_JSON,
    'default_pickle': tzwhere.DEFAULT_PICKLE,
    'default_csv': tzwhere.DEFAULT_CSV,
})


report_memory = False


def main():
    try:
        import docopt
    except ImportError:
        print("Please install the docopt package to use tzwhere.py as a script.")
        import sys
        sys.exit(1)

    args = docopt.docopt(HELP)

    global report_memory
    report_memory = args['--memory']

    if args['write_pickle']:
        if args['--kind'] not in ('json', 'pickle'):
            print("Can't write pickle output from CSV input")
            return
        if args['<output_path>'] is None:
            args['<output_path>'] = tzwhere.DEFAULT_PICKLE
        write_pickle(args['--kind'], args['<input_path>'],
                     args['<output_path>'])
    elif args['write_csv']:
        if args['--kind'] not in ('json', 'pickle'):
            print("Can't write CSV output from CSV input")
            return
        if args['<output_path>'] is None:
            args['<output_path>'] = tzwhere.DEFAULT_CSV
        write_csv(args['--kind'], args['<input_path>'],
                  args['<output_path>'])


def write_pickle(input_kind, input_path, output_path):
    memuse()
    features = tzwhere.read_tzworld(input_kind, input_path)
    memuse()
    tzwhere.write_pickle(features, output_path)
    memuse()


def write_csv(input_kind, input_path, output_path):
    memuse()
    features = tzwhere.read_tzworld(input_kind, input_path)
    memuse()
    tzwhere.write_csv(features, output_path)
    memuse()


def memuse():
    global report_memory
    if not report_memory:
        return

    import subprocess
    import resource

    import sys
    if sys.version_info >= (3, 0):
        sep = '\\n'
    else:
        sep = '\n'

    free = int(str(subprocess.check_output(['free', '-m']
                                           )).split(sep)[2].split()[-1])
    maxrss = int(resource.getrusage(
        resource.RUSAGE_SELF).ru_maxrss / 1000)
    print()
    print('Memory:')
    print('{0:6d} MB free'.format(free))
    print('{0:6d} MB maxrss'.format(maxrss))
    print()

if __name__ == "__main__":
    main()
