import numpy as np
import numpy.testing as npt
import pandas as pd
from ioos_qartod.qc_tests import qc
from ioos_qartod.qc_tests.qc import QCFlags
import unittest

class QartodQcTest(unittest.TestCase):
    def test_lon_lat_bbox(self):
        """Ensure that longitudes and latitudes are within reasonable bounds"""
        lon = np.array([80.0, -78.5, 500.500])
        lat = np.array([np.NaN, 50, -60])
        npt.assert_array_equal(qc.location_set_check(lon, lat),
                              np.array([4, 1, 4]))

    def test_distance_threshold(self):
        """Tests a user defined distance threshold between successive points"""
        lon = np.array([-71.05, -71.06, -80.0])
        lat = np.array([41.0, 41.02, 45.05])
        npt.assert_array_equal(qc.location_set_check(lon, lat,
                                                     range_max=3000.0),
                               np.array([1, 1, 3]))

    def test_range_check_mixed(self):
        """See if user and sensor ranges are picked up"""
        sensor_span = (10, 50)
        user_span = (20, 40)
        vals = np.array([5, 10,  # sensor range
                         15, 20,  # user range
                         25, 30, 35,  # valid
                         40, 45,  # user range
                         51])  # sensor range
        npt.assert_array_equal(qc.range_check(vals, sensor_span, user_span),
                              np.array([4, 4, 3, 3, 1, 1, 1, 3, 3, 4]))

    def test_climatology_check(self):
        # 14 vals - 2010-01-03 to 2010-04-04
        dates = pd.date_range('2010-01-01', '2010-04-10', freq='W')
        # monthly vals
        monthly_clim = {1: (6.0, 10), 2: (1.4, 6.4), 3: (4.2, 13.0)}
        ts = pd.Series(np.array([12.1, 9.0, 1.3, 6.2, 9.9,  # Jan
                                  1.6,  2.0, 9.0, 4.0, # Feb
                                  5.0, 5.5, 10.6, 16.0, # Mar
                                  17.2 # Apr
                                 ]), dates)
        expected = np.array([3, 1, 3, 1, 1, # Jan
                             1, 1, 3, 1, # Feb
                             1, 1, 1, 3, # Mar
                             2], # Apr should be unknown as w/o clim value
                            dtype='i4')
        results = qc.climatology_check(ts, monthly_clim, lambda t: t.month)
        npt.assert_array_equal(results, expected)

    def test_overlapping_threshold_ranges(self):
        """
        Test to see if overlapping sensor and user ranges will throw an
        exception
        """
        vals = np.array([50, 40, 20, 29])
        sensor_span = (10, 30)
        user_span = (20, 40)
        self.assertRaises(ValueError, qc.range_check, vals, sensor_span,
                          user_span)

    def test_bad_extent(self):
        """Tests to make sure invalid extents can't be passed in"""
        vals = np.array([2, 1.0, 3.4, 5.6])
        sensor_span = (1,)
        user_span = np.array([[50, 60], [30, 90]])
        self.assertRaises(ValueError, qc.range_check, vals, sensor_span,
                          user_span)

    def test_spike_detection(self):
        """Test to make ensure single value spike detection works properly"""
        low_thresh, high_thresh = 25, 50
        arr = np.array([10, 12, 999.99, 13, 15, 40, 9, 9])
        # first and last elements should always be good data, unless someone
        # has set a threshold to zero
        expected = [1, 4, 4, 4, 1, 3, 1, 1]
        npt.assert_array_equal(qc.spike_check(arr, low_thresh, high_thresh),
                              expected)

    def test_spike_invalid_threshold_raises_value_error(self):
        """Test that invalid ranges cause an exception to be raised"""
        low_thresh, high_thresh = 50, 50
        arr = np.array([10, 12, 999.99, 13, 15, 40, 9, 9])
        self.assertRaises(ValueError, qc.spike_check, arr, low_thresh,
                          high_thresh)

    def test_rate_of_change(self):
        arr = np.array([2, 10, 2.1, 3, 4, 5, 7, 10, 0, 2, 2.2, 2])
        prev_qc = np.array([3])
        thresh_val = 5
        expected = np.array([3, 3, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1])
        result = qc.rate_of_change_check(arr, thresh_val, prev_qc)
        npt.assert_array_equal(expected, result)

    def test_flat_line_check(self):
        """Make sure flat line check returns expected flag values"""
        low_thresh = 3
        high_thresh = 5
        eps = 0.01
        vals = np.array([1, 2, 2.0001, 2, 2.0001, 2, 2.0001, 2,
                         4, 5, 3, 3.0001, 3.0005, 3.00001])
        npt.assert_array_equal(qc.flat_line_check(vals, low_thresh, high_thresh,
                               eps), [1, 1, 1, 1, 3, 3, 4, 4, 1, 1, 1, 1, 1, 3])

    def test_bad_reps(self):
        """Test that low_reps >= high_reps raises an error in flat line check"""
        self.assertRaises(ValueError, qc.flat_line_check, np.ones(12), 10, 6,
                          0.01)

    def test_float_reps_raises_exception(self):
        """
        Check that non-integer values for repetitions raises a TypeError
        in flat line check
        """
        self.assertRaises(TypeError, qc.flat_line_check, np.ones(12),
                          4.5, 6.93892, 0.01)

    def test_attenuated_signal_check(self):
        """
        Test a time segment for an attenuated signal, comparing against
        standard deviation
        """
        signal = np.array([3, 4, 5, 8.1, 9, 8.5, 8.7, 8.4, 8.2, 8.35, 2, 1])
        # half hour increments
        times = np.arange('2005-02-01T00:00Z', '2005-02-01T06:00Z',
                          dtype='datetime64[30m]')
        time_range=(np.datetime64('2005-02-01T01:30Z'),
                    np.datetime64('2005-02-01T04:30Z'))
        min_var_fail = 0.05
        min_var_warn = 0.7
        flags = qc.attenuated_signal_check(signal, times, min_var_warn,
                                           min_var_fail, time_range)
        npt.assert_array_equal(flags, np.array([2, 2, 2, 3, 3, 3, 3, 3, 3, 3,
                                                2, 2]))

    def test_attenuated_signal_check_range(self):
        """
        Test a time segment for an attenuated signal, comparing against
        range
        """
        signal = np.array([3, 4, 5, 8.1, 9, 8.5, 8.7, 8.4, 8.2, 8.35, 2, 1])
        # half hour increments
        times = np.arange('2005-02-01T00:00Z', '2005-02-01T06:00Z',
                          dtype='datetime64[30m]')
        time_range=(np.datetime64('2005-02-01T01:30Z'),
                    np.datetime64('2005-02-01T04:30Z'))
        min_var_fail = 0.1
        min_var_warn = 0.15
        flags = qc.attenuated_signal_check(signal, times, min_var_warn,
                                           min_var_fail, time_range,
                                           check_type='range')
        npt.assert_array_equal(flags, np.array([2, 2, 2, 1, 1, 1, 1, 1, 1, 1,
                                                2, 2]))
