"""
Photometry Pipeline Configuation File for VATT/VATT4k
2017-02-05, mommermiscience@gmail.com
"""

# Photometry Pipeline
# Copyright (C) 2016-2018  Michael Mommert, mommermiscience@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.


TR50_param = {'telescope_instrument': 'Teleskop Robotik 50 cm',
                'telescope_keyword': 'TR50',
                'observatory_code': 'KOE',  # MPC
                'secpix': (0.9765, 0.9765),  # pixel size
                # before binning # image orientation preferences 
                'flipx': False, 'flipy': True, 'rotate': 0,

                # instrument-specific FITS header keywords
                'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
                'extent': ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
                'ra': 'RA_OBJ',  # telescope pointing, RA
                'dec': 'DEC_OBJ',  # telescope pointin, Dec
                'radec_separator': 'XXX',   # RA/Dec hms separator, use 'XXX'
                # if already in degrees
                'obsmidtime_jd': 'MIDTIMJD',
                'date_keyword': 'DATE-OBS',  # obs date/time
                # keyword; use
                # 'date|time' if
                # separate
                'object': 'OBJECT',  # object name keyword
                'filter': 'FILTER',  # filter keyword
                'filter_translations': {'V': 'V', 'R': 'R',
                                        'I': 'I', 'B': 'B'},
                # filtername translation dictionary
                'exptime': 'EXPTIME',  # exposure time keyword (s)
                'airmass': 'AIRMASS',  # airmass keyword

                # source extractor settings
                'source_minarea': 3,  # default sextractor source minimum N_pixels
                'source_snr': 5,  # default sextractor source snr for registration
                'aprad_default': 5,  # default aperture radius in px
                'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
                'sex-config-file': rootpath+'/setup/TR50.sex',
                'mask_file': {},

                # scamp settings
                'scamp-config-file': rootpath+'/setup/TR50.scamp',
                'reg_max_mag': 16,
                'reg_search_radius': 2,  # deg
                'source_tolerance': 'medium',

                # swarp settings
                'copy_keywords': ('TELESCOP,INSTRUME,FILTER,EXPTIME,OBJECT,' +
                                  'DATE-OBS,TIME-OBS,RA,DEC,SECPIX,AIRMASS,' +
                                  'TEL_KEYW'),
                #                         keywords to be copied in image
                #                         combination using swarp
                'swarp-config-file': rootpath+'/setup/TR50.swarp',

                # default catalog settings
                'astrometry_catalogs': ['USNO-B1'],
                'photometry_catalogs': ['SDSS-R9', 'APASS9']
                }

# add telescope parameters to according lists and dictionaries
implemented_telescopes.append('TR50')
instrument_identifiersinstrument_identifiers = {'FLI': 'TR50'}
telescope_parameters['TR50'] = TR50_param
