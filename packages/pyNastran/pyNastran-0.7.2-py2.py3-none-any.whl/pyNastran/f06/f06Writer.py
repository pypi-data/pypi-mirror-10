#pylint: disable=W0201,C0301,C0111
from __future__ import (nested_scopes, generators, division, absolute_import,
                        print_function, unicode_literals)
from six import string_types, iteritems, PY2
import copy
from datetime import date

import pyNastran
from pyNastran.op2.op2_f06_common import OP2_F06_Common
from pyNastran.op2.result_set import ResultSet


def make_stamp(Title, today=None):
    if 'Title' is None:
        Title = ''

    #lenghts = [7, 8, 5, 5, 3, 4, 4, 6, 9, 7, 8, 8]
    months = [' January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    if today is None:
        today = date.today()
        str_month = months[today.month - 1].upper()
        str_today = '%-9s %2s, %4s' % (str_month, today.day, today.year)
    else:
        (month, day, year) = today
        str_month = months[month - 1].upper()
        str_today = '%-9s %2s, %4s' % (str_month, day, year)
    str_today = str_today  #.strip()

    release_date = '02/08/12'  # pyNastran.__releaseDate__
    release_date = ''
    build = 'pyNastran v%s %s' % (pyNastran.__version__, release_date)
    if Title is None:
        Title = ''
    out = '1    %-67s   %-19s %-22s PAGE %%5i\n' % (Title.strip(), str_today, build)
    return out


def make_f06_header():
    spaces = ''
    lines1 = [
        spaces + '/* -------------------------------------------------------------------  */\n',
        spaces + '/*                              PYNASTRAN                               */\n',
        spaces + '/*                      - NASTRAN FILE INTERFACE -                      */\n',
        spaces + '/*                                                                      */\n',
        spaces + '/*              A Python reader/editor/writer for the various           */\n',
        spaces + '/*                        NASTRAN file formats.                         */\n',
        spaces + '/*                       Copyright (C) 2011-2013                        */\n',
        spaces + '/*               Steven Doyle, Al Danial, Marcin Garrozik               */\n',
        spaces + '/*                                                                      */\n',
        spaces + '/*    This program is free software; you can redistribute it and/or     */\n',
        spaces + '/*    modify it under the terms of the GNU Lesser General Public        */\n',
        spaces + '/*    License as published by the Free Software Foundation;             */\n',
        spaces + '/*    version 3 of the License.                                         */\n',
        spaces + '/*                                                                      */\n',
        spaces + '/*    This program is distributed in the hope that it will be useful,   */\n',
        spaces + '/*    but WITHOUT ANY WARRANTY; without even the implied warranty of    */\n',
        spaces + '/*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the      */\n',
        spaces + '/*    GNU Lesser General Public License for more details.               */\n',
        spaces + '/*                                                                      */\n',
        spaces + '/*    You should have received a copy of the GNU Lesser General Public  */\n',
        spaces + '/*    License along with this program; if not, write to the             */\n',
        spaces + '/*    Free Software Foundation, Inc.,                                   */\n',
        spaces + '/*    675 Mass Ave, Cambridge, MA 02139, USA.                           */\n',
        spaces + '/* -------------------------------------------------------------------  */\n',
        '\n']

    spaces = 46 * ' '
    version = 'Version %8s' % pyNastran.__version__
    lines2 = [
        spaces + '* * * * * * * * * * * * * * * * * * * *\n',
        spaces + '* * * * * * * * * * * * * * * * * * * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *            pyNastran            * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *%s* *\n' % version.center(33),
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *          %15s        * *\n' % pyNastran.__releaseDate2__,
        spaces + '* *                                 * *\n',
        spaces + '* *            Questions            * *\n',
        spaces + '* *        mesheb82@gmail.com       * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* *                                 * *\n',
        spaces + '* * * * * * * * * * * * * * * * * * * *\n',
        spaces + '* * * * * * * * * * * * * * * * * * * *\n\n\n']
    return ''.join(lines1 + lines2)


def sorted_bulk_data_header():
    msg = '0                                                 S O R T E D   B U L K   D A T A   E C H O                                         \n'
    msg += '                 ENTRY                                                                                                              \n'
    msg += '                 COUNT        .   1  ..   2  ..   3  ..   4  ..   5  ..   6  ..   7  ..   8  ..   9  ..  10  .                      \n'
    return msg


def make_end(end_flag=False):
    lines = []
    lines2 = []
    if end_flag:
        lines = [
            '', '',
            '0                                   * * * *  A N A L Y S I S  S U M M A R Y  T A B L E  * * * *',
            '0 SEID  PEID PROJ VERS APRCH      SEMG SEMR SEKR SELG SELR MODES DYNRED SOLLIN PVALID SOLNL LOOPID DESIGN CYCLE SENSITIVITY',
            ' --------------------------------------------------------------------------------------------------------------------------']
        #0     0    1    1 '        '    T    T    T    T    T     F      F      T      0     F     -1            0           F

        seid = 0
        peid = 0
        proj = 1
        vers = 1
        approach = '        '

        SELG = 'T'
        SEMG = 'T'
        SEMR = 'T'
        SEKR = 'T'
        SELR = 'T'
        MODES = 'F'
        DYNRED = 'F'

        SOLLIN = 'T'
        PVALID = 0
        SOLNL = 'F'
        LOOPID = -1
        CYCLE = 0
        SENSITIVITY = 'F'

        msg = '     %s     %s    %s    %s %8r    %s    %s    %s    %s    %s     %s      %s      %s      %s     %s     %s            %s           %s' % (
            seid, peid, proj, vers, approach, SEMG, SEMR, SEKR, SELG, SELR, MODES, DYNRED, SOLLIN, PVALID, SOLNL,
            LOOPID, CYCLE, SENSITIVITY)
        lines.append(msg)

        lines2 = [
            '0SEID = SUPERELEMENT ID.',
            ' PEID = PRIMARY SUPERELEMENT ID OF IMAGE SUPERELEMENT.',
            ' PROJ = PROJECT ID NUMBER.',
            ' VERS = VERSION ID.',
            ' APRCH = BLANK FOR STRUCTURAL ANALYSIS.  HEAT FOR HEAT TRANSFER ANALYSIS.',
            ' SEMG = STIFFNESS AND MASS MATRIX GENERATION STEP.',
            ' SEMR = MASS MATRIX REDUCTION STEP (INCLUDES EIGENVALUE SOLUTION FOR MODES).',
            ' SEKR = STIFFNESS MATRIX REDUCTION STEP.',
            ' SELG = LOAD MATRIX GENERATION STEP.',
            ' SELR = LOAD MATRIX REDUCTION STEP. ',
            ' MODES = T (TRUE) IF NORMAL MODES OR BUCKLING MODES CALCULATED.',
            ' DYNRED = T (TRUE) MEANS GENERALIZED DYNAMIC AND/OR COMPONENT MODE REDUCTION PERFORMED.',
            ' SOLLIN = T (TRUE) IF LINEAR SOLUTION EXISTS IN DATABASE.',
            ' PVALID = P-DISTRIBUTION ID OF P-VALUE FOR P-ELEMENTS',
            ' LOOPID = THE LAST LOOPID VALUE USED IN THE NONLINEAR ANALYSIS.  USEFUL FOR RESTARTS.',
            ' SOLNL = T (TRUE) IF NONLINEAR SOLUTION EXISTS IN DATABASE.',
            ' DESIGN CYCLE = THE LAST DESIGN CYCLE (ONLY VALID IN OPTIMIZATION).',
            ' SENSITIVITY = SENSITIVITY MATRIX GENERATION FLAG.',
            ' ',
            ' No PARAM values were set in the Control File.'
        ]

    lines3 = [
        ' ',
        '1                                        * * * END OF JOB * * *',
        ' ',
        ' '
    ]
    return '\n'.join(lines + lines2 + lines3)


class F06Writer(OP2_F06_Common):
    def __init__(self):
        OP2_F06_Common.__init__(self)
        self.card_count = {}

        self._results = ResultSet(self.get_all_results())

    def get_all_results(self):
        all_results = ['stress', 'strain', 'element_forces', 'constraint_forces'] + self.get_table_types()
        return all_results

    def _clear_results(self):
        self._results.clear()

    def add_results(self, results):
        if isinstance(results, string_types):
            results = [results]
        all_results = self.get_all_results()
        for result in results:
            result = str(result)
            if result not in all_results:
                raise RuntimeError('%r is not a valid result to remove; all_results=%s' % (result, all_results))
            if 'stress' == result:
                stress_results = []
                for result in all_results:
                    if 'stress' in result.lower():
                        stress_results.append(result)
                #stress_results = [result if 'stress' in result.lower() for result in all_results]
                self._results.update(stress_results)
            elif 'strain' == result:
                strain_results = []
                for result in all_results:
                    if 'strain' in result.lower():
                        strain_results.append(result)
                #strain_results = [result if 'strain' in result.lower() for result in all_results]
                self._results.update(strain_results)
            elif 'stress' in result.lower():
                self._results.add('stress')
            elif 'strain' in result.lower():
                self._results.add('strain')
            elif 'spc_forces' == result or 'mpc_forces' == result or 'constraint_forces' == result:
                self._results.add('constraint_forces')
            elif 'force' in result.lower(): # could use more validation...
                self._results.add('element_forces')
            # thermalLoad_VU_3D, thermalLoad_1D, thermalLoad_CONV, thermalLoad_2D_3D
            self._results.add(result)

    def set_results(self, results):
        if isinstance(results, string_types):
            results = [results]
        self._clear_results()
        self.add_results(results)

    def remove_results(self, results):
        self._results.remove(results)

    def make_f06_header(self):
        """If this class is inherited, the F06 Header may be overwritten"""
        return make_f06_header()

    def make_stamp(self, Title, today):
        """If this class is inherited, the PAGE stamp may be overwritten"""
        return make_stamp(Title, today)

    def make_grid_point_singularity_table(self, failed):
        msg = ''
        if failed:
            msg += '0                                         G R I D   P O I N T   S I N G U L A R I T Y   T A B L E\n'
            msg += '0                             POINT    TYPE   FAILED      STIFFNESS       OLD USET           NEW USET\n'
            msg += '                               ID            DIRECTION      RATIO     EXCLUSIVE  UNION   EXCLUSIVE  UNION\n'
            for (nid, dof) in failed:
                msg += '                         %8s        G      %s         0.00E+00          B        F         SB       SB   *\n' % (nid, dof)
        else:
            msg += 'No constraints have been applied...\n'

        page_stamp = self.make_stamp(self.Title, self.date)
        msg += page_stamp % self.page_num
        self.page_num += 1
        return msg

    def write_summary(self, f06, card_count=None):
        summary_header = '                                        M O D E L   S U M M A R Y\n\n'
        summary = ''

        self.cards_to_read = set([

            # rigid elements
            'RBAR', 'RBAR1', 'RBE1', 'RBE2', 'RBE3',

            # spc/mpc constraints
            'SPC', 'SPCADD', 'SPC1', 'SPCD', 'SPCAX',
            'MPC', 'MPCADD',
            'SUPORT', 'SUPORT1',

            # aero cards
            'CAERO1', 'CAERO2', 'CAERO3', 'CAERO4', 'CAERO5',

            # temperature cards
            'CHBDYE', 'CHBDYG', 'CHBDYP',
            'CONV',
        ])


        blocks = [
            ['POINTS', ['GRID', 'GRDSET', ]],
            ['ENTRIES', ['SPOINT']],

            ['ELEMENTS',
             [
                 # these are sorted
                 # elements
                 'CONM1', 'CONM2', 'CMASS1', 'CMASS2', 'CMASS3', 'CMASS4',

                 # springs
                 'CELAS1', 'CELAS2', 'CELAS3', 'CELAS4', 'CELAS5',

                 # bushings
                 'CBUSH', 'CBUSH1D', 'CBUSH2D',

                 # dampers
                 'CDAMP1', 'CDAMP2', 'CDAMP3', 'CDAMP4', 'CDAMP5',

                 # bar flags
                 'BAROR', 'CBARAO',
                 # bars
                 'CBAR', 'CROD', 'CTUBE', 'CBEAM', 'CBEAM3', 'CONROD', 'CBEND',

                 # shells
                 'CTRIA3', 'CTRIA6', 'CTRIAR', 'CTRIAX', 'CTRIAX6',
                 'CQUAD4', 'CQUAD8', 'CQUADR', 'CQUADX', 'CQUAD',

                 # solids
                 'CTETRA', 'CPENTA', 'CHEXA',

                 # other
                 'CSHEAR', 'CVISC', 'CRAC2D', 'CRAC3D',
                 'CGAP', 'CFAST', 'RBE2', 'RBE3',

                 # thermal
                 'CHBDYP', 'CHBDYG', 'CONV',
             ]],
        ]
        #print("self.card_count", self.card_count)
        if card_count is None:
            card_count = self.card_count

        for block in blocks:
            block_name, keys = block
            key_count = 0
            for key in sorted(keys):
                try:
                    value = card_count[key]
                    summary += '                                   NUMBER OF %-8s %-8s = %8s\n' % (key, block_name, value)
                    key_count += 1
                except KeyError:
                    pass
            if key_count:
                summary += ' \n'

        if summary:
            f06.write(summary_header)
            f06.write(summary)

            page_stamp = self.make_stamp(self.Title, self.date)
            f06.write(page_stamp % self.page_num)
            self.page_num += 1

    def write_f06(self, f06_outname, is_mag_phase=False,
                  delete_objects=True, end_flag=False):
        """
        Writes an F06 file based on the data we have stored in the object

        :param self:         the F06 object
        :param f06_outname:  the name of the F06 file to write
        :param is_mag_phase: should complex data be written using Magnitude/Phase
                         instead of Real/Imaginary (default=False; Real/Imag)
                         Real objects don't use this parameter.
        :param delete_objects: should objects be deleted after they're written
                         to reduce memory (default=True)
        :param end_flag: should a dummy Nastran "END" table be made
                         (default=False)
        """
        print("F06:")
        if isinstance(f06_outname, str):
            if PY2:
                f06 = open(f06_outname, 'wb')
            else:
                f06 = open(f06_outname, 'w')
            self.write_summary(f06)
        else:
            assert isinstance(f06_outname, file), 'type(f06_outname)= %s' % f06_outname
            f06 = f06_outname
            f06_outname = f06.name
            print('f06_outname =', f06_outname)

        page_stamp = self.make_stamp(self.Title, self.date)
        if self.grid_point_weight.reference_point is not None:
            print("grid_point_weight")
            self.page_num = self.grid_point_weight.write_f06(f06, page_stamp, self.page_num)
            assert isinstance(self.page_num, int), self.grid_point_weight.__class__.__name__

        if self.oload_resultant is not None:
            self.page_num = self.oload_resultant.write_f06(f06, page_stamp, self.page_num)
            assert isinstance(self.page_num, int), self.oload_resultant.__class__.__name__


        #is_mag_phase = False
        header = ['     DEFAULT                                                                                                                        \n',
                  '\n', '']

        # eigenvalues are written first
        for ikey, result in sorted(iteritems(self.eigenvalues)):
            print('%-18s case=%r' % (result.__class__.__name__, ikey))
            self.page_num = result.write_f06(f06, header, page_stamp,
                                             page_num=self.page_num)
            assert isinstance(self.page_num, int), 'pageNum=%r' % str(self.page_num)
            if delete_objects:
                del result
            self.page_num += 1

        # then eigenvectors
        # has a special header
        iSubcases = sorted(self.iSubcaseNameMap.keys())

        res_keys = []
        for isubcase in iSubcases:
            for subtitle in self.subtitles[isubcase]:
                res_keys.append((isubcase, subtitle))

        #print('res_keys=%s' % res_keys)
        for res_key in res_keys:
            isubcase = res_key[0]
            subtitle = res_key[1]
            label = self.labels[(isubcase, subtitle)]

            is_compressed = len(self.subtitles[isubcase]) == 1
            if is_compressed:
                res_key = isubcase

            if res_key not in self.eigenvectors:
                continue
            result = self.eigenvectors[res_key]
            header[0] = '     %s\n' % subtitle
            header[1] = '0                                                                                                            SUBCASE %i\n' % (isubcase)
            #header[2] = complex/nonlinear
            star = ' '
            if hasattr(self, 'data'):
                star = '*'

            res_length = 18
            res_format = '%%-%is SUBCASE=%%i' % res_length
            res_format_vectorized = '%%-%is SUBCASE=%%i SUBTITLE=%%s' % res_length
            if is_compressed:
                print(star + res_format % (result.__class__.__name__, isubcase))
            else:
                print(star + res_format_vectorized % (result.__class__.__name__, isubcase, subtitle))

            self.page_num = result.write_f06(header, page_stamp,
                                             self.page_num, f=f06, is_mag_phase=is_mag_phase)
            assert isinstance(self.page_num, int), 'pageNum=%r' % str(self.page_num)
            if delete_objects:
                del result
            self.page_num += 1

        # finally, we writte all the other tables
        # nastran puts the tables in order of the Case Control deck,
        # but we're lazy so we just hardcode the order

        # subcase name, subcase ID, transient word & value
        header_old = ['     DEFAULT                                                                                                                        \n',
                      '\n', ' \n']
        header = copy.deepcopy(header_old)
        res_types = [
            self.accelerations,
            self.displacements, self.displacementsPSD, self.displacementsATO, self.displacementsRMS,
            self.scaledDisplacements,  # ???

            self.force_vectors,
            self.load_vectors,
            self.temperatures,
            self.velocities, #self.eigenvectors,

            self.mpc_forces,
            self.spc_forces,
            self.thermal_load_vectors,

            self.strain_energy,


            #------------------------------------------
            # OEF - forces

            # alphabetical order...
            # bars
            self.cbar_force,
            self.cbar100_force,

            # beam
            self.cbend_force,
            self.cbeam_force,

            # alphabetical
            self.celas1_force,
            self.celas2_force,
            self.celas3_force,
            self.celas4_force,

            self.conrod_force,

            self.cquad4_force,
            self.cquad8_force,
            self.cquadr_force,

            self.conrod_force,
            self.crod_force,
            self.cshear_force,
            self.ctria3_force,
            self.ctria6_force,
            self.ctriar_force,
            self.ctube_force,

            # springs
            self.celas1_force,
            self.celas2_force,
            self.celas3_force,
            self.celas4_force,

            # dampers
            self.cdamp1_force,
            self.cdamp2_force,
            self.cdamp3_force,
            self.cdamp4_force,

            # other
            self.cbush_force,
            self.cgap_force,
            self.cvisc_force,

            self.chexa_pressure_force,
            self.cpenta_pressure_force,
            self.ctetra_pressure_force,

            #------------------------------------------
            # OES - strain
            # 1.  cbar
            # 2.  cbeam
            # 3.  crod/ctube/conrod

            # springs
            self.celas1_strain,
            self.celas2_strain,
            self.celas3_strain,
            self.celas4_strain,

            self.nonlinear_celas1_stress,
            self.nonlinear_celas3_stress,

            # bars/beams
            self.cbar_strain,
            self.cbeam_strain,

            # plates
            self.cquad4_composite_strain,
            self.cquad8_composite_strain,
            self.cquadr_composite_strain,
            self.ctria3_composite_strain,
            self.ctria6_composite_strain,
            self.ctriar_composite_strain,

            self.nonlinear_ctria3_strain,
            self.nonlinear_cquad4_strain,
            self.ctriax_strain,

            # rods
            self.nonlinear_crod_strain,
            self.nonlinear_ctube_strain,
            self.nonlinear_conrod_strain,

            self.chexa_strain,
            self.conrod_strain,
            self.cpenta_strain,
            self.cquad4_strain,
            self.cquad8_strain,
            self.cquadr_strain,
            self.crod_strain,
            self.cshear_strain,
            self.ctetra_strain,
            self.ctria3_strain,
            self.ctria6_strain,
            self.ctriar_strain,
            self.ctube_strain,

            # bush
            self.cbush_strain,
            self.nonlinear_cbush_stress,
            self.cbush1d_stress_strain,
            #------------------------------------------
            # cbars/cbeams
            self.cbar_stress,
            self.nonlinear_cbeam_stress,
            self.cbeam_stress,

            # bush
            self.cbush_stress,

            # rods
            self.nonlinear_crod_stress,
            self.nonlinear_ctube_stress,
            self.nonlinear_conrod_stress,

            # shear
            # OES - stress
            self.celas1_stress,
            self.celas2_stress,
            self.celas3_stress,
            self.celas4_stress,

            self.chexa_stress,
            self.conrod_stress,
            self.cpenta_stress,
            self.cquad4_stress,
            self.cquad8_stress,
            self.cquadr_stress,
            self.crod_stress,
            self.cshear_stress,
            self.ctetra_stress,
            self.ctria3_stress,
            self.ctria6_stress,
            self.ctriar_stress,
            self.ctube_stress,

            self.cquad4_composite_stress,
            self.cquad8_composite_stress,
            self.cquadr_composite_stress,
            self.ctria3_composite_stress,
            self.ctria6_composite_stress,
            self.ctriar_composite_stress,

            self.nonlinear_ctria3_stress,
            self.nonlinear_cquad4_stress,
            self.ctriax_stress,

            self.hyperelastic_cquad4_strain,

            #------------------------------------------

            self.grid_point_stresses, self.grid_point_volume_stresses, self.grid_point_forces,
        ]

        for res_key in res_keys:
            #title = self.Title

            isubcase = res_key[0]
            subtitle = res_key[1]
            label = self.labels[(isubcase, subtitle)]

            is_compressed = len(self.subtitles[isubcase]) == 1
            #print(self.subtitles[isubcase])
            if is_compressed:
                res_key = isubcase

            #header[0] = '     %-127s\n' % subtitle
            #header[1] = '0    %-72s                                SUBCASE %-15i\n' % (label, isubcase)
            #header[1] = '0    %-72s                                SUBCASE %-15i\n' % ('',isubcase)

            res_length = self._get_result_length(res_types, res_key)
            if res_length == 0:
                # skipped subcase; no saved results
                continue

            res_format = '%%-%is SUBCASE=%%i%%s' % res_length
            res_format_vectorized = '%%-%is SUBCASE=%%i SUBTITLE=%%s %%s' % res_length

            for res_type in res_types:
                #print("res_type ", res_type)
                header = ['', '']
                #header[0] = '     %s\n' % subtitle
                header[0] = '      %-126s\n' % subtitle
                header[1] = '0     %-32s                                                                       SUBCASE %-15i\n \n' % (label, isubcase)
                #print("res_type = %s" % res_type)

                if res_key in res_type:
                    #header = copy.deepcopy(headerOld)  # fixes bug in case
                    result = res_type[res_key]
                    if result.nonlinear_factor is not None:
                        header.append('')
                    try:
                        element_name = ''
                        if hasattr(result, 'element_name'):
                            element_name = ' - ' + result.element_name

                        star = '*'
                        if hasattr(result, 'data'):
                            star = ' '
                        if is_compressed:
                            print(star + res_format % (result.__class__.__name__, isubcase, element_name))
                        else:
                            print(star + res_format_vectorized % (result.__class__.__name__, isubcase, subtitle, element_name))
                        self.page_num = result.write_f06(header, page_stamp, page_num=self.page_num, f=f06, is_mag_phase=False)
                        assert isinstance(self.page_num, int), 'pageNum=%r' % str(self.page_num)
                    except:
                        #print("result name = %r" % result.name())
                        raise
                    if delete_objects:
                        del result
                    self.page_num += 1
        f06.write(make_end(end_flag))
        f06.close()
