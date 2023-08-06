import os
import unittest
import numpy as np
import imgio
import rawpipe


thisdir = os.path.dirname(__file__)


class RegressionTest(unittest.TestCase):

    def test_fullpipe(self):
        print("\nConfirming bit-exact output of basic ISP blocks...")
        bayer_pattern = "RGGB"
        gamma_mode = "sRGB"
        whitelevel = None
        wb = [1.7, 2.4]
        ccm = np.array([[ 0.9, 0.4, -0.3],   # noqa
                        [-0.2, 1.1,  0.1],   # noqa
                        [ 0.0,-0.4,  1.4]])  # noqa
        expected, maxval = imgio.imread(os.path.join(thisdir, "expected.ppm"))
        raw = np.fromfile(os.path.join(thisdir, "input.raw"), dtype=np.uint16)
        raw = raw.reshape(expected.shape[:2])
        self.assertEqual(raw.shape[0], expected.shape[0])
        self.assertEqual(raw.shape[1], expected.shape[1])
        alg = rawpipe.Algorithms(verbose=True)
        raw = alg.subtract(raw, [10, 20, 30, 40])
        raw = alg.subtract(raw, [246, 236, 226, 216])  # total = 256
        raw = alg.linearize(raw, 0, whitelevel)
        raw = alg.bayer_combine(*alg.bayer_split(raw))  # no-op
        raw = alg.demosaic(raw, bayer_pattern)
        raw = alg.subtract(raw, [0, 0, 0])  # no-op
        raw = alg.wb(raw, wb)
        raw = alg.ccm(raw, ccm)
        raw = alg.gamut(raw, "ACES", p=1.2)
        raw = alg.saturate(raw, lambda x: x ** 0.5)
        raw = rawpipe.verbose.gamma(raw, gamma_mode)
        raw = rawpipe.verbose.quantize(raw, maxval, expected.dtype)
        self.assertEqual(np.count_nonzero(expected - raw), 0)

    def test_bayer_wb(self):
        expected, maxval = imgio.imread(os.path.join(thisdir, "expected.ppm"))
        raw = np.fromfile(os.path.join(thisdir, "input.raw"), dtype=np.uint16)
        raw = raw.reshape(expected.shape[:2])
        raw = raw.astype(np.float32)
        wb = np.asarray([1.7, 2.4]).astype(np.float32)
        res = rawpipe.wb(raw, wb, "GBRG")
        org_b = rawpipe.bayer_split(raw)[1]
        res_b = rawpipe.bayer_split(res)[1]
        self.assertEqual(res.dtype, np.float32)
        np.testing.assert_allclose(org_b * wb[-1], res_b)

    def test_errors(self):
        raw = np.fromfile(os.path.join(thisdir, "input.raw"), dtype=np.uint16)
        res = rawpipe.verbose.gamma(raw, None)  # should be no-op
        res = rawpipe.verbose.gamma(res, "")  # should be no-op
        res = rawpipe.verbose.gamma(res, False)  # should be no-op
        self.assertTrue(np.all(raw == res))
        with self.assertRaises(AssertionError):
            raw = rawpipe.gamma(raw, "srgb")  # expecting "sRGB"
        with self.assertRaises(AssertionError):
            raw = rawpipe.gamma(raw, True)  # does not evaluate to False
        with self.assertRaises(AssertionError):
            raw = rawpipe.demosaic(raw, "RGGB")  # raw is not in [0, 1]


if __name__ == "__main__":
    np.set_printoptions(formatter={'float': lambda x: f"{x:6.4f}"}, linewidth=180)
    unittest.main()
