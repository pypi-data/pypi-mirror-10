# Copyright (C) 2015  Randy Direen <spherepy@direentech.com>
#
# This file is part of SpherePy.
#
# SpherePy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SpherePy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SpherePy.  If not, see <http://www.gnu.org/licenses/>
"""
Randy Direen
2/21/2015

Unit tests for the Spherical Bessel functions and the spht, vspht, ispht,
and vspht routines.

"""
from __future__ import division
from unittest import TestCase

import spherepy as sp
import numpy as np

# TODO: Change all xrange instances to range
# and do a 'from six.moves import range' here
from six.moves import xrange  # @UnresolvedImport



class TestSBessel(TestCase):
    """Tests for the Spherical Bessel functions"""

    def test_misc_excercise(self):
        """:: Just exercise routines I know work"""

        _ = sp.sbesselh1(1.0, 3)
        _ = sp.sbesselh2(1.0, 3)
        _ = sp.sbesselj_array([1.0, 2.0], 3)
        _ = sp.sbessely_array([1.0, 2.0], 3)

        self.assertTrue(True)

    
    def test_sbesselj_sums(self):
        """::Test the jn(z) functions using the summation formula:
        
            Inf
            sum  (2*n+1) * jn(z)**2 = 1
            n=0
            
        I test arguments from around 1.0 to 10,000 to make sure i get the sum 
        to within machine precision.                 
        """
        
        res = True
        try:
            for z in np.linspace(1.0, 10000.0, 10):
                rnd = np.random.normal(0, 100)
                ar = np.abs(rnd) + 1.1
                s = sp.sbesselj_sum(ar, int(np.floor(z + 400)))
                if s > 1e-13:
                    res = False
        except:
            res = False
        
        self.assertTrue(res)


    def test_cross_product(self):
        """::Uses the cross-product relationship to test the routines: 

            j[n+1]y[n] - j[n]y[n+1] = 1 / (z**2)
    
        where j and y are sbesselj or sbessely vectors for a particular z.
        Doing this provides a check to see if the bessel functions are being
        calculated correctly.
    
        The routine returns the maximum of the relative error. 
        
        I start at z = 100ish to avoid overflow errors. This test could be 
        constructed better.
        """
        res = True
        try:
            for z in np.linspace(100, 10000.0, 10):
                s = sp.sbessel_test_cross_product(z, int(np.floor(z + 400)))
                if s > 1e-13:
                    res = False
        except:
            res = False
        
        self.assertTrue(res)
        
        
        
class TestScalarSphericalTransform(TestCase):
    """Testing the scalar spherical harmonic transforms"""
    def test_with_individual_coefficients_set(self):
        """::Testing spht and ispht with single coefficients, first 5 modes.
        """
        res = True
        
        try:
            for n in xrange(0, 6):
                for m in xrange(-n, n + 1):
                    rnd = np.random.normal(0, 10)
                    c = sp.zeros_coefs(15, 15)
                    c[n, m] = rnd
                    p = sp.ispht(c, 50, 50)
                    c2 = sp.spht(p, 15, 15)
                    s = sp.L2_coef(c - c2) / sp.L2_coef(c)
                    
                    if s > 1e-13:
                        res = False
        except:
            res = False
            
        self.assertTrue(res)

    def test_vec_with_individual_coefficients_set(self):
        """::Testing vspht and vispht with single coefficients, first 5 modes.
        """
        res = True
        
        for n in xrange(1, 6):
            for m in xrange(-n, n + 1):
                rnd1 = np.random.normal(0, 10)
                rnd2 = np.random.normal(0, 10)
                vc = sp.zeros_coefs(15, 15, coef_type=sp.vector)
                vc[n, m] = (rnd1, rnd2)
                p = sp.vispht(vc, 50, 50)
                vc2 = sp.vspht(p, 15, 15)
                s = sp.L2_coef(vc - vc2) / sp.L2_coef(vc)
                
                if s > 1e-10:
                    res = False
            
        self.assertTrue(res)

    def test_spht_with_large_random(self):
        """::Generate 100 random modes and test both spht and ispht.
        """

        c = sp.random_coefs(100, 100)
        p = sp.ispht(c, 202, 202)
        c2 = sp.spht(p, 100, 100)

        res = True
        if (sp.L2_coef(c - c2) / sp.L2_coef(c)) > 1e-13:
            res = False
            
        self.assertTrue(res)

    def test_vspht_with_large_random(self):
        """::Generate 100 random modes and test both vspht and vispht.
        """

        c = sp.random_coefs(100, 100, coef_type=sp.vector)
        p = sp.vispht(c, 202, 202)

        c2 = sp.vspht(p, 100, 100)

        res = True
        if (sp.L2_coef(c - c2) / sp.L2_coef(c)) > 1e-13:
            res = False
            
        self.assertTrue(res)

    def test_spht_ispht_no_added_args(self):
        """::Test spht and ispht when nmax, mmax, nrows, ncols are not passed.
        """
        c = sp.random_coefs(100, 100)
        p = sp.ispht(c)
        c2 = sp.spht(p)

        res = True
        if (sp.L2_coef(c - c2) / sp.L2_coef(c)) > 1e-13:
            res = False
            
        self.assertTrue(res)

    def test_spht_ispht_one_added_args(self):
        """::Test spht when only nmax is passed.
        """
        c = sp.random_coefs(100, 100)
        p = sp.ispht(c)
        c2 = sp.spht(p, 5)

        res = True
        if (sp.L2_coef(c[0:5, :] - c2) / sp.L2_coef(c[0:5, :])) > 1e-13:
            res = False
            
        self.assertTrue(res)

    def test_ispht_size_error1(self):
        """::Test ispht error when nrows is too small.
        """
        c = sp.random_coefs(100, 100)
        with self.assertRaises(ValueError):
            _ = sp.ispht(c, 100, 204)

    def test_ispht_size_error2(self):
        """::Test ispht error when ncols is too small.
        """
        c = sp.random_coefs(100, 100)
        with self.assertRaises(ValueError):
            _ = sp.ispht(c, 104, 198)

    def test_vspht_vispht_no_added_args(self):
        """::Test spht and ispht when nmax, mmax, nrows, ncols are not passed.
        """
        c = sp.random_coefs(100, 100, coef_type=sp.vector)
        p = sp.vispht(c)
        c2 = sp.vspht(p)

        res = True
        if (sp.L2_coef(c - c2) / sp.L2_coef(c)) > 1e-13:
            res = False
            
        self.assertTrue(res)

    def test_vspht_vispht_one_added_args(self):
        """::Test vspht when only nmax is passed.
        """
        c = sp.random_coefs(100, 100, coef_type=sp.vector)
        p = sp.vispht(c)
        c2 = sp.vspht(p, 5)

        res = True
        if (sp.L2_coef(c[0:5, :] - c2) / sp.L2_coef(c[0:5, :])) > 1e-13:
            res = False
            
        self.assertTrue(res)

    def test_vispht_size_error1(self):
        """::Test ispht error when nrows is too small.
        """
        c = sp.random_coefs(100, 100, coef_type=sp.vector)
        with self.assertRaises(ValueError):
            _ = sp.vispht(c, 100, 204)

    def test_vispht_size_error2(self):
        """::Test ispht error when ncols is too small.
        """
        c = sp.random_coefs(100, 100, coef_type=sp.vector)
        with self.assertRaises(ValueError):
            _ = sp.vispht(c, 104, 198)

                    
        
