"""Unit test of `imucalibrate` module

"""

import warnings
import pkg_resources as pkg_rsrc
import os.path as osp
import unittest as ut
import numpy as np
import numpy.testing as npt
import xarray as xr
import skdiveMove.imutools as skimu
from scipy.optimize import OptimizeWarning
from skdiveMove.imutools.ellipsoid import _ELLIPSOID_FTYPES


_ICDF0 = (pkg_rsrc
          .resource_filename("skdiveMove",
                             osp.join("tests", "data",
                                      "samsung_galaxy_s5.nc")))
_ICDF1 = (pkg_rsrc
          .resource_filename("skdiveMove",
                             osp.join("tests", "data", "gertrude",
                                      "magnt_accel_calib.nc")))


class TestUtils(ut.TestCase):
    """Test `allan` functions

    """
    def setUp(self):
        imu = (skimu.IMUBase
               .read_netcdf(_ICDF0,
                            acceleration_name="acceleration",
                            angular_velocity_name="angular_velocity",
                            magnetic_density_name="magnetic_density",
                            has_depth=False))

        self.imu = imu

        # Define taus
        maxn = np.floor(np.log2(imu.angular_velocity.shape[0] / 250))
        sampling_rate = imu.angular_velocity.attrs["sampling_rate"]
        omega_taus = ((50.0 / sampling_rate) *
                      np.logspace(0, int(maxn), 100, base=2.0))
        self.omega_taus = omega_taus

        # Ellipsoid data
        magnt_accel_xr = xr.load_dataset(_ICDF1)
        self.magnt_uncalib = magnt_accel_xr["magnetic_density"].values
        self.accel_uncalib = magnt_accel_xr["acceleration"].values

    def test_get_devs(self):
        imu = self.imu
        omega_taus = self.omega_taus
        adevs = imu._allan_deviation("angular_velocity", taus=omega_taus)
        npt.assert_equal(adevs.shape[0], omega_taus.size)
        npt.assert_equal(adevs.shape[1], 6)

    def test_allan_coefs(self):
        imu = self.imu
        omega_taus = self.omega_taus
        adevs = imu._allan_deviation("angular_velocity", taus=omega_taus)

        # allan module function
        adev_x = adevs["angular_velocity_x"]["allan_dev"]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", OptimizeWarning)
            sigmas_d, adevs_reg = skimu.allan_coefs(omega_taus, adev_x)
        npt.assert_equal(len(sigmas_d), 5)
        npt.assert_equal(len(adevs_reg), len(omega_taus))

        # IMU method on sensor suite
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", OptimizeWarning)
            allan_coefs, adevs_fit = imu.allan_coefs("angular_velocity",
                                                     taus=omega_taus)
        npt.assert_equal(allan_coefs.shape, (5, 3))
        npt.assert_equal(adevs_fit.shape, (len(omega_taus), 9))

    def test_ellipsoid(self):
        magnt = self.magnt_uncalib
        accel = self.accel_uncalib

        # Test the different types of ellipsoid fits with the magnetometers
        for ftype in _ELLIPSOID_FTYPES:
            off, gain, rotM = skimu.fit_ellipsoid(magnt, f=ftype)
            npt.assert_equal(off.size, gain.size)
            npt.assert_equal(off.size, 3)
            npt.assert_equal(rotM.shape, (3, 3))

        # Repeat fit and apply ellipsoid to accelerometers
        off, gain, rotM = skimu.fit_ellipsoid(accel, f="sxyz")
        accel_corr = skimu.apply_ellipsoid(accel, offset=off, gain=gain,
                                           rotM=rotM, ref_r=1.0)
        npt.assert_equal(accel.shape, accel_corr.shape)


if __name__ == '__main__':
    ut.main()
