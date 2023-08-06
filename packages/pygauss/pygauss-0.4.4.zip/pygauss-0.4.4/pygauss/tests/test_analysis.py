# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:55:57 2015

@author: chris
"""

from nose import tools as that
from nose_parameterized import parameterized, param

import pygauss as pg

class Test_Analysis(object):
    def setUp(self):
        self.folder = pg.get_test_folder()
    
    def test_initialises(self):
        pg.Analysis(folder_obj=self.folder)

    def test_add_runs(self):

        analysis = pg.Analysis(folder_obj=self.folder)
        analysis.add_runs(headers=['Cation', 'Anion', 'Initial'], 
                                       values=[['emim'], ['cl'],
                                               ['B', 'F', 'FE']],
                    init_pattern='*{0}-{1}_{2}_init.com',
                    opt_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_opt*unfrz.log',
                    freq_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_freq*.log',
                    nbo_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_pop-nbo-full-*.log',
                    alignto=[3,2,1], atom_groups={'emim':range(20), 'cl':[20]})

    @parameterized([param('name','get_optimisation_E'),
                    param('name','calc_bond_angle', [1, 4, 9]),
                    param('name','calc_dihedral_angle', [1, 4, 9, 10]),
                    param('name','calc_min_dist', 'emim', 'cl'),
                    param('name','calc_2plane_angle', [1,2,3], [8,9,10]),
                    param('name','calc_nbo_charge', 'emim'),
                    param('name', 'calc_hbond_energy'),
                    param(['name', 'name', 'name'], 'calc_polar_coords_from_plane', 3, 2, 1, 20)
                  ])
    def test_add_mol_property(self, name, prop, *args, **kwargs):
        analysis = pg.Analysis(folder_obj=self.folder)
        analysis.add_runs(headers=['Cation', 'Anion', 'Initial'],
                          values=[['emim'], ['cl'],
                                  ['B', 'F', 'FE']],
                          init_pattern='*{0}-{1}_{2}_init.com',
                          opt_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_opt*unfrz.log',
                          freq_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_freq*.log',
                          nbo_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_pop-nbo-full-*.log',
                          alignto=[3,2,1], atom_groups={'emim':range(20), 'cl':[20]})

        analysis.add_mol_property(name, prop, *args, **kwargs)

    @parameterized(['initial', 'optimised', 'highlight', 'nbo', 'sopt', 'hbond'])
    def test_tbl_images(self, mtype):

        analysis = pg.Analysis(folder_obj=self.folder)
        analysis.add_runs(headers=['Cation', 'Anion', 'Initial'], 
                                       values=[['emim'], ['cl'],
                                               ['B', 'F', 'FE']],
                    init_pattern='*{0}-{1}_{2}_init.com',
                    opt_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_opt*unfrz.log',
                    freq_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_freq*.log',
                    nbo_pattern='*{0}-{1}_{2}_6-311+g-d-p-_gd3bj_pop-nbo-full-*.log',
                    alignto=[3,2,1], atom_groups={'emim':range(20), 'cl':[20]})

        fig, caption = analysis.plot_mol_images(mtype=mtype, max_cols=2,
                                info_columns=['Cation', 'Anion', 'Initial'],
                                rotations=[[0,0,90]])
